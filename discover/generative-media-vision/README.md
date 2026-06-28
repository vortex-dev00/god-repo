# 🎨 Generative Media & Vision

> Image generation, video synthesis, visual language models, and the creative AI stack.

---

## Current Landscape (June 2026)

The generative media space has consolidated around diffusion-based architectures for images and rectified-flow transformers for video. **Sora was shut down in March 2026** — Runway, Kling, and Pika lead video generation. For images, FLUX and Stable Diffusion 3.5 dominate the open-source space while Midjourney and DALL-E (now integrated into GPT-5.5) dominate closed commercial use.

---

## 1. IMAGE GENERATION

### Closed / Commercial

| Platform | Model | Key Features | Pricing | Link |
|----------|-------|-------------|---------|------|
| **Midjourney** | v6.1+ | Best aesthetic quality, consistent style, highest commercial adoption (~20M users, $500M revenue) | $10-60/mo | https://midjourney.com/ |
| **DALL-E** (OpenAI) | Integrated into GPT-5.5 | Native inside ChatGPT, image editing, inpainting | Part of ChatGPT Plus ($20/mo) | https://openai.com/ |
| **Adobe Firefly** | Firefly 3+ | Commercial-safe (trained on licensed data), Photoshop integration | Part of Creative Cloud | https://firefly.adobe.com/ |
| **Ideogram** | v3+ | Best text-in-image rendering, logo generation | Free tier + $7-20/mo | https://ideogram.ai/ |
| **Google Imagen** | Imagen 3 | Inside Gemini, high photorealism | Part of Gemini | https://deepmind.google/technologies/imagen-3/ |

### Open-Source Image Models

| Model | Architecture | Parameters | Key Strength | Link |
|-------|-------------|-----------|-------------|------|
| **FLUX.1** (Black Forest Labs) | Rectified Flow Transformer | 12B | Best open-source quality, multiple variants (dev/schnell/pro) | https://github.com/black-forest-labs/flux |
| **Stable Diffusion 3.5** (Stability AI) | MMDiT (Multi-Modal DiT) | 2B-8B | Versatile, huge ecosystem of LoRAs/extensions | https://huggingface.co/stabilityai/stable-diffusion-3.5-large |
| **Stable Diffusion XL** | U-Net + Refiner | 6.6B | Mature ecosystem, most LoRAs/checkpoints available | https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 |
| **PixArt-Σ** | DiT (Diffusion Transformer) | 600M | Lightweight, fast, 4K capable | https://github.com/PixArt-alpha/PixArt-sigma |
| **Playground v3** | Custom DiT | — | Strong photorealism | https://playground.com/ |
| **Kolors** (Kwai) | — | — | Chinese-optimized, strong aesthetic | https://github.com/Kwai-Kolors/Kolors |

### Image Generation UIs & Tools

| Tool | ⭐ Stars | Description | Link |
|------|---------|-------------|------|
| **ComfyUI** | ⭐ 75,000+ | Node-based workflow editor — the "Blender of AI image gen." Supports FLUX, SD3.5, SDXL, custom pipelines. Most powerful local UI. | https://github.com/comfyanonymous/ComfyUI |
| **AUTOMATIC1111 (Stable Diffusion WebUI)** | ⭐ 145,000+ | Classic web UI for Stable Diffusion. Huge extension ecosystem. Still widely used but ComfyUI is overtaking for new workflows. | https://github.com/AUTOMATIC1111/stable-diffusion-webui |
| **Fooocus** | ⭐ 42,000+ | One-click SD/FLUX with Midjourney-like simplicity. Best for beginners who want local gen. | https://github.com/lllyasviel/Fooocus |
| **InvokeAI** | ⭐ 24,000+ | Professional creative studio UI. Canvas, layers, inpainting, outpainting. | https://github.com/invoke-ai/InvokeAI |
| **Forge (SD WebUI Forge)** | ⭐ 10,000+ [?] | Performance-optimized fork of AUTOMATIC1111. Faster VRAM usage. | https://github.com/lllyasviel/stable-diffusion-webui-forge |
| **Draw Things** | — | macOS/iOS native Stable Diffusion app | https://drawthings.ai/ |

---

## 2. VIDEO GENERATION

### Closed / Commercial (June 2026)

| Platform | Status | Key Features | Link |
|----------|--------|-------------|------|
| **Runway Gen-3/4** | Leading commercial video gen | Text-to-video, image-to-video, motion brush, camera controls. Professional quality. | https://runwayml.com/ |
| **Kling** (Kuaishou) | Top tier, Chinese origin | 2-min videos, excellent motion, lip-sync. Strong competitor to Runway. | https://klingai.com/ |
| **Pika** | Active, consumer-friendly | Quick video gen, effects, lip-sync. More accessible pricing. | https://pika.art/ |
| **Veo 2** (Google DeepMind) | Integrated into Gemini | High quality, realistic physics, available via Google AI tools. | https://deepmind.google/technologies/veo/ |
| **HeyGen** | AI avatar videos | Realistic talking-head avatars for business/marketing. | https://heygen.com/ |
| **Synthesia** | AI avatar studio | Enterprise avatar creation, 140+ languages. | https://synthesia.io/ |
| **Sora** (OpenAI) | ☠️ **SHUT DOWN March 2026** | Was OpenAI's video gen model. Discontinued. | — |

### Open-Source Video Models

| Model | Description | Link |
|-------|-------------|------|
| **Open-Sora** (HPC-AI Tech) | Open reproduction of Sora-like video gen. DiT-based. | https://github.com/hpcaitech/Open-Sora |
| **Open-Sora-Plan** | Community effort for long video generation | https://github.com/PKU-YuanGroup/Open-Sora-Plan |
| **CogVideo / CogVideoX** (Tsinghua/Zhipu) | Text-to-video diffusion model with 3D attention | https://github.com/THUDM/CogVideo |
| **Mochi 1** (Genmo) | Open-source, high-motion video gen | https://github.com/genmoai/mochi |
| **Wan (Alibaba)** | Open video generation suite | https://github.com/Wan-Video/Wan2.1 [?] |
| **LTX-Video** (Lightricks) | Real-time video gen, fast inference | https://github.com/Lightricks/LTX-Video |
| **AnimateDiff** | Add motion to any SD image model | https://github.com/guoyww/AnimateDiff |

---

## 3. VISUAL LANGUAGE MODELS (VLMs)

Models that understand AND generate based on visual input:

| Model | Provider | Capabilities | Link |
|-------|----------|-------------|------|
| **GPT-5.5 Vision** | OpenAI | Native multimodal — understands images, screenshots, diagrams | https://openai.com/ |
| **Claude Opus 4.8 Vision** | Anthropic | Document understanding, screenshot analysis, chart reading | https://anthropic.com/ |
| **Gemini 3.x Vision** | Google | Native multimodal from training — video understanding, Omni model | https://deepmind.google/models/gemini/ |
| **LLaVA-NeXT** | Open-source | Strong open VLM, various sizes | https://github.com/LLaVA-VL/LLaVA-NeXT |
| **InternVL 2.5** | Shanghai AI Lab | Competitive with GPT-4V on benchmarks | https://github.com/OpenGVLab/InternVL |
| **Qwen-VL 2.5** | Alibaba | Strong multilingual visual understanding | https://github.com/QwenLM/Qwen2.5-VL |
| **Molmo** | AI2 | Open-source pointing + understanding | https://github.com/allenai/molmo [?] |
| **Florence-2** | Microsoft | Lightweight vision foundation model | https://huggingface.co/microsoft/Florence-2-large |
| **SAM 2** (Segment Anything) | Meta | Universal video/image segmentation | https://github.com/facebookresearch/sam2 |
| **Grounding DINO** | IDEA Research | Open-set object detection from text | https://github.com/IDEA-Research/GroundingDINO |

---

## 4. IMAGE EDITING & MANIPULATION

| Tool | Type | Description | Link |
|------|------|-------------|------|
| **Krea AI** | Cloud | Real-time AI image generation & editing | https://krea.ai/ |
| **Playground AI** | Cloud | Freemium image gen + editing | https://playground.ai/ |
| **PhotoRoom** | App | AI background removal, product photos | https://photoroom.com/ |
| **Remove.bg** | Cloud | One-click background removal | https://remove.bg/ |
| **ControlNet** | Open-source | Precise control over diffusion (pose, depth, edges) | https://github.com/lllyasviel/ControlNet |
| **IP-Adapter** | Open-source | Image prompt adapter for style transfer | https://github.com/tencent-ailab/IP-Adapter |
| **InstantID** | Open-source | Zero-shot identity-preserving face generation | https://github.com/InstantID/InstantID |
| **Rembg** | Open-source | Python background removal library | https://github.com/danielgatis/rembg |

---

## 5. 3D GENERATION

| Tool | Description | Link |
|------|-------------|------|
| **Meshy** | Text/image to 3D models (commercial) | https://meshy.ai/ |
| **Tripo AI** | Fast 3D asset generation | https://tripo3d.ai/ |
| **Luma AI (Genie)** | Text-to-3D, NeRF capture | https://lumalabs.ai/ |
| **InstantMesh** | Single-image to 3D mesh | https://github.com/TencentARC/InstantMesh |
| **TripoSR** | Fast single-image 3D reconstruction | https://github.com/VAST-AI-Research/TripoSR |
| **Shap-E** (OpenAI) | Text-to-3D shape generation | https://github.com/openai/shap-e |
| **Point-E** (OpenAI) | Text-to-3D point cloud | https://github.com/openai/point-e |
| **Gaussian Splatting** | Real-time novel view synthesis | https://github.com/graphdeco-inria/gaussian-splatting |

---

## 6. UPSCALING & ENHANCEMENT

| Tool | Description | Link |
|------|-------------|------|
| **Real-ESRGAN** | State-of-the-art image upscaling | https://github.com/xinntao/Real-ESRGAN |
| **Topaz Photo AI** | Commercial upscaling/denoising/sharpening | https://topazlabs.com/ |
| **Remini** | Mobile photo enhancement app | https://remini.ai/ |
| **GFPGAN** | Face restoration | https://github.com/TencentARC/GFPGAN |
| **CodeFormer** | Face restoration (better quality) | https://github.com/sczhou/CodeFormer |
| **Magnific AI** | AI upscaling with hallucinated detail | https://magnific.ai/ |

---

*Last updated: June 2026. Mark [?] = unverified.*
