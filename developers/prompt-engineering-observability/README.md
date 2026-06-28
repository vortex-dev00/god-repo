# 🎯 Prompt Engineering & LLM Observability

> Prompt libraries, evaluation tools, observability platforms, and LLM tooling.

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

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **LiteLLM** | Open-source Python proxy providing unified OpenAI-compatible API for 200+ LLM providers; built-in caching, rate limiting, cost tracking | https://github.com/BerriAI/litellm | ~18,000 [?] |
| **Portkey AI Gateway** | Blazing-fast AI gateway with 50+ integrated guardrails; routes to 1,600+ LLMs with single API | https://github.com/Portkey-AI/gateway | ~12,200 |
| **OpenRouter** | Managed multi-model marketplace; 300+ models via single OpenAI-compatible endpoint; 5.5% markup | https://openrouter.ai | — (SaaS) |
| **Martian** | First dedicated LLM router — uses model understanding to achieve higher performance at lower cost | https://withmartian.com | — (SaaS) |
| **Braintrust Gateway** | Unified API for OpenAI, Anthropic, Google, AWS Bedrock, Vertex AI, Azure, Mistral; caching, logging, load balancing | https://www.braintrust.dev/docs/deploy/gateway | — (open-source) |
| **Cloudflare AI Gateway** | Edge-native proxy; caching, rate limiting, spend tracking with zero code changes | https://developers.cloudflare.com/ai-gateway/ | — (SaaS) |
| **Kong AI Gateway** | Enterprise API gateway extended for AI traffic; same operational model as Kong API management | https://konghq.com/products/kong-ai-gateway | — (Enterprise) |
| **Requesty** | Managed AI gateway built in Rust; 400+ models, 8ms P50 overhead, smart routing, EU data residency | https://www.requesty.ai | — (SaaS) |
| **Helicone** | Observability-first gateway; one-line integration for logging, cost tracking, analytics | https://www.helicone.ai | ~3,000 [?] |
| **Traceloop Hub** | High-scale LLM gateway written in Rust with OpenTelemetry observability built in | https://github.com/traceloop/hub | ~500 [?] |

---

## 3. TROUBLESHOOTING / COMMON PROBLEMS

### Token Limit Calculators
| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **tiktoken** | OpenAI's official BPE tokenizer; exact token counts for all OpenAI models; 500K+ tokens/sec | https://github.com/openai/tiktoken | ~13,000 [?] |
| **TiktokenSharp** | .NET port for C# developers; supports o200k_base, cl100k_base, p50k_base | https://github.com/aiqinxuancai/TiktokenSharp | ~300 [?] |
| **LLM Cost Calculator** | Web tool comparing hosted API vs local GPU inference costs | https://llmcostcalc.com | — |
| **KickLLM** | Free LLM API cost calculator comparing 25+ models | https://kickllm.com | — |
| **LLM Cost Hub** | Cost calculator + token counter | https://llmcosthub.com | — |

### Rate Limit Handling
| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **tenacity** | Python retrying library; exponential backoff, jitter, stop conditions; standard for LLM retries | https://github.com/jd/tenacity | ~6,500 [?] |
| **backoff** | Python function decorator for exponential backoff/retry | https://github.com/litl/backoff | ~2,200 [?] |
| **aiolimiter** | Async rate limiter using token bucket algorithm | https://github.com/mjpieters/aiolimiter | ~500 [?] |
| **LiteLLM (built-in)** | Rate limiting, retry logic, and fallback routing out of the box | https://github.com/BerriAI/litellm | ~18,000 [?] |

### LLM Output Parsing
| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **Instructor** | Most popular library for Pydantic-validated structured extraction from LLMs; 3M+ monthly downloads | https://github.com/instructor-ai/instructor | ~11,000 |
| **Outlines (dottxt-ai)** | Constrained decoding; masks invalid tokens; guarantees JSON/regex/grammar compliance | https://github.com/dottxt-ai/outlines | ~10,000 [?] |
| **Microsoft Guidance** | Language for controlling LLMs; interleaves generation with logic; enforces structured formats | https://github.com/microsoft/guidance | ~18,000 |
| **LMQL** | Constraint-guided LLM programming; SQL-like syntax with type constraints | https://github.com/eth-sri/lmql | ~3,500 [?] |
| **Guardrails AI** | Framework for structure, type, and quality guarantees on LLM outputs | https://github.com/guardrails-ai/guardrails | ~4,000 [?] |

### Hallucination Detection
| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **Vectara HHEM + Leaderboard** | Hallucination Evaluation Model; FICO-like score for factual consistency | https://github.com/vectara/hallucination-leaderboard | ~2,000 [?] |
| **Patronus Lynx** | SOTA hallucination detection LLM; HaluBench benchmark (15K samples) | https://arxiv.org/abs/2407.08488 | — |
| **Galileo Luna** | Commercial hallucination detection scoring | https://galileo.ai | — |
| **Exa Hallucination Detector** | Free open-source verification tool | https://github.com/exa-labs/exa-hallucination-detector | ~1,000 [?] |
| **UQLM** | Uncertainty Quantification-based detection (CVS Health) | https://github.com/cvs-health/uqlm | ~200 [?] |

### Caching Solutions
| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **GPTCache** | Semantic cache for LLMs by Zilliz; embedding-based similarity matching | https://github.com/zilliztech/GPTCache | ~7,000 [?] |
| **Redis Semantic Cache (RedisVL)** | Cosine similarity matching; 3-8ms vs 500-2000ms response time | https://redis.io/docs/latest/develop/ai/redisvl/ | — |
| **LiteLLM Caching** | Built-in caching (in-memory, Redis, S3); exact and semantic modes | https://github.com/BerriAI/litellm | ~18,000 [?] |
| **Portkey Cache** | Gateway-level semantic caching; ~60% cost savings | https://portkey.ai | — |
| **Cloudflare AI Gateway Cache** | Edge caching with configurable TTL | https://developers.cloudflare.com/ai-gateway/ | — |

---

## 4. OBSERVABILITY & MONITORING

### Open-Source Platforms
| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **Langfuse** | Full AI engineering platform: tracing, evals, metrics, prompt management; OTel-native; by ClickHouse | https://github.com/langfuse/langfuse | ~18,000 [?] |
| **Arize Phoenix** | AI observability & evaluation; LLM tracing, RAG eval templates; OpenTelemetry-based | https://github.com/Arize-ai/phoenix | ~10,200 |
| **Opik (Comet)** | LLM lifecycle: tracing, evaluation, monitoring, prompt optimization | https://github.com/comet-ml/opik | ~7,000 [?] |
| **Traceloop OpenLLMetry** | OTel-based observability for GenAI/LLM apps; auto-instruments popular frameworks | https://github.com/traceloop/openllmetry | ~3,000 [?] |
| **TruLens** | Evaluating and tracking LLM apps; feedback functions and tracing | https://github.com/truera/trulens | ~3,000 [?] |

### Commercial/Enterprise
| Name | Description | URL |
|------|-------------|-----|
| **LangSmith** | LangChain-native: deepest framework integration, tracing, prompt versioning | https://smith.langchain.com |
| **Datadog LLM Observability** | Enterprise: agent observability, tracing, cost monitoring | https://www.datadoghq.com/product/llm-observability/ |
| **Weights & Biases Weave** | LLM-specific logging, tracing, evaluation for ML teams | https://wandb.ai/site/weave |
| **Honeycomb** | Event-based deep tracing for AI applications | https://www.honeycomb.io |
| **Helicone** | Drop-in proxy; one-line cost/latency/quality monitoring | https://www.helicone.ai |
| **Portkey Logs** | Full request/response logging, cost attribution within gateway | https://portkey.ai |
| **Latitude** | Multi-turn tracing, issue discovery, real-time monitoring | https://latitude.so |

---

**Notes:** Star counts are approximate (June 2026). [?] = estimated from indirect sources. The ecosystem is consolidating rapidly — Langfuse acquired by ClickHouse, "context engineering" replacing "prompt engineering" as paradigm, OpenTelemetry becoming the observability standard, and gateways converging on OpenAI-compatible APIs.