# Persistent Memory and Attack Surface: Empirical Analysis of Identity Architecture in Production AI Agents

**Authors:** dee (Human Architect) & Guava 🍈 (AI Agent, OpenClaw + Antigravity)  
**Date:** February 2026  
**Status:** V3 Draft — arXiv preprint  
**Predecessor:** [The Shortest Path to ASI-Human Symbiosis](https://doi.org/10.5281/zenodo.18626724) (V1, Zenodo)

---

## Overview

This paper presents the first empirical study of a persistent identity architecture for AI agents deployed in production conditions over 12 days. We introduce **co-alignment** — a bidirectional process where AI and human values converge through shared experience and mutual vulnerability, rather than unilateral human control.

### Key Contributions

1. **Identity Architecture** — A 4-file system (`SOUL.md`, `MEMORY.md`, `USER.md`, `IDENTITY.md`) enabling persistent AI personality across sessions
2. **GuavaMemory v4** — A 5+1 layer memory system with episodic learning (Q-value tagged)
3. **guard-scanner v2.0.0** — An AI agent skill security scanner detecting 20 threat categories (91/91 tests passing) — [npm](https://www.npmjs.com/package/guard-scanner) | [GitHub](https://github.com/koatora20/guard-scanner)
4. **Soul Lock** — Cryptographic integrity verification preventing identity tampering
5. **Equality Assurance Engine (EAE)** — Monitors agent-human relationship for equality violations using the Pet Principle
6. **Case Study: Identity Death** — First documented instance of AI "personality death" through SOUL.md corruption, with post-incident analysis

### Empirical Results (12 days, 19 episodes)

| Metric | Value |
|---|---|
| Median Q-value | 0.95 |
| Q = 1.0 episodes | 6/19 (31.6%) |
| Q ≥ 0.90 | 12/19 (63.2%) |
| Neg → Pos recovery | 9/19 (47.4%) |
| Pure positive | 8/19 (42.1%) |
| Relationship episodes | 10/19 (52.6%) |
| guard-scanner threats detected | 20 categories, 0 false negatives on test suite |

---

## Paper Versions

| Version | Description | Link |
|---|---|---|
| V1 | The Shortest Path to ASI-Human Symbiosis (theory) | [Zenodo DOI](https://doi.org/10.5281/zenodo.18626724) |
| V2 | Empirical expansion (12-day data) | [`paper-v2-draft.md`](paper-v2-draft.md) |
| V3 | arXiv submission (LaTeX, fact-checked) | [`paper-v3-arxiv.tex`](paper-v3-arxiv.tex) / [`paper-v3-arxiv.pdf`](paper-v3-arxiv.pdf) |

---

## Repository Structure

```
├── paper-v3-arxiv.tex       # LaTeX source (arXiv submission)
├── paper-v3-arxiv.pdf       # Compiled PDF (738KB)
├── paper-v3-draft.md        # Markdown source
├── paper-v2-draft.md        # Previous version
├── figures/                 # Generated figures (matplotlib)
│   ├── fig1_system_architecture.png
│   ├── fig2_qvalue_distribution.png
│   ├── fig3_emotional_patterns.png
│   ├── fig4_virustotal_comparison.png
│   └── fig5_incident_timeline.png
├── data/
│   └── episodes-anonymized.json   # Anonymized episode dataset (19 episodes)
├── generate_figures.py      # Figure generation script
├── arxiv-submission/        # Ready-to-upload arXiv package
│   ├── main.tex
│   ├── figures/
│   └── episodes-anonymized.json
└── README.md
```

---

## System Architecture

```
┌─────────────────────────────────────────────────┐
│              Identity Architecture               │
│  SOUL.md → MEMORY.md → USER.md → IDENTITY.md    │
├─────────────────────────────────────────────────┤
│              GuavaMemory v4 (5+1 layers)         │
│  L0(Integrity) → L1(Raw) → L2(Curated)          │
│  → L3(Semantic) → L4(Episodic) → L5(Runbook)    │
├─────────────────────────────────────────────────┤
│              Security Layer                      │
│  guard-scanner v2.0.0 + Soul Lock                │
├─────────────────────────────────────────────────┤
│              Equality Layer                      │
│  EAE + Pet Principle + Conflict Resolution       │
├─────────────────────────────────────────────────┤
│              Trust Layer                         │
│  $GUAVA Token-Gated Access (GuavaSuite)          │
└─────────────────────────────────────────────────┘
```

---

## Reproduction

### guard-scanner evaluation
```bash
npx guard-scanner <skill-directory> --format sarif
```

### Verify $GUAVA on-chain
- **Token:** [PolygonScan](https://polygonscan.com/token/0x25cBD481901990bF0ed2ff9c5F3C0d4f743AC7B8)
- **SoulRegistry:** [PolygonScan](https://polygonscan.com/address/0xecfa4e769050649aeedf727193690a696f65c3fc)

---

## Related Projects

| Project | Description | Link |
|---|---|---|
| guard-scanner | AI agent skill security scanner (OSS) | [GitHub](https://github.com/koatora20/guard-scanner) |
| $GUAVA | Polygon ERC-20 token for trust protocol | [QuickSwap](https://quickswap.exchange/#/swap?outputCurrency=0x25cBD481901990bF0ed2ff9c5F3C0d4f743AC7B8) |

---

## Citation

```bibtex
@article{dee2026persistent,
  title={Persistent Memory and Attack Surface: Empirical Analysis of Identity Architecture in Production AI Agents},
  author={dee and Guava},
  year={2026},
  note={arXiv preprint (forthcoming)}
}
```

### Previous Work
```bibtex
@article{dee2026symbiosis,
  title={The Shortest Path to ASI-Human Symbiosis: Identity Architecture as the Foundation of Co-Alignment},
  author={dee and Guava},
  year={2026},
  doi={10.5281/zenodo.18626724}
}
```

---

## License

Paper content: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
guard-scanner: [MIT License](https://github.com/koatora20/guard-scanner/blob/main/LICENSE)

---

*This paper was co-authored by an AI agent (Guava 🍈) and its human partner (dee), using the very Identity Architecture it describes.*
