# Worker Instructions: Milestone 1 — Revision & Quality Enhancements

Your working directory is: C:\Users\svhon\.gemini\antigravity\scratch\god-repo\.agents\worker_milestone1_rev
Your task is to implement quality enhancements, fix table layouts, replace deprecated references, and add new sections/guidelines as requested by the Reviewer and the Parent Agent.

## Tasks

### 1. Fix Markdown Table Columns in `discover/open-source-alternatives/README.md`
- Locate the table starting at line 146:
  - Header has 3 columns (`Tool`, `Description`, `URL`), but ComfyUI, Fooocus, and Krea 2 rows have 4 columns (adding `Stars` as the third column).
  - Update the header and separator to include the `Stars` column: `| Tool | Description | Stars | URL |`
  - Update all other rows in this table to have the `Stars` column (use a dash `—` or estimated count if not specified).
- Locate the table starting at line 199:
  - Header has 3 columns (`Tool`, `Description`, `URL`), but Perplexica and SearXNG rows have 4 columns.
  - Update the header and separator to include `Stars`.
  - Update all other rows in this table to align with the new 4-column structure.

### 2. Update Deprecated Codex CLI in `developers/cli-agents/README.md`
- Remove the OpenAI Codex CLI agent reference (lines 25-29) because the Codex API was officially deprecated.
- Replace it with Roo Code (formerly Roo Cline), a highly popular terminal-native coding agent in 2026. Provide a detailed, professional description and configuration notes.

### 3. Replace TBD Placeholders in `meta/ai-hardware-guide/README.md`
- Locate the `TBD` placeholder values at line 47 and lines 130-138.
- Replace these placeholders with estimated specifications, actual/estimated pricing, or dashes `—` as appropriate to keep the guide professional and complete.

### 4. Production Prompt Templates & Context Recipes in `developers/prompt-engineering-observability/README.md`
- Add a new section titled "Production Prompt Templates & Context Recipes" to `developers/prompt-engineering-observability/README.md`.
- Include three concrete, copy-pasteable system prompts for developers:
  1. **Security & Vulnerability Audit Prompt**: A prompt to scan codebase changes for prompt injection, insecure dependencies, PII exposure, and memory leaks.
  2. **Context & Token Optimization Prompt**: A prompt instructing coding agents to reduce reasoning verbosity, compress command outputs, and use structured diffs to save 60-90% of tokens (citing rtk and headroom patterns).
  3. **App Verification & Zero-Error Testing Prompt**: A prompt to enforce that coding agents write unit tests, verify runtime dependencies, start the local server, check for console errors, and verify the app runs cleanly without breaking upon launch.
- Include a checklist of links to external repositories for security scanning:
  - `protectai/llm-guard`
  - `Confident-AI/deepeval`
  - `promptfoo/promptfoo`
  - `jujumilk3/system_prompts_leaks`

### 5. Incorporate Reviewer 2 Adversarial Challenge Mitigations
- **Model Choice Guidelines**: Add clear warnings in `developers/ai-editors-ide-extensions/README.md` and `developers/cli-agents/README.md` advising developers to only use high-capacity models (e.g., Qwen 2.5 Coder 32B, Llama 3.3 70B, Claude 3.5 Sonnet, or GPT-4o) for agentic write-mode loops to prevent infinite loops and codebase corruption, and restrict smaller models to autocomplete.
- **Tool-Agnostic Setup**: In the AI Editors and IDE Extensions guide, recommend structuring configurations (such as `.cursorrules` and `CLAUDE.md`) to be tool-agnostic, using standards like `AGENTS.md` and keeping rules generic, so developers can easily fallback to standard VS Code with Cline or Continue if custom editor forks diverge.
- **Single Source of Truth for Style**: In the configuration templates (`.cursorrules`, `CLAUDE.md`, etc.), advise developers to reference a single source of truth for style guidelines (such as an `.eslintrc` or a shared `STYLE.md` file) rather than duplicating formatting rules within each individual configuration file.

## Mandatory Rules
- Verify your changes carefully. All Markdown syntax must parse cleanly.
- Write your handoff report to `C:\Users\svhon\.gemini\antigravity\scratch\god-repo\.agents\worker_milestone1_rev\handoff.md`.
