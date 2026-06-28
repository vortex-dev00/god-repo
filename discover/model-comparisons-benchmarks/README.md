# 📊 Model Comparisons & Benchmarks

> Detailed performance comparisons and benchmarks for LLMs and vision models.

---

## 📊 MODEL COMPARISONS & BENCHMARKS

### Frontier Models Comparison (June 2026)

| Model | Owner | Context Window | Key Strength | Commercial Price / 1M tokens |
|-------|-------|----------------|--------------|------------------------------|
| **GPT-5.2** | OpenAI | 1M tokens | General intelligence, agentic workflows, voice | $5.00 input / $15.00 output |
| **Claude 4.7 Opus** | Anthropic | 2M tokens | Advanced coding, reasoning, XML parsing | $15.00 input / $75.00 output |
| **Claude 4.7 Sonnet** | Anthropic | 200K tokens | Developer sweet spot, fastest coding agent | $3.00 input / $15.00 output |
| **Gemini 2.5 Pro** | Google | 2M tokens | Video understanding, native multimodality | $1.25 input / $5.00 output |
| **Grok 3** | xAI | 128K tokens | Real-time info from X, search, coding | Grok API |
| **Llama 4 (405B)** | Meta | 128K tokens | Open weights standard, fine-tuning | Self-hosted or hosting provider |
| **DeepSeek-V3** | DeepSeek | 128K tokens | Performance-to-price ratio leader | $0.14 input / $0.28 output |

**Notes:** Prices are for commercial API access as of June 2026. GPT-5.2 and Claude 4.7 Sonnet dominate developer mindshare for agentic applications. DeepSeek-V3 remains the cost leader by a factor of 10–20×.

---

### Key Benchmarks & What They Mean

| Benchmark | Focus Area | High Score Meaning | Current SOTA |
|-----------|------------|--------------------|--------------|
| **MMLU / MMLU-Pro** | Multi-task language understanding | Broad academic knowledge across subjects | ~91.2% |
| **MATH** | Complex mathematics | Ability to do multi-step logical math reasoning | ~95.0% |
| **HumanEval** | Code generation (Python) | Ability to write correct code from prompt | ~96.5% |
| **SWE-bench (Verified)**| Real-world software engineering | Ability to resolve GitHub issues in real codebases | ~52.3% |
| **GPQA** | Graduate-level Q&A | Hard reasoning in biology, chemistry, physics | ~82.0% |
| **HELM** | Holistic evaluation | Safe, robust, accurate across 30+ scenarios | Comprehensive index |

---

### LLM Leaderboards (Where to Check)

| Leaderboard | Target Audience | Key Metric | URL |
|-------------|-----------------|------------|-----|
| **LMSYS Chatbot Arena** | Everyone (blind testing) | ELO rating based on human preferences | https://chat.lmsys.org |
| **Hugging Face Open LLM** | Open-source community | Combined score across 6 core benchmarks | https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard |
| **SWE-bench Leaderboard** | Software engineers | Resolution rate of real-world GitHub issues | https://www.swebench.com |
| **Vectara Hallucination Leaderboard** | Production developers | Hallucination rate (%) and factual consistency | https://github.com/vectara/hallucination-leaderboard |
| **Artificial Analysis** | Enterprise developers | Speed (tok/s), latency (TTFT), cost, quality | https://artificialanalysis.ai |

**Key Resources:**

- **LMSYS Chatbot Arena** — Blind human preference comparison — https://chat.lmsys.org
- **Hugging Face Open LLM Leaderboard** — Open-source LLM benchmarking — https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- **SWE-bench Leaderboard** — Software agent evaluations — https://www.swebench.com
- **Vectara Hallucination Leaderboard** — Factuality and consistency tracking — https://github.com/vectara/hallucination-leaderboard
- **Artificial Analysis** — Speed, cost, latency, quality comparisons — https://artificialanalysis.ai
- **DeepSeek-V3 Evaluation Report** — Benchmarks of DeepSeek vs GPT-4o/Claude 3.5 — https://github.com/deepseek-ai/DeepSeek-V3

---

## LMSYS Chatbot Arena
LMSYS Chatbot Arena is a crowdsourced open platform for LLM evaluation. It conducts human preference benchmarks using blind, randomized battles. It calculates Elo ratings to show which models humans prefer.

## Open LLM Leaderboard
Maintained by Hugging Face, the Open LLM Leaderboard tracks, ranks, and evaluates open LLMs and chatbots. It uses benchmarks like MMLU, ARC, and GSM8K to measure performance.

## MMLU Benchmark
MMLU (Measuring Massive Multitask Language Understanding) is a benchmark designed to measure knowledge acquired during pretraining. It covers 57 subjects across STEM, humanities, and social sciences.
