# 🔓 Open-Source Alternatives to Paid Tools

> Free, self-hostable replacements for expensive AI services.

---

## Quick Reference Table

| Paid Tool | Open-Source Alternative | Stars | Repo |
|-----------|----------------------|-------|------|
| ChatGPT | **LibreChat** | ⭐20k+ | https://github.com/danny-avila/LibreChat |
| ChatGPT | **Open WebUI** | ⭐50k+ | https://github.com/open-webui/open-webui |
| ChatGPT | **HuggingChat** | — | https://huggingface.co/chat/ |
| Midjourney | **Fooocus** | ⭐40k+ | https://github.com/lllyasviel/Fooocus |
| Midjourney | **ComfyUI** | ⭐60k+ | https://github.com/comfyanonymous/ComfyUI |
| Midjourney | **AUTOMATIC1111** | ⭐140k+ | https://github.com/AUTOMATIC1111/stable-diffusion-webui |
| GitHub Copilot | **Tabby** | ⭐25k+ | https://github.com/TabbyML/tabby |
| GitHub Copilot | **Continue** | ⭐20k+ | https://github.com/continuedev/continue |
| Notion AI | **Obsidian + Ollama plugins** | — | https://obsidian.md/ |
| Grammarly | **LanguageTool** | ⭐12k+ | https://github.com/languagetool-org/languagetool |
| Zapier AI | **n8n** | ⭐50k+ | https://github.com/n8n-io/n8n |
| ElevenLabs | **Piper TTS** | ⭐7k+ | https://github.com/rhasspy/piper |
| ElevenLabs | **Kokoro TTS** | ⭐15k+ [?] | https://github.com/hexgrad/kokoro |
| Descript | **Whisper + editing scripts** | ⭐70k+ | https://github.com/openai/whisper |
| Perplexity | **Perplexica** | ⭐15k+ | https://github.com/ItzCrazyKns/Perplexica |
| ChatGPT Plugins | **AnythingLLM** | ⭐30k+ [?] | https://github.com/Mintplex-Labs/anything-llm |
| Document AI | **Danswer** | ⭐12k+ | https://github.com/danswer-ai/danswer |
| AI Coding | **OpenHands (OpenDevin)** | ⭐40k+ | https://github.com/All-Hands-AI/OpenHands |
| Devin | **SWE-agent** | ⭐15k+ | https://github.com/princeton-nlp/SWE-agent |

## Self-Hosting Stacks

### 🟢 Beginner (replace ChatGPT in 5 minutes)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3.3
# Install Open WebUI
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway ghcr.io/open-webui/open-webui:main
```

### 🟡 Intermediate (full private AI workspace)
- Ollama + Open WebUI + n8n for automation
- Add RAG with AnythingLLM or PrivateGPT

### 🔴 Advanced (production AI infrastructure)
- vLLM or TGI for high-throughput serving
- LiteLLM as gateway + Langfuse for observability
- Qdrant/Chroma for vector search
