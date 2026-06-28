# 💻 AI Code Editors & IDE Extensions

> The ultimate reference guide for AI-native code editors and IDE extensions.

---

# 🧠 AI Tools God Repo — Exhaustive Research (2025–2026)

---

## 1. AI-NATIVE EDITORS & EXTENSIONS COMPARISON

| Editor / Extension | Primary Developer / Parent | Architecture Type | Key Agentic Capabilities | MCP Support | Config File / Folder | Pricing / Licensing | Key Strengths |
|---|---|---|---|---|---|---|---|
| **Cursor** | Anysphere (xAI / SpaceX) | VS Code Fork | Composer (multi-file editing), Cursor Tab (predictive completions) | Yes | `.cursorrules`, `.cursor/rules/` | Free tier, Pro ($20/mo), Business ($40/mo) | Leading VS Code fork; incredibly fast autocomplete; Composer for codebase-wide edits. |
| **Windsurf** | Codeium (Cognition / Devin Desktop) | VS Code Fork | Cascade Engine (autonomous or interactive execution loops) | Yes | `.windsurfrules` | Free tier, Premium ($20/mo), Teams | Deeply integrated system prompt; Cascade engine maintains real-time codebase state. |
| **Cline** | Open Source Community | VS Code Extension | File read/write, terminal execution, browser automation | Yes | Configured via extension UI / API keys | Open Source (Bring-Your-Own-API-Key) | Fully autonomous agentic loops; permissions-gated shell/file edits; highly customizable. |
| **GitHub Copilot** | GitHub (Microsoft) | IDE Extension | Inline completions, Copilot Chat, workspace context agents | Yes | `github-copilot.xml` / project rules | Usage-based billing (since 2026 backlash) | Pioneer autocomplete; deeply integrated in VS Code, JetBrains, Visual Studio, Xcode. |
| **Continue** | Open Source (Apache 2.0) | IDE Extension | Slash commands, custom context providers, custom autocomplete | Yes | `.continue/config.json` | Fully Free & Open Source | Highly customizable; allows routing to any local model (Ollama) or remote API. |
| **Zed** | Zed Industries | Rust-Native Editor | Assistant Panel, inline prompts, custom model configuration | Yes | `settings.json` | Free & Open Source | Blazing-fast performance (written in Rust); real-time team collaboration; native Ollama/API integration. |

---

## 2. DETAILED TOOL BREAKDOWN

### 🚀 Cursor
- **Overview:** The market leader in AI-native development. In mid-2026, Cursor reached **$4B ARR** and was acquired by **SpaceX under xAI**, aligning it directly with Grok models.
- **Architecture:** A direct fork of VS Code, allowing users to import all their VS Code extensions and settings seamlessly.
- **Key Features:**
  - **Composer (Cmd+I):** A multi-file edit interface that can write code across multiple files in parallel.
  - **Cursor Tab:** High-speed, predictive inline code completion.
  - **Rules for AI:** Uses `.cursorrules` and the `.cursor/rules/` directory to instruct the AI on coding patterns and project architecture.
- **URL:** https://cursor.com
- **GitHub Stars / Open-Weight:** N/A (Proprietary product, open source VS Code base)

### 🌊 Windsurf (Devin Desktop)
- **Overview:** Developed by Codeium, Windsurf was acquired by Cognition in 2026 for **$250M** and integrated with the Devin ecosystem (sometimes referred to as Devin Desktop).
- **Architecture:** VS Code fork featuring Codeium's proprietary AI backend.
- **Key Features:**
  - **Cascade:** The first agentic IDE assistant that can work in "Super-mode" (autonomous execution) or "Write-mode" (interactive editing).
  - **Deep Autocomplete:** Uses Codeium's proprietary local and cloud models for ultra-low latency completions.
- **URL:** https://codeium.com/windsurf

### 🤖 Cline (formerly Claude Dev)
- **Overview:** An open-source VS Code extension that turns the IDE into an autonomous developer agent.
- **Architecture:** Extension-based (works inside standard VS Code).
- **Key Features:**
  - **Agentic Power:** Cline can read/write files, create new projects, execute terminal commands (with user approval), and open a browser to test web applications.
  - **API Flexibility:** Supports Anthropic (Claude), OpenAI, OpenRouter, DeepSeek, Google AI Studio, and local backends (Ollama, LM Studio).
- **URL:** https://github.com/cline/cline
- **GitHub Stars:** ~45,000+ ★

### 🐈 GitHub Copilot
- **Overview:** The pioneer of AI code completions, owned by Microsoft. Following a transition to usage-based billing in 2026 (replacing flat-rate subscriptions due to high computing costs), GitHub Copilot remains the enterprise default.
- **Architecture:** Extension available for VS Code, JetBrains, Xcode, and Visual Studio.
- **Key Features:**
  - **Inline Autocomplete:** The gold standard for quick line completions.
  - **Copilot Chat:** Dedicated side panel with project-wide indexing and slash commands.
- **URL:** https://github.com/features/copilot

### 🔀 Continue
- **Overview:** A fully open-source (Apache 2.0) AI coding assistant designed for developer freedom and local-first configurations.
- **Architecture:** Extension for VS Code and JetBrains IDEs.
- **Key Features:**
  - **BYO-LLM (Bring Your Own LLM):** Custom config allows developers to use local Ollama models (like Qwen 3 or Llama 3.2) or cloud API keys.
  - **Context Providers:** Easily inject customized context (like specific folders, docs, database schemas) into the chat via the `@` symbol.
- **URL:** https://github.com/continuedev/continue
- **GitHub Stars:** ~25,000+ ★

### ⚡ Zed
- **Overview:** A high-performance, collaborative code editor written from scratch in Rust, designed for speed and simplicity.
- **Architecture:** Native, lightweight desktop editor (not a VS Code fork).
- **Key Features:**
  - **GPU Rendering:** Blazing-fast performance; uses the GPU to render text at high frame rates.
  - **Assistant Panel:** Native panel allowing direct interaction with models from Anthropic, OpenAI, or local Ollama instances.
  - **Slash Commands:** `/file`, `/workspace`, `/terminal` commands to inject context directly into the AI prompt.
- **URL:** https://github.com/zed-industries/zed
- **GitHub Stars:** ~50,000+ ★

---

## 3. CONFIGURATION TEMPLATES (CONTEST PARADIGM 2026)

In 2026, **Context Engineering** replaced prompt engineering as the developer standard. These configuration templates allow teams to control the behavior of AI code editors and agents in their codebases.

### 📄 Template A: `.cursorrules` (For Cursor)
Create this file in the root of your project to define coding guidelines, project structure, and file layouts.

```markdown
# Project Rules for Cursor AI

## Tech Stack
- Frontend: Next.js 16 (App Router), React 19, TypeScript
- Styling: Tailwind CSS v4
- Database: Prisma with PostgreSQL
- State Management: React Server Components & Zustand

## Coding Style
- Write clean, functional TypeScript code.
- Prefer server components over client components unless state/effects are required.
- Do not use class components.
- Use arrow functions for component definitions.
- Keep components small and focused. One component per file.

## AI Behavior
- Always search the workspace before creating new utilities or components.
- DO NOT rewrite entire files to make small changes. Only provide the modified diff or code blocks.
- When generating schema files, always run `npx prisma generate` after writing the file.
- Be concise. Skip conversational pleasantries.
```

### 📄 Template B: `AGENTS.md` (For Coding Agents like Cline, Devin, or AutoGPT)
Create this file to define task boundaries, permissions, and execution rules for autonomous agents.

```markdown
# Agent Instructions & Execution Boundary (AGENTS.md)

## Agent Role & Intent
You are an autonomous AI senior software engineer. Your goal is to inspect, test, and write code according to the issue description, ensuring all local tests pass before completing your task.

## Safety & Permission Boundaries
- **ReadOnly Directories:** Never modify contents in `.agents/`, `config/`, or `licenses/`.
- **Command Approvals:** You are permitted to run read-only shell commands (e.g. `npm test`, `git status`, `ls`) without manual confirmation. You MUST request approval for mutating commands (`rm`, `git push`, `docker-compose up`).
- **File Modifications:** You must only write to `src/` and `tests/` directories.

## Coding Rules
- Do not add dependencies without checking `package.json` first.
- Always run local tests (`npm run test`) after any edit to verify you did not introduce regressions.
- If a test fails, analyze the stack trace, correct the error, and re-run.

## Workspace Conventions
- Language: TypeScript ESM
- Linting: Prettier + ESLint
- Test framework: Vitest
```

### 📄 Template C: `CLAUDE.md` (For Anthropic Claude Code & General Coding Assistants)
Originally popularized by Andrej Karpathy for Claude Code, this file contains the project's layout, build commands, and testing configurations.

```markdown
# Claude Code Project Reference (CLAUDE.md)

## Project Overview
This repository is a TypeScript-based backend API service built with Fastify.

## Build and Run Commands
- Install dependencies: `npm install`
- Start dev server: `npm run dev`
- Build project: `npm run build`
- Production run: `npm start`

## Test Commands
- Run all tests: `npm test`
- Run single test: `npx vitest run tests/utils.test.ts`
- Run test coverage: `npm run coverage`

## Coding Guidelines
- **Type Safety:** Always declare strict TypeScript types. Avoid using `any`.
- **Error Handling:** Use Fastify's native error handling. Wrap async calls in try-catch blocks and log via `request.log`.
- **Imports:** Use absolute paths configured in `tsconfig.json` (e.g., `import { db } from '@/database'`).
- **Formatting:** Code must pass Prettier check. Run `npm run format` to fix styles.
```

---

*Last updated: June 2026. Sourced from developer surveys, product release notes, and community recommendations.*
