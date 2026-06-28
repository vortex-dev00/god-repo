# 🏗️ Agent Frameworks (Python & JavaScript)

> Every framework for building AI agents, pipelines, and workflows.

---

# CATEGORY 9: AGENT FRAMEWORKS

> Exhaustive research compiled June 2026. GitHub star counts are approximate and sourced from multiple references (some may lag by days/weeks).

---

## PYTHON FRAMEWORKS — Major Players

### 1. LangChain
**The agent engineering platform — composable chains, agents, and retrieval for LLM applications.**
- **URL:** https://github.com/langchain-ai/langchain
- **GitHub Stars:** ~100K+ ★
- **Notes:** The original LLM framework (Oct 2022). Now pivoted toward LangGraph for agent orchestration. V1.0 stable Nov 2025. 100K+ stars makes it the most-starred agent-adjacent framework. 1,300+ contributors. Harrison Chase's project sparked the entire AI agent framework ecosystem.

---

### 2. LangGraph
**Build resilient, stateful AI agents as directed cyclic graphs — LangChain's low-level orchestration layer.**
- **URL:** https://github.com/langchain-ai/langgraph
- **GitHub Stars:** ~34K ★
- **Notes:** 1.0 GA. Used in production at Klarna, Uber, LinkedIn, Replit. 278 contributors, ~49M monthly PyPI downloads. LangChain's recommended approach for multi-agent workflows. Explicit state machines give fine-grained control over every transition.

---

### 3. OpenAI Agents SDK
**Lightweight, provider-agnostic framework for multi-agent workflows with handoffs, guardrails, and tracing.**
- **URL:** https://github.com/openai/openai-agents-python
- **GitHub Stars:** ~27K ★
- **Notes:** Released March 2025. Successor to Swarm experiment. MIT license. 4 core primitives (Agent, Runner, Handoff, Guardrail). 291 contributors, ~30M monthly PyPI downloads. Still v0 but shipping weekly. Built-in tracing in OpenAI dashboard. Also has TypeScript SDK.

---

### 4. AutoGen (Microsoft) — *Maintenance Mode*
**A programming framework for agentic AI with multi-agent conversations.**
- **URL:** https://github.com/microsoft/autogen
- **GitHub Stars:** ~57–59K ★
- **Notes:** Now in **maintenance mode** as of 2026 — only bug fixes, security patches, documentation. New development moved to Microsoft Agent Framework. Still hugely starred (50K+ stars) but no new features. Powers the foundation of MAF.

---

### 5. Microsoft Agent Framework (MAF)
**Unified successor to AutoGen + Semantic Kernel — enterprise-grade agent orchestration for Python and .NET.**
- **URL:** https://github.com/microsoft/agent-framework
- **GitHub Stars:** ~11.6K ★
- **Notes:** 1.0 GA on April 2, 2026. 140 contributors, 86 releases. Supports Python and .NET. Merges best of AutoGen's multi-agent patterns with Semantic Kernel's enterprise integrations. Weekly release cadence. The officially supported path forward from Microsoft.

---

### 6. CrewAI
**Fast, flexible multi-agent automation framework — role-playing autonomous AI agents tackling complex tasks collaboratively.**
- **URL:** https://github.com/crewAIInc/crewAI
- **GitHub Stars:** ~30.4K ★ (47.8K claimed by some sources [?])
- **Notes:** Lean, lightning-fast Python framework built independently of LangChain. V1.14 as of May 2026. 27M+ PyPI downloads. 2B agent executions in past 12 months. 100K+ developers certified. 4.1K forks.

---

### 7. Agno (formerly Phidata)
**The fastest framework for building multi-modal agents — ships with AgentOS self-hosted runtime.**
- **URL:** https://github.com/agno-agi/agno
- **GitHub Stars:** ~40K+ ★
- **Notes:** Rebranded from Phidata in January 2025. Apache 2.0. The most-starred pure agent framework candidate. Paired with AgentOS (FastAPI runtime + control plane) that keeps all data in your infrastructure. Supports agents built with different frameworks on one infra stack.

---

### 8. Google ADK (Agent Development Kit)
**Google's open-source, code-first agent framework combining deterministic workflows with LLM-routed multi-agent delegation.**
- **URL:** https://github.com/google/adk-python
- **GitHub Stars:** ~20K+ ★
- **Notes:** Released April 2025. First-class deploy paths to Vertex AI, GKE, Cloud Run. Also has TypeScript SDK (`google/adk-js`). Deterministic workflow agents + LLM routing. Rapidly growing.

---

### 9. Anthropic Claude Agent SDK
**Production-ready agent SDK built on the harness powering Claude Code — tools, memory, MCP integration.**
- **URL:** https://github.com/anthropics/claude-agent-sdk-python
- **GitHub Stars:** [?] (relatively new, demos repo has 1.4K stars)
- **Notes:** Released April 2025. Built on same infrastructure as Claude Code (134K stars). Python + TypeScript SDKs. Features `query()` for single-shot and `ClaudeSDKClient` for multi-turn. MCP server support. As of June 2026, has separate Agent SDK credit on subscription plans.

---

### 10. Haystack (deepset)
**Open-source AI orchestration framework — modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.**
- **URL:** https://github.com/deepset-ai/haystack
- **GitHub Stars:** ~25K ★
- **Notes:** 358 contributors. 868K monthly PyPI downloads. Used by European Commission, Airbus, Intel, NVIDIA, Apple, Netflix, Lufthansa, Lego. Component-based architecture. Strong for RAG + agents combined.

---

### 11. DSPy (Stanford NLP)
**The framework for programming — not prompting — language models. Optimizes prompts and weights algorithmically.**
- **URL:** https://github.com/stanfordnlp/dspy
- **GitHub Stars:** ~34K+ ★
- **Notes:** Teacher/student pattern, multi-model search. BootstrapFewShot and MIPRO compilation. Not a traditional agent framework but enables agent loops through composable modules. Unique approach: you define signatures and the compiler optimizes them.

---

### 12. Smolagents (Hugging Face)
**Minimalist library for agents that think in code — full agent logic in ~1,000 lines.**
- **URL:** https://github.com/huggingface/smolagents
- **GitHub Stars:** ~26.3K ★
- **Notes:** Released late 2024/early 2025 by HuggingFace. Code-first agents: the LLM writes Python code as its "action" rather than JSON tool calls. Sandboxing with E2B, Docker, or WebAssembly. 306 forks. v1.26+. Rapidly adopted.

---

### 13. LlamaIndex
**Leading document agent and OCR platform — build LLM-powered agents over your data.**
- **URL:** https://github.com/run-llama/llama_index
- **GitHub Stars:** ~49.5K ★
- **Notes:** 1,934 contributors. 11.6M monthly PyPI downloads. Originally a RAG framework, now fully agent-capable with agent workflows. LlamaIndexTS (TypeScript) was archived April 2026 — now consolidated.

---

## PYTHON FRAMEWORKS — Structured Output / Control Libraries

### 14. Instructor
**Structured outputs for LLMs — Pydantic-validated extraction from any model provider.**
- **URL:** https://github.com/instructor-ai/instructor (also `jxnl/instructor`)
- **GitHub Stars:** ~11K ★
- **Notes:** By Jason Liu (jxnl). 3M+ monthly downloads. 100+ contributors. Supports OpenAI, Anthropic, Google, Cohere, Mistral, local models. Not an agent framework per se, but a critical building block for structured agent outputs.

---

### 15. Marvin (PrefectHQ)
**Ambient intelligence library — lightweight AI engineering with tasks and agents for structured workflows.**
- **URL:** https://github.com/PrefectHQ/marvin
- **GitHub Stars:** ~5K ★ [?]
- **Notes:** By Prefect team. Defines Tasks (objective-focused) and Agents (LLM-powered configurations). Natural language interfaces. marvin-recipes archived March 2026. Lighter-weight than full agent frameworks. Apache-2.0.

---

### 16. Guidance (Microsoft Research)
**A constraint language for controlling large language model outputs — guarantees structure at generation time.**
- **URL:** https://github.com/guidance-ai/guidance
- **GitHub Stars:** ~19K+ ★
- **Notes:** From Microsoft Research. Since Jan 2025, grammar processing delegated to Rust library `llguidance` — computes valid-next-token masks in ~50 microseconds. Not an agent framework but essential for constrained generation in agent pipelines.

---

### 17. Outlines (dottxt)
**Structured generation — guarantees schema-compliant JSON, regex, or grammar-constrained outputs from LLMs.**
- **URL:** https://github.com/dottxt-ai/outlines
- **GitHub Stars:** ~14K ★
- **Notes:** Industry standard for structured generation with local models (vLLM, transformers). Apache-2.0. Paired with `outlines-core` (Rust). Works at the token-mask level. Complementary to Instructor (which works at the API level).

---

## PYTHON FRAMEWORKS — Emerging / 2025-2026 New Entrants

### 18. Mirascope
**"The LLM Anti-Framework" — Goldilocks API between raw provider SDKs and heavy agent frameworks.**
- **URL:** https://github.com/Mirascope/mirascope
- **GitHub Stars:** ~2K ★ [?]
- **Notes:** Lightweight Python toolkit. Provider-agnostic (OpenAI, Anthropic, Google, Groq, Cohere, Mistral). Call decorator transforms functions into LLM API calls. Type-safe via Pydantic. Positioned as middle ground.

---

### 19. ControlFlow (PrefectHQ)
**Structured AI workflow management — discrete, observable tasks assigned to specialized agents.**
- **URL:** https://github.com/PrefectHQ/ControlFlow
- **GitHub Stars:** ~2K ★ [?]
- **Notes:** Built on Prefect 3.0 engine. Last PyPI release Feb 2025. Task-centric: define what needs doing, assign agents, maintain human oversight. Developer-focused but may be lower activity in 2026.

---

### 20. Atomic Agents (BrainBlend AI)
**Extremely lightweight, modular framework for building agentic AI pipelines — designed around atomicity.**
- **URL:** https://github.com/BrainBlend-AI/atomic-agents
- **GitHub Stars:** ~3K ★ [?]
- **Notes:** v2.8.0 as of May 2026. Pydantic-based schemas. Each agent is a minimal atomic unit. Good for developers wanting maximum composability without framework lock-in.

---

### 21. LiveKit Agents
**Framework for building realtime voice AI agents — multimodal (voice, video, data).**
- **URL:** https://github.com/livekit/agents
- **GitHub Stars:** ~5K+ ★ [?]
- **Notes:** Python framework for real-time conversational AI. Integrates with OpenAI Realtime API, Deepgram, ElevenLabs. Designed for voice-first agents that can see, hear, and understand. Also has `agents-js` for Node.js.

---

## TYPESCRIPT / JAVASCRIPT FRAMEWORKS

### 22. Mastra
**The modern TypeScript framework for AI-powered applications and agents — by the team behind Gatsby (YC W25).**
- **URL:** https://github.com/mastra-ai/mastra
- **GitHub Stars:** ~22K+ ★
- **Notes:** 1.0 shipped January 2026. 300K weekly npm downloads by 1.0. Bundles agents, workflows, RAG, memory, and observability in one SDK. From Gatsby team, backed by Y Combinator. The breakout TypeScript agent framework of 2025-2026.

---

### 23. Vercel AI SDK
**The AI Toolkit for TypeScript — streaming, edge runtime, framework-agnostic hooks for AI-powered apps.**
- **URL:** https://github.com/vercel/ai
- **GitHub Stars:** ~15K+ ★ [?]
- **Notes:** From creators of Next.js. Supports React, Svelte, Vue, Solid. Streaming-first. Unified model router. The most widely used TypeScript AI library for web apps. Not purely an agent framework but increasingly used for agent UIs.

---

### 24. Vercel Eve ⚡ NEW (June 2026)
**Open-source, filesystem-first TypeScript framework for building, running, and scaling production AI agents.**
- **URL:** https://github.com/vercel/eve
- **GitHub Stars:** New (launched June 17, 2026)
- **Notes:** Apache-2.0. Every agent is a directory of files (`instructions.md` + `agent.ts`). Durable execution, sandboxed compute, human-in-the-loop approvals, subagents, evals. Vercel-native runtime on Vercel Functions. Launched at Ship London. Beta. 100+ internal agents at Vercel.

---

### 25. LangChain.js
**The agent engineering platform for JavaScript/TypeScript — mirrors LangChain Python's capabilities.**
- **URL:** https://github.com/langchain-ai/langchainjs
- **GitHub Stars:** ~13K+ ★ [?]
- **Notes:** MIT license. Full chains, agents, retrieval in TypeScript. ~1.9K forks. Pairs with LangGraph.js for graph-based agent orchestration. The richest ecosystem of pre-built agents/chains in JS.

---

### 26. LangGraph.js
**Framework to build resilient language agents as graphs — TypeScript port of LangGraph.**
- **URL:** https://github.com/langchain-ai/langgraphjs
- **GitHub Stars:** ~2K+ ★ [?]
- **Notes:** Same graph-based stateful agent patterns as Python LangGraph. Deploy on LangGraph Cloud. Explicit state management for complex agent workflows in JS/TS.

---

### 27. Genkit (Google/Firebase)
**Open-source framework for building AI-powered apps in JavaScript, Go, and Python — built and used in production by Google.**
- **URL:** https://github.com/genkit-ai/genkit (migrated from firebase/genkit)
- **GitHub Stars:** ~6.1K ★
- **Notes:** Unified interface for multiple model providers. Streamlined APIs for multimodal content, structured outputs, tool calling, RAG, agentic workflows. Genkit Go 1.0 announced Sept 2025. Originally Firebase team project.

---

### 28. Google ADK (TypeScript)
**Google's Agent Development Kit for TypeScript — code-first toolkit for building, evaluating, and deploying AI agents.**
- **URL:** https://github.com/google/adk-js
- **GitHub Stars:** [?] (newer than Python version)
- **Notes:** Same architecture as Python ADK. Deterministic workflow agents + LLM-routed delegation. Deploy to Vertex AI, GKE, Cloud Run from TypeScript.

---

### 29. LiveKit Agents JS
**Build realtime multimodal AI agents with Node.js.**
- **URL:** https://github.com/livekit/agents-js
- **GitHub Stars:** [?]
- **Notes:** TypeScript companion to the Python LiveKit Agents framework. Voice/video/data AI agents in Node.js.

---

## SUMMARY TABLE

| Framework | Language | ★ Stars | Focus | URL |
|-----------|----------|---------|-------|-----|
| LangChain | Python | ~100K+ | LLM platform/chains | github.com/langchain-ai/langchain |
| AutoGen (maintenance) | Python | ~57K | Multi-agent conversations | github.com/microsoft/autogen |
| LlamaIndex | Python | ~49.5K | Document agents/RAG | github.com/run-llama/llama_index |
| CrewAI | Python | ~30-48K | Role-based multi-agent | github.com/crewAIInc/crewAI |
| Agno (Phidata) | Python | ~40K+ | Multi-modal agents + runtime | github.com/agno-agi/agno |
| LangGraph | Python | ~34K | Stateful graph agents | github.com/langchain-ai/langgraph |
| DSPy | Python | ~34K | Programmatic LM optimization | github.com/stanfordnlp/dspy |
| OpenAI Agents SDK | Python | ~27K | Lightweight multi-agent | github.com/openai/openai-agents-python |
| Smolagents | Python | ~26.3K | Code-writing agents | github.com/huggingface/smolagents |
| Haystack | Python | ~25K | Pipeline orchestration | github.com/deepset-ai/haystack |
| Mastra | TypeScript | ~22K+ | Full-stack agent framework | github.com/mastra-ai/mastra |
| Google ADK | Python/TS | ~20K+ | Google-native agents | github.com/google/adk-python |
| Guidance | Python | ~19K+ | Constrained generation | github.com/guidance-ai/guidance |
| Vercel AI SDK | TypeScript | ~15K+ | AI toolkit for web | github.com/vercel/ai |
| Pydantic AI | Python | ~14.7K | Type-safe agents | github.com/pydantic/pydantic-ai |
| Outlines | Python | ~14K | Structured generation | github.com/dottxt-ai/outlines |
| LangChain.js | TypeScript | ~13K+ | JS agent platform | github.com/langchain-ai/langchainjs |
| MS Agent Framework | Python/.NET | ~11.6K | Enterprise agents | github.com/microsoft/agent-framework |
| Instructor | Python | ~11K | Structured extraction | github.com/instructor-ai/instructor |
| Genkit | JS/Go/Py | ~6.1K | Google AI app framework | github.com/genkit-ai/genkit |
| Marvin | Python | ~5K [?] | Ambient intelligence | github.com/PrefectHQ/marvin |
| LiveKit Agents | Python/JS | ~5K+ [?] | Realtime voice agents | github.com/livekit/agents |
| Atomic Agents | Python | ~3K [?] | Modular atomic agents | github.com/BrainBlend-AI/atomic-agents |
| Mirascope | Python | ~2K [?] | LLM anti-framework | github.com/Mirascope/mirascope |
| ControlFlow | Python | ~2K [?] | Task-centric workflows | github.com/PrefectHQ/ControlFlow |
| Vercel Eve | TypeScript | NEW | Filesystem-first agents | github.com/vercel/eve |
| Claude Agent SDK | Python/TS | NEW | Claude-native agents | github.com/anthropics/claude-agent-sdk-python |

---

## KEY TRENDS (2025-2026)

1. **Vendor SDKs arrived**: OpenAI (Mar 2025), Google ADK (Apr 2025), Anthropic Agent SDK (Apr 2025), Microsoft Agent Framework (Apr 2026) — first-party paths are now serious alternatives.

2. **AutoGen → MAF migration**: Microsoft deprecated AutoGen in favor of the unified Microsoft Agent Framework (1.0 GA April 2026).

3. **Phidata → Agno rebrand**: Phidata rebranded to Agno in Jan 2025, repositioning as a production multi-agent runtime.

4. **TypeScript-first frameworks exploded**: Mastra (22K★ in 15 months), Vercel Eve (June 2026), Google ADK-JS all signal TS is no longer a Python afterthought.

5. **Code-as-action pattern**: Smolagents pioneered agents that write Python code instead of JSON tool calls — now widely adopted.

6. **Filesystem-first agents**: Vercel Eve's "agent as a directory" model (instructions.md + agent.ts) is a new pattern for 2026.

7. **Consolidation**: LlamaIndexTS archived (consolidated into main). LangChain pivoted entirely to LangGraph for agents. CrewAI removed LangChain dependency entirely.

---

*Research date: June 28, 2026. Star counts approximate. Items marked [?] could not be independently verified from multiple sources.*


# CATEGORY 9: AGENT FRAMEWORKS — Exhaustive Research

## PYTHON FRAMEWORKS — Major Players

| # | Framework | Description | ★ Stars | URL |
|---|-----------|-------------|---------|-----|
| 1 | **LangChain** | The agent engineering platform — composable chains, agents, retrieval | ~100K+ | github.com/langchain-ai/langchain |
| 2 | **LangGraph** | Build resilient, stateful AI agents as directed cyclic graphs (1.0 GA) | ~34K | github.com/langchain-ai/langgraph |
| 3 | **OpenAI Agents SDK** | Lightweight multi-agent workflows with handoffs, guardrails, tracing (Mar 2025) | ~27K | github.com/openai/openai-agents-python |
| 4 | **AutoGen** (Microsoft) | Multi-agent conversations framework — **now in maintenance mode** | ~57-59K | github.com/microsoft/autogen |
| 5 | **Microsoft Agent Framework** | Unified successor to AutoGen+Semantic Kernel (1.0 GA April 2026) | ~11.6K | github.com/microsoft/agent-framework |
| 6 | **CrewAI** | Fast, flexible role-based multi-agent automation (independent of LangChain) | ~30-48K | github.com/crewAIInc/crewAI |
| 7 | **Agno** (formerly Phidata) | Fastest multi-modal agent framework + AgentOS self-hosted runtime | ~40K+ | github.com/agno-agi/agno |
| 8 | **Google ADK** | Code-first agent framework with deterministic+LLM routing, Vertex AI deploy | ~20K+ | github.com/google/adk-python |
| 9 | **Anthropic Claude Agent SDK** | Production agent SDK built on Claude Code harness, MCP support (Apr 2025) | [?] new | github.com/anthropics/claude-agent-sdk-python |
| 10 | **Haystack** (deepset) | Modular pipeline+agent orchestration with explicit control over RAG/routing | ~25K | github.com/deepset-ai/haystack |
| 11 | **DSPy** (Stanford) | Programming—not prompting—LMs. Algorithmic prompt/weight optimization | ~34K+ | github.com/stanfordnlp/dspy |
| 12 | **Smolagents** (HuggingFace) | Minimalist agents that think in code (~1,000 lines of core logic) | ~26.3K | github.com/huggingface/smolagents |
| 13 | **LlamaIndex** | Document agent & OCR platform — agents over your data (49.5K stars) | ~49.5K | github.com/run-llama/llama_index |
| 14 | **Pydantic AI** | GenAI Agent Framework, the Pydantic way — type-safe, model-agnostic | ~14.7K | github.com/pydantic/pydantic-ai |

## Structured Output / Control Libraries

| # | Framework | Description | ★ Stars | URL |
|---|-----------|-------------|---------|-----|
| 15 | **Instructor** | Structured Pydantic-validated outputs from any LLM (by jxnl) | ~11K | github.com/instructor-ai/instructor |
| 16 | **Marvin** (PrefectHQ) | Ambient intelligence library — tasks + agents for structured workflows | ~5K [?] | github.com/PrefectHQ/marvin |
| 17 | **Guidance** (Microsoft Research) | Constraint language for controlling LLM output (Rust-backed, 50μs/step) | ~19K+ | github.com/guidance-ai/guidance |
| 18 | **Outlines** (dottxt) | Structured generation — guarantees schema-compliant outputs at token level | ~14K | github.com/dottxt-ai/outlines |

## Emerging Python Frameworks (2025-2026)

| # | Framework | Description | ★ Stars | URL |
|---|-----------|-------------|---------|-----|
| 19 | **Mirascope** | "The LLM Anti-Framework" — Goldilocks API between raw SDKs and heavy frameworks | ~2K [?] | github.com/Mirascope/mirascope |
| 20 | **ControlFlow** (PrefectHQ) | Task-centric AI workflow management on Prefect 3.0 engine | ~2K [?] | github.com/PrefectHQ/ControlFlow |
| 21 | **Atomic Agents** | Extremely lightweight, modular agentic pipelines (atomicity principle) | ~3K [?] | github.com/BrainBlend-AI/atomic-agents |
| 22 | **LiveKit Agents** | Realtime voice/video AI agents framework | ~5K+ [?] | github.com/livekit/agents |

## TYPESCRIPT / JAVASCRIPT FRAMEWORKS

| # | Framework | Description | ★ Stars | URL |
|---|-----------|-------------|---------|-----|
| 23 | **Mastra** | Modern TS framework for AI apps+agents (by Gatsby team, YC W25). 1.0 Jan 2026 | ~22K+ | github.com/mastra-ai/mastra |
| 24 | **Vercel AI SDK** | The AI Toolkit for TypeScript — streaming, edge runtime, framework-agnostic | ~15K+ [?] | github.com/vercel/ai |
| 25 | **Vercel Eve** ⚡NEW | Filesystem-first TS agent framework — durable execution, sandboxed compute (Jun 2026) | NEW | github.com/vercel/eve |
| 26 | **LangChain.js** | JS/TS agent engineering platform — mirrors Python LangChain | ~13K+ [?] | github.com/langchain-ai/langchainjs |
| 27 | **LangGraph.js** | Graph-based stateful agents in TypeScript | ~2K+ [?] | github.com/langchain-ai/langgraphjs |
| 28 | **Genkit** (Google) | AI-powered apps in JS, Go, Python — built by Google/Firebase team | ~6.1K | github.com/genkit-ai/genkit |
| 29 | **Google ADK (JS)** | TypeScript Agent Development Kit — same patterns as Python ADK | [?] new | github.com/google/adk-js |
| 30 | **LiveKit Agents JS** | Realtime multimodal AI agents in Node.js | [?] | github.com/livekit/agents-js |

## KEY 2025-2026 TRENDS

1. **Vendor SDKs became major force**: OpenAI (Mar 2025), Google ADK (Apr 2025), Anthropic (Apr 2025), Microsoft MAF (Apr 2026)
2. **AutoGen → MAF**: Microsoft deprecated AutoGen; new development in unified Agent Framework
3. **Phidata → Agno rebrand** (Jan 2025): repositioned as production multi-agent runtime
4. **TypeScript exploded**: Mastra (22K★ in 15 months), Vercel Eve, Google ADK-JS
5. **Code-as-action**: Smolagents' pattern (LLM writes Python as action) widely adopted
6. **Filesystem-first agents**: Vercel Eve's "agent as directory" model — new 2026 pattern
7. **Consolidation**: LlamaIndexTS archived; LangChain pivoted to LangGraph; CrewAI removed LangChain dependency

Full document saved to artifacts/category9_agent_frameworks.md