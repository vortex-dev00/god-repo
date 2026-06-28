# 💻 CLI Coding Agents

> Terminal-native AI agents that execute commands, edit files, and build software from your console.

---

# 🏆 AI Tools God Repo — Exhaustive Reference (June 2026)

---

## 1. OVERVIEW

Command-line (CLI) coding agents represent the next evolution of developer tools. Instead of acting as extensions inside an editor, these agents run directly in your terminal, interacting with your shell, file system, git repository, and compiler. By executing test suite runs, reading compiler errors, and fixing code iteratively, CLI agents achieve higher success rates on complex software tasks compared to static code completion tools.

---

## 2. POPULAR CLI CODING AGENTS

### 🚀 Claude Code
- **Developer:** Anthropic
- **Description:** A terminal-native coding agent powered by Anthropic's state-of-the-art models (including Claude 3.5/3.7/4.7). It can run tests, edit source files, explain codebases, and manage git status.
- **Key Feature:** Deep integration with Anthropic's agentic loop system and strict type checking systems.
- **URL:** https://docs.anthropic.com/en/docs/claude-code

### 🦘 Roo Code (formerly Roo Cline)
- **Developer:** Open Source Community
- **Description:** A highly popular terminal-native and editor-integrated coding agent in 2026. It is designed to run locally or connect to remote APIs to perform complex coding operations, read and write files, and execute terminal commands.
- **Key Feature:** Advanced context-aware editing, interactive shell tool support, and tight integration with VS Code/Cursor while remaining functional as a standalone agent.
- **Configuration Notes:** Best configured with specific system instructions in `.roo-rules`. Requires explicit user approval for tool operations (run commands, file edits) to prevent runaway processes.
- **URL:** https://github.com/RooVetGit/Roo-Code

### ⚡ Gemini CLI
- **Developer:** Google AI
- **Description:** A lightweight, customizable CLI tool that wraps Gemini models to perform code transformations, documentation updates, and shell-based problem solving.
- **Key Feature:** Large context window capability allowing direct ingestion of entire directories.
- **URL:** https://github.com/google-gemini/gemini-cli

### 🤝 Aider
- **Developer:** Open Source Community
- **Description:** One of the earliest and most widely adopted command-line AI pair programming tools. Aider allows you to chat with a local or remote model to edit code, write tests, and automatically generate git commit messages.
- **Key Feature:** Automatic git commit generation with detailed descriptions of changes made by the AI.
- **URL:** https://github.com/Aider-AI/aider

---

## 3. MODEL CHOICE GUIDELINES & WARNINGS

> ⚠️ **CRITICAL WARNING FOR WRITE-MODE LOOPS**
>
> When using CLI coding agents in autonomous write-mode loops, developers **must only use high-capacity models** (such as **Claude 3.5 Sonnet**, **GPT-4o**, **Qwen 2.5 Coder 32B**, or **Llama 3.3 70B**). 
> 
> Using lower-capacity or smaller models in write-mode loops frequently leads to:
> - **Infinite loops**: The agent gets stuck executing the same failing commands or rewrite cycles.
> - **Codebase corruption**: The agent makes improper modifications, deletes critical files, or produces syntactically invalid code.
> 
> Restrict smaller/low-capacity models strictly to simple autocomplete tasks or local search assistance, rather than giving them write access or terminal execution capabilities.

---

*Last updated: June 2026. Sourced from developer surveys and open-source repository data.*

