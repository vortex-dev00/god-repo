# 🖥️ AI Hardware Guide

> Which hardware to buy or rent for running AI.

---

## GPU Comparison for AI

| GPU | VRAM | Speed (tok/s)* | Best For | Price |
|-----|------|---------------|----------|-------|
| **RTX 3090** | 24 GB | ~35 tok/s | 7B–30B models | ~$800 used |
| **RTX 4090** | 24 GB | ~55 tok/s | Fastest consumer inference | ~$1,600 |
| **RTX 5090** | 32 GB | ~70 tok/s [?] | Next-gen consumer | ~$2,000 |
| **A100** | 40/80 GB | — | Professional training | Cloud only |
| **H100** | 80 GB | — | State-of-the-art training | Cloud only |
| **H200** | 141 GB | — | Latest datacenter GPU | Cloud only |
| **Apple M4 Pro** | 24 GB unified | ~20 tok/s | Entry Mac AI | $2,000+ |
| **Apple M4 Max** | 64–128 GB unified | ~30 tok/s | Large models on Mac | $3,500–$7,000 |
| **Apple M4 Ultra** | 192 GB unified | ~25 tok/s | Largest models on Mac | $7,000+ |

*Approximate tokens/second for 70B Q4 model with Ollama/llama.cpp

## What Can You Run?

| Model Size | Min VRAM Required | Example Models | GPU Options |
|-----------|-------------------|----------------|-------------|
| 1–3B | 2–4 GB | Phi-4-mini, Llama 3.2 1B | Any modern GPU |
| 7–8B | 6–8 GB | Llama 3.1 8B, Mistral 7B | RTX 3060, M2 |
| 13B | 10–12 GB | Llama 2 13B, CodeLlama 13B | RTX 3080, M3 |
| 30–34B | 20–24 GB | DeepSeek Coder 33B | RTX 4090, M4 Pro |
| 70B | 40–48 GB | Llama 3.3 70B, Qwen 72B | 2x RTX 4090, M4 Max |
| 70B (Q4) | 32–40 GB | Quantized 70B models | M4 Max 64GB+ |
| 405B | 200+ GB | Llama 3.1 405B | Multi-GPU or M4 Ultra |

## Mac vs PC for AI

| | Mac (Apple Silicon) | PC (NVIDIA) |
|---|---|---|
| **Advantage** | Huge unified memory (up to 192GB), silent | Much faster per-GB, CUDA ecosystem |
| **Best for** | Running big models that don't fit in 24GB | Fast inference, training, ComfyUI |
| **Software** | Ollama, LM Studio, llama.cpp | Everything + CUDA-only tools |
| **Budget pick** | M4 Pro 24GB ($2,000) | RTX 4060 Ti 16GB ($450) |
| **Power pick** | M4 Ultra 192GB ($7,000+) | RTX 4090 24GB ($1,600) |

## Cloud GPU Providers

| Provider | Cheapest GPU | $/hr | Best For | Link |
|----------|-------------|------|----------|------|
| **RunPod** | RTX 4090 | ~$0.44/hr | Cheap inference | https://runpod.io/ |
| **Vast.ai** | RTX 3090 | ~$0.20/hr | Budget training | https://vast.ai/ |
| **Lambda Cloud** | H100 | ~$2.49/hr | Serious training | https://lambdalabs.com/ |
| **CoreWeave** | H100 | ~$2.06/hr | Enterprise | https://coreweave.com/ |
| **Paperspace** | RTX 4000 | ~$0.45/hr | Notebooks/dev | https://paperspace.com/ |
| **Together AI** | Serverless | Per token | API inference | https://together.ai/ |
| **Modal** | Serverless | Per second | GPU functions | https://modal.com/ |
| **Replicate** | Serverless | Per second | Run any model | https://replicate.com/ |
| **Google Colab** | T4 (free) | Free/Pro | Learning/prototyping | https://colab.google/ |
| **Kaggle** | T4/P100 | Free | Notebooks | https://kaggle.com/ |

## Free GPU Options for Learning
- **Google Colab** — Free T4 GPU, 12hr sessions — https://colab.research.google.com/
- **Kaggle Notebooks** — 30hr/week free GPU — https://www.kaggle.com/
- **Lightning AI Studios** — Free GPU credits — https://lightning.ai/
- **Gradient (Paperspace)** — Free community GPUs — https://www.paperspace.com/gradient
