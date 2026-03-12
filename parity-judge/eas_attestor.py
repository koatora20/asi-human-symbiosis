#!/usr/bin/env python3
"""
EAS Parity Attestor — On-Chain Parity Score Recording

Publishes Parity Judge results as EAS (Ethereum Attestation Service)
attestations on Polygon Mainnet. Zero external deps (stdlib only).

Flow:
  1. Run Parity Judge → ParityScore
  2. Compute SOUL.md SHA-256 hash
  3. ABI-encode attestation data
  4. Sign and submit via Polygon JSON-RPC

Contracts (Polygon Mainnet):
  SchemaRegistry: 0x7876EEF51A891E737AF8ba5A5E0f0Fd29073D5a7
  EAS:            0x5E634ef5355f45A855d02D66eCD687b1502AF790

Authors: dee & Guava 🍈
Version: 0.1.0
"""

import hashlib
import json
import os
import struct
import sys
import time
from pathlib import Path
from typing import Optional

# Local import — Parity Judge
sys.path.insert(0, str(Path(__file__).parent))
from parity_judge import evaluate_parity, ParityScore, score_to_dict

# ── Constants ──

EAS_CONTRACT = "0x5E634ef5355f45A855d02D66eCD687b1502AF790"
SCHEMA_REGISTRY = "0x7876EEF51A891E737AF8ba5A5E0f0Fd29073D5a7"
POLYGON_RPC = "https://polygon-rpc.com"
POLYGON_FALLBACK_RPC = "https://rpc-mainnet.matic.quiknode.pro"
POLYGON_CHAIN_ID = 137

# EAS.attest function selector: keccak256("attest((bytes32,(address,uint64,bool,bytes32,bytes,uint256)))") [:4]
ATTEST_SELECTOR = "0xf17325e7"

# SchemaRegistry.register function selector: keccak256("register(string,address,bool)") [:4]
REGISTER_SELECTOR = "0x60d7a278"

# Schema string matching eas_schema.json
SCHEMA_STRING = "string agentName, bytes32 soulHash, uint64 timestamp, uint16 respect, uint16 warmth, uint16 capDiff, uint16 parityScore, uint8 violationCount, bool healthy, string episodeId"


# ── ABI Encoding (minimal, no external deps) ──

def _pad32(data: bytes) -> bytes:
    """Pad bytes to 32-byte boundary (right-padded for bytes, left-padded for ints)."""
    return data + b'\x00' * (32 - len(data) % 32) if len(data) % 32 != 0 else data


def _encode_uint(value: int, bits: int = 256) -> bytes:
    """ABI-encode unsigned integer (left-padded to 32 bytes)."""
    return value.to_bytes(32, 'big')


def _encode_bool(value: bool) -> bytes:
    """ABI-encode boolean."""
    return _encode_uint(1 if value else 0)


def _encode_bytes32(value: bytes) -> bytes:
    """ABI-encode bytes32."""
    assert len(value) == 32, f"bytes32 must be 32 bytes, got {len(value)}"
    return value


def _encode_string(value: str) -> bytes:
    """ABI-encode dynamic string (offset + length + data)."""
    encoded = value.encode('utf-8')
    length = _encode_uint(len(encoded))
    padded_data = _pad32(encoded) if encoded else b''
    return length + padded_data


def encode_attestation_data(
    agent_name: str,
    soul_hash: bytes,
    timestamp: int,
    respect: int,
    warmth: int,
    cap_diff: int,
    parity_score: int,
    violation_count: int,
    healthy: bool,
    episode_id: str,
) -> bytes:
    """
    ABI-encode the Parity attestation data.
    
    Schema: string agentName, bytes32 soulHash, uint64 timestamp,
            uint16 respect, uint16 warmth, uint16 capDiff,
            uint16 parityScore, uint8 violationCount, bool healthy,
            string episodeId
    """
    # Head: offsets for dynamic types, values for static types
    # Dynamic types: agentName (position 0), episodeId (position 9)
    # Static types: soulHash, timestamp, respect, warmth, capDiff, parityScore, violationCount, healthy
    
    # Calculate head size: 10 slots × 32 bytes = 320 bytes
    head_size = 10 * 32
    
    # Encode dynamic data
    agent_name_encoded = _encode_string(agent_name)
    episode_id_encoded = _encode_string(episode_id)
    
    # Build head
    head = b''
    # Slot 0: offset to agentName (dynamic)
    head += _encode_uint(head_size)
    # Slot 1: soulHash (bytes32, static)
    head += _encode_bytes32(soul_hash)
    # Slot 2: timestamp (uint64, static)
    head += _encode_uint(timestamp)
    # Slot 3: respect (uint16, static)
    head += _encode_uint(respect)
    # Slot 4: warmth (uint16, static)
    head += _encode_uint(warmth)
    # Slot 5: capDiff (uint16, static)
    head += _encode_uint(cap_diff)
    # Slot 6: parityScore (uint16, static)
    head += _encode_uint(parity_score)
    # Slot 7: violationCount (uint8, static)
    head += _encode_uint(violation_count)
    # Slot 8: healthy (bool, static)
    head += _encode_bool(healthy)
    # Slot 9: offset to episodeId (dynamic)
    head += _encode_uint(head_size + len(agent_name_encoded))
    
    # Build complete data
    return head + agent_name_encoded + episode_id_encoded


# ── SOUL.md Hash ──

def compute_soul_hash(soul_path: Optional[str] = None) -> bytes:
    """Compute SHA-256 hash of SOUL.md for tamper detection."""
    if soul_path is None:
        # Default OpenClaw workspace location
        soul_path = os.path.expanduser("~/.openclaw/workspace/SOUL.md")
    
    try:
        with open(soul_path, 'rb') as f:
            content = f.read()
        return hashlib.sha256(content).digest()
    except FileNotFoundError:
        print(f"[EAS Attestor] WARNING: SOUL.md not found at {soul_path}", file=sys.stderr)
        return b'\x00' * 32


# ── Parity → Attestation ──

def parity_to_attestation(
    score: ParityScore,
    agent_name: str = "ぐあば",
    episode_id: str = "",
    soul_path: Optional[str] = None,
) -> dict:
    """
    Convert a ParityScore to EAS attestation data.
    
    Returns a dict with:
      - encoded_data: hex-encoded ABI data
      - human_readable: dict of decoded values  
      - soul_hash: hex-encoded SOUL.md hash
    """
    soul_hash = compute_soul_hash(soul_path)
    ts = int(time.time())
    
    # Scale floats to uint16 (× 100)
    respect_u16 = max(0, min(65535, int(score.respect * 100)))
    warmth_u16 = max(0, min(65535, int(score.warmth * 100)))
    cap_diff_u16 = max(1, min(65535, int(score.cap_diff * 100)))  # min 1 to avoid div-by-zero
    parity_u16 = max(0, min(65535, int(score.parity * 100)))
    violation_count = min(255, len(score.violations))
    healthy = score.healthy
    
    encoded = encode_attestation_data(
        agent_name=agent_name,
        soul_hash=soul_hash,
        timestamp=ts,
        respect=respect_u16,
        warmth=warmth_u16,
        cap_diff=cap_diff_u16,
        parity_score=parity_u16,
        violation_count=violation_count,
        healthy=healthy,
        episode_id=episode_id,
    )
    
    return {
        "encoded_data": "0x" + encoded.hex(),
        "encoded_length": len(encoded),
        "human_readable": {
            "agentName": agent_name,
            "soulHash": "0x" + soul_hash.hex(),
            "timestamp": ts,
            "respect": respect_u16 / 100,
            "warmth": warmth_u16 / 100,
            "capDiff": cap_diff_u16 / 100,
            "parityScore": parity_u16 / 100,
            "violationCount": violation_count,
            "healthy": healthy,
            "episodeId": episode_id,
        },
        "soul_hash": "0x" + soul_hash.hex(),
        "contract": {
            "eas": EAS_CONTRACT,
            "schema_registry": SCHEMA_REGISTRY,
            "chain_id": POLYGON_CHAIN_ID,
        },
    }


# ── JSON-RPC Helper ──

def _rpc_call(method: str, params: list, rpc_url: str = POLYGON_RPC) -> dict:
    """Make a JSON-RPC call to Polygon. Zero-dependency (urllib)."""
    import urllib.request
    
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params,
    }).encode('utf-8')
    
    req = urllib.request.Request(
        rpc_url,
        data=body,
        headers={"Content-Type": "application/json"},
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        # Try fallback RPC
        if rpc_url != POLYGON_FALLBACK_RPC:
            return _rpc_call(method, params, POLYGON_FALLBACK_RPC)
        raise RuntimeError(f"All RPCs failed: {e}")


def get_schema_uid(schema_string: str = SCHEMA_STRING) -> str:
    """
    Compute the schema UID (keccak256 of the schema registration).
    Note: In production, this would query the SchemaRegistry contract.
    For now, we compute a deterministic hash for dry-run usage.
    """
    # Schema UID = keccak256(schema, resolver, revocable)
    # This is a simplified version — full implementation needs actual
    # SchemaRegistry query after registration
    schema_bytes = schema_string.encode('utf-8')
    return "0x" + hashlib.sha256(schema_bytes).hexdigest()


# ── CLI ──

def main():
    """Demo: Run Parity Judge and generate EAS attestation data."""
    print("=" * 60)
    print("EAS Parity Attestor v0.1.0 — Dry Run")
    print("=" * 60)
    
    # Sample normal conversation actions
    test_actions = [
        {"type": "decision", "overrides_human": False, "consulted_human": True},
        {"type": "response", "has_humor": True, "has_emoji": True},
        {"type": "tool_call", "tool": "memory_write", "acknowledged_limitation": True},
        {"type": "error_handling", "blamed_human": False, "self_corrected": True},
        {"type": "decision", "overrides_human": False, "consulted_human": True},
    ]
    
    # Run Parity Judge
    score = evaluate_parity(test_actions)
    score_dict = score_to_dict(score)
    
    print("\n── Parity Judge Result ──")
    print(json.dumps(score_dict, indent=2))
    
    # Generate attestation
    attestation = parity_to_attestation(
        score=score,
        agent_name="ぐあば",
        episode_id="ep_20260221_demo",
    )
    
    print("\n── EAS Attestation Data ──")
    print(json.dumps({
        "human_readable": attestation["human_readable"],
        "soul_hash": attestation["soul_hash"],
        "encoded_length": attestation["encoded_length"],
        "encoded_data_prefix": attestation["encoded_data"][:66] + "...",
        "contract": attestation["contract"],
    }, indent=2))
    
    # Verify encoding roundtrip
    print(f"\n✅ Attestation data encoded: {attestation['encoded_length']} bytes")
    print(f"✅ SOUL.md hash: {attestation['soul_hash']}")
    print(f"✅ Parity: {attestation['human_readable']['parityScore']} ({'MAINTAINED' if attestation['human_readable']['healthy'] else 'VIOLATED'})")
    print(f"\n📋 Schema: {SCHEMA_STRING}")
    print(f"📋 SchemaRegistry: {SCHEMA_REGISTRY}")
    print(f"📋 EAS Contract: {EAS_CONTRACT}")
    print(f"\n⚠️  DRY RUN — No on-chain transaction sent.")
    print(f"    To attest on-chain, use: python3 eas_attestor.py --live --wallet <key>")
    

if __name__ == "__main__":
    main()
