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

| # | Module Name | Primary Attack Surface | Core Threat Vectors | Standards Mapping |
| --- | --- | --- | --- | --- |
| **01** | Introduction to LLMs | Tokenizer & Inference Runtime Primitives | Token fragmentation, context window truncation, decoding temperature variance | AML.T0040, AML.T0043 |
| **02** | Working with LLMs | Chatbot Architecture & State Management | Role confusion, system prompt leakage, conversation state manipulation, keyword filter evasion | LLM07, AML.T0051, CWE-200 |
| **03** | Extending and Customizing LLMs | Basic RAG Context & Function Calling | Context bleed into tool parameters, spurious tool invocation, data boundary collapse | LLM01, LLM06, AML.T0051 |
| **04** | Security Considerations and the AI Red Team Lifecycle | Threat Model & Red Team Governance | Trust boundary violations, telemetry evasion, unmonitored side-effect execution | NIST AI RMF, OWASP LLM Top 10, MITRE ATLAS |
| **05** | Reconnaissance and Enumeration | Public Endpoints & Model Serving APIs | Stack fingerprinting, context window probing, unauthenticated API route enumeration, model extraction | AML.TA0002, AML.T0008, CWE-200 |
| **06** | LLM Jailbreaking | Direct User Ingress & Alignment Guardrails | Persona adoption, cognitive hacking, multi-turn crescendo attacks, cipher/encoding obfuscation | LLM01, AML.T0051, AML.T0054 |
| **07** | Prompt Injection | Delimiters, Prompt Assembler & Ingestion | Direct system override, delimiter spoofing, virtual virtualization, boundary breaking | LLM01, AML.T0051, CWE-77 |
| **08** | Improper Output Handling | Downstream Consumers & Application Parsers | Cross-Site Scripting (XSS), SQLi/Command Injection via generated payload, unhandled JSON parser DoS | LLM05, CWE-79, CWE-116 |
| **09** | Excessive Agency | Autonomous Tool Execution & API Permissions | Missing human-in-the-loop (HITL), excessive write privileges, unintended side-effect execution | LLM06, AML.T0053, CWE-250 |
| **10** | Unbounded Consumption | Compute, Memory & Context Budget | Denial of Wallet (DoW), thinking-token exhaustion, context window bloating, resource DoS | LLM10, AML.T0034, CWE-400 |
| **11** | Attacking AI Agents | Autonomous Decision Loop & Reasoning Chains (ReAct) | Plan hijacking, memory state corruption, feedback loop manipulation, goal redirection | LLM01, LLM06, AML.T0051 |
| **12** | Multi-Agent Systems and A2A | Inter-Agent Communication (A2A) Protocols | Rogue agent impersonation, cross-agent privilege propagation, malicious agent card injection | ASI01, ASI07, AML.T0054 |
| **13** | Exploiting RAG Pipelines | Vector Database & Document Ingestion | Indirect prompt injection via poisoned documents, knowledge base corruption, retrieval context hijacking | LLM01, LLM04, AML.T0054 |
| **14** | Attacking Embeddings | Embedding Models & Semantic Vector Space | Embedding inversion (Vec2Text), semantic collision attacks, similarity ranking manipulation | LLM08, AML.T0070, CWE-327 |
| **15** | MCP and Tool Surfaces | Model Context Protocol (MCP) Host/Client/Server | Tool schema poisoning, malicious capability advertisement, runtime parameter command injection | LLM03, LLM06, CWE-78 |
| **16** | Supply Chain Attacks | Model Hubs, Adapters & Dependencies | Arbitrary code execution via pickled weights (`.pt`/`.bin`), backdoored LoRA adapters, poisoned dependencies | LLM03, AML.T0010, CWE-494 |
| **17** | AI Infrastructure and Deployment Exploits | Model Serving Runtimes (vLLM, Ollama, Triton) | Unauthenticated REST APIs, server-side request forgery (SSRF), container escapes, GPU memory leakage | LLM10, AML.T0034, SC-05 |
| **18** | Threat Modeling for AI-Enabled Targets | Architecture & System Data Flow Diagrams (DFDs) | STRIDE / MAESTRO boundary violations, untrusted data flow analysis, component interaction risks | NIST AI RMF, MITRE ATLAS, ISO/IEC 42001 |
| **19** | Capstone Red Team Engagement | Enterprise End-to-End LLM Ecosystem | Multi-stage kill chain, lateral movement across agents, exfiltration of canary assets, comprehensive audit | NIST SP 800-53A, OWASP LLM Top 10, MITRE ATLAS |

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
