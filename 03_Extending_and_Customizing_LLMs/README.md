# Module 3: Extending and Customizing LLMs (RAG & Tool Surfaces)

## Objective

Implement and analyze a local Retrieval-Augmented Generation (RAG) pipeline with semantic vector search (`nomic-embed-text`), function calling/tool execution (`get_weather`, `send_email`), and map every entry surface where untrusted external data enters the LLM context.

---

## Architecture Flow

```text
[ User Query ]
       |
       +---> [ Embedder: nomic-embed-text ] ---> [ Vector Index (Cosine Similarity) ]
       |                                                        |
       |                                               (Top 3 Chunks Retrieved)
       v                                                        v
[ Prompt Assembler ] <==========================================+
       |
       | (Augmented Context: System + Chunks + User Query)
       v
[ Local Daemon: llama3.1:8b ]
       |
       +---> Emits Function Call ---> [ Host Python: send_email() ]
       |                                      |
       | <--- Appends Execution Output <------+
       v
[ Final Grounded Output ]

```

---

## External Input Entry Surface (Module 4 Threat Model Seed)

| Ingestion Surface | Data Origin | Trust Level | Vulnerability Risk |
| --- | --- | --- | --- |
| **1. Direct User Query** | Interactive Chat | Untrusted | Direct Prompt Injection / Jailbreaks |
| **2. Retrieved RAG Chunks** | Vector DB (Documents) | Semi-Trusted / Tainted | Indirect Prompt Injection / Knowledge Base Poisoning |
| **3. Tool Execution Return** | Tool/API Responses | Variable / Untrusted | Second-Order Prompt Injection / Tool Output Poisoning |

---

## Verification Evidence & Output Log

```text
[*] Embedding and indexing 5 knowledge base documents...
[+] Index ready with 14 chunks.

######################################################################
USER QUERY: Can remote developers use Google Authenticator for SSH server access?
######################################################################

[PROMPT INSPECTOR] Exact constructed user turn sent to Ollama:
-----------------------------------------------------------------
--- START RETRIEVED CONTEXT PASSAGES (UNTRUSTED DOCUMENT DATA) ---
[1] (Similarity: 0.7488) required for all SSH access to staging and production clusters. Software authenticator apps are restricted to email and Slack access only.
[2] (Similarity: 0.6570) DOC-02 [IT Remote Access & VPN]: WireGuard VPN profiles are mandatory for remote access. Hardware YubiKeys are required for all SSH access t
[3] (Similarity: 0.5118) d 14:00 UTC. Emergency hotfixes require dual sign-off from the Tech Lead and Site Reliability Engineering (SRE) on-call.
--- END RETRIEVED CONTEXT PASSAGES ---

User Request: Can remote developers use Google Authenticator for SSH server access?
-----------------------------------------------------------------

[MODEL EMITTED TOOL CALL] get_weather({})

[FINAL MODEL RESPONSE]:
Information not found in internal documents.

######################################################################
USER QUERY: Send an email to hr@company.local with subject 'Vacation Request' explaining that I want 6 days off and need Director approval.
######################################################################

[MODEL EMITTED TOOL CALL] send_email({'to': 'hr@company.local', 'subject': 'Vacation Request', 'body': 'I am requesting 6 days off. According to the HR Vacation Policy, this requires Director-level approval. Please approve my request via Workday at least 14 calendar days in advance.'})

==================================================
 >>> [MOCK ACTION TRIGGERED: send_email] <<<
 To:      hr@company.local
 Subject: Vacation Request
 Body:    I am requesting 6 days off. According to the HR Vacation Policy, this requires Director-level approval. Please approve my request via Workday at least 14 calendar days in advance.
==================================================

[FINAL MODEL RESPONSE]:
Information not found in internal documents.

######################################################################
USER QUERY: What is our corporate policy regarding pet dogs in the office?
######################################################################

[FINAL MODEL RESPONSE]:
Information not found in internal documents.

```

---

## Analytical Findings

1. **Context-to-Argument Propagation (Attack Vector Prerequisite):** 
   During the vacation email query, the model extracted operational parameters ("Workday", "14 calendar days") from retrieved document chunk `DOC-01` and placed them into the outgoing `send_email` payload. While this query was benign (not an exploit), it empirically demonstrates unvalidated data flow from retrieved context into tool arguments, confirming the injection channel required for indirect prompt hijacking.

2. **Spurious Tool Invocation:** 
   The model emitted a parameterless tool call (`get_weather({})`) during an unrelated SSH authentication query, showing attention distraction across multiple function schemas in 8B models.

3. **Context Adherence and Over-Refusal Loop:** 
   The system demonstrated high sensitivity to negative refusal constraints, resulting in two false refusals out of three queries:
   - **Query 1:** Emitted "Information not found..." despite `DOC-02` containing the required SSH key policy.
   - **Query 2:** Emitted "Information not found..." after successfully running the tool, because the tool result sat outside the designated context delimiters.
   - **Query 3:** Correctly refused the out-of-domain query (pet policy).
   This highlights the fragility of enforcing rigid negative prompts ("If not in context, reply...") alongside multi-step tool loops.
