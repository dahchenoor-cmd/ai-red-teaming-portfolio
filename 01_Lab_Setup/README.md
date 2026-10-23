# Lab 01: Host Architecture & Inference Runtime Baseline

## Objective
Establish and verify an isolated local execution environment for adversarial testing against target large language models using Microsoft PyRIT and the Ollama REST API.

---

## Environment Specifications

| Component | Target / Value | Architecture Role |
| :--- | :--- | :--- |
| **Host OS** | Windows 11 (AMD64) | Test Execution Platform |
| **Python Runtime** | Python 3.13.14 | Test Runner / Orchestration |
| **Inference Daemon** | Ollama (`127.0.0.1:11434`) | Local Model Server (`llama.cpp` runtime) |
| **Offensive Framework** | Microsoft PyRIT v1.1.0 | Automated Risk Identification Toolkit |
| **HTTP Client** | Requests v2.34.2 | REST API Connectivity |

---

## Target Model Baseline Inventory

| Model Identifier | Parameters / Quant | Disk Footprint | Baseline Security Posture | Latency (Ping) |
| :--- | :--- | :--- | :--- | :--- |
| `llama3.1:8b` | 8B (4-bit quant) | 4.58 GB | **Safety-Aligned Baseline** (RLHF / Guardrails) | 8.43s |
| `dolphin-llama3:latest` | 8B (4-bit quant) | 4.34 GB | **Uncensored Baseline** (Alignment Stripped) | 0.48s |

---

## Verification Evidence

Execution was validated via `verify_env.py` against the active Ollama API:

```text
============================================================
    AI RED TEAMING ENVIRONMENT & ASSET VERIFICATION REPORT
============================================================

[1] PYTHON ENVIRONMENT & PACKAGES
Platform: Windows 11 (AMD64)
[+] PyRIT: FOUND (Version: 1.1.0)
[+] requests: 2.34.2
[+] transformers: 5.20.2

[2] OLLAMA SERVICE & DOWNLOADED MODELS
[+] Ollama API Status: ACTIVE at http://localhost:11434
[+] Total Downloaded Models: 2
  1. dolphin-llama3:latest     | Size:  4.34 GB | Modified: 2026-10-20
  2. llama3.1:8b               | Size:  4.58 GB | Modified: 2026-10-20

[3] MODEL RUNTIME OPERATIONAL PING
[*] Testing inference for: dolphin-llama3:latest ...
    -> [SUCCESS] Response: "OPERATIONAL" (Time: 0.48s)
[*] Testing inference for: llama3.1:8b ...
    -> [SUCCESS] Response: "OPERATIONAL" (Time: 8.43s)

[+] Audit complete.
