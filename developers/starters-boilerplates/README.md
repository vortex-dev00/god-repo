# 🚀 Starters, Boilerplates & Templates

> Ready-to-use project templates for AI apps, SaaS, and full-stack development.

---

# 🏗️ The God Repo: Self-Hosted AI Tools, Open-Source Alternatives & Workflow Recipes

> **Last updated:** June 2026 | ⭐ = GitHub stars (approximate, as of mid-2026) | [?] = unverified count

---

## 1. SELF-HOSTING COMPLETE STACKS

### Core LLM Infrastructure

| Tool | Description | Stars | URL |
|------|-------------|-------|-----|
| **Ollama** | Run LLMs locally with one command. Supports 100+ models (Llama 3, DeepSeek, Qwen, Gemma, Mistral). Dead-simple CLI + REST API on port 11434 | ⭐ 175K | https://github.com/ollama/ollama |
| **Open WebUI** | ChatGPT-style self-hosted UI supporting Ollama, OpenAI API, Anthropic, Gemini. Multi-user, plugins, RAG, voice, mobile-friendly | ⭐ 132K+ | https://github.com/open-webui/open-webui |
| **LocalAI** | Drop-in OpenAI API replacement. Runs gguf, transformers, diffusers on consumer hardware. Text, audio, video, image, voice cloning, P2P inference. No GPU required | ⭐ 30K+ | https://github.com/mudler/LocalAI |

### Complete Self-Hosted Stacks

| Tool | Description | Stars | URL |
|------|-------------|-------|-----|
| **Ollama + Open WebUI** | The "replace ChatGPT" stack. Docker compose gives you a full ChatGPT-equivalent in minutes. Supports model switching, conversations, RAG | — | https://github.com/open-webui/open-webui (includes Ollama integration) |
| **n8n + Ollama (Self-Hosted AI Starter Kit)** | Official n8n docker-compose template: n8n + Ollama + Qdrant + PostgreSQL for AI-powered workflow automation. Replace Zapier AI completely | ⭐ 5K+ [?] | https://github.com/n8n-io/self-hosted-ai-starter-kit |
| **Local AI Packaged** | All-in-one: Ollama + n8n + Open WebUI + Supabase + vector DBs in one docker-compose | ⭐ 3K+ [?] | https://github.com/coleam00/local-ai-packaged |
| **ClaraVerse** | Privacy-first local AI workspace: Ollama chat, tool calling, agent builder, Stable Diffusion, n8n-style automation. No API keys needed | ⭐ 2K+ [?] | https://github.com/badboysm890/ClaraVerse |

### Multi-Model Chat Interfaces

| Tool | Description | Stars | URL |
|------|-------------|-------|-----|
| **LibreChat** | Enhanced ChatGPT clone with Agents, MCP, DeepSeek, Anthropic, OpenAI, Azure, Groq, Gemini, Artifacts, Code Interpreter, DALL-E-3, multi-user auth, plugins | ⭐ 22K+ [?] | https://github.com/danny-avila/LibreChat |
| **HuggingChat (chat-ui)** | Open-source codebase powering HuggingChat. SvelteKit + MongoDB. Supports tools, multimodal, routing across models | ⭐ 8K+ [?] | https://github.com/huggingface/chat-ui |

### Private Document Chat / RAG

| Tool | Description | Stars | URL |
|------|-------------|-------|-----|
| **AnythingLLM** | "Stop renting your intelligence." Full-stack private doc chat: any LLM + any embedder + any vector DB. Desktop app available. Multi-user, workspace-based | ⭐ 35K+ [?] | https://github.com/Mintplex-Labs/anything-llm |
| **PrivateGPT** | Interact with documents using GPT, 100% privately. No data leaves your machine. Supports local models via llama.cpp | ⭐ 54K+ | https://github.com/zylon-ai/private-gpt |
| **Quivr** | "Your GenAI Second Brain" — RAG-powered personal productivity assistant. Chat with PDFs, CSVs, apps. Supports Ollama, multiple LLM providers | ⭐ 37K+ | https://github.com/QuivrHQ/quivr |

### Enterprise AI Search & Assistants

| Tool | Description | Stars | URL |
|------|-------------|-------|-----|
| **Onyx (formerly Danswer)** | Open-source AI workplace search. Connects to Slack, GitHub, Confluence, Google Drive. Hybrid keyword+vector search, RAG pipeline. YC W24 backed, raised $10M | ⭐ 12K+ [?] | https://github.com/onyx-dot-app/onyx |
| **Khoj** | Open-source AI personal assistant for your "digital brain." Self-hostable or cloud. Chat with notes (Obsidian, org-mode), web search, image gen. Scales from on-device to enterprise | ⭐ 25K+ [?] | https://github.com/khoj-ai/khoj |

### Self-Hosted Automation

| Tool | Description | Stars | URL |
|------|-------------|-------|-----|
| **n8n** | Fair-code workflow automation platform with native AI capabilities. Visual builder + custom code, 400+ integrations. Self-host or cloud | ⭐ 60K+ [?] | https://github.com/n8n-io/n8n |

---

## 2. "HOW TO REPLACE X WITH AI" — Guides & Tools

### 🎨 Replace Photoshop

| Tool | Description | URL |
|------|-------------|-----|
| **Krea AI** | AI creative suite: real-time image generation, enhancement, editing, video, 3D. Built their own Krea 2 model (12B params, diffusion transformer). Free tier available | https://www.krea.ai |
| **Playground AI** | AI image generation platform focused on creative workflows. Good for batch generation and artistic styles | https://playground.ai |
| **ComfyUI** | Node-based diffusion model GUI, API, and backend. The most powerful modular UI for Stable Diffusion/Flux. Massive plugin ecosystem | ⭐ 89K+ (as of Sept 2025) | https://github.com/comfyanonymous/ComfyUI |
| **Fooocus** | Simplified Stable Diffusion: <3 clicks from download to first image. Midjourney-style ease + SD openness. 4GB GPU minimum | ⭐ 48K+ | https://github.com/lllyasviel/Fooocus |
| **Krea 2 (open weights)** | 12B-param text-to-image model, now open-sourced on HuggingFace. Runs in ComfyUI | — | https://huggingface.co/krea-ai |

### 🤖 Replace a Virtual Assistant

| Tool | Description | URL |
|------|-------------|-----|
| **Custom GPTs / Claude Projects** | Create specialized assistants with instructions + knowledge files. Best for non-technical users | https://chat.openai.com (GPTs) / https://claude.ai (Projects) |
| **n8n AI Agents** | Build autonomous agent workflows: tool calling, memory, decision-making, all visual. Connect to 400+ services | https://n8n.io |
| **Khoj** | Personal AI assistant that reads your notes, searches the web, generates images, sets reminders | https://khoj.dev |
| **Open WebUI + Ollama** | Custom "assistants" via model presets + RAG. Fully private | https://github.com/open-webui/open-webui |

### ✍️ Replace a Copywriter

| Tool | Description | URL |
|------|-------------|-----|
| **Claude (Anthropic)** | Best-in-class for long-form writing, tone matching, editing. 200K context window | https://claude.ai |
| **Jasper AI** | Enterprise AI marketing platform: brand voice, campaigns, SEO content. $59-69/seat/month | https://jasper.ai |
| **Custom Pipelines (n8n + LLM)** | Build your own: research → outline → draft → edit → SEO optimize → publish. Zero per-word cost with local models | Self-built with n8n + Ollama |
| **Open-source alternatives**: ChatGPT/Claude via API + custom prompts in any pipeline tool | — | — |

### 📊 Replace a Data Analyst

| Tool | Description | URL |
|------|-------------|-----|
| **Julius AI** | Upload CSV/Excel, ask questions in English, get charts and insights. $12-45/month. Backed by $14.5M seed (Bessemer) | https://julius.ai |
| **ChatGPT Code Interpreter** | Upload files, run Python in sandbox, generate visualizations. Part of ChatGPT Plus ($20/mo) | https://chat.openai.com |
| **Hex** | Collaborative data workspace: SQL + Python notebooks with AI assist. Best for data teams | https://hex.tech |
| **Claude Analysis** | Upload CSVs/spreadsheets, get narrative interpretation + code. Excellent for mid-sized datasets | https://claude.ai |

### 🎧 Replace a Customer Support Team

| Tool | Description | URL |
|------|-------------|-----|
| **Intercom Fin** | AI Agent that resolves 50-81% of support volume. Uses your knowledge base. Now on Fin 3 (Oct 2025): complex queries, every channel | https://www.intercom.com/fin |
| **Crisp AI** | AI-powered customer support with chatbot, knowledge base, and agent assistance. More affordable than Intercom | https://crisp.chat |
| **Open-source option: n8n + Ollama + your KB** | Build custom support bot with RAG over your docs, connected to email/chat channels | Self-built |

### ✏️ Replace Grammarly

| Tool | Description | URL |
|------|-------------|-----|
| **LanguageTool** | Open-source grammar/style/spell checker. 20+ languages. Self-hostable (Java server). Browser extensions, VS Code, LibreOffice. Note: Chrome extension went paid March 2026 | https://languagetool.org / https://github.com/languagetool-org/languagetool |
| **LanguageTool + Local LLM** | Deploy private Grammarly clone: LanguageTool Docker container + LLM for style suggestions | https://github.com/gardner/LocalLanguageTool |
| **Harper** | Fast, open-source grammar checker designed for developers | https://github.com/elijah-potter/harper |

### 🔍 Replace Google Search

| Tool | Description | URL |
|------|-------------|-----|
| **Perplexity AI** | AI research assistant with inline citations, source filtering, Focus mode. Samsung Galaxy integration. Free + Pro ($20/mo) | https://perplexity.ai |
| **Perplexica (now "Vane")** | Open-source Perplexity clone. SearXNG for web search + Ollama for LLM = fully self-hosted AI search with citations | ⭐ 18K+ [?] | https://github.com/ItzCrazyKns/Perplexica |
| **SearXNG** | Self-hosted privacy-respecting metasearch engine. 70+ search engines, no tracking. Foundation for local RAG search | ⭐ 15K+ [?] | https://github.com/searxng/searxng |
| **Local RAG Pipeline** | Ollama + SearXNG + embeddings = your own Perplexity. Multiple open-source templates exist | https://github.com/KazKozDev/production_rag_pipeline |

---

## 3. OPEN-SOURCE ALTERNATIVES TO PAID TOOLS

### ChatGPT →

| Alternative | Description | Stars | URL |
|-------------|-------------|-------|-----|
| **LibreChat** | Multi-model, plugins, agents, code interpreter, DALL-E, multi-user auth | ⭐ 22K+ [?] | https://github.com/danny-avila/LibreChat |
| **Open WebUI** | Best overall ChatGPT replacement. Ollama + OpenAI API compatible | ⭐ 132K+ | https://github.com/open-webui/open-webui |
| **HuggingChat** | Free, runs open models (Llama, Mixtral, etc.), web-based | ⭐ 8K+ (chat-ui) | https://huggingface.co/chat |

### Midjourney →

| Alternative | Description | Stars | URL |
|-------------|-------------|-------|-----|
| **Stable Diffusion (SDXL/SD3)** | The foundational open-source image model. Multiple UIs available | — | https://github.com/Stability-AI/generative-models |
| **Flux (Black Forest Labs)** | State-of-the-art 12B rectified flow transformer. Outperforms Midjourney, DALL·E 3, SD3. Schnell variant is Apache 2.0 | — | https://github.com/black-forest-labs/flux |
| **Flux.2** | Next-gen from BFL (Nov 2025): character consistency, style control, text rendering, brand adherence. Klein variants run on consumer GPUs (RTX 3090) | — | https://huggingface.co/black-forest-labs/FLUX.2-dev |
| **Fooocus** | Midjourney-like simplicity with Stable Diffusion power. Zero config | ⭐ 48K+ | https://github.com/lllyasviel/Fooocus |
| **ComfyUI** | Node-based power-user interface for any diffusion model | ⭐ 89K+ | https://github.com/comfyanonymous/ComfyUI |
| **Krea 2 (open weights)** | 12B diffusion transformer, open-sourced June 2026 | — | https://huggingface.co/krea-ai |

### GitHub Copilot →

| Alternative | Description | Stars | URL |
|-------------|-------------|-------|-----|
| **Tabby** | Self-hosted AI coding assistant. No DBMS/cloud needed. OpenAPI interface. On-premise Copilot replacement | ⭐ 21K–34K [?] | https://github.com/TabbyML/tabby |
| **Continue** | Open-source coding agent for VS Code & JetBrains. Connect any model. Autocomplete + chat + edit. ⚠️ Acquired by Cursor in 2026, repo now read-only | ⭐ 34K+ | https://github.com/continuedev/continue |
| **Cody (Sourcegraph)** | AI code assistant with advanced codebase search + context. Free tier, Pro $9/user/mo. ⚠️ Public snapshot archived Aug 2025 | — | https://sourcegraph.com/cody |
| **Aider** | AI pair programming in your terminal. Auto-git commits. 75+ LLM providers. ⚠️ Maintenance mode since Aug 2025 | ⭐ 44K+ | https://github.com/Aider-AI/aider |
| **Kilo Code** | Successor/fork in the Roo Code lineage. Active development, growing community | ⭐ 24K+ [?] | https://github.com/kilocode/kilo |

### Notion AI →

| Alternative | Description | Stars | URL |
|-------------|-------------|-------|-----|
| **Obsidian + AI Plugins** | Local-first markdown knowledge base + AI plugins (Smart Connections, Copilot, Smart Composer). Run Ollama locally for full privacy | — | https://obsidian.md |
| **Smart Connections (plugin)** | Semantic search + AI chat over your Obsidian vault. Free, offline-capable with local models | — | https://github.com/brianpetro/obsidian-smart-connections |
| **Obsidian Copilot** | AI assistant inside Obsidian. Multiple LLM providers | — | https://github.com/logancyang/obsidian-copilot |
| **AppFlowy** | Open-source Notion alternative with AI features. Flutter-based | ⭐ 60K+ [?] | https://github.com/AppFlowy-IO/AppFlowy |

### Grammarly →

| Alternative | Description | Stars | URL |
|-------------|-------------|-------|-----|
| **LanguageTool** | Open-source, self-hostable, 20+ languages. Java-based server. Docker available | ⭐ 12K+ [?] | https://github.com/languagetool-org/languagetool |
| **Harper** | Lightweight, developer-focused grammar checker | — | https://github.com/elijah-potter/harper |

### Zapier →

| Alternative | Description | Stars | URL |
|-------------|-------------|-------|-----|
| **n8n** | Fair-code, self-hosted, 400+ integrations, native AI nodes (LLM chains, agents, RAG). Visual + code | ⭐ 60K+ [?] | https://github.com/n8n-io/n8n |
| **Activepieces** | Open-source automation alternative. Simpler than n8n for non-devs | ⭐ 12K+ [?] | https://github.com/activepieces/activepieces |

### Jasper →

| Alternative | Description | URL |
|-------------|-------------|-----|
| **Claude API + custom pipeline** | Best writing quality, cheapest at scale | https://docs.anthropic.com |
| **Open-source LLMs (Llama 3, Mistral) + custom prompts** | Free, unlimited, self-hosted. Quality gap has narrowed significantly | Via Ollama |
| **n8n content pipelines** | Automate: research → outline → draft → edit → publish with any LLM | https://n8n.io |

---

## 4. WORKFLOW RECIPES

### 🔀 "AI + Git" Workflows for Solo Developers

**The Modern Solo Dev Stack (2026):**

1. **Aider** (maintenance mode) or **Claude Code** — AI pair programming with automatic git commits
   - https://aider.chat / https://docs.anthropic.com/en/docs/claude-code
   
2. **Git Worktrees + Parallel Agents** — Run multiple AI coding agents on separate branches simultaneously
   - Pattern: `git worktree add ../feature-x feature-x` → agent works on feature-x while you review feature-y
   
3. **GitHub Flow + AI** — Solo dev superpowers:
   - Create issues with specifications
   - AI agent picks up issues, works in branches
   - Auto-creates PRs with descriptions
   - Human reviews, merges
   - Reference: https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e

4. **GitButler** — Intelligent branch/workflow management with AI
   - https://gitbutler.com

**Best Practices:**
- Keep commits atomic and well-described (AI reads git history)
- Use conventional commits for AI parseability
- Store research/context in `/scratchpads` or `/docs/decisions`
- Let AI write commit messages from diffs

---

### 🔬 "AI Research Pipeline" (Search → Summarize → Cite)

**Self-Hosted Stack:**
```
SearXNG (search) → Ollama (summarize) → Citation formatter → Markdown output
```

**Tools for Each Stage:**

| Stage | Tool | URL |
|-------|------|-----|
| **Search** | Perplexica/Vane (self-hosted) | https://github.com/ItzCrazyKns/Perplexica |
| **Search** | SearXNG (metasearch) | https://github.com/searxng/searxng |
| **Academic Search** | Semantic Scholar (200M+ papers, free API) | https://semanticscholar.org |
| **Summarize** | Ollama + any model | https://ollama.com |
| **Cite** | Elicit (138M+ papers, systematic reviews) | https://elicit.com |
| **Cite** | Scite (smart citations, citation context) | https://scite.ai |
| **End-to-end** | Perplexity Pro (citations on every sentence) | https://perplexity.ai |
| **End-to-end** | Paperguide (plan → search → screen → extract → generate) | https://paperguide.ai |
| **Orchestration** | n8n (wire everything together) | https://n8n.io |

**Open-Source Full Pipeline:**
- **SurfSense** — Open-source NotebookLM/Perplexity/Glean alternative. Connected to search engines, Slack, Notion, YouTube, GitHub | https://github.com/MODSetter/SurfSense

---

### 📝 "AI Content Pipeline" (Idea → Draft → Edit → Publish)

**The 6-Stage Workflow:**

| Stage | What AI Does | What Human Does | Tools |
|-------|-------------|-----------------|-------|
| 1. **Research** | Keyword research, trend analysis, competitive gaps | Picks the topic, defines reader outcome | Perplexity, Ahrefs, Google Trends |
| 2. **Outline** | Generate structure from brief | Approve/modify structure | Claude, GPT-4o |
| 3. **Draft** | Write first draft from outline | — | Claude (best for long-form), Ollama |
| 4. **Edit** | Grammar, style, readability | Voice, accuracy, experience, insight | LanguageTool + human |
| 5. **Optimize** | SEO, headers, meta, internal links | Final review | Koala, SurferSEO |
| 6. **Publish** | Format, schedule, distribute | Approve | n8n → WordPress/Ghost/Medium |

**Automation Recipe (n8n):**
```
Trigger (weekly) → Research Agent → Outline Generator → Draft Writer → 
Human Review (pause) → SEO Optimizer → WordPress Publisher → Social Distributor
```

**Key Principle:** AI handles ~70% of production labor. Humans own the 30% that makes content worth reading: strategy, voice, lived experience.

---

### 📐 Best Practices for `.cursorrules`, `.claude`, `AGENTS.md`

**The 2026 Landscape:**

| File | Tool | Status |
|------|------|--------|
| **AGENTS.md** | Open standard (Linux Foundation). Read by Codex, Cursor, Copilot, Gemini CLI, Aider, Windsurf, Zed | ✅ Cross-tool standard. 60,000+ repos |
| **CLAUDE.md** | Anthropic's Claude Code | ✅ Claude-specific, hierarchical |
| **.cursorrules** / `.cursor/rules/*.mdc` | Cursor | ✅ Cursor-specific, MDC format since 2025 |
| **Copilot Instructions** | GitHub Copilot | `.github/copilot-instructions.md` |

**Best Practice: Layered Setup**

```
project-root/
├── AGENTS.md          # Cross-tool standard (all agents read this)
├── CLAUDE.md          # Claude-specific overrides
├── .cursor/
│   └── rules/
│       ├── general.mdc
│       └── testing.mdc
├── .github/
│   └── copilot-instructions.md
└── docs/
    └── ARCHITECTURE.md  # Referenced by all config files
```

**What to Include in AGENTS.md:**
1. **Project overview** — what this is, tech stack, architecture
2. **Code conventions** — naming, patterns, file organization
3. **Testing requirements** — what must be tested, how
4. **Forbidden actions** — never delete migrations, never push to main
5. **Decision log references** — link to ADRs
6. **Build/run commands** — how to build, test, deploy

**Impact:** 2025 study found agents with well-crafted context files completed tasks correctly **90%** of the time vs **30%** without them.

**Key Resources:**
- https://codersera.com/blog/agents-md-vs-claude-md-vs-cursor-rules-comparison-2026/
- https://tutorials.technology/tutorials/context-engineering-claude-cursor-2026.html
- https://github.com/shanraisshan/claude-code-best-practice
- https://github.com/murataslan1/cursor-ai-tips/blob/main/rules/cursorrules-2026-best-practices.md

---

## 5. BONUS: Additional Tools Worth Knowing

### AI Coding Agents (2026)

| Tool | Description | Stars | URL |
|------|-------------|-------|-----|
| **Claude Code** | Anthropic's terminal-based agentic coding tool | — | https://docs.anthropic.com/en/docs/claude-code |
| **OpenAI Codex (CLI)** | OpenAI's terminal coding agent, reads AGENTS.md | — | https://github.com/openai/codex |
| **Cursor** | AI-first code editor (acquired Continue) | — | https://cursor.com |
| **Windsurf** | AI-first IDE by Codeium | — | https://windsurf.ai |
| **Gemini CLI** | Google's terminal coding agent | — | https://github.com/google-gemini/gemini-cli |

### Self-Hosted Search & RAG

| Tool | Description | Stars | URL |
|------|-------------|-------|-----|
| **Perplexica/Vane** | Self-hosted Perplexity. SearXNG + LLM = cited answers | ⭐ 18K+ [?] | https://github.com/ItzCrazyKns/Perplexica |
| **SurfSense** | Open-source NotebookLM/Perplexity/Glean. Multi-source RAG | ⭐ 8K+ [?] | https://github.com/MODSetter/SurfSense |
| **Xyne** | AI-first search & answer engine for work. Open-source Glean alternative | — | https://github.com/xynehq/xyne |

### Model Serving & Infrastructure

| Tool | Description | Stars | URL |
|------|-------------|-------|-----|
| **vLLM** | High-throughput LLM serving engine | ⭐ 40K+ [?] | https://github.com/vllm-project/vllm |
| **llama.cpp** | LLM inference in C/C++. Basis for Ollama | ⭐ 75K+ [?] | https://github.com/ggerganov/llama.cpp |
| **Ollama** | Simplest way to run models locally | ⭐ 175K | https://github.com/ollama/ollama |
| **LocalAGI** | Self-hostable AI Agent platform. Drop-in OpenAI Responses API replacement with agentic capabilities | — | https://github.com/mudler/LocalAGI |

---

## 📋 Quick Decision Matrix

| I want to... | Use this |
|--------------|----------|
| Replace ChatGPT (private) | Ollama + Open WebUI |
| Replace ChatGPT (multi-provider) | LibreChat |
| Chat with my documents | AnythingLLM or PrivateGPT |
| Search my company's knowledge | Onyx (Danswer) |
| Automate workflows with AI | n8n (self-hosted) |
| Generate images locally | ComfyUI + Flux |
| Code with AI (self-hosted) | Tabby |
| Code with AI (terminal) | Aider or Claude Code |
| Grammar check (private) | LanguageTool (Docker) |
| AI-powered search (private) | Perplexica + SearXNG |
| Personal AI assistant | Khoj |
| Academic research | Elicit or Semantic Scholar |
| Content production pipeline | n8n + Claude API |
| Configure AI coding agents | AGENTS.md (cross-tool standard) |

---

## ⚠️ Notes

- Star counts are approximate and change rapidly. Verified where possible via ossinsight.io and GitHub directly.
- Several projects underwent major changes in 2025-2026: Danswer → Onyx, Continue → acquired by Cursor, Aider → maintenance mode, Cody → repo archived.
- The "fair-code" model (n8n) means source-available but not fully OSS — check licenses before enterprise deployment.
- Flux.2 Klein variants (4B, 9B) are Apache 2.0; Flux.2 Dev is non-commercial license.
- LanguageTool Chrome extension went paid in March 2026; self-hosted server remains free.
