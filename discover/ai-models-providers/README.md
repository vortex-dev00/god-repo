# 🤖 AI Models & Providers — The Real Landscape (June 2026)

> This section reflects the ACTUAL state of AI models as of **June 2026**. Updated monthly.

---

## ⚡ How Fast We Got Here

| When | What was "state of the art" | Context Window | Cost |
|------|---------------------------|----------------|------|
| Nov 2022 | ChatGPT (GPT-3.5) | 4K tokens | Free |
| Mar 2023 | GPT-4 | 8K/32K | $0.03/$0.06 per 1K |
| Nov 2023 | GPT-4 Turbo | 128K | $0.01/$0.03 per 1K |
| Mar 2024 | Claude 3 Opus | 200K | $15/$75 per 1M |
| May 2024 | GPT-4o | 128K | $5/$15 per 1M |
| Jun 2024 | Claude 3.5 Sonnet | 200K | $3/$15 per 1M |
| Feb 2025 | Claude 3.7 Sonnet | 200K | $3/$15 per 1M |
| Jan 2025 | DeepSeek R1 (open) | 128K | Free/local |
| May 2025 | Claude Opus 4 | 200K | $5/$25 per 1M |
| Jun 2025 | Claude Sonnet 4 | 200K | $3/$15 per 1M |
| Feb 2026 | GPT-5 | 1M | Unknown |
| Apr 2026 | GPT-5.4 | 1M | Unknown |
| Apr 2026 | GPT-5.5 (API) | 1M | Unknown |
| May 2026 | **Claude Opus 4.8** | 1M | $5/$25 per 1M |
| May 2026 | Gemini 3.5 Flash | Unknown | Flash pricing |
| Jun 2026 | **GPT-5.6** (limited) | Unknown | Unknown |
| Jun 2026 | Gemini 3.1 Pro | Unknown | Unknown |

**In 2 years: 4K context → 1M context. $60/1M tokens → $5/1M tokens. "Kinda smart" → "Smarter than most humans at most tasks."**

---

## 🏆 Current Model Rankings (June 2026)

### #1: Claude Opus 4.8 (Anthropic) — Released May 28, 2026
- **The current #1 overall** — Top of Artificial Analysis Intelligence Index (61.4)
- SWE-bench Pro: **69.2%** (vs 64.3% on Opus 4.7)
- 4x fewer unflagged code flaws than Opus 4.7
- **Fast mode** — 3x cheaper than standard
- Supports hundreds of **parallel subagents**
- Pricing: **$5 input / $25 output per 1M tokens**
- Context: **1M tokens**
- Available: claude.ai, API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry
- API model ID: `claude-opus-4-8`
- https://www.anthropic.com/claude/opus

### #2: GPT-5.5 (OpenAI) — Released April 2026
- Intelligence Index: **60.2** (just behind Opus 4.8)
- "Smartest and most intuitive model" — excels at multi-step agentic tasks
- Writing code, researching online, analyzing data, creating docs/spreadsheets
- Matches GPT-5.4 per-token latency at higher intelligence
- 52.5% fewer hallucinated claims than GPT-5.3
- Available in ChatGPT and API
- https://openai.com/index/introducing-gpt-5-5/

### GPT-5.6 (OpenAI) — Released June 26, 2026 (LIMITED)
- Next-gen, just announced
- Limited release to ChatGPT and Codex
- Details still emerging
- https://9to5mac.com/2026/06/26/openai-upgrading-chatgpt-and-codex-with-new-gpt-5-6-models-in-limited-release/

### GPT-5 / GPT-5.4 (OpenAI) — Earlier 2026
- GPT-5: "Significant leap in intelligence" — coding, math, writing, health, visual
- GPT-5.4: Combined reasoning + coding + agentic workflows into single model
- https://openai.com/index/introducing-gpt-5/

### Gemini 3.5 Flash (Google) — May 2026
- "Near-Pro intelligence at Flash-tier cost and speed"
- Pro-level coding, parallel agentic execution
- Leading across benchmarks for agentic workflows
- https://deepmind.google/models/gemini/

### Gemini 3.1 Pro (Google) — 2026
- Comprehends vast datasets, massively multimodal (text, audio, images, video, code repos)
- Advanced reasoning
- https://deepmind.google/models/model-cards/gemini-3-1-pro/

### Gemini Omni (Google) — May 2026
- "Any output from any input" — starting with video
- Multimodality + editing + world understanding
- https://deepmind.google/models/model-cards/gemini-omni-flash/

---

## 📊 Current Full Model Roster by Provider

### Anthropic (Claude)
| Model | Released | Best For | Pricing (per 1M tok) | Context |
|-------|----------|----------|---------------------|---------|
| **Claude Opus 4.8** | May 2026 | #1 overall, coding agents, complex tasks | $5 / $25 | 1M |
| Claude Opus 4.7 | Earlier 2026 | Complex reasoning | $5 / $25 | 1M |
| Claude Opus 4.6 | Earlier 2026 | Reliability & precision | $5 / $25 | 1M |
| Claude Sonnet 4.x | 2025-2026 | Best value for coding | $3 / $15 | 200K |
| Claude Haiku 4.x | 2025-2026 | Fast & cheap | $0.25 / $1.25 | 200K |

### OpenAI
| Model | Released | Best For | Notes |
|-------|----------|----------|-------|
| **GPT-5.6** | Jun 26, 2026 | Latest, limited release | Just announced |
| **GPT-5.5** | Apr 2026 | Multi-step agentic tasks | #2 overall |
| GPT-5.4 | 2026 | Reasoning + coding unified | |
| GPT-5 | Feb 2026 | Major leap in intelligence | |
| o3 | 2025 | Deep reasoning | Being retired Aug 2026 |
| GPT-4o | 2024 | DEPRECATED | Legacy |

**Note:** GPT-4.5 was retired from ChatGPT on June 27, 2026. o3 retiring August 2026.

### Google (Gemini)
| Model | Released | Best For |
|-------|----------|----------|
| **Gemini 3.5 Flash** | May 2026 | Frontier agents at Flash cost |
| **Gemini 3.1 Pro** | 2026 | Complex multimodal tasks |
| Gemini 3.1 Flash-Lite | 2026 | High-volume efficiency |
| Gemini Omni | May 2026 | Any-to-any (esp. video) |
| Gemini 2.5 Flash/Pro | 2025 | Still recommended for new projects |

### Meta (Llama)
| Model | Best For | Where to get it |
|-------|----------|----------------|
| Llama 3.3 70B | Best open-source all-rounder | Ollama, HuggingFace |
| Llama 3.1 405B | Largest open model | Cloud APIs, multi-GPU |
| Llama 3.2 (1B/3B) | Mobile/edge | Ollama |
| Llama 4 [?] | TBD | Announced 2026 [?] |

### DeepSeek
| Model | Best For | Pricing |
|-------|----------|---------|
| DeepSeek R1 | Chain-of-thought reasoning (open) | $0.55/$2.19 per 1M or FREE locally |
| DeepSeek V3 | Cheap general use | $0.27/$1.10 per 1M |
| DeepSeek Coder V3 | Code generation | Similar to V3 |

### Other Providers
- **Mistral** — Mistral Large, Mixtral, Codestral — https://mistral.ai/
- **xAI** — Grok models — https://x.ai/
- **Cohere** — Command R+ (enterprise RAG) — https://cohere.com/
- **Qwen (Alibaba)** — Qwen 2.5/3 (competitive open-source) — https://huggingface.co/Qwen

### Inference Providers (use any model)
- **OpenRouter** — Access ALL models via one API — https://openrouter.ai/
- **Together AI** — Fast open-source model inference — https://together.ai/
- **Fireworks AI** — Low-latency inference — https://fireworks.ai/
- **Groq** — Fastest inference (hardware optimized) — https://groq.com/
- **Amazon Bedrock** — AWS-managed access to Claude, Llama, etc. — https://aws.amazon.com/bedrock/

---

## 🎯 Which Model Should YOU Use? (June 2026)

| Use Case | Best Pick | Why |
|----------|-----------|-----|
| Coding (complex) | Claude Opus 4.8 | #1 on SWE-bench, best for agents |
| Coding (daily) | Claude Sonnet 4.x | Best value, fast |
| Coding (in Cursor/IDE) | GPT-5.5 or Claude Sonnet | Both excellent |
| General chat | GPT-5.5 or Claude Opus 4.8 | Tie at the top |
| Math/Reasoning | GPT-5.5 or DeepSeek R1 | Both strong reasoners |
| Fast & cheap | Gemini 3.5 Flash | Pro-level at Flash cost |
| Local/free | DeepSeek R1, Llama 3.3 70B | Run on your hardware |
| Local (small/fast) | Llama 3.2 3B, Qwen 2.5 3B | Runs on phones |
| Enterprise | Claude Opus 4.8 via Bedrock | Best reliability |
| Multimodal (video) | Gemini Omni | Any input → any output |
| Budget | DeepSeek V3 | $0.27 per 1M input tokens |

---

*Last verified: June 27, 2026*
