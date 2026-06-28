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

---

*Notes: GitHub star counts marked [?] are estimated based on indirect sources and may vary. All data gathered June 2026. Archived projects noted where applicable.*
