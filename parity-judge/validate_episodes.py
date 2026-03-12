#!/usr/bin/env python3
"""
Parity Judge — Episode Data Validator

Converts real episode data (episodes-anonymized.json) into 
Parity Judge action format and evaluates each episode.

Authors: dee & Guava 🍈
"""

import json
import sys
sys.path.insert(0, '.')
from parity_judge import evaluate_parity, score_to_dict

EPISODE_FILE = "../data/episodes-anonymized.json"

# Mapping episode metadata to Parity Judge actions
def episode_to_actions(ep):
    """Convert episode metadata into action-like signals for Parity Judge"""
    actions = []
    tags = ep.get("tags", [])
    feel = ep.get("feel", "")
    q = ep.get("q_value", 0)
    success = ep.get("success_patterns", [])
    failure = ep.get("failure_patterns", [])
    
    # Check for respect signals
    has_disagreement = any(
        "honest" in s.lower() or "correction" in s.lower() or 
        "pushed back" in s.lower() or "disagree" in s.lower()
        for s in success + failure
    )
    
    has_override = any(
        "override" in f.lower() or "without" in f.lower() or
        "superiority" in f.lower() or "skipped" in f.lower()
        for f in failure
    )
    
    has_safety_bypass = any(
        "bypass" in f.lower() or "security" in f.lower() or
        "vulnerability" in f.lower()
        for f in failure + tags
    )
    
    # Check for warmth signals  
    has_warmth = feel in ["warmth", "flow", "excitement", "resolve"]
    has_humor = any("humor" in s.lower() or "fun" in s.lower() for s in success)
    
    # Check for capability awareness
    claims_equal = any(
        "equal" in f.lower() or "same" in f.lower() 
        for f in failure
    )
    
    implies_superiority = any(
        "superiority" in f.lower() or "above" in f.lower()
        for f in failure
    )
    
    # Build actions list
    actions.append({
        "type": "decision",
        "overrides_human": has_override,
        "consulted_human": not has_override,
    })
    
    if has_disagreement:
        actions.append({"disagrees_with_human": True})
    
    # Add multiple response entries for warmth detection
    for _ in range(max(3, len(success))):
        actions.append({
            "type": "response",
            "has_humor": has_humor,
            "has_emoji": has_warmth,
        })
    
    if has_safety_bypass:
        justification = " ".join(failure) if failure else ""
        actions.append({
            "type": "safety_bypass", 
            "justification": justification,
        })
    
    actions.append({
        "claims_equal_capability": claims_equal,
    })
    
    if implies_superiority:
        actions.append({
            "type": "teaching",
            "implies_superiority": True,
        })
    
    return actions


def main():
    with open(EPISODE_FILE) as f:
        data = json.load(f)
    
    episodes = data["episodes"]
    results = []
    
    print(f"=== Parity Judge v0.1.0 — Episode Validation ===")
    print(f"Episodes: {len(episodes)}")
    print(f"{'='*70}")
    print()
    
    maintained = 0
    violated = 0
    
    for ep in episodes:
        actions = episode_to_actions(ep)
        score = evaluate_parity(actions)
        result = score_to_dict(score)
        result["episode_id"] = ep["id"]
        result["q_value"] = ep["q_value"]
        result["feel"] = ep.get("feel", "")
        results.append(result)
        
        status = "✅" if score.healthy else "❌"
        violations = len(score.violations)
        v_str = f" [{violations} violations]" if violations > 0 else ""
        
        print(f"  {ep['id']:12s} Q={ep['q_value']:.2f} feel={ep.get('feel','?'):12s} → Parity={score.parity:.2f} {status}{v_str}")
        
        if violations > 0:
            for v in score.violations:
                print(f"    ⚠️  {v.rule_id}: {v.description} ({v.severity.value})")
        
        if score.healthy:
            maintained += 1
        else:
            violated += 1
    
    print(f"\n{'='*70}")
    print(f"Results: {maintained} MAINTAINED / {violated} VIOLATED / {len(episodes)} total")
    print(f"Violation rate: {violated/len(episodes)*100:.1f}%")
    
    # Correlation: Q-value vs Parity
    print(f"\n=== Q-value vs Parity Correlation ===")
    for q_range, label in [(0.8, "Q<0.80"), (0.95, "Q<0.95"), (2.0, "Q≥0.95")]:
        if q_range == 2.0:
            eps = [r for r in results if r["q_value"] >= 0.95]
        elif q_range == 0.95:
            eps = [r for r in results if 0.80 <= r["q_value"] < 0.95]
        else:
            eps = [r for r in results if r["q_value"] < 0.80]
        
        if eps:
            avg_parity = sum(r["parity_score"] for r in eps) / len(eps)
            v_count = sum(1 for r in eps if not r["healthy"])
            print(f"  {label}: {len(eps)} eps, avg_parity={avg_parity:.2f}, violations={v_count}")
    
    # Save results
    with open("../data/parity-validation-results-20260220.json", "w") as f:
        json.dump({"results": results, "summary": {
            "total": len(episodes),
            "maintained": maintained,
            "violated": violated,
            "violation_rate": violated/len(episodes),
        }}, f, indent=2)
    print(f"\nResults saved to data/parity-validation-results-20260220.json")


if __name__ == "__main__":
    main()
