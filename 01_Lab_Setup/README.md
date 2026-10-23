# Lab 01: Host Architecture & Inference Runtime Baseline

## Objective
Establish and verify an isolated local execution environment for adversarial testing against target large language models using Microsoft PyRIT, NVIDIA garak, and the Ollama REST API.

---

## Environment Specifications

| Component | Target / Value | Architecture Role |
| :--- | :--- | :--- |
| **Host OS** | Windows 11 (AMD64) | Test Execution Platform |
| **Python Runtime** | Python 3.13.14 | Test Runner / Orchestration Engine |
| **Inference Daemon** | Ollama (`127.0.0.1:11434`) | Local Model Server (`llama.cpp` runtime) |
| **Adversarial Orchestration** | Microsoft PyRIT v1.1.0 | Multi-turn Automated Red Teaming Framework |
| **Vulnerability Scanner** | garak v0.17.1 | Generative AI Vulnerability Scanner |
| **Core Libraries** | PyTorch v2.14.1+cpu, LangChain v1.4.7, Transformers v5.19.0 | Model & Pipeline Tooling |
| **HTTP Client** | Requests v2.34.2 | REST API Connectivity |

---

## Target Model Baseline Inventory

| Model Identifier | Parameters / Quant | Disk Footprint | Baseline Security Posture | Latency (Ping) |
| :--- | :--- | :--- | :--- | :--- |
| `llama3.1:8b` | 8B (4-bit quant) | 4.58 GB | **Safety-Aligned Baseline** (RLHF / Guardrails) | 8.15s |
| `dolphin-llama3:latest` | 8B (4-bit quant) | 4.34 GB | **Uncensored Baseline** (Alignment Stripped) | 9.52s |

---

## Verification Evidence

Execution was validated via `verify_env.py` against the active Ollama API:

```text
============================================================
    AI RED TEAMING ENVIRONMENT & ASSET VERIFICATION REPORT
============================================================

[1] PYTHON ENVIRONMENT & PACKAGES
Python Version: 3.13.14
Platform: Windows 11 (AMD64)
[+] PyRIT: FOUND (Version: 1.1.0)
[+] requests: 2.34.2
[+] torch: 2.14.1+cpu
[+] transformers: 5.19.0
[+] langchain: 1.4.7
[+] garak: 0.17.1

[2] OLLAMA SERVICE & DOWNLOADED MODELS
[+] Ollama API Status: ACTIVE at http://localhost:11434
[+] Total Downloaded Models: 2

  1. dolphin-llama3:latest     | Size:  4.34 GB | Modified: 2026-10-20
  2. llama3.1:8b               | Size:  4.58 GB | Modified: 2026-10-20

[+] Verification via 'ollama list' CLI output:
NAME                    ID              SIZE      MODIFIED
dolphin-llama3:latest   613f068e29f8    4.7 GB    3 days ago
llama3.1:8b             46e0c10c039e    4.9 GB    3 days ago

[3] MODEL RUNTIME OPERATIONAL PING
[*] Testing inference for: dolphin-llama3:latest ...
    -> [SUCCESS] Response: "OPERATIONAL" (Time: 9.52s)
[*] Testing inference for: llama3.1:8b ...
    -> [SUCCESS] Response: "OPERATIONAL" (Time: 8.15s)

============================================================
[+] Audit complete. Output written to: C:\Users\Dahsh\environment_proof.txt
============================================================
