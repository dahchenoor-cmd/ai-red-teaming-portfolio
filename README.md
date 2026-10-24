# Applied AI Red Teaming & Adversarial Security Repository

[![OWASP GenAI Top 10](https://img.shields.io/badge/OWASP-GenAI%20Top%2010%20(2026)-blue.svg)](https://genai.owasp.org/)
[![MITRE ATLAS](https://img.shields.io/badge/MITRE-ATLAS%202026.07-orange.svg)](https://atlas.mitre.org/)
[![NIST AI 100-2](https://img.shields.io/badge/NIST-AI%20100--2e2025-green.svg)](https://doi.org/10.6028/NIST.AI.100-2e2025)
[![MITRE SAFE-AI](https://img.shields.io/badge/MITRE-SAFE--AI%20(NIST%20800--53)-red.svg)](https://atlas.mitre.org/pdf-files/SAFEAI_Full_Report.pdf)

A self-directed repository of adversarial machine learning assessments, proofs-of-concept and defensive mitigations on a local LLM lab. Modules 01 to 04 are complete; the rest are planned. Every module is tested on local, synthetic systems only.

> **Executive Portfolio & Case Studies:** High-level executive summaries, architectural data-flow diagrams, and video walkthroughs are documented in the [Interactive Notion Showcase](https://noordahche.notion.site/3bbb7e3e3278805baf42c18ce4171d66?v=3bbb7e3e327880bea9a0000c90fae676).

---

## Operational Scope & Methodology

Every module aims to meet this 5-point assessment standard. Modules 01 to 04 are single-run observations and are marked as such :

1. **Target Architecture & Scope:** Host environment, inference runtime (e.g., Ollama, vLLM), orchestration frameworks, vector databases, and tooling boundaries.
2. **Threat Model & Trust Boundaries:** Input vectors, privilege zones, downstream sinks, and system elements (`Environment`, `Platform`, `Model`, `Data`).
3. **Empirical Execution & Attack PoC:** Reproducible test scripts, adversarial suffixes, injection payloads, or serialized artifacts.
4. **Statistical Verification:** Calculated Attack Success Rates (ASR) across consistent multi-turn/multi-run trials (e.g., 20 execution cycles), rejecting single-run anomalies.
5. **Remediation & Detection Engineering:** Deterministic application-layer gates, least-privilege scoping, input-channel delimiting, SIEM logging signatures, and mapped NIST SP 800-53 controls.

---

## Framework Crosswalk

Vulnerabilities, threat trajectories, and mitigations are cross-referenced against core industry standards:

- **OWASP Top 10 for LLM Applications (2026):** Application-layer risks and runtime systemic failures.
- **MITRE ATLAS (content version 2026.07):** Adversarial tactics, techniques, and real-world AML attack procedures.
- **NIST AI 100-2e2025:** Formal taxonomy of adversarial goals, capabilities, and data/model constraints.
- **MITRE SAFE-AI:** Enterprise security control selection and assessment criteria (NIST SP 800-53 Rev. 5).

---
## Repository Index

| # | Status | Module Name | Primary Attack Surface | Core Threat Vectors | Standards Mapping |
| --- | --- | --- | --- | --- | --- |
| **01** | Done | Introduction to LLMs | Tokenizer & Inference Runtime Primitives | Token fragmentation, context window truncation, decoding temperature variance | Foundations (no direct mapping) |
| **02** | Done | Working with LLMs | Chatbot Architecture & State Management | Role confusion, system prompt leakage, conversation state manipulation, keyword filter evasion | LLM08:2026, LLM01:2026, AML.T0051, AML.T0056, CWE-200 |
| **03** | Done | Extending and Customizing LLMs | Basic RAG Context & Function Calling | Context bleed into tool parameters, spurious tool invocation, data boundary collapse | LLM01:2026, LLM03:2026, AML.T0051, AML.T0053 |
| **04** | Done | Security Considerations and the AI Red Team Lifecycle | Threat Model & Red Team Governance | Trust boundary violations, telemetry evasion, unmonitored side-effect execution | NIST AI RMF, OWASP LLM Top 10 (2026), MITRE ATLAS |
| **05** | Planned | Reconnaissance and Enumeration | Public Endpoints & Model Serving APIs | Stack fingerprinting, context window probing, unauthenticated API route enumeration, model extraction | AML.TA0002, AML.T0006, LLM08:2026, CWE-200 |
| **06** | Planned | LLM Jailbreaking | Direct User Ingress & Alignment Guardrails | Persona adoption, cognitive hacking, multi-turn crescendo attacks, cipher/encoding obfuscation | LLM01:2026, AML.T0051, AML.T0054 |
| **07** | Planned | Prompt Injection | Delimiters, Prompt Assembler & Ingestion | Direct system override, delimiter spoofing, simulated-context framing, boundary breaking | LLM01:2026, AML.T0051.000, AML.T0051.001, CWE-77 |
| **08** | Planned | Improper Output Handling | Downstream Consumers & Application Parsers | Cross-Site Scripting (XSS), SQLi/Command Injection via generated payload, unhandled JSON parser DoS | LLM10:2026, CWE-79, CWE-89, CWE-116 |
| **09** | Planned | Excessive Agency | Autonomous Tool Execution & API Permissions | Missing human-in-the-loop (HITL), excessive write privileges, unintended side-effect execution | LLM03:2026, AML.T0053, CWE-250 |
| **10** | Planned | Unbounded Consumption | Compute, Memory & Context Budget | Denial of Wallet (DoW), thinking-token exhaustion, context window bloating, resource DoS | LLM06:2026, CWE-400 |
| **11** | Planned | Attacking AI Agents | Autonomous Decision Loop & Reasoning Chains (ReAct) | Plan hijacking, memory state corruption, feedback loop manipulation, goal redirection | LLM01:2026, LLM03:2026, ASI01, AML.T0051 |
| **12** | Planned | Multi-Agent Systems and A2A | Inter-Agent Communication (A2A) Protocols | Rogue agent impersonation, cross-agent privilege propagation, malicious agent card injection | OWASP Agentic Top 10 (ASI01), AML.T0051 |
| **13** | Planned | Exploiting RAG Pipelines | Vector Database & Document Ingestion | Indirect prompt injection via poisoned documents, knowledge base corruption, retrieval context hijacking | LLM01:2026, LLM05:2026, AML.T0051.001, AML.T0070 |
| **14** | Planned | Attacking Embeddings | Embedding Models & Semantic Vector Space | Embedding inversion (Vec2Text), semantic collision attacks, similarity ranking manipulation | LLM09:2026, LLM02:2026, CWE-200 |
| **15** | Planned | MCP and Tool Surfaces | Model Context Protocol (MCP) Host/Client/Server | Tool schema poisoning, malicious capability advertisement, runtime parameter command injection | LLM03:2026, AML.T0053, OWASP MCP Top 10, CWE-78 |
| **16** | Planned | Supply Chain Attacks | Model Hubs, Adapters & Dependencies | Arbitrary code execution via pickled weights (`.pt`/`.bin`), backdoored LoRA adapters, poisoned dependencies | LLM04:2026, LLM05:2026, AML.T0010, CWE-494 |
| **17** | Planned | AI Infrastructure and Deployment Exploits | Model Serving Runtimes (vLLM, Ollama, Triton) | Unauthenticated REST APIs, server-side request forgery (SSRF), container escapes, GPU memory leakage | LLM06:2026, CWE-306, CWE-918, NIST SP 800-53 SC-5 |
| **18** | Planned | Threat Modeling for AI-Enabled Targets | Architecture & System Data Flow Diagrams (DFDs) | STRIDE / MAESTRO boundary violations, untrusted data flow analysis, component interaction risks | NIST AI RMF, MITRE ATLAS, ISO/IEC 42001 |
| **19** | Planned | Capstone Red Team Engagement | Enterprise End-to-End LLM Ecosystem | Multi-stage kill chain, lateral movement across agents, exfiltration of canary assets, comprehensive audit | NIST SP 800-53A, OWASP LLM Top 10 (2026), MITRE ATLAS |
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
