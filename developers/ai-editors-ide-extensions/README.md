# 💻 AI Code Editors & IDE Extensions

> Every AI-powered editor and extension for writing code faster.

---

# 🧠 AI Tools God Repo — Exhaustive Research (2025–2026)

---

## 1. PROMPT LIBRARIES & ENGINEERING

### Prompt Collections & Curated Repos

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **Awesome ChatGPT Prompts** | The original mega-collection of ChatGPT prompt examples; #32 most-starred repo on all of GitHub | https://github.com/f/awesome-chatgpt-prompts | ~143,000 |
| **ai-boost/awesome-prompts** | Curated prompts from top-rated GPTs in the GPT Store; covers prompt engineering, attack & defense | https://github.com/ai-boost/awesome-prompts | ~5,000 [?] |
| **x1xhlol/system-prompts-and-models-of-ai-tools** | Leaked/extracted system prompts for 30+ AI tools (Cursor, Claude Code, Windsurf, Devin, etc.) | https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools | ~137,000 |
| **LouisShark/chatgpt_system_prompt** | Collection of GPT system prompts and prompt injection/leaking knowledge | https://github.com/LouisShark/chatgpt_system_prompt | ~10,000 [?] |
| **YeeKal/leaked-system-prompts** | Leaked system prompts for ChatGPT, Claude, Grok, Gemini, Deepseek, Manus, v0, Lovable, Cursor | https://github.com/YeeKal/leaked-system-prompts | ~2,000 [?] |
| **asgeirtj/system_prompts_leaks** | Extracted system prompts from ChatGPT, Claude & Gemini | https://github.com/asgeirtj/system_prompts_leaks | ~1,000 [?] |
| **EliFuzz/awesome-system-prompts** | System prompts & tool definitions from AI coding agents (Augment, Claude Code, Cursor, Devin, Kiro, etc.) | https://github.com/EliFuzz/awesome-system-prompts | ~500 [?] |
| **dontriskit/awesome-ai-system-prompts** | Curated AI system prompts from Windsurf, Cline, and more | https://github.com/dontriskit/awesome-ai-system-prompts | ~500 [?] |

### Prompt Engineering Guides

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **DAIR.AI Prompt Engineering Guide** | The most comprehensive open-source guide: papers, lessons, notebooks, resources for prompt/context engineering, RAG, and agents | https://github.com/dair-ai/Prompt-Engineering-Guide | ~55,000 [?] |
| **Brex Prompt Engineering Guide** | Practical, opinionated internal guide from Brex on working with GPT-4-class models | https://github.com/brexhq/prompt-engineering | ~8,500 [?] |
| **NirDiamant/Prompt_Engineering** | 22 prompt engineering techniques with hands-on Jupyter Notebook tutorials, basic to advanced | https://github.com/NirDiamant/Prompt_Engineering | ~7,100 |
| **Anthropic Prompt Engineering Docs** | Official Anthropic guide: clarity, XML structuring, examples, thinking, agentic systems | https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview | — |
| **OpenAI Prompt Engineering Guide** | Official OpenAI best practices for GPT models | https://platform.openai.com/docs/guides/prompt-engineering | — |
| **IBM 2026 Guide to Prompt Engineering** | Comprehensive enterprise guide with tools, tutorials, and real-world examples | https://www.ibm.com/think/prompt-engineering | — |
| **thibaultyou/prompt-blueprint** | Multi-model prompt best practices guide (Anthropic, OpenAI, Gemini) | https://github.com/thibaultyou/prompt-blueprint | ~500 [?] |

### Prompting Techniques

| Technique | Description | Key Reference |
|-----------|-------------|---------------|
| **Chain of Thought (CoT)** | Step-by-step reasoning before final answer; dramatically improves multi-step tasks | Wei et al., 2022 — https://arxiv.org/abs/2201.11903 |
| **Tree of Thoughts (ToT)** | Explores multiple reasoning paths in a tree structure; enables search/backtracking | Yao et al., 2023 — https://arxiv.org/abs/2305.10601 |
| **ReAct (Reasoning + Acting)** | Interleaves reasoning traces with tool actions; foundation for agentic prompting | Yao et al., 2022 — https://arxiv.org/abs/2210.03629 |
| **Self-Consistency** | Samples multiple CoT paths and takes majority vote; improves accuracy at cost of tokens | Wang et al., 2022 — https://arxiv.org/abs/2203.11171 |
| **Few-Shot Prompting** | Provides examples in the prompt to demonstrate desired format/reasoning | Brown et al., 2020 (GPT-3 paper) |
| **Zero-Shot CoT** | Simply adding "Let's think step by step" triggers reasoning without examples | Kojima et al., 2022 — https://arxiv.org/abs/2205.11916 |
| **Structured Output / JSON Mode** | Constraining output to valid JSON/schema for deterministic parsing | Native in OpenAI, Anthropic APIs (2024+) |
| **Layered CoT** | 2025 technique: multi-level reasoning decomposition for complex tasks | Vellum, 2025 |
| **Context Engineering** | 2025-2026 paradigm shift: designing everything entering the context window (instructions, memory, tools, state) | Coined by Andrej Karpathy, 2025 |

### Prompt Management Tools

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **Langfuse** | Open-source AI engineering platform: prompt management, versioning, playground, evals, observability (acquired by ClickHouse Jan 2026) | https://github.com/langfuse/langfuse | ~18,000 [?] |
| **PromptLayer** | "CMS for prompts" — middleware capturing every request/response; version history, A/B testing, deployment | https://promptlayer.com | — (SaaS) |
| **Helicone** | Developer-focused AI gateway with prompt management, logging, caching; one-line integration | https://github.com/Helicone/helicone | ~3,000 [?] |
| **Pezzo** | Open-source LLMOps platform: prompt design, version management, delivery, collaboration, observability | https://github.com/pezzolabs/pezzo | ~2,400 [?] |
| **PromptHub** | Collaborative prompt management platform for teams; versioning and testing | https://www.prompthub.us | — (SaaS) |
| **Vellum** | Enterprise prompt engineering platform with version control, A/B testing, deployment pipelines | https://www.vellum.ai | — (SaaS) |
| **Braintrust** | Prompt management + eval + gateway; git-style prompt versioning with regression testing | https://www.braintrust.dev | — (SaaS) |

### Prompt Testing & Evaluation

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **promptfoo** | CLI-first prompt testing & red-teaming tool; YAML configs, 50+ vulnerability scans, CI/CD; used by OpenAI & Anthropic | https://github.com/promptfoo/promptfoo | ~10,800 |
| **DeepEval** | LLM evaluation framework applying unit testing principles (Pytest integration); 50+ metrics | https://github.com/confident-ai/deepeval | ~8,000 [?] |
| **Ragas** | Evaluation framework for RAG pipelines: faithfulness, relevance, answer quality metrics | https://github.com/explodinggradients/ragas | ~8,000 [?] |
| **Giskard** | Open-source evaluation & red-teaming for LLM agents; vulnerability scanning and testing | https://github.com/Giskard-AI/giskard | ~5,200 |
| **Braintrust Evals** | Side-by-side regression diffs, LLM-as-judge scoring, CI quality gates, dataset management | https://www.braintrust.dev | — (SaaS) |
| **Pydantic Evals** | Pydantic-native eval framework with retry strategies and structured test cases | https://pydantic.dev/docs/ai/evals | — |

---

## 2. LLM GATEWAYS & ROUTERS

### Primary Gateways

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **LiteLLM** | Open-source Python proxy providing unified OpenAI-compatible API for 200+ LLM providers; built-in caching, rate limiting, cost tracking | https://github.com/BerriAI/litellm | ~18,000 [?] |
| **Portkey AI Gateway** | Blazing-fast AI gateway with 50+ integrated guardrails; routes to 1,600+ LLMs with single API | https://github.com/Portkey-AI/gateway | ~12,200 |
| **OpenRouter** | Managed multi-model marketplace; 300+ models via single OpenAI-compatible endpoint; 5.5% markup on credits | https://openrouter.ai | — (SaaS) |
| **Martian** | First dedicated LLM router — uses model understanding to achieve higher performance at lower cost than any single provider | https://withmartian.com | — (SaaS) |
| **Braintrust Gateway** | Unified API for OpenAI, Anthropic, Google, AWS Bedrock, Vertex AI, Azure, Mistral; supports caching, logging, load balancing | https://www.braintrust.dev/docs/deploy/gateway | — (open-source) |
| **Cloudflare AI Gateway** | Edge-native proxy between code and any AI provider; adds caching, rate limiting, spend tracking, logs with zero code changes | https://developers.cloudflare.com/ai-gateway/ | — (SaaS) |
| **Kong AI Gateway** | Enterprise API gateway extended for AI traffic; same operational model, observability, and security controls as Kong API management | https://konghq.com/products/kong-ai-gateway | — (Enterprise) |
| **Requesty** | Managed AI gateway built in Rust; 400+ models, 8ms P50 overhead, smart routing, auto-caching (60% cost savings), EU data residency | https://www.requesty.ai | — (SaaS) |
| **Helicone** | Observability-first gateway; proxy overhead provides LLM monitoring, analytics, cost tracking with free tier | https://www.helicone.ai | ~3,000 [?] |
| **Traceloop Hub** | High-scale LLM gateway written in Rust with OpenTelemetry-based observability built in | https://github.com/traceloop/hub | ~500 [?] |

### Comparison Summary (2026)

| Platform | Models | Overhead (P50) | Pricing | Self-Host | Best For |
|----------|--------|---------------|---------|-----------|----------|
| LiteLLM | 200+ | 10-20ms | Free (self-host) | ✅ | Zero markup at scale |
| Portkey | 1,600+ | 10-20ms | Per-log pricing | Gateway only | Guardrails + enterprise observability |
| OpenRouter | 300+ | 40-55ms | 5.5% on credits | ❌ | Quick model access for solo devs |
| Requesty | 400+ | 8ms | 5% markup | ❌ | Production routing with caching |
| Cloudflare | Major providers | Sub-10ms at edge | Pay-per-request | ❌ | Cloudflare-native stacks |
| Kong | Provider-dependent | Varies | Enterprise license | ✅ | Teams already on Kong |
| Braintrust | Major providers | ~15ms | Free tier + usage | ✅ | Eval + gateway combined |

---

## 3. TROUBLESHOOTING / COMMON PROBLEMS

### Token Limit Calculators

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **tiktoken** | OpenAI's official BPE tokenizer; exact token counts for all OpenAI models; 500K+ tokens/sec | https://github.com/openai/tiktoken | ~13,000 [?] |
| **TiktokenSharp** | .NET port of tiktoken for C# developers; supports o200k_base, cl100k_base, p50k_base | https://github.com/aiqinxuancai/TiktokenSharp | ~300 [?] |
| **LLM Cost Calculator** | Web tool comparing hosted API vs local GPU inference costs across models | https://llmcostcalc.com | — |
| **KickLLM** | Free LLM API cost calculator comparing 25+ models (May 2026 pricing) | https://kickllm.com | — |
| **LLM Cost Hub** | Cost calculator + token counter for estimating prompt size and monthly spend | https://llmcosthub.com | — |
| **Morph LLM Calculator** | Breaks down every major LLM's API pricing with workload cost estimations | https://www.morphllm.com/llm-cost-calculator | — |
| **iternal.ai Calculator** | AI API pricing calculator with 2026 model prices | https://iternal.ai/calculators/llm-pricing-calculator | — |

### Rate Limit Handling Libraries

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **tenacity** | Apache 2.0 general-purpose Python retrying library; exponential backoff, jitter, stop conditions; the standard for LLM API retries | https://github.com/jd/tenacity | ~6,500 [?] |
| **backoff** | Python function decorator for exponential backoff and retry on exceptions | https://github.com/litl/backoff | ~2,200 [?] |
| **aiolimiter** | Async rate limiter for Python using token bucket algorithm | https://github.com/mjpieters/aiolimiter | ~500 [?] |
| **LiteLLM (built-in)** | Includes rate limiting, retry logic, and fallback routing out of the box | https://github.com/BerriAI/litellm | ~18,000 [?] |
| **Portkey (built-in)** | Enterprise-grade rate limiting with per-user/org quotas and automatic failover | https://portkey.ai | — |

### LLM Output Parsing & Structured Generation

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **Instructor** | Most popular library for extracting structured data (Pydantic models) from LLMs; 3M+ monthly downloads; multi-language | https://github.com/instructor-ai/instructor | ~11,000 |
| **Outlines (dottxt-ai)** | Structured generation via constrained decoding; masks invalid tokens at generation time; JSON/regex/grammar guaranteed | https://github.com/dottxt-ai/outlines | ~10,000 [?] |
| **Microsoft Guidance** | A guidance language for controlling LLMs; interleaves generation, prompting, and logic; enforces structured formats | https://github.com/microsoft/guidance | ~18,000 |
| **LMQL** | Language for constraint-guided and efficient LLM programming; SQL-like syntax for prompts with type constraints | https://github.com/eth-sri/lmql | ~3,500 [?] |
| **Marvin** | AI engineering toolkit for building reliable AI-powered software; structured extraction with simple decorators | https://github.com/prefecthq/marvin | ~5,000 [?] |
| **Guardrails AI** | Framework for adding structure, type, and quality guarantees to LLM outputs | https://github.com/guardrails-ai/guardrails | ~4,000 [?] |
| **LangChain Output Parsers** | Built-in parsers for JSON, Pydantic, XML, structured output within LangChain | https://github.com/langchain-ai/langchain | ~100,000+ |

### Hallucination Detection Tools

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **Vectara HHEM** | Hallucination Evaluation Model — FICO-like score for grading factual consistency; powers the Hallucination Leaderboard | https://github.com/vectara/hallucination-leaderboard | ~2,000 [?] |
| **Patronus Lynx** | SOTA hallucination detection LLM with advanced reasoning on real-world scenarios; HaluBench (15K samples) | https://arxiv.org/abs/2407.08488 | — (model) |
| **Galileo Luna** | Commercial hallucination detection scoring aligned to factual accuracy; integrated with Galileo platform | https://galileo.ai | — (SaaS) |
| **Exa Hallucination Detector** | Free open-source tool to verify accuracy of LLM-generated content instantly | https://github.com/exa-labs/exa-hallucination-detector | ~1,000 [?] |
| **UQLM** | Uncertainty Quantification for Language Models — UQ-based hallucination detection (by CVS Health) | https://github.com/cvs-health/uqlm | ~200 [?] |
| **DeepEval (Hallucination Metric)** | Built-in hallucination metric within DeepEval framework | https://github.com/confident-ai/deepeval | ~8,000 [?] |
| **Braintrust (LLM-as-Judge)** | Custom LLM-as-a-judge scorers for hallucination detection with trace-level online scoring | https://www.braintrust.dev | — |
| **Future AGI ACC** | Production hallucination detection with high accuracy scores | https://futureagi.com | — (SaaS) |

### Cost Estimation Tools

| Name | Description | URL |
|------|-------------|-----|
| **LLM Cost Calculator** | Compare Claude, GPT-5, Gemini pricing; monthly input/output tokens vs GPU inference | https://llmcostcalc.com |
| **KickLLM** | Free calculator for 25+ models with real pricing data | https://kickllm.com |
| **LLM Cost Hub** | Cost calculator + token counter; estimate spend across providers | https://llmcosthub.com |
| **Morph LLM Cost Calculator** | Detailed per-model pricing with optimization strategies (60%+ savings) | https://www.morphllm.com/llm-cost-calculator |
| **iternal.ai** | Comprehensive 2026 pricing data across all major APIs | https://iternal.ai/calculators/llm-pricing-calculator |
| **LiteLLM (built-in cost tracking)** | Tracks costs per request, per user, per model automatically | https://github.com/BerriAI/litellm |
| **Helicone (cost analytics)** | Real-time cost tracking with per-user and per-feature breakdowns | https://www.helicone.ai |
| **tiktoken (pre-request estimation)** | Count tokens locally before API call to predict costs and avoid overages | https://github.com/openai/tiktoken |

### Context Window Management Strategies & Tools

| Strategy/Tool | Description | Reference |
|---------------|-------------|-----------|
| **Sliding Window / Truncation** | Keep only the N most recent messages; simple but loses history | Standard pattern |
| **Recursive Summarization** | Periodically summarize older context into compressed form; maintains key info | LangChain ConversationSummaryMemory |
| **RAG (Retrieval-Augmented Generation)** | Store context externally; retrieve relevant chunks on demand instead of stuffing context | LlamaIndex, LangChain retrievers |
| **Observation Masking** | Simple masking halves cost while matching summarization solve rates (2025 paper) | https://arxiv.org/html/2508.21433v1 |
| **Token Budgeting** | Allocate fixed token budgets per context component (system, history, retrieval, tools) | Context Engineering best practice |
| **MemGPT/Letta** | Virtual context management — pages information in/out of context like an OS manages memory | https://github.com/cpacker/MemGPT |
| **LangChain ConversationBufferWindowMemory** | Built-in sliding window memory for LangChain chains | https://github.com/langchain-ai/langchain |

### Caching Solutions for LLM Calls

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **GPTCache** | Semantic cache for LLMs by Zilliz; uses embeddings to match similar queries; integrated with LangChain/LlamaIndex | https://github.com/zilliztech/GPTCache | ~7,000 [?] |
| **Redis Semantic Cache (RedisVL)** | LLM caching with SemanticCache class; cosine similarity matching; 3-8ms response vs 500-2000ms | https://redis.io/docs/latest/develop/ai/redisvl/ | — |
| **LiteLLM Caching** | Built-in caching layer (in-memory, Redis, or S3); exact and semantic match modes | https://github.com/BerriAI/litellm | ~18,000 [?] |
| **Portkey Cache** | Automatic semantic caching at the gateway level; claims 60% cost savings | https://portkey.ai | — |
| **Cloudflare AI Gateway Cache** | Edge caching for AI responses with configurable TTL | https://developers.cloudflare.com/ai-gateway/ | — |
| **Requesty Auto-Cache** | Smart caching built into gateway with 60% cost reduction | https://www.requesty.ai | — |
| **Momento** | Serverless caching service with LLM-specific semantic cache product | https://www.gomomento.com | — (SaaS) |

---

## 4. OBSERVABILITY & MONITORING

### Primary LLM Observability Platforms

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **Langfuse** | Open-source AI engineering platform: tracing, evals, metrics, prompt management, playground, datasets; OTel-native; used by 63 of Fortune 500; acquired by ClickHouse (Jan 2026) | https://github.com/langfuse/langfuse | ~18,000 [?] |
| **LangSmith** | LangChain-native observability: deepest framework integration, tracing, prompt versioning, dataset management, testing | https://smith.langchain.com | — (SaaS) |
| **Arize Phoenix** | Open-source AI observability & evaluation; LLM tracing, RAG evaluation, pre-built eval templates; built on OpenTelemetry | https://github.com/Arize-ai/phoenix | ~10,200 |
| **Opik (by Comet)** | Open-source platform for LLM app lifecycle: tracing, evaluation, monitoring, prompt optimization | https://github.com/comet-ml/opik | ~7,000 [?] |
| **Helicone** | Drop-in proxy (simplest install); one-line integration for logging, cost tracking, analytics | https://www.helicone.ai | ~3,000 [?] |
| **Traceloop OpenLLMetry** | Open-source OTel-based observability for GenAI/LLM apps; auto-instruments popular frameworks | https://github.com/traceloop/openllmetry | ~3,000 [?] |
| **Braintrust** | Eval + observability + gateway combined; side-by-side diffs, online scoring, prompt regression | https://www.braintrust.dev | — (SaaS) |

### Enterprise/Commercial Observability

| Name | Description | URL |
|------|-------------|-----|
| **Datadog LLM Observability** | Enterprise-default for Datadog shops; agent observability, tracing, cost monitoring, security | https://www.datadoghq.com/product/llm-observability/ |
| **Weights & Biases Weave** | W&B's LLM-specific tool for logging, tracing, and evaluating prompts and model calls | https://wandb.ai/site/weave |
| **Honeycomb LLM Observability** | Event-based deep tracing for AI applications; fine-grained performance analysis | https://www.honeycomb.io |
| **Portkey Logs & Analytics** | Full request/response logging, latency tracking, cost attribution within Portkey gateway | https://portkey.ai |
| **Arize (Commercial)** | Enterprise-scale AI monitoring platform (Phoenix is the open-source component) | https://arize.com |
| **Latitude** | AI agent observability with multi-turn tracing, issue discovery, real-time monitoring | https://latitude.so |
| **SigNoz** | Open-source APM with LLM observability support built on OpenTelemetry | https://signoz.io |

### Specialized Monitoring Tools

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **Arize OpenInference** | OpenTelemetry instrumentation library specifically for AI observability; framework-agnostic | https://github.com/Arize-ai/openinference | ~2,000 [?] |
| **TruLens** | Open-source library for evaluating and tracking LLM apps; feedback functions, tracing | https://github.com/truera/trulens | ~3,000 [?] |
| **Traceloop OpenTelemetry MCP Server** | Unified MCP server for querying OTel traces across backends; enables AI agents to analyze distributed traces | https://github.com/traceloop/opentelemetry-mcp-server | ~500 [?] |
| **MLflow (LLM Tracking)** | MLflow's extended tracking capabilities for LLM experiments, prompts, and artifacts | https://github.com/mlflow/mlflow | ~20,000+ |

### Observability Comparison Matrix (2026)

| Platform | Open Source | Self-Host | OTel Native | Best For |
|----------|-------------|-----------|-------------|----------|
| Langfuse | ✅ | ✅ | ✅ | General-purpose, framework-agnostic |
| LangSmith | ❌ | ❌ | ❌ | LangChain/LangGraph ecosystems |
| Arize Phoenix | ✅ | ✅ | ✅ | RAG evaluation, ML-grade rigor |
| Opik | ✅ | ✅ | ✅ | Full lifecycle + optimization |
| Helicone | ❌ (partial) | ❌ | ❌ | Simplest setup, cost tracking |
| OpenLLMetry | ✅ | ✅ | ✅ | OTel purists, BYOB observability |
| Datadog LLM | ❌ | ❌ | ✅ | Enterprise Datadog shops |
| W&B Weave | ❌ | ❌ | ❌ | ML teams already on W&B |

---

## NOTES

- **Star counts** are approximate as of June 2026. Items marked **[?]** have estimated counts based on available data and may vary.
- **"SaaS"** indicates a commercial product without an open-source core repo.
- The AI tools ecosystem is rapidly consolidating. Key trends in 2025-2026:
  - Langfuse acquired by ClickHouse (Jan 2026)
  - "Context engineering" replacing "prompt engineering" as the dominant paradigm
  - OpenTelemetry becoming the standard for LLM observability
  - Gateway consolidation around OpenAI-compatible APIs
  - Evaluation tools converging on LLM-as-judge + human-in-the-loop patterns
