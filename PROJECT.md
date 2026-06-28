# Project: god-repo restructuring and June/July 2026 updates

## Architecture
- This is a documentation repository consisting of markdown (`.md`) files.
- The structure is hierarchical, grouped into folders: `developers`, `discover`, `everyone`, `learn`, `meta`, and `state-of-ai`.
- Integrity is defined as:
  1. Valid Markdown syntax (clean compilation/rendering).
  2. Fully resolved relative file links and page anchors.
  3. Content accuracy aligned with the state of AI in June/July 2026.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| 1 | Restructure Mismatched Content (R1) & AI Editors (R2) | Relocate all 8 mismatched sections identified by Explorer 1; clean up duplicate sections; write the new AI Editors & Extensions guide; resolve the missing `developers/cli-agents` directory. | none | IN_PROGRESS |
| 2 | June/July 2026 AI Landscape Updates (R3) | Update all repository guides to reflect OpenAI, Anthropic, Google, Cursor, and breakout repos for June/July 2026, including the 10 cutting-edge topics (Agent handoff/routing, LLM-as-a-judge, Structured outputs, Adversarial red-teaming, versioning registries, Tool use design, SLMs, Synthetic data, semantic cache, memory architectures). | M1 | PLANNED |
| 3 | Link & Markdown Verification (R4) | Verify Markdown formatting and check that all relative links resolve correctly using the offline verification scripts. | M2 | PLANNED |

## Code Layout
- `developers/` - Guides for developers (agents, MCP, local AI, vectors, editors, etc.)
- `discover/` - Lists of models, directories, open-source alternatives, comparisons
- `everyone/` - Consumer tools, mobile apps, profession-based guides, free tools
- `learn/` - High-level learning material, courses, research papers
- `meta/` - Hardware guide, news, cloud providers
- `state-of-ai/` - Market adoption statistics, model rankings, ARR stats
- `.agents/` - Coordination metadata files for subagents (not part of the repository content)

## Interface Contracts
Since this is a documentation repository, "interfaces" are defined by the relative links between documents:
- **Index Links**: Central index files (`README.md` and `developers/README.md`) must point to folders containing valid `README.md` files.
- **Header Anchor Links**: Any cross-reference must link to existing headers.
