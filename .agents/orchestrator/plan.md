# Plan: god-repo restructuring and June/July 2026 updates

## Objective
Restructure file contents to align with directory paths (R1), create a missing AI editors/extensions guide (R2), update content to reflect June/July 2026 state-of-the-art AI landscape (R3), and verify markdown/relative links integrity (R4).

## Phases of Execution

### Phase 1: Exploration and Planning
1. Spawn an Explorer subagent (`teamwork_preview_explorer`) to:
   - Identify location of mismatched files described in R1.
   - Inspect their content structure.
   - Look for existing lists of AI models/providers, state-of-ai, and mega-github-repos to identify target locations for R3.
   - Check if there are existing tests, build commands, lint setups, or link-check tools.
2. Based on the explorer's report, define the milestones in `PROJECT.md`.

### Phase 2: Restructuring and Creation (R1 & R2)
1. Spawn a Worker subagent (`teamwork_preview_worker`) to:
   - Move sections from `llm-gateways-routers/README.md` to `devops-cicd-ai-tools/README.md`.
   - Move sections from `ai-editors-ide-extensions/README.md` to `llm-gateways-routers/README.md`.
   - Move sections from `rag-vector-databases/README.md` to `starters-boilerplates/README.md`.
   - Move sections from `starters-boilerplates/README.md` to `discover/open-source-alternatives/README.md`.
   - Move hardware guides from `devops-cicd-ai-tools/README.md` to `meta/ai-hardware-guide/README.md`.
   - Move mobile apps guide from `devops-cicd-ai-tools/README.md` to `everyone/ai-mobile-apps/README.md`.
   - Move model comparisons from `devops-cicd-ai-tools/README.md` to `discover/model-comparisons-benchmarks/README.md`.
   - Move news resources from `devops-cicd-ai-tools/README.md` to `meta/ai-news-staying-updated/README.md`.
   - Create `developers/ai-editors-ide-extensions/README.md` as specified in R2.
2. Spawn Reviewer and Forensic Auditor subagents to review changes.

### Phase 3: Content Updates (R3)
1. Spawn a Worker subagent to update the relevant files (like `discover/ai-models-providers/README.md`, `state-of-ai/README.md`, `developers/mega-github-repos/README.md`) with:
   - OpenAI's GPT-5.6 (Sol, Terra, Luna) limited rollout and GPT-5.5.
   - Anthropic's Claude Fable 5 / Mythos 5, Claude Opus 4.8, and the deprecation of original Claude 4 Sonnet/Opus models.
   - Google's Gemini 3.5 Pro delay, Gemini 3.5 Flash / Omni.
   - Cursor's $4B ARR and acquisition by SpaceX under xAI.
   - Popularity of OpenClaw, Superpowers, ECC, hermes-agent, and token optimization tools (rtk, caveman, headroom).
2. Spawn Reviewer and Forensic Auditor subagents to review changes.

### Phase 4: Link and Formatting Verification (R4)
1. Spawn a Challenger/Worker to verify all relative links and Markdown files.
2. Ensure everything compiles/renders cleanly.
3. Run forensic audit and final verification.
