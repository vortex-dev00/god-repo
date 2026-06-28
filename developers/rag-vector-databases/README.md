# 🗄️ RAG & Vector Databases

> Retrieval Augmented Generation tools and vector storage solutions.

---

# CATEGORY 10: RAG & VECTOR DATABASES

## Vector Databases

### Tier 1 — Market Leaders

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **Milvus** | High-performance, cloud-native vector database built for scalable ANN search. Oldest purpose-built vector DB (2019). Used by NVIDIA, Salesforce, eBay, Airbnb, DoorDash. | ~40,000+ ⭐ | https://github.com/milvus-io/milvus |
| **Qdrant** | High-performance vector search engine written in Rust. Sub-10ms p95 latency, built-in quantization, horizontal scaling beyond 50M vectors. | ~22,000+ ⭐ [?] | https://github.com/qdrant/qdrant |
| **Weaviate** | Open-source vector database with objects + vectors storage, combining vector search with structured filtering. GraphQL/REST APIs. Native hybrid search + multi-tenancy. | ~14,000+ ⭐ [?] | https://github.com/weaviate/weaviate |
| **Pinecone** | Fully managed, serverless vector database. Zero-ops, scales automatically. Free tier (2GB), Standard $50/mo minimum. Best for teams wanting no infrastructure management. | Proprietary (closed-source) | https://www.pinecone.io/ |
| **Chroma** | Open-source AI-native embedding database. Serverless + scalable. Used in 90,000+ open-source codebases, 15M+ monthly downloads. Apache 2.0 license. | ~27,900+ ⭐ | https://github.com/chroma-core/chroma |
| **pgvector** | Open-source vector similarity search extension for PostgreSQL. Best when you already have Postgres and need ACID-compliant vector search up to ~10M vectors. | ~13,000+ ⭐ [?] | https://github.com/pgvector/pgvector |

### Tier 2 — Strong Contenders

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **LanceDB** | Developer-friendly embedded retrieval library for multimodal AI. Written in Rust, built on Lance columnar format. Serverless, no server management needed. | ~5,000+ ⭐ [?] | https://github.com/lancedb/lancedb |
| **Vespa** | AI search platform from Yahoo. Combines big data, vector search, ML-ranking, and real-time inference. Production-grade at massive scale. | ~6,000+ ⭐ [?] | https://github.com/vespa-engine/vespa |
| **Turbopuffer** | Serverless vector database optimized for cost-efficient large-scale search. Object-storage-native architecture. | Proprietary | https://turbopuffer.com/ |
| **Redis (Vector Search)** | Redis Stack includes vector similarity search via RediSearch module. Good for existing Redis users wanting vector capabilities. | Part of Redis | https://redis.io/docs/interact/search-and-query/query/vector-search/ |
| **Elasticsearch (Vector Search)** | Dense vector field type + kNN search. Good for teams already on Elastic who need vector capabilities alongside full-text. | Part of Elastic | https://www.elastic.co/elasticsearch/vector-database |
| **MongoDB Atlas Vector Search** | Vector search integrated into MongoDB Atlas. Good for teams already on MongoDB wanting semantic search without new infra. | Part of MongoDB | https://www.mongodb.com/products/platform/atlas-vector-search |
| **FAISS** | Facebook AI Similarity Search. Library (not DB) for efficient similarity search. Best for research/batch workloads, not production serving. | ~32,000+ ⭐ [?] | https://github.com/facebookresearch/faiss |

---

## RAG Frameworks & Orchestration

### Tier 1 — Primary RAG Frameworks

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **LangChain** | The agent engineering platform. Largest ecosystem for LLM app development. Comprehensive tooling for chains, agents, retrieval, and RAG implementations. 868K+ monthly PyPI downloads. | ~100,000+ ⭐ [?] | https://github.com/langchain-ai/langchain |
| **LlamaIndex** | Leading document agent and OCR platform. Best for data ingestion, parsing messy PDFs/tables, and structured retrieval. 91.3% recall@10 on mixed-format reports. 500K+ monthly active users. | ~39,000+ ⭐ | https://github.com/run-llama/llama_index |
| **Haystack** (deepset) | Open-source AI orchestration framework. Modular pipelines for RAG, semantic search, and agentic workflows. Used by European Commission, Airbus, Intel, NVIDIA, Apple, Netflix. | ~25,300+ ⭐ | https://github.com/deepset-ai/haystack |
| **DSPy** (Stanford NLP) | Framework for *programming*—not prompting—language models. Optimizes prompts and weights automatically. Great for sophisticated RAG pipelines with automatic prompt optimization. | ~34,000+ ⭐ | https://github.com/stanfordnlp/dspy |

### Tier 2 — Specialized RAG Engines & Platforms

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **RAGFlow** (InfiniFlow) | Open-source RAG engine based on deep document understanding. Visual workflows, web UI, GDPR-compliant local inference. One of GitHub's fastest-growing AI projects in 2025. | ~78,300+ ⭐ | https://github.com/infiniflow/ragflow |
| **Dify** | Open-source LLM app development platform. Combines AI workflow, RAG pipeline, agent capabilities, model management, and observability. Hit 100K stars June 2025. | ~140,000+ ⭐ | https://github.com/langgenius/dify |
| **Cognita** (TrueFoundry) | Modular open-source RAG framework. Swappable components: data loaders, parsers, embedders, vector stores, retrievers, query engines. **Archived March 2026.** | ~2,000+ ⭐ [archived] | https://github.com/truefoundry/cognita |
| **Verba** (Weaviate) | The Golden RAGtriever — end-to-end RAG chatbot with Weaviate backend. Under 10 min setup. **Archived June 2026** — replaced by Elysia agentic RAG. | ~6,000+ ⭐ [archived] | https://github.com/weaviate/Verba |
| **LangChain RAG-from-Scratch** | Educational reference implementation showing RAG from first principles using LangChain. | ~3,000+ ⭐ [?] | https://github.com/langchain-ai/rag-from-scratch |
| **EmbedChain** (now mem0) | Simplest RAG framework — 3 lines to working RAG. Free, lightweight. | ~10,000+ ⭐ [?] | https://github.com/mem0ai/mem0 |
| **Ragie** | Managed RAG-as-a-service. No retrieval code needed, API-first. | Proprietary | https://ragie.ai/ |

---

---

# CATEGORY 13: SYSTEM STARTERS & BOILERPLATES

## Full-Stack Meta-Frameworks & Starters

### T3 Stack

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **create-t3-app** | CLI to scaffold a typesafe Next.js app with tRPC + Tailwind + Prisma + NextAuth. Modular — each piece is optional. The gold standard for typesafe full-stack React. | ~26,000+ ⭐ (1,100 forks) | https://github.com/t3-oss/create-t3-app |
| **create-t3-turbo** | T3 Stack + Expo React Native in a Turborepo monorepo. Full-stack web + mobile from one codebase. | ~5,000+ ⭐ [?] | https://github.com/t3-oss/create-t3-turbo |

### Vercel AI SDK Templates

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **Vercel Chatbot** (formerly AI Chatbot) | Full-featured, hackable Next.js AI chatbot. Uses AI Gateway for multi-model support (OpenAI, Anthropic, Google, xAI). Production-ready with auth, streaming, artifacts. | ~5,000+ ⭐ [?] | https://github.com/vercel/chatbot |
| **Vercel AI SDK** | The AI Toolkit for TypeScript. Unified API across 25+ providers (v6.0 Dec 2025). Switch providers by changing 2 lines. | ~15,000+ ⭐ [?] | https://github.com/vercel/ai |
| **Gemini AI Chatbot Template** | Vercel template using Google Gemini models with AI SDK. Swap to OpenAI/Anthropic/Cohere easily. | Template | https://vercel.com/templates/ai/gemini-ai-chatbot |

### Next.js + Supabase Starters

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **nextjs/saas-starter** (Vercel official) | Official Next.js + Postgres + Stripe + shadcn/ui SaaS starter. Minimal, production-ready. | ~7,000+ ⭐ [?] | https://github.com/nextjs/saas-starter |
| **next-supabase-stripe-starter** | Highest quality SaaS starter with Next.js + Supabase + Stripe + shadcn/ui. | ~1,500+ ⭐ [?] | https://github.com/KolbySisk/next-supabase-stripe-starter |
| **Nextbase** | Free boilerplate for Next.js 14+ + Supabase + Tailwind + TypeScript. Includes ESLint, Prettier, Husky, Jest, Playwright, React Query. | ~2,000+ ⭐ [?] | https://github.com/chrisnguyen96/nextbase-nextjs-supabase-starter |
| **Supabase + Next.js Template** (Razikus) | Production-ready SaaS template. Auth, user management, file storage, task management, RLS policies. Includes React Native + Expo mobile app. i18n support. | ~500+ ⭐ [?] | https://github.com/Razikus/supabase-nextjs-template |

---

## SaaS Starters & Boilerplates (Premium)

| Name | Description | Price | URL |
|------|-------------|-------|-----|
| **ShipFast** | Next.js + Tailwind + MongoDB + Stripe boilerplate. Optimizes for speed-to-market. Auth, payments, email, SEO, landing page pre-wired. One-time purchase. | $199–$299 | https://shipfa.st/ |
| **Makerkit** | Next.js SaaS Starter Kit. Hybrid account modes, deep AI tooling (AI Agents, MCP Server), multiple deployment targets (Supabase/Firebase/Prisma). New: Next.js 16, Figma UI. | ~$299–$499 | https://makerkit.dev/ |
| **Supastarter** | SaaS starter for Next.js & Nuxt. Multi-tenancy, payment support, Supabase-native. Optimized for AI coding agents & developers. Scalable architecture. | ~$299–$499 | https://supastarter.dev/ |
| **SaaSBold** | Full-stack Next.js SaaS boilerplate. All essential integrations, user/admin dashboards, landing page, design source. Has a free "lite" version on GitHub. | $149+ (lite: free) | https://saasbold.com/ |
| **Gravity** | Node.js + React SaaS boilerplate. Built-in auth, Stripe billing, admin tools. Battle-tested. | ~$399 [?] | https://usegravity.app/ |
| **RevKit** | Next.js SaaS boilerplate optimized for AI-assisted development. Tailwind + TypeScript + Stripe. | ~$299 [?] | https://designrevision.com/blog/shipfast-vs-supastarter-vs-revkit |
| **Shipfastai** (Python) | Production-ready SaaS boilerplate for Python developers. FastAPI backend + Next.js frontend + JWT auth + Stripe + RAG pipelines + multi-provider LLM support. | ~$199 [?] | https://docs.shipfastai.dev/ |

---

## Authentication Starters

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **Better Auth** | Framework-agnostic TypeScript-first auth library. Sessions, OAuth, email verification, 2FA, multi-tenancy. Zero lock-in. Fastest growing auth framework 2025–2026. 100K+ weekly npm downloads. YC-backed. | ~28,800+ ⭐ | https://github.com/better-auth/better-auth |
| **Auth.js** (formerly NextAuth.js) | Open-source authentication for Next.js. Supports multiple providers, database adapters, JWT/session strategies. The most popular OSS auth for Next.js. | ~25,000+ ⭐ [?] | https://github.com/nextauthjs/next-auth |
| **Clerk** | Managed auth service with deepest App Router integration. Pre-built components, Server Component support. Free tier: 50K MAU. Not OSS but has open starter templates. | Proprietary (free tier) | https://clerk.com/ |
| **Clerk Next.js Auth Starter** | Official Clerk starter template for Next.js App Router with auth pre-configured. | Template | https://github.com/clerk/nextjs-auth-starter-template |

---

## Open-Source ChatGPT Clones (Worth Forking)

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **Open WebUI** | Most popular self-hosted AI interface. Supports Ollama, OpenAI API, and dozens of providers. Beautiful UX, strong community. 355K+ community members. | ~136,000+ ⭐ | https://github.com/open-webui/open-webui |
| **LobeChat** (lobehub) | Open-source modern-design AI chat framework. Multi-provider support, Knowledge Base (RAG), Vision/TTS/Plugins/Artifacts. One-click deployment. | ~59,000–70,600 ⭐ | https://github.com/lobehub/lobe-chat |
| **LibreChat** | Enhanced ChatGPT clone with Agents, MCP, multi-provider support (OpenAI, Anthropic, Google, Azure, etc.), code interpreter, RAG API, secure multi-user auth. Active development. | ~39,900+ ⭐ | https://github.com/danny-avila/LibreChat |
| **Dify** | LLM app development platform with visual workflow builder, RAG pipeline, agent capabilities, model management. More than a chat clone — full AI app builder. | ~140,000+ ⭐ | https://github.com/langgenius/dify |
| **Jan** | Open-source ChatGPT alternative that runs 100% offline on your device. Desktop app, multiple engine support (llama.cpp, TensorRT-LLM). | ~25,000+ ⭐ [?] | https://github.com/janhq/jan |
| **AnythingLLM** | Local-first agent experience. Full desktop app with RAG, multi-LLM support, document chat, embeddings management. "Stop renting your intelligence." | ~35,000+ ⭐ [?] | https://github.com/Mintplex-Labs/anything-llm |
| **Chatbox** | Desktop/iOS/Android AI chat client. Supports multiple providers. Clean UI. | ~25,000+ ⭐ [?] | https://github.com/Bin-Huang/chatbox |

---

## AI Agent Starter Kits

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **Google Agent Starter Pack** | Production-ready AI agent templates for Google Cloud. CI/CD, evaluation, observability. Now in maintenance — active development moved to `agents-cli`. | ~3,900 ⭐ | https://github.com/GoogleCloudPlatform/agent-starter-pack |
| **Full-Stack AI Agent Template** (Vstorm) | CLI generator: FastAPI + Next.js 15 with AI Agents, RAG, streaming, auth, 20+ integrations. Supports PydanticAI or LangChain. 5 AI frameworks, 75+ config options. | ~614+ ⭐ | https://github.com/vstorm-co/full-stack-ai-agent-template |
| **Production Agent Starter Kit** | Production-style AI agent starter with RAG, MCP tools, HITL workflows, tracing, evals, and deployment. | New [?] | https://github.com/sudotty/production-agent-starter-kit |
| **Agent Starter Kit** (ntorga) | Scaffold for multi-model, personalized Natural Language AI Harness (NLAH). | New [?] | https://github.com/ntorga/agent-starter-kit |
| **Microsoft Generative AI for Beginners** | Course + examples including AI Agents chapter. Great educational starter for understanding agent patterns. | ~70,000+ ⭐ [?] | https://github.com/microsoft/generative-ai-for-beginners |
| **LangGraph** (LangChain) | Framework for building stateful, multi-actor agent applications. The standard for complex agent workflows. | Part of LangChain ecosystem | https://github.com/langchain-ai/langgraph |
| **CrewAI** | Framework for orchestrating role-playing AI agents. Easy multi-agent systems. | ~25,000+ ⭐ [?] | https://github.com/crewAIInc/crewAI |
| **AutoGen** (Microsoft) | Framework for building multi-agent conversational systems. | ~40,000+ ⭐ [?] | https://github.com/microsoft/autogen |

---

## "Build Your Own X AI" Starter Repos

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **Vercel Chatbot** | Build your own AI chatbot (Next.js + AI SDK + multi-model). The canonical "build your own ChatGPT." | ~5,000+ ⭐ [?] | https://github.com/vercel/chatbot |
| **LanceDB Vercel Chatbot** | Build an AI chatbot with website context from LanceDB vector store. | ~200+ ⭐ [?] | https://github.com/lancedb/lancedb-vercel-chatbot |
| **RAGFlow** | Build your own enterprise RAG system with visual workflows and deep doc understanding. | ~78,300+ ⭐ | https://github.com/infiniflow/ragflow |
| **Quivr** | Build your own "second brain" AI — personal knowledge management with RAG. | ~35,000+ ⭐ [?] | https://github.com/QuivrHQ/quivr |
| **PrivateGPT** | Build your own private AI assistant. Interact with documents privately, 100% offline. | ~55,000+ ⭐ [?] | https://github.com/zylon-ai/private-gpt |
| **LocalGPT** | Chat with your documents on local device using local LLMs. Privacy-focused. | ~20,000+ ⭐ [?] | https://github.com/PromtEngineer/localGPT |
| **OpenDevin/OpenHands** | Build your own AI software engineer / coding agent. | ~45,000+ ⭐ [?] | https://github.com/All-Hands-AI/OpenHands |
| **Haystack RAG App** | Example RAG backend + UI using Haystack framework. | ~500+ ⭐ [?] | https://github.com/deepset-ai/haystack-rag-app |
| **Blazity next-saas-starter** | Free responsive landing page template for SaaS products (JAMStack). | ~3,000+ ⭐ [?] | https://github.com/Blazity/next-saas-starter |

---

## Free / Open-Source SaaS Starters (Community)

| Name | Description | GitHub Stars | URL |
|------|-------------|-------------|-----|
| **nextjs/saas-starter** | Official Vercel/Next.js SaaS starter. Next.js + Postgres + Stripe + shadcn/ui. | ~7,000+ ⭐ [?] | https://github.com/nextjs/saas-starter |
| **Saas-Starter-Kit/Saas-Kit-supabase** | React + Next.js + Prisma + Supabase SaaS template. | ~15 ⭐ | https://github.com/Saas-Starter-Kit/Saas-Kit-supabase |
| **The-SaaS-Factory (Next 14)** | Professional Next.js 14 SaaS Boilerplate. Powerful and scalable stack. | ~1,000+ ⭐ [?] | https://github.com/The-SaaS-Factory/next-14-saas-boilerplate |
| **SaaSBold Lite** | Free open-source version of SaaSBold. Full-stack starter kit. | New (2026) | https://github.com/SaaSBold/saasbold-lite |
| **Paddle Next.js Starter Kit** | Complete SaaS starter powered by Paddle Billing (Stripe alternative). | ~500+ ⭐ [?] | https://github.com/PaddleHQ/paddle-nextjs-starter-kit |
| **nextjs-better-auth** | Next.js 16 + Better Auth + Drizzle ORM + Supabase starter. | New | https://github.com/jabirdev/nextjs-better-auth |

---

## Key Decision Frameworks

### Vector Database Selection (2026)

| If you need... | Choose... |
|---|---|
| Zero ops, managed, getting started fast | **Pinecone** |
| Open-source control + low latency | **Qdrant** |
| Already running Postgres | **pgvector** |
| Heavy document ingestion + hybrid search | **Weaviate** |
| Billion-scale, enterprise | **Milvus** |
| Embedded/serverless, no server | **LanceDB** or **Chroma** |
| Full-stack search (text + vectors + ML ranking) | **Vespa** |

### RAG Framework Selection (2026)

| If you need... | Choose... |
|---|---|
| Largest ecosystem + flexibility | **LangChain** |
| Best document ingestion/parsing | **LlamaIndex** |
| Production-grade pipelines | **Haystack** |
| Visual workflows + deep doc understanding | **RAGFlow** |
| Automatic prompt optimization | **DSPy** |
| Full LLM app platform (not just RAG) | **Dify** |

### SaaS Starter Selection (2026)

| If you need... | Choose... |
|---|---|
| Validate idea fast (solo dev) | **ShipFast** ($199) |
| Build for years, team features | **Makerkit** ($299+) |
| Supabase-native, modern stack | **Supastarter** ($299+) |
| Free, official, minimal | **nextjs/saas-starter** (free) |
| Full typesafety | **create-t3-app** (free) |
| AI chatbot/agent | **Vercel Chatbot** or **Full-Stack AI Agent Template** |

---

*Notes: GitHub star counts marked [?] are estimated based on indirect sources and may vary. All data gathered June 2026. Archived projects noted where applicable.*
