# 🔌 MCP (Model Context Protocol) Ecosystem

> The open standard for connecting AI models to tools, data, and services.

---

# CATEGORY 6: MCP (Model Context Protocol) — Exhaustive Research

## Overview

The **Model Context Protocol (MCP)** is an open standard introduced by Anthropic in **November 2024** that standardizes how AI systems (LLMs) integrate with external tools, data sources, and systems. Uses JSON-RPC 2.0, client-host-server architecture inspired by LSP. Donated to the **Agentic AI Foundation** (Linux Foundation) in December 2025. Co-founders: Anthropic, Block, OpenAI. Platinum members: AWS, Google, Microsoft, Cloudflare, Bloomberg.

**Ecosystem scale (mid-2026):** 19,630+ servers tracked (PulseMCP); 600+ MCP clients; adopted by OpenAI, Google, Microsoft, AWS, Cloudflare, and virtually every major AI tool.

---

## 1. OFFICIAL — modelcontextprotocol GitHub Org (48.4k followers, 42 repos)

### Official MCP SDKs

| SDK | Repository | Stars | Tier |
|-----|-----------|-------|------|
| **TypeScript** | modelcontextprotocol/typescript-sdk | ⭐ 12,742 | Tier 1 |
| **Python** | modelcontextprotocol/python-sdk | ⭐ 23,470 | Tier 1 |
| **C#** | modelcontextprotocol/csharp-sdk | ⭐ 4,400 | Tier 1 (w/ Microsoft) |
| **Go** | modelcontextprotocol/go-sdk | — | Tier 1 |
| **Java** | modelcontextprotocol/java-sdk | — | Tier 2 (w/ Spring AI) |
| **Rust** | modelcontextprotocol/rust-sdk | ⭐ 3,570 | Tier 2 |
| **Swift** | modelcontextprotocol/swift-sdk | — | Tier 3 |
| **Ruby** | modelcontextprotocol/ruby-sdk | — | Tier 3 |
| **PHP** | modelcontextprotocol/php-sdk | — | Tier 3 |
| **Kotlin** | modelcontextprotocol/kotlin-sdk | — | Tier 3 (w/ JetBrains) |

### MCP Inspector — ⭐ 10,210
- Visual testing/debugging tool for MCP servers — https://github.com/modelcontextprotocol/inspector

### Reference Servers (modelcontextprotocol/servers) — ⭐ 87,800
**Active:** Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time
**Archived:** AWS KB Retrieval, Brave Search, EverArt, GitHub, GitLab, Google Drive, Google Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack (now Zencoder), SQLite

### modelcontextprotocol.io Docs
Sections: What is MCP?, Architecture, SDKs, Build a Server, Connect to Local/Remote Servers, Agent Skills, Clients, Security, Inspector, Debugging, Examples, Specification (versions 2025-03-26, 2025-06-18, 2025-11-25), Registry, SEPs, Extensions, Community

### MCP Clients
Claude Desktop, Claude Code, ChatGPT Desktop/Apps, Cursor, Windsurf, VS Code + GitHub Copilot, Cline, Zed, Goose, Google Antigravity, Amazon Q Developer, Kiro, Gemini, Continue, Sourcegraph Cody, Replit, Nimbalyst, 5ire, BoltAI, MCP-Bridge, and 600+ more (PulseMCP tracks them)

---

## 2. COMMUNITY SERVERS — By Category

### Dev Tools
- **GitHub MCP Server** (Official GitHub) — https://github.com/github/github-mcp-server
- **GitLab MCP Server** (Official GitLab) — https://docs.gitlab.com/...mcp_server/
- **Filesystem** (Reference) — modelcontextprotocol/servers
- **mcp-filesystem-server** (Go) — https://github.com/mark3labs/mcp-filesystem-server
- **Terminal Controller MCP** — https://github.com/GongRzhe/terminal-controller-mcp
- **Docker MCP** — via docker.com/blog
- **Cursor MCP Servers** — https://github.com/cursor/mcp-servers

### Databases
- **Postgres MCP Pro** — ⭐ ~2,300, industrial-strength index tuning
- **MongoDB MCP** (Official) — 40+ tools
- **mcp-alchemy** — Multi-DB (SQLite, PG, MySQL, MariaDB, Oracle, MS-SQL) — https://github.com/runekaagaard/mcp-alchemy
- **mcp-database-server** — SQLite, SQL Server, PostgreSQL — https://github.com/executeautomation/mcp-database-server
- **Supabase MCP**, DuckDB, BigQuery, ClickHouse, Neon, PlanetScale [?]

### Productivity
- **Notion MCP** (Official) — https://github.com/makenotion/notion-mcp-server
- **Linear MCP** — https://github.com/jerhadf/linear-mcp-server
- **Trello MCP** — https://github.com/delorenj/mcp-server-trello
- **Todoist MCP** — https://github.com/koki-develop/todoist-mcp-server
- **Todoist AI** (Official Doist) — https://github.com/mcp/doist/todoist-ai
- **mcp-ticketer** (Linear, GitHub, Jira, Asana) — https://github.com/bobmatnyc/mcp-ticketer

### Communication
- **Google Workspace MCP** (Official Google) — Gmail, Drive, Calendar — https://developers.google.com/workspace/guides/configure-mcp-servers
- **Gmail MCP** (Official Google) — https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server
- **Gmail MCP** (Community) — https://github.com/GongRzhe/Gmail-MCP-Server
- **Microsoft MCP** (Official) — Outlook, etc. — https://github.com/microsoft/mcp
- Discord, Telegram, Twilio [?]

### Search & Browser
- **Brave Search** (Official, replaced reference)
- **Firecrawl MCP** — https://docs.firecrawl.dev/mcp
- **Playwright MCP** (Microsoft, launched 2025)
- **mcp-playwright** — https://github.com/executeautomation/mcp-playwright
- **Puppeteer** (Reference, archived)
- **Cloudflare Browser Rendering MCP** — https://developers.cloudflare.com/browser-rendering/platform/playwright-mcp/
- Tavily, Exa, SearXNG, Perplexity [?]

### Cloud & Infrastructure
- **AWS MCP Servers** (66+ official) — https://github.com/awslabs/mcp — includes S3, Lambda, CDK, CFN, Bedrock, HealthOmics, MSK, Support, API, Documentation
- **Google Cloud MCP** (Official) — managed MCP for GCP
- **Google Maps MCP** (Official) — https://developers.google.com/maps/ai/grounding-lite/reference/mcp
- **Microsoft/Azure MCP** — https://github.com/microsoft/mcp
- **Cloudflare MCP** — Workers, KV, R2, D1
- Railway, Vercel, Terraform, Kubernetes, Netlify [?]

### AI & ML
- **Hugging Face MCP** — via HF Context Course
- Replicate, Together AI, Ollama, LangChain MCP Adapters [?]

### Finance
- **Stripe MCP** (Official) — remote at mcp.stripe.com — https://github.com/mcp/com.stripe/mcp
- Plaid, QuickBooks, Coinbase [?]

### Media
- **mcp-youtube** — https://github.com/anaisbetts/mcp-youtube
- **Spotify MCP** — https://github.com/varunneal/spotify-mcp
- 129+ YouTube MCP servers on PulseMCP

### Monitoring & Observability
- **Datadog MCP** (Official) — https://docs.datadoghq.com/mcp_server/
- **Grafana MCP** (Official) — https://grafana.com/docs/grafana/latest/developer-resources/mcp/
- **Sentry** — MCP monitoring instrumentation — https://blog.sentry.io/introducing-mcp-server-monitoring/
- PagerDuty, New Relic, Prometheus (via Grafana) [?]

### Maps & Location
- **Google Maps MCP** (Official) — mapstools.googleapis.com/mcp
- **mcp-google-map** (Community) — https://github.com/cablate/mcp-google-map

---

## 3. CATALOGS AND REGISTRIES

| Registry | Description | URL | Scale |
|----------|-------------|-----|-------|
| **Official MCP Registry** | Canonical registry (Anthropic, GitHub, PulseMCP, Microsoft) | https://registry.modelcontextprotocol.io/ | ~2,000 |
| **GitHub MCP Org** | GitHub-hosted registry namespace | https://github.com/mcp | — |
| **punkpeye/awesome-mcp-servers** | Largest community-curated list, web dir at Glama | https://github.com/punkpeye/awesome-mcp-servers | ⭐ ~35k+ |
| **Smithery.ai** | Marketplace with deploy/install/manage | https://smithery.ai/servers | ~7,300 |
| **mcp.so** | Popular discovery platform | https://mcp.so | Large |
| **PulseMCP** | Largest tracker (updated daily) | https://www.pulsemcp.com/servers | 19,630+ |
| **Glama** | Web directory (punkpeye backend) | https://glama.ai/mcp/servers | — |
| **wong2/awesome-mcp-servers** | Curated list | https://github.com/wong2/awesome-mcp-servers | — |
| **TensorBlock/awesome-mcp-servers** | Comprehensive collection | https://github.com/TensorBlock/awesome-mcp-servers | — |
| **mcparmory/registry** | Production-ready for 64+ APIs | https://github.com/mcparmory/registry | — |
| **mcpservers.org** | Discovery site | https://mcpservers.org | — |
| **MACH Alliance Registry** | Enterprise MCP directory | https://machalliance.org/mach-alliance-mcp-registry | — |

Items marked [?] are referenced in secondary sources but primary URL/star count not directly verified.

# 🏆 AI Tools God Repo — Exhaustive Reference (June 2026)

---

## 1. AI DEVOPS & CI/CD

### 🔍 AI PR Review Tools

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **CodeRabbit** | AI-native code review platform; leads GitHub with 180K reviews/30 days. Atlas interface for complex PRs. $40M ARR. | https://coderabbit.ai | SaaS (archived OSS: `coderabbitai/ai-pr-reviewer`) |
| 2 | **Qodo PR-Agent** | Open-source LLM-powered PR reviewer — auto-descriptions, code suggestions, Q&A on diffs. Supports GitHub/GitLab/Bitbucket. | https://github.com/qodo-ai/pr-agent | ⭐ 11.9k |
| 3 | **Ellipsis** | AI teammate that reviews PRs for logical errors, anti-patterns, security issues, and documentation drift. No source code persistence. | https://ellipsis.dev | SaaS (closed-source) |
| 4 | **Bito AI** | AI code review agent using full system context — code, commits, issues, docs, Slack. IDE + Git workflow. | https://bito.ai | GitHub: `gitbito/bitoai` [?] |
| 5 | **Codacy AI** | Plug-and-play DevSecOps; 40+ language support. AI Reviewer auto-enabled March 2026. GitHub/GitLab/Bitbucket. | https://codacy.com | SaaS (GitHub Marketplace) |
| 6 | **Sourcery** | AI-powered refactoring + code review; focuses on code quality improvements and style consistency. | https://sourcery.ai | SaaS + IDE plugins |
| 7 | **Greptile** | Agentic AI code review v3 (June 2026) — full codebase awareness, 256% improvement over v2. | https://greptile.com | SaaS |
| 8 | **GitHub Copilot Code Review** | Native GitHub code review (launched April 2025); reached parity with CodeRabbit within months. | https://github.com/features/copilot | Part of Copilot |
| 9 | **Amazon Q Developer** | AWS's AI code reviewer + IDE assistant — reviews PRs, generates code, security scanning. | https://aws.amazon.com/q/developer/ | SaaS |
| 10 | **CodeAnt AI** | AI code review focusing on reducing false positives. | https://codeant.ai | SaaS [?] |

---

### 🧪 AI Test Generation

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **Qodo Cover** (formerly CodiumAI Cover Agent) | AI-powered automated test generation and code coverage enhancement. LLM-prompting approach. | https://github.com/qodo-ai/qodo-cover | ⭐ 5.5k |
| 2 | **Diffblue Cover** | Reinforcement-learning-based Java unit test generator. Enterprise-focused, CI/CD integration. | https://diffblue.com | Commercial (GitHub Marketplace) |
| 3 | **Qodo (IDE)** | AI testing assistant in VS Code/JetBrains — analyzes code behavior, generates comprehensive unit tests. | https://qodo.ai | SaaS + IDE |
| 4 | **GitHub Copilot (test gen)** | `/tests` slash command generates unit tests from code context. | https://github.com/features/copilot | Part of Copilot |
| 5 | **CodiumAI** (now Qodo) | Originally standalone; merged into Qodo brand. Pioneered AI test generation in IDE (2022). | https://codium.ai | → Qodo |
| 6 | **Early (YC)** | AI agent that finds & fixes bugs before code ships; generates regression tests. | https://early.ai | SaaS [?] |
| 7 | **Codegen (Maige)** | AI test generation for React/TypeScript components. | https://codegen.com | SaaS [?] |

---

### 💬 AI Commit Message Generators

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **OpenCommit** | Most feature-rich GPT wrapper for git — generate messages with any LLM in 1 sec. Supports Ollama local models. Also GitHub Action. | https://github.com/di-sukharev/opencommit | ⭐ 7.3k |
| 2 | **AICommits** | CLI that writes git commit messages with AI. Clean, minimal. By Nutlope (Hassan El Mghari). | https://github.com/Nutlope/aicommits | ⭐ 9k |
| 3 | **ai-commit** | ✨ Make commits easier with ChatGPT, Gitmoji and Conventional Commits. | https://github.com/insulineru/ai-commit | ⭐ ~400 [?] |
| 4 | **claude-commit** | AI-powered git commit message generator using Claude Agent SDK and Claude Code CLI. | https://github.com/JohannLai/claude-commit | ⭐ ~200 [?] |
| 5 | **commitai** | CLI tool analyzing diffs to craft semantic commit messages. Multiple AI providers, custom templates, pre-commit hooks. | https://github.com/lguibr/commitai | ⭐ ~100 [?] |
| 6 | **smart-commit** | Generate clean, consistent git commit messages using AI. Preview before commit, issue key extraction. | https://github.com/vicc/smart-commit | ⭐ ~50 [?] |
| 7 | **GitHub Copilot (commit msg)** | Built-in commit message suggestion in VS Code and CLI via Copilot. | Built into Copilot | N/A |

---

### 📝 AI Changelog Generators

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **git-cliff** | Highly customizable changelog generator following Conventional Commits. Regex-powered parsers, Rust-based. | https://github.com/orhun/git-cliff | ⭐ 12k |
| 2 | **CommitFlow** | Watches GitHub repos, uses AI to turn raw commits into user-friendly release notes, publishes to customizable changelog page. | https://commitflow.org | SaaS [?] |
| 3 | **ReleasePad** | Generates release notes from GitHub commits with AI — review a draft instead of writing from scratch. | https://releasepad.io | SaaS |
| 4 | **OpenChangelog** | AI-powered platform that auto-generates categorized changelogs for GitHub/GitLab projects. | https://openchangelog.io | SaaS [?] |
| 5 | **AI Changelog Generator (entro314)** | AI-powered changelog generator with MCP server support. | https://github.com/entro314-labs/AI-Changelog-Generator | ⭐ ~50 [?] |
| 6 | **ai-release-notes-generator** | GitHub Action that reads merged PRs and auto-generates release notes via Claude AI — posts to Slack, Notion, or GitHub Releases. | https://github.com/christiancaviedes/ai-release-notes-generator | ⭐ ~30 [?] |
| 7 | **github-changelog-ai-generator** | OpenClaw MCP-based AI changelog tool. | https://github.com/openclaw-mcp-vps/github-changelog-ai-generator | ⭐ ~20 [?] |

---

### 📚 AI Documentation Generators

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **Mintlify** | AI-native docs platform — docs-as-code, API reference generation, AI chat, MCP support. Used by 1000+ companies. | https://mintlify.com | SaaS (GitHub: `mintlify/docs`) |
| 2 | **ReadMe AI** | CLI tool that auto-generates README files from any codebase URL/path using LLMs. | https://github.com/eli64s/readme-ai | ⭐ 2.9k |
| 3 | **Swimm AI** | AI coding assistant + continuous documentation. Auto-detects doc drift on PRs, generates docs from code snippets. | https://swimm.io | SaaS (GitHub App) |
| 4 | **GitBook (AI-native)** | AI-native documentation platform with SOC2+ISO27001. Covers product/dev/internal docs. | https://gitbook.com | SaaS |
| 5 | **ReadMe** | Polished API reference with visual editor. GitHub AI Writer watches PRs and proposes doc updates. | https://readme.com | SaaS |
| 6 | **Docusaurus + AI plugins** | React-based static site generator (Meta) — community AI plugins for auto-generation. | https://docusaurus.io | ⭐ 60k+ |
| 7 | **Document360** | AI-powered knowledge base with writing assistant. | https://document360.com | SaaS |
| 8 | **Moxie Docs** | Living docs tied to PR workflows for GitHub teams. | https://moxiedocs.com [?] | SaaS [?] |
| 9 | **Notion AI (docs)** | AI-assisted documentation within Notion workspace. | https://notion.so | SaaS |
| 10 | **Scribe** | Auto-generates step-by-step documentation from screen recordings. | https://scribehow.com | SaaS |

---

### 🤖 AI Code Review Bots for GitHub (Summary)

| Bot | Integration | Key Differentiator |
|-----|-------------|-------------------|
| CodeRabbit | GitHub App | Highest volume reviewer on GitHub (180K reviews/mo) |
| Qodo PR-Agent | GitHub Action / App | Open-source, self-hostable |
| GitHub Copilot | Native GitHub | First-party, tightly integrated |
| Greptile | GitHub App | Full codebase-aware, agentic |
| Codacy | GitHub App | DevSecOps + quality gates |
| Bito AI | GitHub App | Full system context (Slack, docs, issues) |
| Ellipsis | GitHub App | Bug fixes + review in one |
| Amazon Q | GitHub App | AWS ecosystem integration |
| Sourcery | GitHub App | Refactoring-focused |

---

## 2. AI TERMINAL TOOLS

### 🖥️ AI-Native Terminals

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **Warp** | Rust-based agentic development environment born from the terminal. Built-in AI agents write code, debug, automate from natural language. | https://warp.dev | ⭐ 62.5k |

---

### ⌨️ AI CLI / Shell Tools

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **ShellGPT (shell-gpt)** | Command-line productivity tool powered by LLMs. Generates shell commands, code snippets, documentation. All major shells. | https://github.com/TheR1D/shell_gpt | ⭐ 12.1k |
| 2 | **AIChat** | All-in-one LLM CLI — Shell Assistant, Chat-REPL, RAG, AI Tools & Agents. OpenAI/Claude/Gemini/Ollama/Groq+. Rust-based. | https://github.com/sigoden/aichat | ⭐ 10.2k |
| 3 | **ai-shell** | CLI that converts natural language to shell commands. Open-source Copilot CLI alternative. By Builder.io. | https://github.com/BuilderIO/ai-shell | ⭐ 5.3k |
| 4 | **tgpt** | AI chatbots in terminal without needing API keys. Go-based, multiple free providers. | https://github.com/aandrew-me/tgpt | ⭐ 3.2k |
| 5 | **GitHub Copilot CLI** | AI-powered agent in your terminal — reviews code, generates tests, debugs, deploys. Full agentic execution. | https://docs.github.com/copilot/concepts/agents/about-copilot-cli | Part of Copilot |
| 6 | **Amazon Q Developer CLI** | AWS's AI terminal agent (successor to Fig/CodeWhisperer CLI). Autocomplete + natural language commands. | https://aws.amazon.com/q/developer/ | SaaS |
| 7 | **OpenAI Codex CLI** | Terminal-based AI coding agent by OpenAI. GPT-5.5 powered. | https://github.com/openai/codex | ⭐ ~40k [?] |
| 8 | **Claude Code** | Anthropic's CLI agent — terminal-native, edits files, runs tests, shows diffs. Opus 4.7 model. | https://claude.ai/code | Commercial |
| 9 | **Gemini CLI** | Google's CLI agent (105K stars pre-retirement June 2026; replaced by Antigravity CLI). | https://github.com/google-gemini/gemini-cli (deprecated) | ⭐ 105k (archived) |
| 10 | **OpenCode** | Open-source CLI coding agent. 168K stars, de facto OSS standard in 2026. | https://github.com/opencode-ai/opencode [?] | ⭐ 168k [?] |
| 11 | **chatGPT-shell-cli** | Simple shell script to use OpenAI from terminal. No Python/JS required. | https://github.com/0xacx/chatGPT-shell-cli | ⭐ ~1.2k [?] |

---

### 🐚 AI Shell History & Autocomplete

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **Atuin** | Magical shell history — replaces shell history with SQLite DB, encrypted sync, AI-powered search. Rust-based. | https://github.com/atuinsh/atuin | ⭐ 30.4k |
| 2 | **Fig** (now Amazon Q CLI) | Terminal autocomplete + AI suggestions. Acquired by AWS, merged into Amazon Q Developer. | (discontinued as standalone) | Legacy |

---

## 3. AI SECURITY & PRIVACY

### 🔒 AI Firewalls & Guardrails

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **LLM Guard** (Protect AI) | Open-source security toolkit for LLM interactions — scans inputs/outputs for prompt injection, PII, toxicity, jailbreaks. | https://github.com/protectai/llm-guard | ⭐ 3.1k |
| 2 | **NeMo Guardrails** (NVIDIA) | Open-source toolkit for adding programmable guardrails to LLM-based conversational systems. Dialog management built in. | https://github.com/NVIDIA/NeMo-Guardrails | ⭐ 6.6k |
| 3 | **Lakera Guard** (now Check Point) | AI security API protecting against prompt injection, jailbreaks, and data leakage in real time. Acquired by Check Point early 2026. | https://lakera.ai | SaaS (commercial) |
| 4 | **Rebuff** (Protect AI) | LLM Prompt Injection Detector — multi-layer defense with heuristics, LLM analysis, and vector DB. | https://github.com/protectai/rebuff | ⭐ ~1.5k (archived May 2025) |
| 5 | **NVIDIA Garak** | LLM vulnerability scanner — probes for hallucination, data leakage, prompt injection, toxicity, jailbreaks, and more. | https://github.com/NVIDIA/garak | ⭐ 8.2k |
| 6 | **Prediction Guard** | Enterprise LLM gateway with built-in PII detection, toxicity filtering, factual checks. Self-hosted option. | https://predictionguard.com | SaaS + self-hosted |
| 7 | **Vigil** | Open-source prompt injection detection library. Lightweight scanner. | https://github.com/deadbits/vigil-llm [?] | ⭐ ~600 [?] |
| 8 | **SecuPrompt** | Protect AI from prompt injection — open-source detection. | https://github.com/CaviraOSS/SecuPrompt | ⭐ ~100 [?] |
| 9 | **prompt-guard** | Advanced prompt injection defense — multi-language detection, severity scoring, security auditing. | https://github.com/seojoonkim/prompt-guard | ⭐ ~50 [?] |

---

### 🕵️ Prompt Injection Detection Tools

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **LLM Guard** | (See above) — dedicated `PromptInjection` scanner module. | https://github.com/protectai/llm-guard | ⭐ 3.1k |
| 2 | **NVIDIA Garak** | (See above) — prompt injection is one of its core probe categories. | https://github.com/NVIDIA/garak | ⭐ 8.2k |
| 3 | **Lakera Guard** | Real-time prompt attack detection with <2ms latency. | https://lakera.ai | SaaS |
| 4 | **Open-Prompt-Injection** | Academic benchmark for prompt injection attacks and defenses. | https://github.com/liu00222/Open-Prompt-Injection | ⭐ ~500 [?] |
| 5 | **awesome-prompt-injection** | Curated list of prompt injection research, tools, and resources. | https://github.com/FonduAI/awesome-prompt-injection | ⭐ ~500 [?] |
| 6 | **Microsoft PyRIT** | Python Risk Identification Toolkit for generative AI — red-teaming tool by Microsoft. | https://github.com/Azure/PyRIT [?] | ⭐ ~2k [?] |
| 7 | **CrowdStrike Falcon AIDR** | Enterprise AI detection and response for LLM threats. | https://crowdstrike.com | Commercial |

---

### 🔐 Data Anonymization for LLMs

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **Microsoft Presidio** | Open-source framework for detecting, redacting, masking, and anonymizing PII across text, images, structured data. NLP + pattern matching. | https://github.com/microsoft/presidio | ⭐ 9.7k |
| 2 | **LLM Guard (PII Scanner)** | Built-in PII detection/anonymization module for LLM input/output pipelines. | https://github.com/protectai/llm-guard | ⭐ 3.1k |
| 3 | **Stanza NER + custom pipeline** | Stanford NLP entity recognition for building custom PII redaction pipelines. | https://github.com/stanfordnlp/stanza | ⭐ ~7k [?] |
| 4 | **spaCy + presidio** | Common pattern: spaCy NER models feed into Presidio anonymization engine. | https://spacy.io | ⭐ ~30k [?] |
| 5 | **LiteLLM Proxy (PII masking)** | LiteLLM proxy with Presidio integration — masks PII before sending to LLM, unmasks on response. | https://github.com/BerriAI/litellm | ⭐ ~15k [?] |
| 6 | **Private AI** | Commercial PII redaction API with 50+ entity types. On-prem deployment available. | https://private-ai.com | Commercial |
| 7 | **Gretel.ai** | Synthetic data + anonymization platform. Transforms sensitive datasets for safe LLM training. | https://gretel.ai | SaaS |
| 8 | **Truto PII Gateway** | Zero-data-retention gateway for redacting PII before LLM calls via MCP. | https://truto.one | SaaS [?] |

---

### 🏠 Private/Local LLM Deployment

| # | Name | Description | URL | ⭐ Stars |
|---|------|-------------|-----|----------|
| 1 | **Ollama** | Get up and running with local LLMs instantly. CLI + API, auto GPU detection, massive model library. The de facto standard. | https://github.com/ollama/ollama | ⭐ 175k |
| 2 | **llama.cpp** | LLM inference in C/C++ — the engine underneath Ollama and most local LLM tools. GGUF format. | https://github.com/ggml-org/llama.cpp | ⭐ 118k |
| 3 | **Open WebUI** | Self-hosted ChatGPT-style interface for Ollama/OpenAI APIs. 136K+ stars, 282M Docker downloads. | https://github.com/open-webui/open-webui | ⭐ 115k+ |
| 4 | **GPT4All** | Run local LLMs on any device — desktop app by Nomic AI. Open-source, commercial-use OK. | https://github.com/nomic-ai/gpt4all | ⭐ 77.4k |
| 5 | **LocalAI** | Free, open-source OpenAI alternative. Self-hosted drop-in replacement. No GPU required. Text/audio/video/images. | https://github.com/mudler/LocalAI | ⭐ 47.2k |
| 6 | **LM Studio** | Desktop app for running LLMs locally on Apple Silicon/integrated GPUs. Friendly GUI. | https://lmstudio.ai | Closed-source (free) |
| 7 | **Jan** | Open-source ChatGPT alternative that runs 100% offline. Privacy-first. | https://jan.ai | ⭐ ~25k [?] |
| 8 | **vLLM** | Production-grade LLM serving with high throughput (85+ tok/s). PagedAttention. | https://github.com/vllm-project/vllm | ⭐ ~35k [?] |
| 9 | **AnythingLLM** | All-in-one AI desktop app — chat with documents using any LLM, RAG built-in. | https://anythingllm.com | ⭐ ~30k [?] |
| 10 | **Text Generation Inference (TGI)** | Hugging Face's production LLM serving with observability. | https://github.com/huggingface/text-generation-inference | ⭐ ~10k [?] |
| 11 | **Docker Model Runner** | Containerized local LLM deployment for DevOps workflows. | https://docs.docker.com/model-runner/ [?] | Built into Docker |
| 12 | **LobeChat** | Multi-agent collaboration workspace with local LLM support. | https://github.com/lobehub/lobe-chat | ⭐ ~50k [?] |
| 13 | **LibreChat** | Self-hosted multi-model chat interface — OpenAI, Anthropic, local models. | https://github.com/danny-avila/LibreChat | ⭐ ~20k [?] |

---

### 🏗️ Self-Hosted Alternatives to Cloud AI

| Category | Self-Hosted Alternative | Replaces |
|----------|------------------------|----------|
| Chat UI | Open WebUI, LibreChat, LobeChat | ChatGPT, Claude.ai |
| LLM Engine | Ollama, LocalAI, vLLM | OpenAI API, Anthropic API |
| Code Assistant | Continue.dev, Tabby | GitHub Copilot |
| Search | SearXNG + local LLM | Perplexity |
| Image Gen | Stable Diffusion WebUI | DALL-E, Midjourney |
| Embeddings | sentence-transformers locally | OpenAI Embeddings |
| RAG | AnythingLLM, PrivateGPT | Cloud RAG services |
| Voice | Whisper.cpp (local) | Cloud transcription |

---

## 📊 Star Counts Summary (Verified June 2026)

| Tool | Stars |
|------|-------|
| Ollama | 175k |
| llama.cpp | 118k |
| Open WebUI | 115k+ |
| GPT4All | 77.4k |
| Warp | 62.5k |
| LocalAI | 47.2k |
| Atuin | 30.4k |
| ShellGPT | 12.1k |
| git-cliff | 12k |
| PR-Agent | 11.9k |
| AIChat | 10.2k |
| Microsoft Presidio | 9.7k |
| AICommits | 9k |
| NVIDIA Garak | 8.2k |
| OpenCommit | 7.3k |
| NeMo Guardrails | 6.6k |
| Qodo Cover | 5.5k |
| ai-shell | 5.3k |
| tgpt | 3.2k |
| LLM Guard | 3.1k |
| ReadMe AI | 2.9k |

---

> **Legend:**
> - [?] = Star count unverified or approximate (based on indirect sources)
> - "SaaS" = Closed-source commercial product without a public star-able repo
> - Stars accurate as of web scraping June 28, 2026
