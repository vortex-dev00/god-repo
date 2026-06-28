# 💎 Hidden Gems — Small Repos That Deserve More Stars

> Under 5,000 stars. Most under 1,000. All actively maintained, all solve real problems. The stuff awesome-lists miss.

---

## Why This Page Exists

Everyone knows about LangChain (90K+ ⭐), Ollama (100K+ ⭐), and ComfyUI (75K+ ⭐). But the best developer tools are often built by one person, have 200 stars, and do their job perfectly. This page is for those.

**Rules for inclusion:**
- Under 5,000 stars (most are under 1,000)
- Actively maintained (commits in last 3 months)
- Solves a REAL problem, not a toy/demo
- Actually works (not vaporware)

---

## 🖥️ AI for Terminal & Shell

*Not the famous ones — the small ones nobody talks about.*

| Repo | ⭐ | What It Does | Why It's a Gem |
|------|-----|-------------|----------------|
| [ekkinox/yai](https://github.com/ekkinox/yai) | ~870 | AI terminal assistant in Go — natural language → shell commands | Beautiful TUI, context-aware, remembers shell history |
| [bakks/butterfish](https://github.com/bakks/butterfish) | ~530 | Wraps your existing bash/zsh with inline AI superpowers | Copilot-for-shell without leaving your terminal |
| [darrenburns/elia](https://github.com/darrenburns/elia) | ~1,800 | Gorgeous TUI for chatting with LLMs (local + cloud) | Keyboard-centric, Textual-based, works with Ollama |
| [matheusml/zsh-ai](https://github.com/matheusml/zsh-ai) | ~50 | Type `# kill port 3000` → get the command | Single-file ZSH plugin, zero dependencies |
| [randombk/llm2sh](https://github.com/randombk/llm2sh) | ~200 | Plain-language to multi-command shell sequences | Sudo-aware, multi-provider, handles complex pipelines |
| [vitali87/llm-shell](https://github.com/vitali87/llm-shell) | ~80 | 100% private shell AI via Ollama | Fully offline, no API keys, no data leaves your machine |
| [smadgulkar/spren](https://github.com/smadgulkar/spren-ai-terminal-assistant-rust) | ~30 | Rust terminal AI — cross-platform (Bash/PS/CMD) | Blazing fast binary, safe execution with preview |
| [dwmkerr/terminal-ai](https://github.com/dwmkerr/terminal-ai) | ~150 | Lightweight CLI designed for piping & scripting | MCP protocol support, built for automation |
| [simonw/llm](https://github.com/simonw/llm) | ~4,800 | CLI for interacting with LLMs — extensible via plugins | Plugin ecosystem, pipe-friendly, stores chat history in SQLite |

---

## 🔀 AI-Powered Git Tools

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [Sitoi/ai-commit](https://github.com/Sitoi/ai-commit) | ~400 | Multi-provider commit message gen (OpenAI/Azure/DeepSeek/Gemini/Claude) |
| [vicc/smart-commit](https://github.com/vicc/smart-commit) | ~150 | Clean commit messages — extracts issue keys from branches automatically |
| [shanginn/git-aicommit](https://github.com/shanginn/git-aicommit) | ~50 | Minimal, does one thing well, interactive confirmation |
| [git-extensions/git-ai](https://github.com/git-extensions/git-ai) | ~80 | Native `git ai` subcommand — Claude-powered conventional commits |
| [0xkaz/claude-auto-commit](https://github.com/0xkaz/claude-auto-commit) | ~25 | Claude Code SDK-powered, multi-language, context-aware |
| [AhmadTchnology/CommitLog-AI](https://github.com/AhmadTchnology/CommitLog-AI) | ~20 | One command: git history → beautiful CHANGELOG.md |
| [nyaomaru/changelog-bot](https://github.com/nyaomaru/changelog-bot) | ~30 | Dual-mode: CLI or GitHub Action for changelog generation |

---

## 🔍 LLM Observability (Tiny Alternatives to LangSmith)

| Repo | ⭐ | What It Does | Why It's a Gem |
|------|-----|-------------|----------------|
| [lmnr-ai/lmnr](https://github.com/lmnr-ai/lmnr) | ~2,500 | Open-source AI agent observability platform (YC S24) | Timeline view of agent execution, sub-agent tracking |
| [Scale3-Labs/langtrace](https://github.com/Scale3-Labs/langtrace) | ~2,200 | OpenTelemetry-based end-to-end LLM tracing | Vendor-neutral, supports all major frameworks |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | ~2,800 | Pure OTel instrumentation for GenAI | Send traces to Datadog, Jaeger, Grafana — your choice |
| [traceloop/hub](https://github.com/traceloop/hub) | ~100 | High-scale LLM gateway in Rust + built-in OTel | Blazing fast, gateway + observability in one binary |
| [codeintegrity-ai/mutahunter](https://github.com/codeintegrity-ai/mutahunter) | ~800 | AI mutation testing — tests the quality of YOUR tests | LLM-generated mutants, language-agnostic |

---

## 📦 Small but Powerful LLM Libraries

| Repo | ⭐ | What It Does | Why It's a Gem |
|------|-----|-------------|----------------|
| [jackmpcollins/magentic](https://github.com/jackmpcollins/magentic) | ~2,000 | LLMs as Python functions via `@prompt` decorators | Cleanest API — just decorate a function, get structured output |
| [Mirascope/mirascope](https://github.com/Mirascope/mirascope) | ~1,500 | Pythonic LLM toolkit — type-safe, provider-agnostic | No massive framework — just clean Python with types |
| [MadcowD/ell](https://github.com/MadcowD/ell) | ~1,200 | Lightweight prompt engineering library | Prompts as versioned Python functions |
| [lennartpollvogt/ollama-instructor](https://github.com/lennartpollvogt/ollama-instructor) | ~200 | Structured outputs from Ollama with Pydantic validation | Bridge between Ollama and instructor-style patterns |
| [1rgs/jsonformer](https://github.com/1rgs/jsonformer) | ~4,200 | Bulletproof structured JSON generation | Token-by-token constraint — GUARANTEES valid JSON |
| [nadeesha/structlm](https://github.com/nadeesha/structlm) | ~50 | Token-efficient schema for structured LLM output | Minimal token overhead vs raw JSON schema |
| [firattamur/llmdantic](https://github.com/firattamur/llmdantic) | ~80 | Pydantic-first LLM outputs with retry/validation | Clean decorator pattern, automatic error recovery |

---

## ⚡ LLM Routers & Gateways

| Repo | ⭐ | What It Does | Why It's a Gem |
|------|-----|-------------|----------------|
| [maximhq/bifrost](https://github.com/maximhq/bifrost) | ~1,200 | Enterprise AI gateway — 50× faster than LiteLLM | 11μs overhead at 5K RPS, cluster mode, Apache 2.0 |
| [inference-gateway/inference-gateway](https://github.com/inference-gateway/inference-gateway) | ~300 | Unified gateway for Ollama + OpenAI + Groq + Anthropic | Single endpoint, MCP support |
| [EinStack/glide](https://github.com/EinStack/glide) | ~100 | Model gateway in Go for production GenAI | Unified API, health checks, fallback chains |
| [theopenco/llmgateway](https://github.com/theopenco/llmgateway) | ~100 | Route + analyze LLM requests with budget controls | Analytics dashboard, request logging |
| [egoist/ai-proxy](https://github.com/egoist/ai-proxy) | ~126 | Dead simple proxy for OpenAI/Anthropic/Gemini/Groq | Single file, MIT license, just works |
| [Writesonic/GPTRouter](https://github.com/Writesonic/GPTRouter) | ~900 | Multi-LLM + image model management with fallbacks | From Writesonic, production-proven |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | ~40 | Smart router — 78% cost savings, micropayments | Pay-per-token across 30+ models |

---

## 🔌 Unknown MCP Servers That Solve Real Problems

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [spences10/mcp-memory-sqlite](https://github.com/spences10/mcp-memory-sqlite) | ~200 | Give AI persistent memory with SQLite |
| [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | ~200 | 200+ tools for AI-powered reverse engineering via Ghidra |
| [chongdashu/unreal-mcp](https://github.com/chongdashu/unreal-mcp) | ~800 | Control Unreal Engine through natural language |
| [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) | ~4,000 | The reference Go MCP library |
| [ssut/Remote-MCP](https://github.com/ssut/Remote-MCP) | ~300 | Type-safe remote MCP communication |
| [jacksteamdev/obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools) | ~300 | Obsidian ↔ MCP bridge (semantic search + Templater) |
| [IBM/ibmi-mcp-server](https://github.com/IBM/ibmi-mcp-server) | ~50 | MCP for IBM i (AS/400) — legacy mainframe meets AI |
| [launchdarkly/mcp-server](https://github.com/launchdarkly/mcp-server) | ~20 | Feature flag management through AI conversations |
| [cap-js/mcp-server](https://github.com/cap-js/mcp-server) | ~10 | AI-assisted SAP CAP application development |

---

## 📝 Prompt Management & Versioning

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [pezzolabs/pezzo](https://github.com/pezzolabs/pezzo) | ~2,800 | Full LLMOps platform — design, version, deliver, observe prompts |
| [PromptPal/PromptPal](https://github.com/PromptPal/PromptPal) | ~200 | Self-hosted, DX-first prompt serving |
| [doganarif/promptpilot](https://github.com/doganarif/promptpilot) | ~40 | CLI for versioning + A/B testing prompts |
| [thompson0012/promptv](https://github.com/thompson0012/promptv) | ~30 | Git-like version control for prompts (`promptv commit/diff/log`) |

---

## 📄 AI Documentation Generators

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [context-labs/autodoc](https://github.com/context-labs/autodoc) | ~1,900 | Auto-generate docs for entire codebases with LLMs |
| [born3am/README-AI](https://github.com/born3am/README-AI) | ~1,500 | One command → polished README with badges |
| [toolworks-dev/auto-md](https://github.com/toolworks-dev/auto-md) | ~300 | Flatten repos into AI/LLM-ready markdown |
| [genericmilk/docudoodle](https://github.com/genericmilk/docudoodle) | ~40 | Document legacy code nobody wants to touch |
| [andgom97/autodoc-gen](https://github.com/andgom97/autodoc-gen) | ~20 | CPU-only: auto docs + unit tests + architecture diagrams |
| [TrySita/AutoDocs](https://github.com/TrySita/AutoDocs) | ~30 | Living docs that update as code changes |

---

## 🧪 AI-Powered Testing

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [qodo-ai/qodo-cover](https://github.com/qodo-ai/qodo-cover) | ~4,500 | AI test generation — first OSS impl of Meta's TestGen-LLM |
| [anti-work/shortest](https://github.com/anti-work/shortest) | ~4,000 | Write tests in English, AI executes browser interactions |
| [codeintegrity-ai/mutahunter](https://github.com/codeintegrity-ai/mutahunter) | ~800 | Mutation testing — tests whether your tests actually work |
| [hghianni/EvoMaster](https://github.com/hghianni/EvoMaster) | ~800 | AI-driven fuzzing for REST and GraphQL APIs |

---

## 🔬 AI Code Review (Not the Big Ones)

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [huggingface/serge](https://github.com/huggingface/serge) | ~500 | GitHub-native AI reviewer — respects CODEOWNERS |
| [mehdihadeli/AIAssist](https://github.com/mehdihadeli/AIAssist) | ~200 | Full review workflow from CLI, local + cloud models |
| [MoaKK/AI-Code-Reviewer](https://github.com/MoaKK/AI-Code-Reviewer) | ~30 | Drop-in GitHub Action, Claude-powered inline comments |
| [NOAA-EMC/ci-llm-code-review](https://github.com/NOAA-EMC/ci-llm-code-review) | ~20 | Gemini-powered, built & tested at NOAA (US govt) |

---

## 🎨 AI Image Tools (Not the Famous Ones)

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [AppMana/comfyui-nunchaku](https://github.com/AppMana/comfyui-nunchaku) | ~2,000 | Run FLUX in **4-bit on 8GB VRAM** | 
| [layerdiffuse (ComfyUI)](https://github.com/huchenlei/ComfyUI-layerdiffuse) | ~1,500 | Transparent image generation in ComfyUI |
| [city96/ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) | ~1,500 | GGUF quantization for image models — not just text |
| [Upscayl](https://github.com/upscayl/upscayl) | ~4,500 | Free open-source AI image upscaler (GUI app) |
| [advimman/lama (IOPaint)](https://github.com/Sanster/IOPaint) | ~4,000 | Free inpainting tool — remove anything from images |
| [krita-ai-diffusion](https://github.com/Acly/krita-ai-diffusion) | ~3,500 | Full AI generation inside Krita (free Photoshop alternative) |

---

## 🤖 AI Agents & RAG (Small Frameworks)

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [headroom-ai/headroom](https://github.com/headroom-ai/headroom) | ~100 | **60-95% context compression** for LLM calls |
| [kagisearch/vectordb](https://github.com/kagisearch/vectordb) | ~600 | Minimal Python vector DB from Kagi — batteries included |
| [fynnfluegge/codeqai](https://github.com/fynnfluegge/codeqai) | ~300 | Chat with your codebase locally via embeddings |
| [sanonone/kektordb](https://github.com/sanonone/kektordb) | ~100 | In-memory vector DB + AI gateway in single Go binary |
| [MinishLab/semble](https://github.com/MinishLab/semble) | ~200 | Semantic code search — 98% fewer tokens than grep |
| [bespokelabsai/curator](https://github.com/bespokelabsai/curator) | ~1,500 | Production-grade synthetic data generation |

---

## 🗣️ Voice, TTS & Transcription (Hidden Gems)

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [Whishper](https://github.com/pluja/whishper) | ~2,000 | Self-hosted Whisper with web UI, subtitles, translation |
| [chidiwilliams/buzz](https://github.com/chidiwilliams/buzz) | ~4,500 | Desktop app for offline transcription (Whisper GUI) |
| [thewh1teagle/vibe](https://github.com/thewh1teagle/vibe) | ~1,000 | Cross-platform transcription app — fast, simple |
| [TextyMcSpeechy](https://github.com/TextyMcSpeechy/TextyMcSpeechy) | ~200 | Ultra-lightweight TTS for home assistants |
| [myshell-ai/OpenVoice](https://github.com/myshell-ai/OpenVoice) | ~3,500 | Instant voice cloning — granular tone/style control |

---

## 🏠 Self-Hosted AI Assistants (Not the Big Ones)

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [khoj-ai/khoj](https://github.com/khoj-ai/khoj) | ~4,500 | Self-hosted AI second brain — search your docs, notes, conversations |
| [ClaraVerse](https://github.com/badboysm890/ClaraVerse) | ~1,500 | Open-source personal AI assistant with local model support |
| [Hollama](https://github.com/fmaclen/hollama) | ~800 | Minimal chat UI for Ollama — clean, fast, no bloat |
| [Enchanted](https://github.com/AugustDev/enchanted) | ~3,000 | macOS/iOS native Ollama client — beautiful Apple-native UI |
| [Mobile-Artificial-Intelligence/maid](https://github.com/Mobile-Artificial-Intelligence/maid) | ~1,500 | Cross-platform AI chat with local models on mobile |

---

## ⚙️ Quantization & Model Optimization

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [xhedit/quantkit](https://github.com/xhedit/quantkit) | ~200 | One CLI for ALL quant formats (GGUF, GPTQ, AWQ, EXL2) |
| [ModelCloud/GPTQModel](https://github.com/ModelCloud/GPTQModel) | ~1,200 | Multi-platform GPTQ with Nvidia/AMD/Intel/Apple acceleration |
| [dgacitua/hf-gguf-quantize](https://github.com/dgacitua/hf-gguf-quantize) | ~50 | End-to-end: download HF model → quantize → GGUF package |

---

## 🔎 AI-Powered Local File Search

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [yoanbernabeu/grepai](https://github.com/yoanbernabeu/grepai) | ~1,700 | Semantic grep + call graphs, 100% local, MCP built-in |
| [mixedbread-ai/mgrep](https://github.com/mixedbread-ai/mgrep) | ~500 | Semantic grep for code, images, PDFs — understands meaning |
| [prasaar/aiwhispr](https://github.com/prasaar/aiwhispr) | ~100 | Semantic search for documents (PDF, DOCX, PPTX, CSV) |

---

## 🧬 Synthetic Data & Dataset Tools

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [argilla-io/distilabel](https://github.com/argilla-io/distilabel) | ~1,800 | Synthetic data pipelines — Magpie, SPIN, DPO built-in |
| [meta-llama/synthetic-data-kit](https://github.com/meta-llama/synthetic-data-kit) | ~1,500 | Meta's official synthetic data toolkit |
| [hitsz-ids/synthetic-data-generator](https://github.com/hitsz-ids/synthetic-data-generator) | ~600 | High-quality structured tabular synthetic data |

---

## 🌐 AI API Aggregators

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | ~500 | Unified hub for 1000+ models, cross-format translation |
| [egoist/ai-proxy](https://github.com/egoist/ai-proxy) | ~126 | Dead simple, single-file proxy for all major providers |
| [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy) | ~50 | Universal gateway with load-balancing |

---

## 📱 AI for Everyday People (Non-Dev Hidden Gems)

| Repo | ⭐ | What It Does |
|------|-----|-------------|
| [WritingTools](https://github.com/theJayTea/WritingTools) | ~3,000 | Apple Intelligence-style writing tools for Windows/Linux |
| [Blinko](https://github.com/blinko-space/blinko) | ~2,500 | AI-powered note-taking with auto-tagging and search |
| [screenpipe](https://github.com/mediar-ai/screenpipe) | ~4,000 | 24/7 screen + audio capture with AI search (Rewind-alt) |
| [Karakeep (Hoarder)](https://github.com/karakeep-app/karakeep) | ~4,500 | AI-powered bookmark manager — auto-tags, full-text search |
| [Inbox Zero](https://github.com/elie222/inbox-zero) | ~3,500 | AI email management — auto-categorize, bulk unsubscribe |
| [Linkwarden](https://github.com/linkwarden/linkwarden) | ~3,500 | Self-hosted bookmark archive with AI tagging |
| [Meetily](https://github.com/Zackriya-Solutions/meeting-minutes) | ~2,500 | Local-first AI meeting notes — no cloud, no subscription |
| [Page Assist](https://github.com/nicepkg/page-assist) | ~2,000 | Browser extension to chat with any webpage using local AI |
| [Actual AI](https://github.com/actualbudget/actual) | ~4,000 | AI-powered personal finance (local-first budgeting) |
| [Harper](https://github.com/elijah-potter/harper) | ~2,000 | Open-source grammar checker (Grammarly alternative) |

---

## 🏆 Ultra-Small Gems (<500 Stars)

The absolute hidden treasures:

| Repo | ⭐ | One-Liner |
|------|-----|-----------|
| [jamierpond/tokencount](https://github.com/jamierpond/tokencount) | ~100 | `wc` for tokens. Dead simple. |
| [prompt-tower](https://github.com/prompt-tower/prompt-tower) | ~300 | Visual prompt builder for complex multi-file contexts |
| [rryam/VecturaKit](https://github.com/rryam/VecturaKit) | ~50 | Swift vector DB — on-device RAG for iOS/macOS |
| [krokozyab/Agent-Fusion](https://github.com/krokozyab/Agent-Fusion) | ~30 | Local RAG search in a single JAR |
| [zsh-ai](https://github.com/matheusml/zsh-ai) | ~50 | `# describe what you want` → shell command |
| [spren](https://github.com/smadgulkar/spren-ai-terminal-assistant-rust) | ~30 | Rust terminal AI, cross-platform, safe execution |
| [cap-js/mcp-server](https://github.com/cap-js/mcp-server) | ~10 | SAP + AI via MCP — niche but huge for enterprise devs |
| [autodoc-gen](https://github.com/andgom97/autodoc-gen) | ~20 | CPU-only auto-docs with architecture diagrams |

---

## 📊 Summary

| Category | Count | Star Range |
|----------|-------|-----------|
| Terminal/Shell AI | 9 | 30–4,800 |
| Git Tools | 7 | 20–400 |
| LLM Observability | 5 | 100–2,800 |
| LLM Libraries | 7 | 50–4,200 |
| LLM Routers/Gateways | 7 | 40–1,200 |
| MCP Servers | 9 | 10–4,000 |
| Prompt Management | 4 | 30–2,800 |
| Documentation | 6 | 20–1,900 |
| Testing | 4 | 800–4,500 |
| Code Review | 4 | 20–500 |
| Image/ComfyUI | 6 | 1,500–4,500 |
| Agents/RAG | 6 | 100–1,500 |
| Voice/TTS | 5 | 200–4,500 |
| Self-Hosted | 5 | 800–4,500 |
| Quantization | 3 | 50–1,200 |
| Local Search | 3 | 100–1,700 |
| Synthetic Data | 3 | 600–1,800 |
| API Aggregators | 3 | 50–500 |
| Everyday People | 10 | 2,000–4,500 |
| Ultra-Small (<500) | 8 | 10–300 |
| **TOTAL** | **~114** | **10–4,800** |

---

## How to Find More Gems

1. **GitHub Explore → Trending → Sort by "recently updated"** with low star filters
2. **Reddit r/LocalLLaMA** — weekly "what tools are you using?" threads
3. **Hacker News "Show HN"** — filter for AI/LLM, sort by points
4. **awesome-mcp-servers** — scroll past the first 20 to find niche ones
5. **tensorchord/Awesome-LLMOps** — deep cuts at the bottom of each section
6. **GitHub orgs** of known tools — check their other repos (e.g., Traceloop, Qodo, EinStack)

---

*Last updated: June 2026. Star counts approximate. [?] = unverified. PRs welcome — especially for repos under 200 ⭐.*
