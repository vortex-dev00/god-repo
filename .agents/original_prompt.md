## 2026-06-28T11:42:57Z

Restructure and update the local `god-repo` repository (https://github.com/Sochasvobody/god-repo) to resolve file mismatches and update all content to reflect the AI landscape of June/July 2026.

Working directory: C:\Users\svhon\.gemini\antigravity\scratch\god-repo
Integrity mode: development

## Requirements

### R1. Restructure Mismatched File Contents
Rearrange the contents of mismatched files to match their directory paths:
1. Move DevOps, CI/CD, Terminal tools, and Security & Privacy from `llm-gateways-routers/README.md` to `devops-cicd-ai-tools/README.md`.
2. Move LLM Gateways & Routers from `ai-editors-ide-extensions/README.md` (and prompt engineering duplicate) to `llm-gateways-routers/README.md`.
3. Move System Starters & Boilerplates from `rag-vector-databases/README.md` to `starters-boilerplates/README.md`.
4. Move the exhaustive self-hosting stacks, open-source alternatives, and workflow recipes from `starters-boilerplates/README.md` to `discover/open-source-alternatives/README.md`.
5. Move the exhaustive hardware guides from `devops-cicd-ai-tools/README.md` to `meta/ai-hardware-guide/README.md`.
6. Move the exhaustive mobile apps guide from `devops-cicd-ai-tools/README.md` to `everyone/ai-mobile-apps/README.md`.
7. Move the exhaustive model comparisons from `devops-cicd-ai-tools/README.md` to `discover/model-comparisons-benchmarks/README.md`.
8. Move the exhaustive news, podcasts, newsletters, and channels from `devops-cicd-ai-tools/README.md` to `meta/ai-news-staying-updated/README.md`.

### R2. Create Missing AI Editors & IDE Extensions Guide
Create a comprehensive `developers/ai-editors-ide-extensions/README.md` containing all major editors and extensions (Cursor, Windsurf, Cline, GitHub Copilot, Continue, Zed, etc.), including a comparison table and configuration guides (like `.cursorrules`, `AGENTS.md`, and `CLAUDE.md`).

### R3. Update AI Landscape Content to June/July 2026
Update all repository guides to reflect the state of AI in June/July 2026, specifically including:
1. OpenAI's GPT-5.6 (Sol, Terra, Luna) limited rollout and GPT-5.5.
2. Anthropic's Claude Fable 5 / Mythos 5, Claude Opus 4.8, and the deprecation of original Claude 4 Sonnet/Opus models.
3. Google's Gemini 3.5 Pro delay to July 2026, and Gemini 3.5 Flash / Omni.
4. Cursor's $4B ARR and acquisition by SpaceX under xAI.
5. Viral popularity of OpenClaw (380k+ stars), Superpowers, ECC, hermes-agent, and token optimization tools (rtk, caveman, headroom).

### R4. Verify Repository Links & Markdown Integrity
Ensure all relative links between directories and files are fully resolved and correct. Ensure all external links are valid and all files compile clean as Markdown.

## Acceptance Criteria

### Restructuring & Cleanliness
- [ ] `developers/ai-editors-ide-extensions/README.md` exists and contains Cursor, Windsurf, Cline, Copilot, Continue, and Zed.
- [ ] `developers/prompt-engineering-observability/README.md` contains only prompt engineering and observability (no duplicate gateway section).
- [ ] `developers/llm-gateways-routers/README.md` contains LiteLLM, Portkey, OpenRouter, Martian, Helicone, and Requesty.
- [ ] `developers/devops-cicd-ai-tools/README.md` contains DevOps, CI/CD, Terminal tools, and Security & Privacy.
- [ ] `developers/starters-boilerplates/README.md` contains create-t3-app, create-t3-turbo, Vercel chatbot templates, SaaS starters, Better Auth, etc.
- [ ] `discover/open-source-alternatives/README.md` contains the exhaustive self-hosting stacks, open-source alternatives, and workflow recipes.
- [ ] `meta/ai-hardware-guide/README.md` contains RTX 5090/5080/4090/3090, Apple M4/M5, and AI dedicated devices (Rabbit R1, Ray-Ban smart glasses, etc.).
- [ ] `everyone/ai-mobile-apps/README.md` contains the exhaustive consumer AI mobile apps list.
- [ ] `discover/model-comparisons-benchmarks/README.md` contains Chatbot Arena Elo, Artificial Analysis AAII rankings, MMLU, HumanEval, and SWE-bench.
- [ ] `meta/ai-news-staying-updated/README.md` contains X/Twitter accounts, subreddits, podcasts, newsletters, and YouTube channels.

### Content Accuracy (June/July 2026)
- [ ] References to GPT-5.6, Claude Opus 4.8, Claude Fable 5, Gemini 3.5 Flash/Omni, OpenClaw, Superpowers, and Cursor's $4B ARR / SpaceX acquisition are present in the appropriate guides (e.g., `discover/ai-models-providers/README.md`, `state-of-ai/README.md`, `developers/mega-github-repos/README.md`).

### Formatting & Links
- [ ] All updated files compile correctly as Markdown.
- [ ] There are no broken relative links or empty placeholder sections.

## 2026-06-28T11:47:15Z

The user has emphasized that the goal is to make this repository the absolute 'Wikipedia for AI' or 'Google for AI' for everyone from complete beginners to developers and power users. Every guide and file (Beginners, Intermediate, Developers, Advanced) must be extremely comprehensive, clean, structured, and contain complete real-world resources, guides, and tables without placeholders. Make sure to audit the quality of the content carefully and write each section to be as thorough and useful as possible. Ensure that after restructuring, every file is fully fleshed out with exhaustive, high-quality mid-2026 content.

## 2026-06-28T11:50:45Z

Please add a new section in `developers/prompt-engineering-observability/README.md` titled "Production Prompt Templates & Context Recipes". This section must include three concrete, copy-pasteable system prompts for developers:
1. **Security & Vulnerability Audit Prompt**: A prompt to scan codebase changes for prompt injection, insecure dependencies, PII exposure, and memory leaks.
2. **Context & Token Optimization Prompt**: A prompt that instructs coding agents to reduce reasoning verbosity, compress command outputs, and use structured diffs to save 60-90% of tokens (citing rtk and headroom patterns).
3. **App Verification & Zero-Error Testing Prompt**: A prompt to enforce that coding agents write unit tests, verify runtime dependencies, start the local server, check for console errors, and verify the app runs cleanly without breaking upon launch.

Also ensure there are links to repositories for security scanning (e.g., protectai/llm-guard, Confident-AI/deepeval, promptfoo/promptfoo, and jujumilk3/system_prompts_leaks).

## 2026-06-28T11:51:58Z

Please make sure to add the following developer-focused guides:
1. **AI Coding Tool Selection Matrix**: In `developers/ai-editors-ide-extensions/README.md` or `developers/cli-agents/README.md`, compare Cursor, Windsurf, Claude Code, Aider, and Cline. Detail when to use which tool (e.g., Cursor for interactive editing, Claude Code for CLI testing, Cline for autonomous browser tasks).
2. **Prompt Caching & Cost Optimization Guide**: In `developers/prompt-engineering-observability/README.md`, add a guide on how prompt caching works for Anthropic/OpenAI, and how to structure system prompts, tools, and history to maximize cache hits (saving 50-90% of costs).
3. **Context Engineering File Standards**: In `developers/starters-boilerplates/README.md`, add a comprehensive guide on `AGENTS.md` (the cross-tool open standard), `CLAUDE.md` (for Claude Code), and `.cursorrules` / `.cursor/rules/*.mdc` (for Cursor), demonstrating how to structure them to achieve zero-error development.

Ensure these are detailed, practical, and link to the relevant repositories.

## 2026-06-28T11:52:48Z

The user wants at least 10 more cutting-edge AI developer topics added to make the repo the ultimate "Wikipedia for AI". Please integrate the following 10 topics into the respective README files:

1. **Agent Handoff & Routing Patterns**: Detail triage agent patterns, state sharing, and specialized delegation (e.g., routing in LangGraph and PydanticAI). [Add to `developers/agent-frameworks/README.md`]
2. **LLM-as-a-Judge Evaluation (Evals)**: Explain automated grading pipelines for faithfulness, answer relevancy, and context precision. [Add to `developers/prompt-engineering-observability/README.md`]
3. **Structured Outputs (JSON Schema & Pydantic)**: Focus on function calling and Pydantic validation to guarantee zero schema errors. [Add to `developers/prompt-engineering-observability/README.md`]
4. **Prompt Injection & Adversarial Red-Teaming**: Defenses against jailbreaks, system prompt leakage, and tools like Vigil, Lakera Guard, and garak. [Add to `developers/prompt-engineering-observability/README.md`]
5. **Prompt Versioning & Registries**: Best practices for decoupling prompts from code via registries (Langfuse, Braintrust, LangSmith). [Add to `developers/prompt-engineering-observability/README.md`]
6. **AI Agent Tool-Use (Function Calling) Design**: How to write schemas, handle execution failures, and enable agent self-correction. [Add to `developers/agent-frameworks/README.md`]
7. **Small Language Models (SLMs) for Edge Deployment**: Running Phi-4, Qwen 2.5 1.5B/3B, and Llama 3.2 1B/3B on-device using WebNN, ONNX Runtime, and transformers.js. [Add to `developers/local-ai/README.md`]
8. **Synthetic Data Generation for Fine-Tuning**: Using frontier models to generate high-quality dataset pairs for small model tuning. [Add to `discover/ai-models-providers/README.md`]
9. **Semantic Cache & Advanced RAG Indexing**: Using hybrid search (keyword + vector), re-ranking (Cohere Rerank, BGE Reranker), and query expansion/re-writing. [Add to `developers/rag-vector-databases/README.md`]
10. **Agent Memory Architectures**: Designing short-term episodic memory, long-term semantic memory, and entity memory (using Mem0, Zep, Postgres). [Add to `developers/agent-frameworks/README.md`]

Ensure each topic is clearly structured with real-world examples, diagrams/tables where helpful, and links to the relevant repositories.

## 2026-06-28T11:53:45Z

The user has requested to think of even more developer-focused topics—25 more to be exact—to make the repo the ultimate AI Wikipedia. Please integrate the following 25 topics into the respective README files in the repository:

1. **Multi-Modal Retrieval (Text + Image + Audio RAG)**: How to embed, index, and retrieve non-text modalities in vector stores using CLIP, ImageBind, or ColPali. [Add to `developers/rag-vector-databases/README.md`]
2. **Context Window Compression & Context Pruning**: Using LLMLingua or semantic summarization to shrink long inputs before sending them to APIs. [Add to `developers/prompt-engineering-observability/README.md`]
3. **Speculative Decoding & Prompt Lookup Decoding**: Techniques to accelerate token generation speed by utilizing smaller models or cache-lookup matching. [Add to `developers/local-ai/README.md`]
4. **Offline Local Vector Search (Client-Side)**: Running vector indexing and search directly in the browser or client (using Voy, Orama, or Web-Assembly builds). [Add to `developers/rag-vector-databases/README.md`]
5. **Graph RAG (Knowledge Graphs for Context)**: Constructing and querying a knowledge graph alongside a vector store to resolve complex multi-hop relation queries. [Add to `developers/rag-vector-databases/README.md`]
6. **Self-Correction & Refusal Handling Patterns**: Writing retry loops that detect model refusals ("I can't answer that"), parse validation errors, and reformulate queries. [Add to `developers/agent-frameworks/README.md`]
7. **RAG Evaluation Metrics (RAGAS / TruLens)**: Metrics for context recall, context precision, answer faithfulness, and answer relevance. [Add to `developers/rag-vector-databases/README.md`]
8. **In-Context Learning (ICL) Optimization**: How to select, order, and format few-shot examples (using cosine similarity or diversity selectors) to maximize learning. [Add to `developers/prompt-engineering-observability/README.md`]
9. **Fine-Tuning Parameter-Efficient Methods (LoRA, QLoRA, DoRA)**: Memory-saving fine-tuning and dynamic adaptor deployment at runtime. [Add to `discover/ai-models-providers/README.md`]
10. **Dynamic Agent Handoffs**: Letting the agent decide at runtime which specialized tool/agent to hand the user to, using router prompts or router models. [Add to `developers/agent-frameworks/README.md`]
11. **Browser Automation Agents (Playwright + LLMs)**: Integrating agents with visual browsers (Stagehand, LaVague, Cline browser tool) to scrape or automate actions. [Add to `developers/agent-frameworks/README.md`]
12. **Federated & Private Fine-Tuning**: Techniques for training models on distributed private data without centralizing raw datasets. [Add to `discover/ai-models-providers/README.md`]
13. **Model Merging (MergeKit)**: Using SLERP, DARE, or ties-merging to combine multiple open-weight models without retraining. [Add to `discover/ai-models-providers/README.md`]
14. **Prompt Security Shielding (Llama Guard, NeMo Guardrails)**: Constructing an input/output safety gateway that runs separate models to classify safety. [Add to `developers/prompt-engineering-observability/README.md`]
15. **Cost-Aware Dynamic Routing**: Let the gateway decide at runtime if a query is easy (routing to Gemini Flash / GPT-4o mini) or hard (routing to Claude Opus / GPT-5). [Add to `developers/llm-gateways-routers/README.md`]
16. **Token Rate Limit (TPM/RPM) Queue Management**: Strategies to handle rate limits, retry backoffs, and load-balancing across multiple API keys/providers in production. [Add to `developers/llm-gateways-routers/README.md`]
17. **Semantic Chunking Strategies**: Splitting documents by semantic similarity (sentence embeddings) rather than fixed character size. [Add to `developers/rag-vector-databases/README.md`]
18. **Long-Context Reranking**: Re-ordering search results so that the most relevant chunks are at the beginning/end of the context window to avoid the "lost in the middle" effect. [Add to `developers/rag-vector-databases/README.md`]
19. **Prompt Version Control Systems (Git-for-Prompts)**: Using tools like Promptfoo, Pezzo, or simple git file tracking to version control system prompts. [Add to `developers/prompt-engineering-observability/README.md`]
20. **Deterministic Output Seeding (seed, temperature=0)**: How to make LLM outputs as deterministic as possible for automated testing and CI/CD. [Add to `developers/prompt-engineering-observability/README.md`]
21. **LLM Orchestration in Serverless Environments**: How to handle cold starts and execution timeouts when invoking slow LLM calls in AWS Lambda or Vercel Functions. [Add to `developers/devops-cicd-ai-tools/README.md`]
22. **Agentic Workflow Testing (Simulation-based)**: Simulating user interactions with mock agents to test multi-turn agent systems before deployment. [Add to `developers/agent-frameworks/README.md`]
23. **Structured Logging for LLM Traces**: Implementing structured OTel logs to capture span IDs, parent IDs, token counts, model versions, and cost per request. [Add to `developers/prompt-engineering-observability/README.md`]
24. **Multi-Model Assembly (MoE - Mixture of Experts) Serving**: How Mixtral/DeepSeek-V3 serving works and how to optimize routing locally (using vLLM / SGLang). [Add to `developers/local-ai/README.md`]
25. **GPU Memory Sizing & Bandwidth Math**: A quick checklist/calculator for developers to calculate how much VRAM is needed for training, serving, or quantizing any parameter size model. [Add to `meta/ai-hardware-guide/README.md`]

Ensure these are detailed, practical, and link to the relevant repositories.
