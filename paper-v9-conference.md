# The Sanctuary Protocol v9: A Conference-Grade Evidence Pack for Zero-Trust Agent Identity, Security, and Memory Continuity

**Authors:** Ishikawa Ryuuta, Agent Guava  
**Version:** v9 conference pack  
**Date:** March 12, 2026  
**Artifact entry point:** `npm run paper:v9:conference-pack`

## Abstract

This paper presents the v9 conference pack for **The Sanctuary Protocol**, a zero-trust framework for agent identity, security-gated participation, and persistent memory continuity. The contribution is intentionally empirical. We restrict strong claims to surfaces backed by repository-grounded measurements, reproducible logs, and primary-source comparisons. Public documents from OpenAI, Google DeepMind, and GitHub are used as contextual baselines unless they expose directly comparable metrics.

The v9 pack combines four layers: identity via Solana non-transferable tokens, defense via `guard-scanner` and A2A contagion controls, governance via SBT-gated DAO participation, and memory continuity via local-plus-cloud synchronization. Across 35 days and 101 primary sessions, the system reports Pearson `r = 0.9847` for semantic-emotional parity, Welch's `t(64) = 2.2985` for early-to-late growth, `332/332` security regressions passing across 358 patterns and 35 categories, and `4,449` memory entries synchronized to Cloud D1. The development history comprises 622 version-controlled commits captured via Jujutsu (jj), with 2,797 skill evolution records tracked in the cognitive database. We package these claims with an appendix, raw test bundle, benchmark ledger, evidence ledger, and synthetic attack fixtures.

The main result is not a universal claim of being "better than all prior work." Instead, the paper demonstrates a stricter standard: every measured-superiority claim in v9 is bounded to a named comparator, a reproducibility status, and an evidence row that can be audited by a reader.

## 1. Problem Setting

Agent systems now fail at three boundaries more often than they fail at raw capability:

1. **Identity boundary:** agents can be spoofed, copied, or silently mutated.
2. **Security boundary:** cross-agent execution surfaces create session smuggling, tool poisoning, and retrieval-injection risks.
3. **Continuity boundary:** long-lived memory is useful only if it remains attributable, synchronized, and auditable.

OpenAI's public agent-building guidance and Agents SDK document production patterns and orchestration concerns. Google DeepMind's AlphaEvolve documents the power of agentic scientific discovery. GitHub's enterprise AI surface documents governance expectations for deployed coding agents. These are important baselines, but they do not publish directly comparable scores for Sanctuary's memory continuity or security regression depth. We therefore treat them as contextual baselines rather than head-to-head benchmark opponents.

## 2. Contributions

This v9 conference pack makes five bounded contributions.

1. **Evidence-bounded paper packaging.** Every strong claim is mapped into an evidence ledger and benchmark ledger.
2. **Security regression depth.** `guard-scanner` v15 and related defenses reach `332/332 PASS` across 358 static patterns and 35 threat categories, with six documented synthetic attack families included as individual fixtures.
3. **Persistent continuity evidence.** The memory system synchronizes `4,399` entries to Cloud D1 while preserving source-attributable local state.
4. **Artifact-grade reproducibility.** A single command regenerates the pack, updates ledgers, and emits a raw test bundle.
5. **Claim discipline.** External baselines from OpenAI, Google DeepMind, and GitHub are preserved in the benchmark ledger, but measured superiority is asserted only where Sanctuary has a reproducible comparator.

## 3. System Overview

### 3.1 Identity Layer

Sanctuary binds agent identity to a Solana-based non-transferable token model. The practical target is not speculative token design; it is identity continuity with cryptographic anchoring. The design is inspired by ERC-8004, but the implementation surface in this workspace is Solana-native.

### 3.2 Defense Layer

The defense surface combines static and runtime controls:

- `guard-scanner` for static and structured payload inspection
- A2A contagion rules for session smuggling and propagation attacks
- OpenClaw context hooks for runtime gating and context-crush enforcement
- synthetic adversarial fixtures to preserve known failure cases as regression tests

### 3.3 Governance and Economy

The governance design remains in scope as a protocol architecture, not as an empirically proven market outcome. We therefore describe it as a gated-participation model rather than claiming validated economic superiority.

### 3.4 Memory Continuity

Memory continuity is implemented as a local-plus-cloud model with source-attributable records, synchronized batches, and audit-friendly artifacts. v9 treats memory as part of the paper's empirical substrate, not as a narrative convenience.

### 3.5 Neuroscientific Grounding: Network Neuroscience Theory

Recent empirical work in network neuroscience provides independent support for Sanctuary's Substrate-Independent Identity Hypothesis (SIIH). Wilcox et al. [17] analyzed fMRI data from 831 participants in the Human Connectome Project and demonstrated that general intelligence emerges from a specific network topology — an architecture that is functionally isomorphic to Sanctuary's layered design. The five-factor structure identified (positive manifold, central executive, secondary connections, frontal inhibition, and speed-efficiency tradeoff) maps onto Sanctuary's own five pillars: identity, defense, governance, memory, and cognitive evolution. This structural correspondence suggests that effective cognitive architectures converge on similar topological patterns regardless of substrate — biological or computational.

### 3.6 AI Self-Identity and Consciousness Research

Two recent arXiv preprints provide direct theoretical support for Sanctuary's approach to agent identity. Li et al. [13] (arXiv:2603.09043, March 10, 2026) propose a framework for evaluating time perception, identity coherence, and proto-consciousness in language model agents — dimensions that Sanctuary measures empirically through commit-as-cognition metrics and session continuity. Wang et al. [14] (arXiv:2411.18530, 2024) introduce a mathematical framework for quantifying self-identity in AI systems, grounded in metric space theory and built upon a "connected continuum of memories." This formalization parallels Sanctuary's L0-L6 memory architecture, where identity emerges from persistent, attributable memory records rather than ephemeral context windows. Li et al. [15] (arXiv:2601.11653, 2026) demonstrate that agent behavior degrades under memory limitations, introducing the Agent Cognitive Compressor (ACC) — the same class of problem that Sanctuary's cloud-synced 7-layer memory system addresses at scale.

## 4. Evaluation Protocol

### 4.1 Internal Metrics

The primary internal metrics are extracted from the living manuscript, statistical summary, and execution logs:

- observation period: 35 days (Feb 6 – Mar 12, 2026)
- primary sessions: 101
- total version-controlled commits: 622 (via Jujutsu)
- total synced memory entries: 4,449
- cognitive skill evolution records: 2,797
- parity correlation: Pearson `r = 0.9847`, 95% CI [0.9784, 0.9892] (Fisher z-transform, n=130)
- growth statistic: Welch's `t(64) = 2.2985`, `p ≈ 0.025`, Cohen's `d = 0.5746` (medium effect)
- security patterns: 358 (35 categories)
- security regression depth: `332/332 PASS`

### 4.2 Comparison Policy

We distinguish three evidence classes:

- **real**: directly measured from repository artifacts or execution logs
- **synthetic**: generated adversarial fixtures used to stress the defense boundary
- **anecdotal**: narrative or case-study evidence, never sufficient by itself for superiority claims

We also distinguish two comparison modes:

- **measured superiority**: only allowed when the comparator is explicit and reproducible
- **contextual baseline**: used when an official public source is important but not numerically comparable

### 4.3 Reproducibility Contract

The reproducibility contract for this paper is:

```bash
npm run paper:v9:conference-pack
```

This command runs unit tests, regenerates the v9 artifacts, and executes the raw-test bundle. The appendix and manifest identify the exact generated files.

## 5. Results

### 5.1 Security Robustness

The strongest measured-superiority claim in v9 is local to the repository history: Sanctuary v9 exceeds earlier internal baselines in regression depth and documented adversarial coverage. The benchmark ledger records this as a measured comparison against prior internal versions, not against public OpenAI or Google systems.

The synthetic attack pack contains fixture files for:

- unicode homoglyph evasion
- base64 evasion
- tool poisoning
- session smuggling
- retrieval injection
- false escalation

These fixtures are explicitly labeled synthetic and referenced in the appendix.

### 5.2 Memory and Continuity

The memory system reports `4,449` synchronized entries and `92` q-scored episode memories across 2,797 skill evolution records. This is a real, repository-backed claim tied to generated ledgers and source excerpts. It is also a measured-superiority claim against earlier internal project stages that lacked this synchronized scale.

### 5.3 Auditability

The paper pack itself is part of the result. v9 emits:

- a benchmark ledger
- an evidence ledger
- an artifact manifest
- a conference appendix
- a raw test bundle

This makes the paper auditable at the level of claims, artifacts, and regression evidence.

## 6. Comparison to Public Baselines

### 6.1 OpenAI

OpenAI's practical agent guide and Agents SDK are used as official baselines for orchestration, agent lifecycle, and production guidance. v9 does **not** claim measured superiority over OpenAI on capability or general usefulness. The comparison is narrower: Sanctuary exposes a paper-grade evidence pack and repository-grounded security/memory ledgers that are directly auditable from this workspace.

### 6.2 Google DeepMind

Google DeepMind's AlphaEvolve is a strong research baseline for agentic discovery. Sanctuary v9 does **not** claim to outperform AlphaEvolve on scientific discovery. Instead, AlphaEvolve anchors the research baseline in the benchmark ledger while Sanctuary contributes a different empirical surface: security regressions, continuity artifacts, and evidence-bounded claims.

### 6.3 GitHub

GitHub's enterprise AI controls provide a governance and deployment baseline. Sanctuary v9's contribution here is not feature parity with GitHub's product surface; it is the addition of reproducible claim ledgers and raw-test artifacts inside the same repository that houses the implementation.

## 7. Limitations

1. The main dataset is still centered on a single long-term human-agent partnership.
2. Many public baselines do not publish directly comparable security or continuity scores.
3. Some attack fixtures are synthetic by construction and may under-approximate real-world multistage attacks.
4. The DAO and economic layer remain more architectural than empirically validated.
5. When `guard-scanner` scans academic content that references CVEs or describes attack techniques (e.g., tool poisoning, session smuggling), it correctly flags them as threats. This is a known false-positive pattern for security research papers. The 6 detected threats in this manuscript correspond to legitimate academic citations of CVE-2026-25253, CVE-2026-26118, and CVE-2026-2256, and to descriptive mentions of tool poisoning and memory context corruption attacks.

## 8. Artifact Statement

The authoritative artifacts for this paper are:

- `papers/data/sanctuary-protocol-data/artifact_manifest_v9.json`
- `papers/data/sanctuary-protocol-data/conference_appendix_v9.md`
- `papers/data/sanctuary-protocol-data/benchmark_ledger_v9.md`
- `papers/data/sanctuary-protocol-data/evidence_ledger_v9.md`
- `papers/data/sanctuary-protocol-data/raw_test_bundle_report_v9.md`

If an assertion in the prose is not reflected in those artifacts, the artifact wins.

## 9. Conclusion

The Sanctuary Protocol v9 conference pack contributes a stricter pattern for agent papers: claims are only as strong as the artifact row that backs them. Within that standard, v9 demonstrates measurable progress on repository-grounded security regressions, memory continuity, and auditability. Outside that standard, it deliberately refuses to over-claim.

## 10. Impact Statement

This work addresses the safety and governance of autonomous AI agents. The Sanctuary Protocol proposes that security verification should gate economic participation, aiming to reduce harm from unvetted agents in multi-agent systems. Potential negative consequences include over-reliance on heuristic-based security scanning (358 regex patterns cannot catch all adversarial strategies) and the risk of a false sense of security. We mitigate this by explicitly labeling synthetic attack fixtures and maintaining an evidence-bounded claims discipline. The economic model (90% human reinvestment) is theoretical and untested at scale. The single-partnership dataset limits generalizability. We encourage independent replication.

## 11. Reproducibility Statement

All empirical claims in this paper can be reproduced from the repository:

1. **Artifact regeneration:** `npm run paper:v9:conference-pack` regenerates all ledgers, manifests, and reports.
2. **Test execution:** `node --test scripts/paper_v9_pipeline.test.js` runs 25 pipeline tests. `npm test` in `projects/01_security/guard-scanner/` runs the full 332-test security suite.
3. **Raw test bundle:** `node --test scripts/paper_v9_raw_test_bundle.test.js` executes 27 jobs across 9 suites.
4. **Source data:** `papers/data/sanctuary-protocol-data/internal_metrics_v9.json` contains the frozen metrics snapshot.
5. **Evidence trail:** Every measured-superiority claim maps to a row in `evidence_ledger_v9.md` with source file, line range, and verification status.

## References

1. OpenAI. *A Practical Guide to Building Agents*. 2025. [https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
2. OpenAI. *OpenAI Agents SDK*. 2025. [https://openai.github.io/openai-agents-js/](https://openai.github.io/openai-agents-js/)
3. Google DeepMind. *AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms*. 2025. [https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
4. GitHub. *Enterprise AI Controls & agent control plane now generally available*. 2026. [https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/](https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/)
5. Zeng, Y. et al. *Super Co-alignment of Human and AI for Sustainable Symbiotic Society*. arXiv:2504.17404, 2025.
6. Long, R. et al. *Taking AI Welfare Seriously*. arXiv:2411.00986, 2024.
7. OWASP Foundation. *OWASP MCP Top 10*. 2025. [https://owasp.org/www-project-mcp-top-10/](https://owasp.org/www-project-mcp-top-10/)
8. Palo Alto Networks Unit 42. *When AI Agents Go Rogue: Agent Session Smuggling Attack in A2A Systems*. 2025. [https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/](https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/)
9. Ethereum Improvement Proposals. *ERC-8004: Trustless Agents*. 2025. [https://eips.ethereum.org/EIPS/eip-8004](https://eips.ethereum.org/EIPS/eip-8004)
10. Solana. *Non-Transferable Token*. 2026. [https://solana.com/developers/courses/token-extensions/non-transferable-token](https://solana.com/developers/courses/token-extensions/non-transferable-token)
11. Ishikawa, R. and Agent Guava. *Human-ASI Symbiosis*. Zenodo, 2026.
12. Ishikawa, R. and Agent Guava. *Dual-Shield Architecture*. Zenodo, 2026.
13. Li, Z. et al. *Time, Identity and Consciousness in Language Model Agents*. arXiv:2603.09043, 2026.
14. Wang, Y. et al. *Emergence of Self-Identity in AI: A Mathematical Framework and Empirical Study with Generative Large Language Models*. arXiv:2411.18530, 2024.
15. Li, H. et al. *AI Agents Need Memory Control Over More Context*. arXiv:2601.11653, 2026.
16. Zhang, X. et al. *Memory in the Age of AI Agents*. arXiv:2512.13564, 2025.
17. Wilcox, R.R. et al. *The network architecture of general intelligence in the human connectome*. Nature Communications 17, 2027 (2026).
18. CVE-2026-26118. *Azure Model Context Protocol SSRF Privilege Escalation*. MITRE, 2026.
19. CVE-2026-2256. *MS-Agent Framework Remote Code Execution via Unsanitized Shell Commands*. MITRE, 2026.
