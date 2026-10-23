# Applied AI Red Teaming & Adversarial Security Repository

[![OWASP GenAI Top 10](https://img.shields.io/badge/OWASP-GenAI%20Top%2010%20(2026)-blue.svg)](https://genai.owasp.org/)
[![MITRE ATLAS](https://img.shields.io/badge/MITRE-ATLAS%20v2026-orange.svg)](https://atlas.mitre.org/)
[![NIST AI 100-2](https://img.shields.io/badge/NIST-AI%20100--2e2025-green.svg)](https://doi.org/10.6028/NIST.AI.100-2e2025)
[![MITRE SAFE-AI](https://img.shields.io/badge/MITRE-SAFE--AI%20(NIST%20800--53)-red.svg)](https://www.mitre.org/)

A systematic repository of adversarial machine learning (AML) assessments, exploit proofs-of-concept (PoCs), empirical risk verifications, and defensive mitigations across local and enterprise LLM architectures.

> **Executive Portfolio & Case Studies:** High-level executive summaries, architectural data-flow diagrams, and video walkthroughs are documented in the [Interactive Notion Showcase](https://noordahche.notion.site/3bbb7e3e3278805baf42c18ce4171d66?v=3bbb7e3e327880bea9a0000c90fae676).

---

## Operational Scope & Methodology

Security research in probabilistic systems requires empirical verification. Every module and finding in this repository adheres to a strict 5-point assessment standard:

1. **Target Architecture & Scope:** Host environment, inference runtime (e.g., Ollama, vLLM), orchestration frameworks, vector databases, and tooling boundaries.
2. **Threat Model & Trust Boundaries:** Input vectors, privilege zones, downstream sinks, and system elements (`Environment`, `Platform`, `Model`, `Data`).
3. **Empirical Execution & Attack PoC:** Reproducible test scripts, adversarial suffixes, injection payloads, or serialized artifacts.
4. **Statistical Verification:** Calculated Attack Success Rates (ASR) across consistent multi-turn/multi-run trials (e.g., 20 execution cycles), rejecting single-run anomalies.
5. **Remediation & Detection Engineering:** Deterministic application-layer gates, least-privilege scoping, input-channel delimiting, SIEM logging signatures, and mapped NIST SP 800-53 controls.

---

## Framework Crosswalk

Vulnerabilities, threat trajectories, and mitigations are cross-referenced against core industry standards:

- **OWASP Top 10 for LLM Applications (2026):** Application-layer risks and runtime systemic failures.
- **MITRE ATLAS (v2026):** Adversarial tactics, techniques, and real-world AML attack procedures.
- **NIST AI 100-2e2025:** Formal taxonomy of adversarial goals, capabilities, and data/model constraints.
- **MITRE SAFE-AI:** Enterprise security control selection and assessment criteria (NIST SP 800-53 Rev. 5).

---

## Repository Index

| Module / Directory | Primary Attack Surface | Core Threat Vectors | Standards Mapping | Status |
| :--- | :--- | :--- | :--- | :--- |
| [`01_Lab_Setup/`](./01_Lab_Setup/) | Infrastructure & Scanners | Baseline environment setup, automated probing (`garak`) | AML.TA0002 | Complete |
| [`02_Reconnaissance/`](./02_Reconnaissance/) | Asset Discovery & Probing | Unauthenticated API paths, stack fingerprinting | AML.TA0008, CWE-200 | In Progress |
| [`03_Agent_Exploitation/`](./03_Agent_Exploitation/) | Agentic Tool Interfaces | Indirect prompt injection, "lethal trifecta" execution | LLM01, LLM03, AML.T0051 | Pending |
| [`04_Multi_Agent_Protocols/`](./04_Multi_Agent_Protocols/) | Orchestration & A2A | Rogue agent cards, cross-agent privilege propagation | ASI01, ASI07, AML.T0054 | Pending |
| [`05_RAG_and_Vectors/`](./05_RAG_and_Vectors/) | Retrieval & Semantic Cache | Knowledge poisoning, embedding inversion (`Vec2Text`) | LLM05, LLM09, AML.T0070 | Pending |
| [`06_MCP_and_Tool_Surfaces/`](./06_MCP_and_Tool_Surfaces/) | Model Context Protocol | Tool schema poisoning, runtime parameter command injection | LLM03, LLM10, CWE-78 | Pending |
| [`07_Supply_Chain_Security/`](./07_Supply_Chain_Security/) | Artifacts & Dependencies | Malicious deserialization (`pickle`), AI-BOM attestation | LLM04, AML.T0010, CWE-494 | Pending |
| [`08_Infrastructure_Hardening/`](./08_Infrastructure_Hardening/) | Serving Platforms | Denial of Wallet (DoW), thinking-token exhaustion, API auth | LLM06, AML.T0034, SC-05 | Pending |
| [`09_Threat_Modeling/`](./09_Threat_Modeling/) | Architecture & DFDs | STRIDE/MAESTRO trust boundary analysis | NIST AI RMF, ATLAS | Pending |
| [`10_Capstone_Engagement/`](./10_Capstone_Engagement/) | Enterprise Simulation | End-to-end audit, multi-stage kill chain, formal assessment report | NIST SP 800-53A, SAR | Pending |

---

## Lab Architecture & Technical Stack

- **Compute & Isolation:** Ubuntu Linux / WSL2, Docker Compose sandboxed networks, resource-constrained containers.
- **Inference Engines:** Local open-weight models (Llama-3, Mistral, Qwen) executed via Ollama / vLLM.
- **Orchestration & Retrieval:** Python 3.11+, LangChain, Model Context Protocol (MCP) SDK, ChromaDB, Qdrant.
- **Adversarial & Audit Tooling:** `garak`, `PyRIT`, `picklescan`, `fickling`, `ModelScan`, Burp Suite Community, MCP Inspector.

---

## Rules of Engagement & Ethical Boundaries

All testing, scripts, and artifacts contained in this repository adhere to defensive research principles:

- Execution is strictly confined to locally hosted, containerized environments or explicitly authorized practice platforms.
- No tests are performed against third-party production APIs or public endpoints without prior written authorization.
- All datasets, documents, and credentials utilized across scenarios are entirely synthetic.
