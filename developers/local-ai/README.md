# 🖥️ Local AI (Run Models on Your Machine)

> Everything you need to run AI models locally — LLMs, image gen, voice, video.

---

# CATEGORY 8: LOCAL AI — Exhaustive Research (2025–2026)

---

## 1. LLM RUNNERS & INTERFACES

### Ollama
**One-line:** CLI-first tool to download, run, and serve open-source LLMs locally with one command; ships a built-in model library with hundreds of models.
**URL:** https://ollama.com | **Repo:** https://github.com/ollama/ollama
**⭐ GitHub Stars:** ~168k
**Model Library:** https://ollama.com/library — Ships hundreds of variants across Llama 3.x, Mistral, Gemma 3/4, DeepSeek, Qwen 3, Qwen3-Coder, Phi-4, LLaVA, gpt-oss, MiniMax, GLM-5, Kimi-K2, embedding models, and vision models.

**Best Models per Use Case (2025–2026):**
| Use Case | Model | Notes |
|----------|-------|-------|
| Overall quality | Llama 3.3 70B | 86.0 MMLU, needs 40GB VRAM |
| Coding (flagship) | Qwen3-Coder-Next | ~70% SWE-Bench, runs on 16GB laptop (3B active from 80B MoE) |
| Coding (mid-range) | Qwen 2.5 Coder 32B | 92.7% HumanEval, 20GB VRAM |
| All-rounder (mid-range) | Qwen 2.5 32B | 83.2 MMLU, 20GB VRAM |
| AI Agents / Tool-calling | Qwen3 8B | Apache 2.0, native tool-calling, fits ~8GB Q4_K_M |
| Reasoning (small) | DeepSeek-R1 (distill) | Chain-of-thought local reasoning |
| General (8GB RAM) | Llama 3.1 8B / Phi-4 14B | Best quality/RAM ratio |
| Fastest small | Mistral 7B | Lowest latency at 7B |
| Multilingual | Qwen 2.5 7B | Strong CJK + code |
| Vision/Multimodal | Gemma 4 / LLaVA | Image understanding |
| Embeddings | nomic-embed-text / mxbai-embed-large | For RAG pipelines |

---

### LM Studio
**One-line:** Free desktop app (Mac/Win/Linux) from Element Labs for downloading and running local LLMs with a chat UI, HuggingFace model browser, OpenAI-compatible API on localhost:1234, RAG, and CLI (`lms`).
**URL:** https://lmstudio.ai | **Docs:** https://www.lmstudio.ai/docs
**⭐ GitHub Stars:** Closed-source (no public repo)
**Key Features:**
- Built on llama.cpp (CPU/GPU) and Apple MLX (Apple Silicon)
- Integrated HuggingFace model catalog browser
- OpenAI-compatible local API server (localhost:1234)
- Document chat (RAG) built-in
- `lms` CLI + `llmster` headless daemon for automation
- Python & TypeScript SDKs
- GGUF quantized model support
- Runs fully offline, no cloud dependency

---

### Jan
**One-line:** Open-source ChatGPT alternative that runs 100% offline; supports multiple engines (llama.cpp, TensorRT-LLM), multimodal image input, and MCP integration.
**URL:** https://jan.ai | **Repo:** https://github.com/janhq/jan
**⭐ GitHub Stars:** ~43.1k (Global Rank #591)
**License:** Apache-2.0
**Key Features:**
- Desktop app (Mac/Win/Linux)
- Multiple inference backends (llama.cpp, TensorRT-LLM)
- Image/multimodal support (added 2025)
- Stable MCP (Model Context Protocol) integration
- Intelligent model capability detection
- Enhanced tool calling
- Extension system

---

### Open WebUI
**One-line:** Extensible, feature-rich, self-hosted AI platform (web UI) designed for offline use; supports Ollama, OpenAI API, and many backends with RAG, RBAC, pipelines, and plugins.
**URL:** https://openwebui.com | **Repo:** https://github.com/open-webui/open-webui
**⭐ GitHub Stars:** ~115k
**Setup:**
```bash
# Quickest start (Docker, with bundled Ollama):
docker run -d -p 3000:8080 --gpus all -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:ollama

# Or standalone (connect to existing Ollama):
docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=http://host.docker.internal:11434 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main
```
**Key Features:**
- Multi-model chat, RAG (document upload), pipelines, plugins
- MCP servers support
- RBAC (role-based access control) for teams
- OpenAI-compatible API passthrough
- Fastest-starred repo in the local AI space

---

### GPT4All
**One-line:** Run local LLMs on any device (desktop app by Nomic AI); open-source, commercially-usable, with built-in local document Q&A.
**URL:** https://gpt4all.io | **Repo:** https://github.com/nomic-ai/gpt4all
**⭐ GitHub Stars:** ~77.4k (Global Rank #192)
**License:** MIT
**Key Features:**
- Cross-platform desktop app (Windows/Mac/Linux)
- Local document Q&A (private RAG)
- Runs on CPU (no GPU required) or GPU-accelerated
- Plugin architecture
- Python bindings

---

### Pinokio
**One-line:** One-click AI app installer ("AI Browser") — install and run ComfyUI, Stable Diffusion, LLMs, and hundreds of AI tools with zero configuration.
**URL:** https://pinokio.computer | **Repo:** https://github.com/pinokiocomputer/pinokio
**⭐ GitHub Stars:** ~7.5k
**Key Features:**
- One-click install scripts for 100+ AI applications
- Manages Python environments, CUDA dependencies automatically
- Cross-platform (Windows/Mac/Linux)
- Community-contributed install scripts
- Handles ComfyUI, AUTOMATIC1111, Fooocus, LangFlow, FaceFusion, etc.

---

## 2. PRODUCTION INFERENCE ENGINES

### vLLM
**One-line:** High-throughput, memory-efficient LLM inference and serving engine with PagedAttention; the de facto open-source production serving solution.
**URL:** https://vllm.ai | **Repo:** https://github.com/vllm-project/vllm
**⭐ GitHub Stars:** ~83k (Global Rank — top-tier)
**License:** Apache-2.0
**Key Features:**
- PagedAttention for efficient KV-cache memory management
- Continuous batching for maximum throughput
- Tensor parallelism, pipeline parallelism
- OpenAI-compatible API server
- Supports 100+ model architectures
- Powers Amazon Rufus, LinkedIn AI features in production
- Speculative decoding, prefix caching, chunked prefill

---

### llama.cpp
**One-line:** LLM inference in pure C/C++ — the foundational engine enabling CPU/GPU inference of quantized GGUF models on consumer hardware.
**URL:** https://github.com/ggml-org/llama.cpp (org) | **Repo:** https://github.com/ggerganov/llama.cpp
**⭐ GitHub Stars:** ~71.7k
**License:** MIT
**Key Features:**
- GGUF quantization format (Q2–Q8, K-quants)
- Runs on CPU, CUDA, Metal (Apple Silicon), Vulkan, ROCm, SYCL
- Powers Ollama, LM Studio, Jan, GPT4All under the hood
- llama-server: built-in OpenAI-compatible HTTP API
- Active development by Georgi Gerganov / ggml-org
- Supports virtually all popular open models

---

### Text Generation Inference (TGI)
**One-line:** Hugging Face's high-performance LLM serving toolkit with tensor parallelism and dynamic batching. ⚠️ **ARCHIVED** as of March 2026; in maintenance mode since Dec 2025.
**URL:** https://huggingface.co/docs/text-generation-inference | **Repo:** https://github.com/huggingface/text-generation-inference
**⭐ GitHub Stars:** ~10.9k
**License:** Apache-2.0
**Status:** Archived March 21, 2026. Only maintenance fixes accepted since Dec 2025. Users encouraged to migrate to vLLM or SGLang.
**Key Features (historical):**
- Tensor parallelism, continuous batching, quantization (GPTQ, AWQ, EETQ)
- Flash Attention, Paged Attention
- Supported Llama, Falcon, StarCoder, BLOOM, GPT-NeoX, T5

---

## 3. SELF-HOSTED CODING ASSISTANT

### Tabby
**One-line:** Self-hosted AI coding assistant — an open-source, on-premises alternative to GitHub Copilot with code completion and chat.
**URL:** https://tabby.tabbyml.com | **Repo:** https://github.com/TabbyML/tabby
**⭐ GitHub Stars:** ~33.5k
**License:** Apache-2.0
**Key Features:**
- Self-contained (no DBMS or cloud service needed)
- OpenAPI interface for easy integration
- Supports consumer-grade GPUs (RTX 3060+)
- IDE extensions: VS Code, JetBrains, Vim/Neovim
- Repository-level code context (RAG over your codebase)
- Supports running StarCoder, CodeLlama, DeepSeek-Coder, and other code models
- Answer engine for code questions

---

## 4. LOCAL IMAGE GENERATION

### AUTOMATIC1111 (Stable Diffusion WebUI)
**One-line:** The most popular Gradio-based web UI for Stable Diffusion; supports txt2img, img2img, inpainting, extensions, and LoRA/ControlNet.
**URL:** https://github.com/AUTOMATIC1111/stable-diffusion-webui
**⭐ GitHub Stars:** ~145k [?] (Wikipedia reports 136k as of July 2024; likely ~140-145k by mid-2026)
**License:** AGPL-3.0
**Key Features:**
- txt2img, img2img, inpainting, outpainting
- Extension ecosystem (ControlNet, ADetailer, Regional Prompting, etc.)
- LoRA, Textual Inversion, Hypernetwork support
- SDXL, SD 1.5, SD 2.x support
- Batch processing, tiling, highres fix
- API endpoint for automation

---

### ComfyUI
**One-line:** The most powerful node-based/graph diffusion model UI with API and backend; maximum flexibility via visual workflows.
**URL:** https://www.comfy.org | **Repo:** https://github.com/comfyanonymous/ComfyUI
**⭐ GitHub Stars:** ~70k+
**License:** GPL-3.0
**Key Features:**
- Node-based visual workflow editor
- Supports SD 1.5, SDXL, SD3, Flux, HunyuanDiT, video models
- 2,000+ community custom nodes
- API-first design for pipeline automation
- Video generation integration (Wan2.1, LTX-Video, HunyuanVideo)
- Lower VRAM usage than A1111 (optimized execution graph)
- Growth 340% in 2024–2025

---

### InvokeAI
**One-line:** Professional-grade creative engine for Stable Diffusion with a polished WebUI, unified canvas, and node-based workflow editor.
**URL:** https://invoke.ai | **Repo:** https://github.com/invoke-ai/InvokeAI
**⭐ GitHub Stars:** ~27.5k (Global Rank #1288)
**License:** Apache-2.0
**Key Features:**
- Industry-leading WebUI with unified canvas
- Node-based workflow editor (similar to ComfyUI but polished)
- CLI support
- Foundation for commercial products
- Supports SDXL, Flux, ControlNet, IP-Adapter
- Mac (MPS), Windows, Linux (CUDA)

---

### Fooocus
**One-line:** Simplified Stable Diffusion UI focused on prompting and generating — "Midjourney-like" ease with local SD power. Minimal configuration needed.
**URL:** https://github.com/lllyasviel/Fooocus
**⭐ GitHub Stars:** ~43.3k
**License:** GPL-3.0
**Key Features:**
- Opinionated defaults (no parameter tweaking needed)
- Built-in style presets
- Inpainting, outpainting, image prompt
- SDXL-focused
- Extremely beginner-friendly
- By the creator of ControlNet (lllyasviel)

---

## 5. LOCAL VOICE / SPEECH

### OpenAI Whisper
**One-line:** State-of-the-art open-source speech recognition model supporting 99 languages; runs locally for transcription and translation.
**URL:** https://github.com/openai/whisper
**⭐ GitHub Stars:** ~103.2k (Global Rank #109)
**License:** MIT
**Key Features:**
- Multiple model sizes: tiny, base, small, medium, large, large-v2, large-v3
- Multilingual transcription (99 languages)
- Translation to English
- Runs on CPU or GPU
- Encoder-decoder Transformer architecture
- Word-level timestamps (with whisper-timestamped)

---

### faster-whisper
**One-line:** CTranslate2-based reimplementation of Whisper — up to 4x faster than openai/whisper with same accuracy, lower memory, 8-bit quantization on CPU+GPU.
**URL:** https://github.com/SYSTRAN/faster-whisper
**⭐ GitHub Stars:** ~23.8k (Global Rank #1646)
**License:** MIT
**Key Features:**
- 4x faster than original Whisper
- INT8 quantization on both CPU and GPU
- Batched inference support
- VAD (Voice Activity Detection) integration
- Compatible with all Whisper model sizes
- Used as backend in many local AI voice assistants

---

### Piper
**One-line:** Fast, local neural text-to-speech system optimized for Raspberry Pi and edge devices; supports 30+ languages.
**URL:** https://github.com/rhasspy/piper (archived Oct 2025) | **Successor:** https://github.com/OHF-Voice/piper1-gpl
**⭐ GitHub Stars:** ~11.1k (Global Rank #4627)
**License:** MIT (original) → GPL (piper1-gpl fork)
**Status:** Original repo archived October 6, 2025. Development continues as `piper1-gpl` under OHF-Voice.
**Key Features:**
- Extremely fast inference (real-time on CPU, even Raspberry Pi)
- 30+ languages with multiple voices
- VITS-based neural architecture
- Small model sizes (15–100MB per voice)
- Designed for home assistant / embedded use

---

### Coqui TTS
**One-line:** Deep learning toolkit for Text-to-Speech, battle-tested in research and production; supports XTTS v2 with voice cloning in 13+ languages.
**URL:** https://github.com/coqui-ai/TTS | **Community fork:** https://github.com/idiap/coqui-ai-TTS
**⭐ GitHub Stars:** ~45.4k
**License:** MPL-2.0
**Status:** Coqui (the company) shut down in late 2024. The repo remains available; community maintenance continues via Idiap fork.
**Key Features:**
- XTTS v2: voice cloning from 6-second audio sample
- 13+ language support
- Streaming with <200ms latency
- Multiple architectures (Tacotron2, VITS, Bark, XTTS)
- Fine-tuning support
- Python API + CLI

---

### Kokoro TTS
**One-line:** Open-weight TTS model with only 82M parameters delivering quality comparable to models 10x larger; Apache-licensed, ultra-fast.
**URL (model):** https://huggingface.co/hexgrad/Kokoro-82M | **Repo:** https://github.com/hexgrad/kokoro
**⭐ GitHub Stars:** ~7.7k
**License:** Apache-2.0
**Key Features:**
- 82M parameters — runs on any hardware instantly
- Quality comparable to much larger models
- Under $0.06/hour of audio when served via API
- Multi-language (English, Chinese, Japanese, Korean, French, etc.)
- Multiple voice presets
- ONNX, GGUF export options
- Rust implementation available (lucasjinreal/Kokoros)

---

## 6. LOCAL VIDEO GENERATION

### LTX-Video (Lightricks)
**One-line:** First DiT-based video generation model generating high-quality video in real-time (30 FPS at 1216×704, faster than real-time playback); open-weights.
**URL:** https://github.com/Lightricks/LTX-Video | **Desktop App:** https://github.com/Lightricks/LTX-Desktop
**⭐ GitHub Stars:** ~7.2k
**License:** Open-weight (custom permissive)
**Key Features:**
- LTX-2.3: synchronized 4K video + audio in a single pass, up to 50fps, 20 seconds
- Real-time generation on consumer GPUs
- Text-to-video and image-to-video
- ComfyUI integration (official nodes)
- Desktop app available
- First open model to generate synced audio+video

---

### Wan2.1 / Wan2.2 (Alibaba)
**One-line:** Open and advanced large-scale video generative models from Alibaba; available in 1.3B and 14B parameter sizes for text/image-to-video.
**URL:** https://github.com/Wan-Video/Wan2.1
**⭐ GitHub Stars:** ~14k
**License:** Apache-2.0
**Key Features:**
- 1.3B (runs on consumer GPU) and 14B variants
- Text-to-video, image-to-video
- Chinese and English text generation within video
- ComfyUI integration
- Style transfer, local editing capabilities
- Fine-tunable

---

### HunyuanVideo (Tencent)
**One-line:** Systematic framework for large video generation; HunyuanVideo 1.5 is a lightweight (8.3B param) open-source model achieving state-of-the-art quality on consumer GPUs.
**URL:** https://github.com/Tencent-Hunyuan/HunyuanVideo | v1.5: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
**⭐ GitHub Stars:** [?] ~5-8k (across repos)
**License:** Open-weight (Tencent license)
**Key Features:**
- HunyuanVideo 1.5: 8.3B parameters, runs on consumer GPUs
- Image-to-video (HunyuanVideo-I2V)
- Custom video generation (HunyuanCustom)
- ComfyUI integration
- Progressive model scaling

---

### CogVideoX (THUDM / Zhipu AI)
**One-line:** Text and image-to-video generation using expert Transformer architecture; available in 2B and 5B variants.
**URL:** https://github.com/THUDM/CogVideo
**⭐ GitHub Stars:** ~11.3k
**License:** Open-weight
**Key Features:**
- CogVideoX-2B (entry-level, lower VRAM) and 5B (higher quality)
- 3D VAE + Expert Transformer architecture
- Text-to-video, image-to-video
- ComfyUI and Diffusers integration
- Fine-tunable with LoRA

---

## SUMMARY TABLE

| Tool | Category | ⭐ Stars | URL |
|------|----------|---------|-----|
| Ollama | LLM Runner | ~168k | https://github.com/ollama/ollama |
| LM Studio | LLM Runner (GUI) | Closed-source | https://lmstudio.ai |
| Jan | LLM Runner | ~43.1k | https://github.com/janhq/jan |
| Open WebUI | LLM Frontend | ~115k | https://github.com/open-webui/open-webui |
| GPT4All | LLM Runner | ~77.4k | https://github.com/nomic-ai/gpt4all |
| Pinokio | AI App Installer | ~7.5k | https://github.com/pinokiocomputer/pinokio |
| vLLM | Production Inference | ~83k | https://github.com/vllm-project/vllm |
| llama.cpp | Inference Engine | ~71.7k | https://github.com/ggml-org/llama.cpp |
| TGI (HuggingFace) | Production Inference | ~10.9k | https://github.com/huggingface/text-generation-inference |
| Tabby | Coding Assistant | ~33.5k | https://github.com/TabbyML/tabby |
| AUTOMATIC1111 | Image Gen UI | ~140-145k [?] | https://github.com/AUTOMATIC1111/stable-diffusion-webui |
| ComfyUI | Image/Video Gen | ~70k+ | https://github.com/comfyanonymous/ComfyUI |
| InvokeAI | Image Gen | ~27.5k | https://github.com/invoke-ai/InvokeAI |
| Fooocus | Image Gen | ~43.3k | https://github.com/lllyasviel/Fooocus |
| Whisper | Speech-to-Text | ~103.2k | https://github.com/openai/whisper |
| faster-whisper | Speech-to-Text | ~23.8k | https://github.com/SYSTRAN/faster-whisper |
| Piper | TTS | ~11.1k | https://github.com/rhasspy/piper |
| Coqui TTS | TTS | ~45.4k | https://github.com/coqui-ai/TTS |
| Kokoro TTS | TTS | ~7.7k | https://github.com/hexgrad/kokoro |
| LTX-Video | Video Gen | ~7.2k | https://github.com/Lightricks/LTX-Video |
| Wan2.1 | Video Gen | ~14k | https://github.com/Wan-Video/Wan2.1 |
| HunyuanVideo | Video Gen | ~5-8k [?] | https://github.com/Tencent-Hunyuan/HunyuanVideo |
| CogVideoX | Video Gen | ~11.3k | https://github.com/THUDM/CogVideo |

---

## NOTES & STATUS FLAGS

- **[ARCHIVED]** TGI — archived March 2026, in maintenance mode since Dec 2025. Migrate to vLLM/SGLang.
- **[ARCHIVED]** Piper (rhasspy/piper) — archived Oct 2025. Successor: OHF-Voice/piper1-gpl.
- **[COMPANY SHUTDOWN]** Coqui AI — company shut down late 2024. Repo remains; community fork at idiap/coqui-ai-TTS.
- **[?]** AUTOMATIC1111 star count extrapolated from Wikipedia (136k July 2024) + growth trend.
- **[?]** HunyuanVideo star count estimated across multiple repos (main + v1.5 + I2V).
- All star counts sourced from GitHub/star-history.com as of June 2026 and may vary ±1-2k.

---
*Research compiled: June 28, 2026*
