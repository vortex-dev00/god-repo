# 🖥️ AI Hardware Guide

> Which hardware to buy or rent for running AI.

---

## 🖥️ AI HARDWARE & DEVICES

### NVIDIA GPUs for AI — Complete Buying Guide

| GPU | VRAM | Best For | Price Range |
|-----|------|----------|-------------|
| RTX 3090 (used) | 24GB GDDR6X | Budget local AI, 70B models at Q4 | ~$699 used |
| RTX 4070 Ti Super | 16GB GDDR6X | 13B–34B models, best new-card value | ~$799 |
| RTX 4090 | 24GB GDDR6X | Fastest consumer AI card (52 tok/s on 70B) | ~$1,599 |
| RTX 5090 | 32GB GDDR7 | Flagship Blackwell consumer; fits 70B at Q5; 1,792 GB/s bandwidth | $1,999 MSRP |
| RTX 5080 | 16GB GDDR7 | Mid-range Blackwell; local LLM sweet spot | ~$999 |
| RTX A6000 / RTX 6000 Ada | 48GB GDDR6 | Professional workstation AI/ML | $4,500–$6,800 |
| NVIDIA L40S | 48GB GDDR6 | Enterprise inference (5× A100 FP32) | Cloud only |
| NVIDIA A100 | 40/80GB HBM2e | Legacy data center training/inference | $10,000–$15,000 |
| NVIDIA H100 | 80GB HBM3 | Enterprise AI training gold standard | $27,000–$40,000 |
| NVIDIA H200 | 141GB HBM3e | Extended-memory Hopper for large models | $30,000–$45,000 |
| NVIDIA B200 | 192GB HBM3e | Blackwell data center; 4× H100 inference speed; 8 TB/s | $30,000–$50,000 |
| NVIDIA GB200 NVL72 | 13.4TB unified (72 GPUs) | Rack-scale AI; 1.44 exaflops FP4 | ~$3M per rack |

**Key Resources:**

- **Tom's Hardware GPU Reviews** — In-depth hardware benchmarks and reviews — https://www.tomshardware.com/tag/rtx-5090
- **LocalAIMaster GPU Guide** — Real-world local LLM benchmarks with tok/s comparisons — https://localaimaster.com/blog/best-gpus-for-ai-2025
- **Spheron RTX 5090 vs H100 vs B200** — Which GPU for which workload breakdown — https://www.spheron.network/blog/rtx-5090-vs-h100-vs-b200/
- **AceCloud GPU Guide** — Complete deep learning GPU comparison 2026 — https://acecloud.ai/blog/how-to-find-the-best-gpu-for-deep-learning/
- **Atlantic.net Top 12 NVIDIA GPUs** — Covers entire Blackwell/Hopper/Ampere lineup — https://www.atlantic.net/gpu-server-hosting/top-10-nvidia-gpus-for-ai/
- **Slyd Training GPU Guide** — TCO analysis and deployment recommendations — https://slyd.com/guides/training-gpu-guide
- **Slyd Inference GPU Guide** — Real-world inference benchmarks — https://slyd.com/guides/inference-gpu-guide
- **NVIDIA GeForce RTX 5090 Official** — Official specs and features — https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/

---

### Apple Silicon for AI

| Chip | NPU (TOPS) | Max Unified Memory | Memory Bandwidth | Best For |
|------|------------|---------------------|------------------|----------|
| M4 | 38 TOPS | 32GB | 120 GB/s | Light local LLM (7B–13B), on-device ML |
| M4 Pro | 38 TOPS | 64GB | 273 GB/s | Serious local AI work, 34B models |
| M4 Max | 38 TOPS | 128GB | 546 GB/s | Running 70B+ models locally; inference beast |
| M3 Ultra | 32 TOPS | 192GB | 800 GB/s | Maximum Apple local AI (Mac Studio/Pro) |
| M5 (Oct 2025) | 4× M4 GPU AI perf | — | — | Next-gen; Neural Accelerator in every GPU core |

**Key Points:**
- Apple Silicon excels at **energy efficiency** and **unified memory** — no VRAM bottleneck
- M4 Max with 128GB can run 70B+ parameter models entirely in memory via llama.cpp/Ollama
- MLX (Apple's ML framework) optimized for Apple Silicon; growing ecosystem
- M5 announced October 2025 with 4× GPU AI performance vs M4
- Developer bypassed Apple restrictions to unlock 15.8 TFLOPS from M4 Neural Engine

**Key Resources:**

- **Apple M4 for Local AI Guide (2026)** — Mac Studio + MacBook guide for LLM inference — https://localaimaster.com/blog/apple-m4-for-ai-guide
- **Apple M4 Chip AI Deep Dive** — Architecture and capabilities analysis — https://www.penbrief.com/apple-m4-chip-ai-capabilities-deep-dive/
- **Apple Silicon vs NVIDIA CUDA for AI** — Head-to-head comparison — https://scalastic.io/en/apple-silicon-vs-nvidia-cuda-ai-2025/
- **Apple M4 Pro/Max Newsroom** — Official specs and ML capabilities — https://www.apple.com/uk/newsroom/2024/10/apple-introduces-m4-pro-and-m4-max/
- **M5 Announcement** — Next-gen Apple Silicon for AI — https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/
- **MLX Framework (Apple)** — Apple's native ML framework for Apple Silicon — https://github.com/ml-explore/mlx

---

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

---

## Mac vs PC for AI

| | Mac (Apple Silicon) | PC (NVIDIA) |
|---|---|---|
| **Advantage** | Huge unified memory (up to 192GB), silent | Much faster per-GB, CUDA ecosystem |
| **Best for** | Running big models that don't fit in 24GB | Fast inference, training, ComfyUI |
| **Software** | Ollama, LM Studio, llama.cpp | Everything + CUDA-only tools |
| **Budget pick** | M4 Pro 24GB ($2,000) | RTX 4060 Ti 16GB ($450) |
| **Power pick** | M4 Ultra 192GB ($7,000+) | RTX 4090 24GB ($1,600) |

---

### NPU Laptops (Copilot+ PCs)

**What is a Copilot+ PC?**
Windows 11 laptop with a dedicated NPU rated at 40+ TOPS, minimum 16GB RAM, 256GB storage. Enables on-device AI features (Live Captions, Cocreator, Recall, Windows Studio Effects) without cloud dependency.

| Platform | NPU TOPS | Key Models | Notes |
|----------|----------|------------|-------|
| Snapdragon X Elite (Gen 1) | 45 TOPS | Surface Laptop 7, HP OmniBook X, Lenovo Yoga Slim 7x | ARM-based; exceptional battery (20+ hrs) |
| Snapdragon X2 Elite (Gen 2, 2026) | 80 TOPS | ASUS, Lenovo IdeaPad, HP OmniBook 2026 | 31% faster, 43% less power; ARM |
| Snapdragon X2 Elite Extreme | 80+ TOPS | Premium pro-level laptops | Pro workloads and AI-driven experiences |
| Intel Core Ultra Series 2 (Lunar Lake) | 48 TOPS | Various ultrabooks | x86; better app compatibility |
| Intel Core Ultra Series 3 (Panther Lake) | 50+ TOPS | ASUS 2026 laptops | Latest Intel AI platform |
| AMD Ryzen AI 300 (Strix Point) | 50 TOPS | ASUS, Lenovo, HP | x86; strong integrated GPU |
| AMD Ryzen AI 9 HX 370 | 50 TOPS | Premium AMD laptops | Top AMD offering |

**Price Range:** $499 (budget) to $1,099+ (premium creator)

**Key Resources:**

- **PCMag Best Copilot+ Laptops 2026** — Comprehensive reviews and buying guide — https://uk.pcmag.com/laptops/159100/the-best-copilot-laptops-of-2025/
- **HP AI Laptop Processor Comparison** — Snapdragon vs Ryzen AI vs Intel Core Ultra — https://www.hp.com/us-en/shop/tech-takes/ai-laptop-processor-comparison-snapdragon-ryzen-intel
- **HP OmniBook X Guide** — Copilot+ PC comparison guide — https://www.hp.com/us-en/shop/tech-takes/hp-omnibook-x-ai-laptop-comparison-guide
- **TechSpot Snapdragon X2 Launch** — X2 Elite specs and benchmarks — https://www.techspot.com/news/111995-snapdragon-x2-laptops-reach-retail-aggressive-memory-display.html
- **The Gadgeteer Snapdragon X2 2026** — Why Wave Two wins — https://the-gadgeteer.com/2026/05/13/snapdragon-x2-elite-laptops-2026/
- **ASUS AI PC Guide 2026** — Choosing between Snapdragon X2 and Intel Panther Lake — https://www.asus.com/us/blog/a-look-at-2026-asus-laptops-with-the-snapdragon-glymur-or-intel-panther-lake-platforms/
- **Skywork Copilot+ PC Guide** — Ultimate guide to the platform — https://skywork.ai/blog/ultimate-guide-copilot-ai-laptop/
- **Microsoft Copilot+ PC Requirements** — Official developer guide — https://learn.microsoft.com/en-us/windows/ai/

---

### GPU Cloud Rentals

| Provider | H100 Price/hr | B200 Price/hr | Best For | URL |
|----------|---------------|---------------|----------|-----|
| **RunPod** | ~$2.49 | $4.99 | Best cost+speed balance; community cloud | https://www.runpod.io |
| **Vast.ai** | ~$1.27 (A100) | Varies | Cheapest marketplace; variable reliability | https://vast.ai |
| **Lambda Labs** | $2.99–$4.29 | $4.99 | Zero egress fees; consistent multi-region | https://lambdalabs.com |
| **CoreWeave** | $2.65 (reserved/yr) | — | Best reserved pricing; enterprise-grade | https://www.coreweave.com |
| **Paperspace (DigitalOcean)** | $5.95 (dedicated) | — | Best Jupyter integration; pleasant UX | https://www.paperspace.com |
| **Nebius** | $2.95 | — | Strong EU compliance; stable pricing | https://nebius.ai |
| **TensorDock** | ~$1.80 | — | Budget-friendly with decent support | https://tensordock.com |
| **Hyperstack** | Varies | — | Enterprise security focus | https://hyperstack.cloud |
| **GPU Mart** | Varies | Varies | Good SLA and cold start times | https://gpu-mart.com |
| **AWS (p5 instances)** | $3–$4+ | — | Broadest ecosystem; highest price | https://aws.amazon.com/ec2/instance-types/p5/ |
| **Google Cloud (A3)** | $3–$4+ | — | TPU alternative available | https://cloud.google.com/gpu |
| **Azure (ND H100)** | $3–$4+ | — | Microsoft ecosystem integration | https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/ |

**Key Market Facts (2026):**
- H100 spot prices collapsed ~64% from 2024 peak
- Neoclouds are 30–85% cheaper than hyperscalers (AWS/Azure/GCP)
- B200 availability growing at CoreWeave, RunPod, Lambda
- Hyperscalers charge 3–6× more per GPU-hour than specialized providers

**Key Resources:**

- **RunPod GPU Cloud Comparison** — H100/H200 pricing and developer experience — https://www.runpod.io/articles/alternatives/best-gpu-cloud-providers-for-ai-and-ml
- **Introl Cloud Comparison** — Lambda vs Paperspace vs Vast.ai detailed breakdown — https://introl.com/blog/lambda-paperspace-vast-gpu-cloud-comparison-2025
- **Saturn Cloud GPU Report** — Neocloud infrastructure comparison — https://saturncloud.io/reports/gpu-cloud-comparison-report/
- **Intuition Labs H100 Pricing** — 15+ providers compared ($1.49–$6.98/hr) — https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison
- **GPU-Mart Provider Comparison** — 7 providers benchmarked across 6 dimensions — https://www.gpu-mart.com/blog/compare-gpu-providers
- **AI Tool Discovery Cloud GPU Guide** — Provider overview and analysis — https://www.aitooldiscovery.com/ai-infra/cloud-gpu-providers-compared

---

## Free GPU Options for Learning
- **Google Colab** — Free T4 GPU, 12hr sessions — https://colab.research.google.com/
- **Kaggle Notebooks** — 30hr/week free GPU — https://www.kaggle.com/
- **Lightning AI Studios** — Free GPU credits — https://lightning.ai/
- **Gradient (Paperspace)** — Free community GPUs — https://www.paperspace.com/gradient

---

### AI Dedicated Devices

| Device | Price | Status (2026) | What It Does |
|--------|-------|---------------|--------------|
| Rabbit R1 | $199 | ⚠️ Struggling (mass returns, near-insolvent) | Pocket AI companion; walkie-talkie to an AI agent |
| Humane AI Pin | $699 + $24/mo | ❌ Dead (shut down Feb 2025, patents sold to HP for $116M) | Wearable AI with laser projector display |
| Friend Pendant | $129 | ⚠️ Mixed reviews; pivoting to software | Always-listening AI companion necklace |
| Limitless Pendant | $99 | ❌ Acquired by Meta (Dec 2025); no longer sold | Meeting transcription and personal AI memory |
| Meta Ray-Ban Smart Glasses | $379 | ✅ Active & thriving | AI-powered glasses with camera, Meta AI built in |
| Even Realities G2 | $599 | ✅ Active | Minimalist AR display glasses with AI assistant |
| Bee AI | ~$50 | ✅ Active | Wearable AI for daily recording and memory |
| Plaud Note Pin | $169 | ✅ Active | AI meeting recorder and transcriber wearable |
| Omi (formerly Based Hardware) | $89 | ✅ Active | Open-source AI wearable pendant |

**Key Takeaways for 2026:**
- The standalone AI device category has largely **failed** — phones + glasses won
- **Meta Ray-Ban glasses** emerged as the winning AI wearable form factor
- Pendants/pins are being absorbed into glasses and earbuds
- AI wearable value lies in **transcription/memory** (Plaud, Omi) not general assistant tasks

**Key Resources:**

- **Forbes Best AI Wearables 2025** — Tested Bee, Plaud Pin, Omi, Limitless for a month — https://www.forbes.com/sites/forbes-personal-shopper/article/best-ai-wearables/
- **The Gadgeteer Best AI Wearables 2026** — Current market landscape — https://the-gadgeteer.com/2026/05/05/best-ai-wearables-2026/
- **Dymesty Wearable AI Devices Guide** — 7 devices that actually work — https://dymesty.com/blogs/articles/humane-ai-pin-alternatives-wearable-ai-devices
- **Recolx AI Hardware Guide** — Post-hype efficiency analysis — https://recolx.ai/blogs/blog/the-ultimate-guide-to-ai-hardware-after-the-hype-efficiency-is-king
- **Friend Official** — AI companion necklace — https://www.friend.com
- **Meta Ray-Ban AI Glasses** — Official product page — https://www.meta.com/au/ai-glasses/meta-ray-ban-display/
