# 🤖 AI Models & Providers

> Every AI API with pricing, context windows, and capabilities.

---

# CATEGORY 12: AI MODELS & PROVIDERS (Raw APIs)

> Exhaustive research compiled June 2026. Prices in USD per million tokens (MTok) unless otherwise noted. All dates verified against official sources where possible.

---

## 1. ANTHROPIC (Claude)

**URL:** https://www.anthropic.com / https://docs.anthropic.com

### Current Models (as of June 2026)

| Model | Input/MTok | Output/MTok | Context Window | Release Date |
|-------|-----------|-------------|----------------|--------------|
| **Claude Opus 4.8** | $5.00 | $25.00 | 1M (API/Bedrock), 500K (chat) | ~May 2026 |
| **Claude Opus 4.7** | $5.00 | $25.00 | 1M (API), 500K (chat) | ~Apr 2026 |
| **Claude Opus 4.6** | $5.00 | $25.00 | 1M (API), 500K (chat) | ~Mar 2026 |
| **Claude Sonnet 4.6** | $3.00 | $15.00 | 1M (Code), 500K (chat) | ~Mar 2026 |
| **Claude Haiku 4.5** | $1.00 | $5.00 | 200K | ~Late 2025 |
| **Claude Opus 4** | $15.00 | $75.00 | 200K | May 22, 2025 |
| **Claude Sonnet 4** | $3.00 | $15.00 | 200K (expandable to 1M) | May 22, 2025 |

### Key Details
- **Claude Opus 4 / Sonnet 4** — Launched May 22, 2025. 200K context window (later expanded). Introduced "Extended Thinking" (multi-hour autonomous operation). Hybrid models: instant responses + deep reasoning mode.
- **Claude Opus 4.8** — Latest flagship (June 2026). Optimized for coding, agents, deeper reasoning. 1M context on API by default. 128K max output tokens. Adaptive thinking.
- **Claude Fable 5** — Next-gen model for multi-day autonomous tasks, available on Bedrock. [?]
- **Prompt caching** — 90% discount on cached input tokens.
- **Batch API** — 50% discount on standard pricing.
- **Consumer plans**: Free / Pro ($20/mo) / Max ($100–$200/mo)

---

## 2. OPENAI

**URL:** https://openai.com / https://platform.openai.com

### Current Models

| Model | Input/MTok | Output/MTok | Context Window | Release Date |
|-------|-----------|-------------|----------------|--------------|
| **GPT-4.1** | $2.00 | $8.00 | 1M tokens | Apr 14, 2025 |
| **GPT-4.1 Mini** | $0.40 | $1.60 | 1M tokens | Apr 14, 2025 |
| **GPT-4.1 Nano** | $0.10 | $0.40 | 1M tokens | Apr 14, 2025 |
| **GPT-4o** | $2.50 | $10.00 | 128K tokens | May 2024 |
| **GPT-4o Mini** | $0.15 | $0.60 | 128K tokens | Jul 2024 |
| **o3** (reasoning) | $2.00 | $8.00 | 200K tokens | Apr 16, 2025 |
| **o3-pro** (reasoning) | [?] higher | [?] higher | 200K tokens | Jun 10, 2025 |
| **o4-mini** (reasoning) | $1.10 | $4.40 | 200K tokens | Apr 16, 2025 |
| **o1** (reasoning) | $15.00 | $60.00 | 200K tokens | Sep 2024 |

### Key Details
- **GPT-4.1 family** — Purpose-built for coding & instruction following. 1M-token context with excellent long-context comprehension. 54.6% on SWE-Bench Verified. 75% prompt caching discount.
- **o3 / o4-mini** — Reasoning models released Apr 16, 2025. Can call tools within chain-of-thought. o3 is the "most intelligent" model; o4-mini is budget reasoning.
- **GPT-4o** — Retired from ChatGPT (Feb 13, 2026) but still available via API.
- **GPT-5 series** — GPT-5.3 Instant (128K) and GPT-5.4 Thinking (196K) existed but were retired from ChatGPT Feb 2026. [?]
- **Prompt caching**: 50–75% discount on cached tokens depending on model.

---

## 3. GOOGLE (Gemini)

**URL:** https://ai.google.dev / https://cloud.google.com/vertex-ai

### Current Models

| Model | Input/MTok | Output/MTok | Context Window | Release Date |
|-------|-----------|-------------|----------------|--------------|
| **Gemini 2.5 Pro** | $1.25 | $10.00 | 1M tokens (up to 2M [?]) | Mar 2025 (GA Jun 2025) |
| **Gemini 2.5 Flash** | $0.30 | $2.50 | 1M tokens | ~May 2025 |
| **Gemini 2.5 Flash-Lite** | ~$0.10 | ~$1.00 | 1M tokens [?] | ~Sep 2025 |
| **Gemini 2.0 Flash** | $0.10 | $0.40 | 1M tokens | Late 2024/Early 2025 |
| **Gemini 3.1 Pro** | [?] | $12.00 | [?] | ~2026 [?] |
| **Gemini 3.5 Flash** | $1.50 | $9.00 | [?] | ~2026 [?] |

### Key Details
- **Gemini 2.5 Pro** — Google's flagship 2025 thinking model. 1M-token context (some sources say 2M). 66K max output tokens. First place on LMArena leaderboard. Best-in-class for video understanding and document extraction.
- **Gemini 2.5 Flash** — "Workhorse" model with built-in thinking capabilities. Adjustable thinking budget. 1M context, 66K output.
- **Thinking budget** — Developers control how much the model "thinks" before responding.
- **Free tier** available via Google AI Studio.
- **Consumer plans**: Free / Google AI Pro ($19.99/mo) / Google AI Ultra ($249.99/mo)

---

## 4. META (Llama)

**URL:** https://llama.meta.com / https://huggingface.co/meta-llama

### Current Models

| Model | Parameters | Architecture | Context Window | Release Date |
|-------|-----------|--------------|----------------|--------------|
| **Llama 4 Scout** | 109B total (17B active) | MoE, 16 experts | 10M tokens | Apr 5, 2025 |
| **Llama 4 Maverick** | 400B total (17B active) | MoE, 128 experts | 1M tokens [?] | Apr 5, 2025 |
| **Llama 4 Behemoth** | ~2T total (288B active) | MoE, 16 experts | [?] | Shelved / not shipped |
| **Llama 3.3 70B** | 70B | Dense | 128K tokens | Late 2024 |
| **Llama 3.2 90B** | 90B | Dense (multimodal) | 128K tokens | Sep 2024 |
| **Llama 3.1 405B** | 405B | Dense | 128K tokens | Jul 2024 |

### Key Details
- **Llama 4** — Natively multimodal (image input). Open-weight under Llama 4 Community License.
- **Where to get it**: Hugging Face (`meta-llama`), Ollama (`ollama run llama4`), direct download from Meta.
- **How to run locally**:
  - **Ollama** — `ollama run llama4` (Scout Q4_K_M = ~67GB)
  - **MLX** — For Apple Silicon (32GB+ for Scout, 96GB+ for Maverick)
  - **vLLM / TGI** — For multi-GPU server setups
  - **Hardware**: Scout runs on 32GB+ unified memory Mac or 2× A100-80G. Maverick needs 96GB+.
- **No per-token cost** — You own the weights. Run air-gapped, fine-tune freely.
- **API access** (hosted): Available via Together AI, Fireworks AI, Groq, AWS Bedrock, Azure.
- **Muse Spark** (Apr 2026) — Meta's first proprietary/closed-weight API-only reasoning model. [?]

---

## 5. MISTRAL AI

**URL:** https://mistral.ai / https://docs.mistral.ai

### Current Models

| Model | Input/MTok | Output/MTok | Context Window | Release Date |
|-------|-----------|-------------|----------------|--------------|
| **Mistral Large 3** | $2.00–$2.50 | $6.00–$8.00 | 128K [?] | Dec 2, 2025 |
| **Mistral Medium 3.5** | $1.50 | $7.50 | 128K [?] | ~2026 |
| **Mistral Medium 3** | $0.40 | $2.00 | 128K | May 7, 2025 |
| **Mistral Small 4** | $0.10–$0.15 | $0.30–$0.60 | 128K [?] | ~Mar 2026 |
| **Magistral Medium** | $2.00 | $5.00 | [?] | ~Jun 2025 |
| **Ministral 3 (3B)** | $0.10 | $0.10 | 128K [?] | Dec 2025 |

### Key Details
- **Mistral Medium 3.5** — Frontier-class multimodal model. Open weights (Modified MIT). Agentic/coding optimized. Adjustable `reasoning_effort` parameter.
- **Mistral Medium 3** — Enterprise-grade, frontier capabilities at reduced cost. Released May 2025.
- **Mistral Small 4** — Combines reasoning (from Magistral), multimodal (from Pixtral), and coding (from Devstral) in one model.
- **Magistral** — Reasoning-focused model line (like OpenAI's o-series).
- **Le Chat** — Consumer app. Free tier / Pro ($14.99/mo).
- **Available on**: Mistral API (La Plateforme), AWS Bedrock, Azure, self-hosted.

---

## 6. DEEPSEEK

**URL:** https://www.deepseek.com / https://api-docs.deepseek.com

### Current Models

| Model | Input/MTok | Output/MTok | Context Window | Release Date |
|-------|-----------|-------------|----------------|--------------|
| **DeepSeek V4 Flash** | $0.14 | $0.28 | 128K [?] | ~2026 |
| **DeepSeek V4 Pro** | $0.435–$1.74 | $0.87–$3.48 | 128K [?] | ~2026 |
| **DeepSeek V3** (deepseek-chat) | $0.07 (cache hit)–$0.14 | $0.28 | 128K | Dec 2024 / Jan 2025 |
| **DeepSeek R1** (reasoning) | $0.55 | $2.19 | 128K | Jan 2025 |

### Key Details
- **DeepSeek V3/V4** — 671B parameter MoE model. MIT licensed. Matches/exceeds GPT-4o on many benchmarks at a fraction of the cost.
- **DeepSeek R1** — Reasoning model matching OpenAI o1. MIT license. Full model = 671B params, needs 320GB+ VRAM. Distilled versions available (1.5B to 70B).
- **Cache discount**: 90% off for cache hits (as low as $0.014/MTok input).
- **Free tier**: chat.deepseek.com (free web chat). 5M free tokens for new developer accounts.
- **Local options**:
  - Ollama: `ollama run deepseek-r1` (distilled versions: 1.5B, 7B, 8B, 14B, 32B, 70B)
  - Full model requires multi-GPU (8× A100 or similar)
- **Note**: `deepseek-chat` and `deepseek-reasoner` endpoints deprecated July 2026; replaced by `deepseek-v4-flash`.

---

## 7. xAI (Grok)

**URL:** https://x.ai / https://docs.x.ai

### Current Models

| Model | Input/MTok | Output/MTok | Context Window | Release Date |
|-------|-----------|-------------|----------------|--------------|
| **Grok 4.3** | $1.25 | $2.50 | 1M tokens | Apr 30, 2026 |
| **Grok 4.20** | $2.00 | $6.00 | 1M [?] | [?] 2026 |
| **Grok 4.1 Fast** | $0.20 | $0.50 | [?] | [?] 2026 |
| **Grok 4** | [?] | [?] | 256K tokens | Jul 2025 [?] |
| **Grok 3** | $3.00 [?] | $15.00 [?] | 131K (1M on some sources) | Feb 17, 2025 |
| **Grok 3 Mini** | [?] | [?] | 131K | Feb 2025 |

### Key Details
- **Grok 3** — Released Feb 17, 2025. Introduced "Think" mode (reasoning scratch-pad). 93.3% on AIME 2025. Real-time X (Twitter) data integration.
- **Grok 4.3** — Current flagship (Apr 2026). Reasoning model for complex logic, math, science. 1M context. Knowledge cutoff Dec 2025.
- **Unique feature**: Live X/Twitter grounding — real-time access to X platform data via Web Search / X Search tools.
- **Consumer plans**: X Premium+ includes Grok access. SuperGrok for heavy users.
- **API**: OpenAI-compatible API format at `api.x.ai`.

---

## 8. COHERE

**URL:** https://cohere.com / https://docs.cohere.com

### Current Models

| Model | Input/MTok | Output/MTok | Context Window | Release Date |
|-------|-----------|-------------|----------------|--------------|
| **Command A+** | $2.50 | $10.00 | 128K [?] | ~2025 |
| **Command A** | $2.50 | $10.00 | 128K [?] | ~2025 |
| **Command R+** | $2.50 | $10.00 | 128K | Mar 2024 |
| **Command R** | $0.15 | $0.60 | 128K | Mar 2024 |
| **Command R7B** | $0.0375 | $0.15 | 128K [?] | ~2024 |
| **Embed v4** | $0.10/MTok | — | — | ~2025 |
| **Rerank 3.5** | Per search | — | — | ~2025 |

### Key Details
- **Command R+** — Enterprise-grade RAG-optimized model. Excellent for grounded generation with citations.
- **Command A/A+** — Latest generation models, same pricing as R+.
- **Specialties**: RAG, tool use, enterprise search, multilingual (10+ languages).
- **Free trial tier**: 100 API calls/min, 1,000/month.
- **Embed v4** — Cheapest vector embedding option ($0.10/MTok).
- **Enterprise focus**: On-prem deployment available. SOC 2, HIPAA compliant.

---

## 9. TOGETHER AI

**URL:** https://www.together.ai / https://www.together.ai/pricing

### Overview
Fast inference platform hosting 100+ open-source models. OpenAI-compatible API.

### Pricing (representative, per MTok)

| Model | Input/MTok | Output/MTok |
|-------|-----------|-------------|
| Llama 3.1 8B | $0.10–$0.20 | $0.20–$0.40 |
| Llama 3.3 70B | $0.88–$0.90 | $0.88–$0.90 |
| Llama 3.1 405B | $2.50 | $7.50 |
| DeepSeek V3 | varies | varies |
| Mixtral 8x7B | $0.60 | $0.60 |
| Qwen 3.5 397B | [?] | [?] |

### Key Details
- **Serverless inference**: $0.03–$4.50/MTok depending on model.
- **Dedicated endpoints**: $6.49/hr per H100 GPU.
- **GPU clusters**: $5.49/hr (on-demand) to $3.99/hr (reserved) per H100.
- **Fine-tuning**: Per-MTok training data + per-hour hosting.
- **Speed**: ~45 tok/s on Mixtral 8x7B.
- **Supports**: Llama 4, DeepSeek V3/R1, Qwen, Mistral, and many more.

---

## 10. FIREWORKS AI

**URL:** https://fireworks.ai / https://fireworks.ai/pricing

### Pricing (representative, per MTok)

| Model | Input/MTok | Output/MTok |
|-------|-----------|-------------|
| Llama 3.1 8B | $0.15–$0.20 | $0.20 |
| Llama 3.1 70B | $0.30 | $1.20 |
| Llama 3.1 405B | $1.05 | $3.00 |
| Mixtral 8x7B | $0.20 | $0.20 |

### Key Details
- **Ultra-low latency**: As low as 40ms per completion. Optimized for speed.
- **Cached input tokens**: 50% discount by default.
- **OpenAI-compatible API** — Drop-in replacement.
- **Available on Microsoft Foundry** (Azure).
- **Free tier** available for prototyping.
- **Best for**: Latency-sensitive applications, prototyping with open-source models.

---

## 11. GROQ

**URL:** https://groq.com / https://groq.com/pricing

### Pricing (representative, per MTok)

| Model | Input/MTok | Output/MTok |
|-------|-----------|-------------|
| Llama 3.1 8B | $0.05 | $0.08 |
| Llama 3.3 70B | $0.59 | $0.79 |
| Mixtral 8x7B | $0.24 | $0.24 [?] |

### Key Details
- **LPU (Language Processing Unit)** — Custom silicon designed specifically for LLM inference.
- **Speed king**: 480 tok/s on Llama 3-70B. 3ms time-to-first-token (TTFT). 200+ tok/s consistently.
- **Free tier**: All models, 30 RPM, no credit card required.
- **Paid tier**: Higher rate limits, enterprise SLAs.
- **Model selection**: Limited compared to Together/Fireworks (focused on Llama, Mixtral, Gemma).
- **Best for**: Interactive applications needing instant responses, chatbots.

---

## 12. AMAZON BEDROCK

**URL:** https://aws.amazon.com/bedrock / https://docs.aws.amazon.com/bedrock

### Available Models (June 2026)

| Provider | Models Available |
|----------|----------------|
| **Anthropic** | Claude Fable 5, Opus 4.8, Opus 4.7, Opus 4.6, Opus 4.5, Haiku 4.5, Sonnet 4.6 |
| **Meta** | Llama 4 Scout, Llama 4 Maverick, Llama 3.2 (11B, 90B), Llama 3.1 (8B, 70B, 405B) |
| **Mistral** | Mistral Large 3, Ministral 3 family, Voxtral Mini/Small, Magistral Small |
| **Cohere** | Command R+, Command R, Embed |
| **AI21** | Jamba models |
| **Amazon** | Titan Text, Titan Embeddings, Nova |
| **Stability AI** | Stable Diffusion models |

### Key Details
- **Single API endpoint** for multiple providers — unified AWS SDK access.
- **Pay-per-use**: Pricing mirrors or slightly exceeds direct provider pricing (AWS margin).
- **On-Demand & Provisioned Throughput** options.
- **How to access**: AWS Console → Bedrock → Model Access (request access per model). No separate accounts needed.
- **Features**: Guardrails, Knowledge Bases (RAG), Agents, Fine-tuning, Model Evaluation.
- **Regions**: us-east-1, us-west-2, eu-west-1, ap-northeast-1 (varies by model).
- **Security**: VPC, IAM, CloudTrail, encryption at rest.

---

## 13. HUGGING FACE INFERENCE API

**URL:** https://huggingface.co / https://huggingface.co/docs/api-inference

### Pricing Tiers

| Service | Pricing |
|---------|---------|
| **Serverless Inference (Free)** | Rate-limited (~few hundred requests/hr) |
| **Serverless Inference (Pro)** | $9/mo for higher rate limits |
| **Inference Providers** | Pay-as-you-go, no markup. 200+ models from multiple providers. |
| **Inference Endpoints (Dedicated)** | From $0.032/CPU-core/hr; $0.50+/GPU/hr |
| **Enterprise** | $150/user/month |

### Representative Token Pricing (Serverless)
| Model | Cost/1K tokens |
|-------|---------------|
| Llama 2 7B | ~$0.002 |
| Llama 2 70B | ~$0.01 |
| Llama 3 70B | ~$0.045–$0.055 |

### Key Details
- **200+ models** available via unified API. No infrastructure management.
- **Inference Providers** — Routes to optimal backend (AWS, GCP, etc.). Transparent pricing, no HF markup.
- **Inference Endpoints** — Dedicated GPU instances. Per-minute billing. Auto-scaling. Custom models supported.
- **Hub ecosystem** — 500K+ models, datasets, Spaces.
- **Pro account** ($9/mo): Higher rate limits, priority inference, private repos.
- **Best for**: Experimenting with many models, deploying custom/fine-tuned models, embeddings.

---

## COMPARATIVE PRICING SUMMARY (Input/Output per MTok)

| Provider/Model | Input | Output | Context | Speed |
|---------------|-------|--------|---------|-------|
| Claude Opus 4.8 | $5.00 | $25.00 | 1M | Medium |
| Claude Sonnet 4.6 | $3.00 | $15.00 | 1M | Fast |
| Claude Haiku 4.5 | $1.00 | $5.00 | 200K | Very Fast |
| GPT-4.1 | $2.00 | $8.00 | 1M | Fast |
| o3 | $2.00 | $8.00 | 200K | Slow (reasoning) |
| o4-mini | $1.10 | $4.40 | 200K | Medium |
| Gemini 2.5 Pro | $1.25 | $10.00 | 1M | Medium |
| Gemini 2.5 Flash | $0.30 | $2.50 | 1M | Fast |
| DeepSeek V4 Flash | $0.14 | $0.28 | 128K | Fast |
| DeepSeek R1 | $0.55 | $2.19 | 128K | Slow (reasoning) |
| Grok 4.3 | $1.25 | $2.50 | 1M | Medium |
| Mistral Medium 3 | $0.40 | $2.00 | 128K | Fast |
| Mistral Small 4 | $0.10 | $0.30 | 128K | Very Fast |
| Cohere Command R+ | $2.50 | $10.00 | 128K | Medium |
| Cohere Command R | $0.15 | $0.60 | 128K | Fast |
| Groq (Llama 3.3 70B) | $0.59 | $0.79 | 128K | **Fastest** |
| Together (Llama 70B) | $0.88 | $0.88 | 128K | Fast |
| Fireworks (Llama 70B) | $0.30 | $1.20 | 128K | Very Fast |
| Llama 4 Scout (self-hosted) | Free | Free | 10M | Varies |

---

## QUICK REFERENCE LINKS

| Provider | API Docs | Pricing Page |
|----------|----------|-------------|
| Anthropic | https://docs.anthropic.com | https://www.anthropic.com/pricing |
| OpenAI | https://platform.openai.com/docs | https://openai.com/api/pricing |
| Google Gemini | https://ai.google.dev | https://ai.google.dev/gemini-api/docs/pricing |
| Meta Llama | https://llama.meta.com | Free (open-weight) |
| Mistral | https://docs.mistral.ai | https://mistral.ai/pricing |
| DeepSeek | https://api-docs.deepseek.com | https://api-docs.deepseek.com/quick_start/pricing |
| xAI (Grok) | https://docs.x.ai | https://docs.x.ai/developers/pricing |
| Cohere | https://docs.cohere.com | https://cohere.com/pricing |
| Together AI | https://docs.together.ai | https://www.together.ai/pricing |
| Fireworks AI | https://docs.fireworks.ai | https://fireworks.ai/pricing |
| Groq | https://console.groq.com/docs | https://groq.com/pricing |
| Amazon Bedrock | https://docs.aws.amazon.com/bedrock | https://aws.amazon.com/bedrock/pricing |
| Hugging Face | https://huggingface.co/docs/api-inference | https://huggingface.co/pricing |

---

*Notes: Pricing can vary by region, volume tier, and promotional discounts. Items marked [?] could not be fully verified against official primary sources. Models are frequently updated — check provider pages for latest versions. Compiled June 28, 2026.*
