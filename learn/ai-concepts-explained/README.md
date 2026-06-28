# 🧠 AI Concepts Explained

> Every AI concept, explained simply. From "What is an LLM?" to "How does RAG work?"

---

# 🧠 AI Wikipedia — Concepts, Terminology & Explanations

> **The god repo where anyone can understand anything AI-related.**
> If someone doesn't understand ANYTHING about AI, this section tells them where to learn it.

---

## 📚 CORE CONCEPTS PEOPLE GOOGLE

### What is an LLM / How Do LLMs Work

| Resource | Description | URL |
|----------|-------------|-----|
| **Google's Intro to LLMs** | Official Google developer guide — clear, authoritative explanation of what LLMs are and how they work | https://developers.google.com/machine-learning/resources/intro-llms |
| **KDnuggets Beginner's Guide (2025)** | Comprehensive beginner walkthrough covering transformer architecture, training, and capabilities | https://www.kdnuggets.com/large-language-models-beginners-guide-2025 |
| **LLMs 101: A Practical Guide (2026)** | Tokens → Transformer → Attention → KV cache → next token prediction, explained step by step | https://medium.com/@gauravdombale007/llms-101-a-practical-guide-2026-edition-824e16692742 |
| **Cisco: Fundamentals of AI** | "Strip away the hype: an LLM predicts the next word in a sequence" — excellent plain-English explanation | https://blogs.cisco.com/ai/the-fundamentals-of-ai-what-every-curious-person-should-know-about-how-language-models-work |
| **LLMs from Scratch Using Middle School Math** | Explains LLMs using only middle school math — exceptional for non-technical audiences | https://medium.com/data-science/understanding-llms-from-scratch-using-middle-school-math-e602d27ec876 |
| **IMD: LLMs Explained** | Business-school-quality explanation of how LLMs work in AI | https://www.imd.org/blog/digital-transformation/large-language-models-llms/ |

---

### What is RAG (Retrieval Augmented Generation)

| Resource | Description | URL |
|----------|-------------|-----|
| **NVIDIA: What is RAG** | The gold-standard technical explainer from NVIDIA — clear, visual, authoritative | https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/ |
| **McKinsey: What is RAG** | Business-friendly explanation of RAG and why it matters for enterprise AI | https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-retrieval-augmented-generation-rag |
| **Databricks: What is RAG** | Technical but accessible — explains the hybrid framework combining LLMs with external data | https://www.databricks.com/blog/what-is-retrieval-augmented-generation |
| **DigitalOcean: What is RAG** | Covers history (introduced 2020), architecture, and practical implementation | https://www.digitalocean.com/resources/articles/rag |
| **Wikipedia: RAG** | Community-maintained comprehensive reference with citations | https://en.wikipedia.org/wiki/Retrieval-augmented_generation |
| **Elastic: What is RAG** | Explains how RAG combines retrieval models with generation models | https://www.elastic.co/what-is/retrieval-augmented-generation |

---

### Fine-Tuning vs RAG vs Prompt Engineering (When to Use What)

| Resource | Description | URL |
|----------|-------------|-----|
| **Towards AI: The Definitive Decision Framework (2026)** | The most comprehensive comparison — when to prompt, when to retrieve, when to fine-tune | https://medium.com/towards-artificial-intelligence/fine-tuning-vs-rag-vs-prompting-the-definitive-decision-framework-for-2026-723fc1c863af |
| **Taskade: Fine-Tuning vs RAG** | TL;DR rule: "prompt first, retrieve for knowledge, fine-tune for behavior" | https://www.taskade.com/blog/fine-tuning-vs-rag |
| **Raftlabs: Cost Comparison** | Prompt engineering = free; RAG = $10K-$80K; Fine-tuning = $20K-$150K+ | https://www.raftlabs.com/blog/llm-fine-tuning-guide |
| **Codebasics: RAG vs Fine-Tuning (2026)** | Practical software engineer's guide to choosing the right approach | https://codebasics.io/blog/rag-vs-fine-tuning-vs-prompt-engineering-which-should-a-software-engineer-choose-in-2026 |
| **Substack: Fine-Tuning vs Prompting vs RAG** | "The most common pattern is reaching for fine-tuning when prompting would work" | https://arslandg.substack.com/p/fine-tuning-vs-prompting-vs-rag-when |

---

### What are Tokens, Context Windows, Temperature, Top-P

| Resource | Description | URL |
|----------|-------------|-----|
| **Ken Muse: How Temperature, Top-K, Top-P, and Min-P Control LLM Output** | The clearest technical explanation of all sampling parameters with visuals | https://www.kenmuse.com/blog/how-temp-topk-topp-minp-control-llm-output/ |
| **Machine Learning Mastery: Token Selection Statistics** | Logits → Temperature → Top-P walkthrough with math | https://machinelearningmastery.com/the-statistics-of-token-selection-logits-temperature-and-top-p-walkthrough/ |
| **Domenico Soriano: Tokens, Embeddings, Temperature, and Top-P** | Complete explainer covering tokenization, embeddings, attention, and sampling in one article | https://www.domsoria.com/2025/11/how-large-language-models-work-tokens-embeddings-temperature-and-top-p/ |
| **StackViv: LLM Parameters & API Guide** | Practical guide to all LLM configuration dials and what they do | https://stackviv.ai/blog/llm-parameters-api-guide |
| **LayerX: How to Control LLM Output** | Temperature, Top-P & beyond — production-focused guide | https://layerx.xyz/br/blog/llm-temperature-sampling-guide |

---

### What is an AI Agent vs Chatbot vs Copilot

| Resource | Description | URL |
|----------|-------------|-----|
| **Taskade: AI Agents vs Copilots vs Chatbots (2026)** | Full taxonomy — chatbots steer conversation, copilots help steer work, agents steer workflows | https://www.taskade.com/blog/agents-vs-copilots |
| **Microsoft: Understanding AI Agents vs Chatbots** | Official Microsoft explanation of the autonomy spectrum | https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/do-more-with-ai/general-ai/understanding-ai-agents-vs-chatbots/ |
| **Tray.ai: Agent vs Copilot vs Chatbot** | "The difference comes down to autonomy, capability, and how each interacts with systems" | https://tray.ai/blog/agent-vs-copilot-vs-chatbot |
| **Stack AI: Key Differences and How to Choose** | "Chatbots steer conversation. Copilots help a person steer. Agents steer the workflow itself." | https://www.stack-ai.com/insights/ai-agents-vs-copilots-vs-chatbots-key-differences-use-cases-and-how-to-choose |
| **Deel: Agents vs Chatbots vs Copilots** | Fit-for-purpose framework with clear use cases for each | https://www.deel.com/blog/agents-vs-copilots-vs-chatbots/ |

---

### What is MCP (Model Context Protocol)

| Resource | Description | URL |
|----------|-------------|-----|
| **Composio: MCP Explained** | "The USB-C port equivalent for agentic systems" — Anthropic's own framing, clearly explained | https://composio.dev/blog/what-is-model-context-protocol-mcp-explained |
| **OpenCV: Beginner's Guide to MCP** | Introduced by Anthropic in late 2024, bridges AI assistants and data ecosystems | https://opencv.org/model-context-protocol/ |
| **Philipp Schmid: MCP Introduction** | Concise developer-focused overview of the open standard | https://www.philschmid.de/mcp-introduction |
| **Encore.dev: What is MCP — Developer's Guide** | Supported by Claude Desktop, Cursor, VS Code — practical getting-started guide | https://encore.dev/articles/what-is-mcp |
| **Taskade: Complete MCP Guide (2026)** | Three primitives, adoption timeline, and real-world usage | https://www.taskade.com/blog/mcp-your-ai-agents-superpower-for-real-world-context-and-automation |
| **Anthropic's MCP Deep Dive** | Technical medium article covering architecture for developers | https://medium.com/@amanatulla1606/anthropics-model-context-protocol-mcp-a-deep-dive-for-developers-1d3db39c9fdc |

---

### What is Function Calling / Tool Use

| Resource | Description | URL |
|----------|-------------|-----|
| **Google Cloud: Introduction to Function Calling** | Official Google documentation — the canonical reference | https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling |
| **Towards Data Science: Tool Calling Explained (2026)** | "How AI Agents Decide What to Do Next" — mechanism explained clearly | https://towardsdatascience.com/tool-calling-explained-how-ai-agents-decide-what-to-do-next/ |
| **Medium: What is Function Calling** | "The difference between an LLM that talks about doing things and one that actually does them" | https://medium.com/data-science-collective/what-is-function-calling-569c0b709062 |
| **FutureAGI: Tool Use Across Providers** | Cross-provider comparison of function calling implementations | https://futureagi.com/blog/llm-function-calling-2025/ |
| **Towards Data Science: JSON Mode vs Function Calling** | Clarifies the confusion between structured outputs and tool use | https://towardsdatascience.com/structured-outputs-with-llms-json-mode-function-calling-and-when-to-use-each/ |

---

### What are Embeddings / Vector Search

| Resource | Description | URL |
|----------|-------------|-----|
| **Databricks: What is Vector Search** | "Finds results based on meaning, not just matching keywords" — excellent conceptual intro | https://www.databricks.com/blog/vector-search |
| **Google Cloud: Introduction to Embeddings and Vector Search** | Official Google documentation on embeddings as high-dimensional vectors | https://cloud.google.com/bigquery/docs/vector-search-intro |
| **Weaviate: Vector Search Explained** | Clear visual explanation of how embeddings capture semantic meaning | https://www.weaviate.io/blog/vector-search-explained |
| **Meilisearch: What is Vector Search (2025)** | Beginner-friendly explanation contrasting vector search with keyword search | https://www.meilisearch.com/blog/what-is-vector-search |
| **Medium: From Words to Vectors — Beginner's Guide** | Written specifically for developers starting with AI — demystifies the jargon | https://medium.com/@erickramirezau/from-words-to-vectors-a-beginners-guide-to-vector-search-and-ai-databases-18aa2f1a3b36 |
| **Elastic: Introduction to Vector Search** | Production-focused guide from the search company | https://www.elastic.co/search-labs/blog/introduction-to-vector-search |

---

### What is Quantization (GGUF, GPTQ, AWQ)

| Resource | Description | URL |
|----------|-------------|-----|
| **LocalAIMaster: GGUF vs GPTQ vs AWQ (2026)** | The definitive comparison — "the single most important technique for fitting 70B into 8-24GB VRAM" | https://localaimaster.com/blog/quantization-explained |
| **Fungies.io: LLM Quantization Guide (2026)** | Three formats dominate: GGUF (CPU/cross-platform), GPTQ (GPU), AWQ (highest quality) | https://fungies.io/llm-quantization-gguf-awq-gptq-guide-2026/ |
| **Maarten Grootendorst: Which Quantization Method** | Visual, well-explained comparison with practical recommendations | https://maartengrootendorst.com/blog/gguf/ |
| **SitePpoint: Quantization Explained for Local LLMs** | Q4_K_M vs AWQ vs FP16 — real tradeoffs in quality, speed, and compatibility | https://www.sitepoint.com/quantization-q4km-vs-awq-fp16-local-llms/ |
| **Hardware Corner: How It Works** | "Think of it like MP3 compression for audio" — great analogy for non-technical readers | https://www.hardware-corner.net/quantization-local-llms-formats/ |
| **Calmops: GPTQ, AWQ, and GGUF for Deployment** | Technical deep-dive into trade-offs between precision, speed, and memory | https://calmops.com/algorithms/llm-quantization-gptq-awq-gguf/ |

---

### What is LoRA / QLoRA (Parameter-Efficient Fine-Tuning)

| Resource | Description | URL |
|----------|-------------|-----|
| **Towards Data Science: LoRA Intuitively and Exhaustively Explained** | The best single article on LoRA — intuitive first, then deep | https://towardsdatascience.com/lora-intuitively-and-exhaustively-explained-e944a6bff46b/ |
| **LearnCodeCamp: LoRA Fine-Tuning Explained** | "Keeps original weights frozen, learns a low-rank correction on top" — math made clear | https://learncodecamp.net/lora-finetuning-explained/ |
| **GeeksForGeeks: Fine-Tuning using LoRA and QLoRA** | Beginner-friendly tutorial with code examples | https://www.geeksforgeeks.org/fine-tuning-using-lora-and-qlora/ |
| **LetsDataScience: Master LoRA and QLoRA** | Consumer GPU guide — full fine-tuning of 7B = 14GB; LoRA = fraction of that | https://letsdatascience.com/blog/fine-tuning-llms-with-lora-and-qlora-complete-guide |
| **Medium: LoRA & QLoRA In-Depth** | From the basics to advanced implementation details | https://firastlili.medium.com/lora-qlora-fine-tuning-explained-in-depth-4ae9875b12f3 |
| **Blockchain Council: LoRA, QLoRA, and Adapters** | Reduces memory 10-20x, retains ~90-95% of full fine-tuning quality | https://www.blockchain-council.org/ai/parameter-efficient-fine-tuning-lora-qlora-adapters-explained/ |

---

### What is RLHF, DPO, Constitutional AI

| Resource | Description | URL |
|----------|-------------|-----|
| **Hugging Face: From RLHF to DPO** | Clear three-phase walkthrough of RLHF, then how DPO simplifies it | https://huggingface.co/blog/ariG23498/rlhf-to-dpo |
| **Sundeep Teki: Post-Training LLMs Guide (2026)** | SFT → RLHF → DPO → GRPO — the complete alignment stack explained | https://www.sundeepteki.org/advice/the-complete-guide-to-post-training-llms-how-sft-rlhf-dpo-and-grpo-shape-llms |
| **Towards AI: Beyond RLHF** | "DPO and AI Feedback are taking over" — the new era of alignment | https://pub.towardsai.net/beyond-rlhf-ef46f7907c98 |
| **Anthropic: Constitutional AI** | The original blog post from Anthropic explaining their Constitutional AI approach | https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback |
| **Tianpan.co: What RLHF, DPO, and RLAIF Actually Mean** | Product engineer's practical guide to alignment techniques | https://tianpan.co/blog/2026-04-17-post-training-alignment-dpo-rlaif-product-engineers |
| **mbrenndoerfer: RLAIF & Constitutional AI** | Interactive explainer on scalable alignment without humans | https://mbrenndoerfer.com/writing/rlaif-constitutional-ai-scalable-alignment |

---

### What is Multimodal AI

| Resource | Description | URL |
|----------|-------------|-----|
| **McKinsey: What is Multimodal AI** | "AI that can understand text, images, audio, and video all at the same time" — authoritative | https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-multimodal-ai |
| **IBM: What is Multimodal AI** | Comprehensive technical explanation covering all modalities | https://www.ibm.com/think/topics/multimodal-ai/ |
| **ExplainX: Complete Guide (2026)** | Models that accept/produce more than one data type in a unified system | https://explainx.ai/blog/what-is-multimodal-ai-complete-guide-2026 |
| **Shopify: What is Multimodal AI (2025)** | Business-friendly explanation with practical examples | https://www.shopify.com/uk/blog/what-is-multimodal-ai |
| **LocalAIMaster: Multimodal AI 2025** | GPT-5, Claude 4.5, Gemini 2.5 — how frontier models handle multiple modalities | https://localaimaster.com/blog/multimodal-ai-standard-text-vision-voice-2025 |

---

### What is Inference vs Training

| Resource | Description | URL |
|----------|-------------|-----|
| **NVIDIA: Training vs Inference** | "Training is studying for an exam. Inference is sitting the exam." — the canonical explainer | https://blogs.nvidia.com/blog/difference-deep-learning-training-inference-ai/ |
| **DigitalOcean: AI Inference vs Training** | "Training adjusts parameters; inference produces predictions in real time" | https://www.digitalocean.com/resources/articles/ai-inference-vs-training |
| **TechTarget: Key Differences and Tradeoffs** | Comprehensive comparison of hardware, cost, and optimization approaches | https://www.techtarget.com/searchEnterpriseAI/tip/AI-inference-vs-training-Key-differences-and-tradeoffs |
| **StackViv: Training vs Inference in AI** | Clean summary — training happens once, inference runs continuously | https://stackviv.ai/blog/training-vs-inference-ai |

---

### What are Transformers / Attention Mechanism

| Resource | Description | URL |
|----------|-------------|-----|
| **Jay Alammar: The Illustrated Transformer** | THE definitive visual explainer — universally recommended, beautifully illustrated | https://jalammar.github.io/illustrated-transformer/ |
| **mbrenndoerfer: The Transformer — Interactive** | Interactive walkthrough of "Attention Is All You Need" | https://mbrenndoerfer.com/writing/transformer-attention-is-all-you-need |
| **Calmops: Transformer Architecture Explained** | Technical deep-dive into self-attention, multi-head attention, and positional encoding | https://calmops.com/algorithms/transformer-attention-mechanisms/ |
| **Medium: Transformers Explained — Why Attention Is All You Need** | "Every token attends to all other tokens simultaneously — no recurrence" | https://medium.com/@lmpo/transformers-explained-why-attention-is-truly-all-you-need-2e3669242965 |
| **Starmorph: From Attention to GPT-4o and Claude** | End-to-end journey from attention mechanism to modern LLMs | https://blog.starmorph.com/blog/intro-to-transformers |

---

## 🎓 BEST "EXPLAIN AI" RESOURCES (Educators & Courses)

### Video-Based Learning

| Resource | Description | URL |
|----------|-------------|-----|
| **3Blue1Brown: Neural Networks Series** | The most beautiful visual explanation of neural networks, gradient descent, and backpropagation ever made. Grant Sanderson's animations make deep concepts genuinely intuitive. | https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000 |
| **Andrej Karpathy: Neural Networks — Zero to Hero** | Former OpenAI/Tesla AI director builds neural networks from scratch. Two tracks: technical and general audience. The 3.5-hour LLM deep dive is legendary. | https://karpathy.ai/zero-to-hero.html |
| **Andrej Karpathy: YouTube Channel** | Educational videos on AI — technical track and general audience track | https://www.youtube.com/@AndrejKarpathy |
| **fast.ai: Practical Deep Learning for Coders** | Jeremy Howard's top-down approach — build things first, understand theory after. Free course + free book. | https://course.fast.ai/ |
| **Stanford CS229: Machine Learning** | Andrew Ng's legendary course — broad intro to ML and statistical pattern recognition. Free lectures. | https://cs229.stanford.edu/ |
| **Stanford CS224n: NLP with Deep Learning** | The gold-standard NLP course — covers transformers, attention, LLMs in depth | https://stanford.edu/class/cs224n/ |
| **MIT 6.7960: Deep Learning** | Covers MLPs, CNNs, RNNs, transformers, theory, and applications. Free on OCW. | https://ocw.mit.edu/courses/6-7960-deep-learning-fall-2024/ |
| **MIT 6.S191: Introduction to Deep Learning** | Fast-paced intro with TensorFlow hands-on projects | https://ocw.mit.edu/courses/6-s191-introduction-to-deep-learning-january-iap-2020/ |
| **Google's Machine Learning Crash Course** | Google's fast-paced, practical intro — animated videos, interactive visualizations, hands-on exercises | https://developers.google.com/machine-learning/crash-course |

---

### Blogs & Written Resources

| Resource | Description | URL |
|----------|-------------|-----|
| **Jay Alammar's Blog** | "Visualizing machine learning one concept at a time" — The Illustrated Transformer, Illustrated GPT-2, Illustrated BERT. Gold standard for visual ML explanations. | https://jalammar.github.io/ |
| **Lilian Weng's Blog (Lil'Log)** | OpenAI researcher's comprehensive deep-dives: agents, hallucinations, reward hacking, RLHF, diffusion models. Exhaustive references on every topic. | https://lilianweng.github.io/ |
| **Sebastian Raschka: Ahead of AI** | LLM research engineer & author of "Build a Large Language Model From Scratch." Curated paper lists, state-of-LLMs reviews, and clear technical writing. | https://magazine.sebastianraschka.com/ |
| **Chip Huyen** | Stanford ML Systems lecturer, author of "Designing Machine Learning Systems" and "AI Engineering." MLOps guide, interview prep, and systems design resources. | https://huyenchip.com/ |
| **Chip Huyen: AI Engineering Resources** | Curated resources for AI engineers — 1200+ reference links from her book | https://github.com/chiphuyen/aie-book |
| **Sebastian Raschka: Blog & Notes** | Quick paper notes on recent AI research, benchmarks, and architecture updates | https://sebastianraschka.com/blog/ |

---

## 📖 AI GLOSSARIES — Best Existing References

| Resource | Description | URL |
|----------|-------------|-----|
| **Google's Machine Learning Glossary** | The most comprehensive ML glossary — hundreds of terms with clear examples, from fundamentals to LLM-specific concepts. Continuously updated. | https://developers.google.com/machine-learning/glossary |
| **Google Cloud: Generative AI Glossary** | Focused specifically on generative AI terminology | https://cloud.google.com/docs/generative-ai/glossary |
| **TechCrunch: AI Terms Glossary (2026)** | Living document updated regularly — "So you've heard these AI terms and nodded along; let's fix that" | https://techcrunch.com/2026/04/12/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/ |
| **MIT Sloan: AI Glossary** | Academic-quality glossary from MIT's teaching technologies team | https://mitsloanedtech.mit.edu/ai/basics/glossary/ |
| **Digital Applied: 200 Essential Agentic AI Terms (2026)** | Collapses competing terminology (tool vs function, plan vs scratchpad) into one shared reference | https://www.digitalapplied.com/blog/agentic-ai-glossary-200-essential-terms-2026 |
| **UsefulAI: 40 Key Terms for 2025** | Concise, curated glossary of the most important terms | https://usefulai.com/glossary |
| **Digital Applied: 60 AI Agent Terms (2026)** | Focused on the agentic AI vocabulary explosion of 2025-2026 | https://www.digitalapplied.com/blog/ai-agent-glossary-2026-60-essential-terms |

---

## 📄 RESEARCH PAPERS EVERY AI PERSON SHOULD KNOW

### The Foundational Papers

| Paper | Authors/Year | One-Line Description | URL |
|-------|-------------|---------------------|-----|
| **Attention Is All You Need** | Vaswani et al., 2017 | THE paper that introduced the Transformer architecture — replaced RNNs with self-attention. Everything modern AI is built on this. | https://arxiv.org/abs/1706.03762 |
| **BERT: Pre-training of Deep Bidirectional Transformers** | Devlin et al., 2018 | Introduced bidirectional pre-training — revolutionized NLP by training on both left and right context simultaneously | https://arxiv.org/abs/1810.04805 |
| **GPT-3: Language Models are Few-Shot Learners** | Brown et al., 2020 | Demonstrated that scaling up language models enables few-shot learning without fine-tuning — the paper that launched the LLM era | https://arxiv.org/abs/2005.14165 |
| **GPT-4 Technical Report** | OpenAI, 2023 | Large multimodal model capable of processing images and text — the frontier model that mainstreamed AI | https://arxiv.org/abs/2303.08774 |
| **Chain-of-Thought Prompting Elicits Reasoning** | Wei et al., 2022 | Showed that asking models to "think step by step" dramatically improves complex reasoning | https://arxiv.org/abs/2201.11903 |
| **Constitutional AI: Harmlessness from AI Feedback** | Bai et al. (Anthropic), 2022 | Trains AI to be harmless using self-critique and a set of principles — no human labels needed | https://arxiv.org/abs/2212.08073 |
| **LoRA: Low-Rank Adaptation of Large Language Models** | Hu et al., 2021 | Freezes pre-trained weights and trains small low-rank matrices instead — made fine-tuning accessible on consumer hardware | https://arxiv.org/abs/2106.09685 |
| **FlashAttention: Fast and Memory-Efficient Exact Attention** | Dao et al., 2022 | Made transformer training 2-3x faster by being IO-aware — foundational infrastructure paper | https://arxiv.org/abs/2205.14135 |
| **Training Language Models to Follow Instructions (InstructGPT/RLHF)** | Ouyang et al. (OpenAI), 2022 | The paper that made ChatGPT possible — fine-tuning with human feedback to follow instructions | https://arxiv.org/abs/2203.02155 |
| **Mixture of Experts in LLMs (Survey)** | Various, 2024 | Comprehensive review of MoE — how models like GPT-4 use sparse expert routing for efficiency | https://arxiv.org/abs/2407.06204 |

### Additional Important Papers

| Paper | Year | Description | URL |
|-------|------|-------------|-----|
| **GPT-1: Improving Language Understanding by Generative Pre-Training** | 2018 | The first GPT paper — introduced generative pre-training + fine-tuning | https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf |
| **GPT-2: Language Models are Unsupervised Multitask Learners** | 2019 | Showed language models can perform tasks without explicit training | https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf |
| **DPO: Direct Preference Optimization** | Rafailov et al., 2023 | Eliminates the reward model from RLHF — simpler, cheaper alignment | https://arxiv.org/abs/2305.18290 |
| **QLoRA: Efficient Finetuning of Quantized LLMs** | Dettmers et al., 2023 | Fine-tune a 65B model on a single 48GB GPU — democratized fine-tuning | https://arxiv.org/abs/2305.14314 |

---

### Where to Find & Read AI Papers

| Platform | Description | URL |
|----------|-------------|-----|
| **arXiv** | The primary preprint server for AI/ML research — where papers are first published | https://arxiv.org/list/cs.AI/recent |
| **Papers With Code** | Links papers to their code implementations + state-of-the-art leaderboards | https://paperswithcode.com/ |
| **Semantic Scholar** | AI-powered academic search — TLDR summaries, citation graphs, influence scoring | https://www.semanticscholar.org/ |
| **Hugging Face Papers** | Community-curated daily ML papers with discussions and implementations | https://huggingface.co/papers |
| **ar5iv** | arXiv papers rendered as accessible HTML (easier to read than PDFs) | https://ar5iv.labs.arxiv.org/ |
| **Connected Papers** | Visual tool to explore related papers as a graph | https://www.connectedpapers.com/ |

---

## 🗺️ LEARNING PATHS — Where to Start

### "I know nothing about AI" → Start here:
1. **3Blue1Brown Neural Networks playlist** (visual intuition)
2. **Google ML Crash Course** (structured learning)
3. **Jay Alammar's Illustrated Transformer** (understand the architecture)

### "I'm a developer who wants to use AI" → Start here:
1. **Andrej Karpathy: Zero to Hero** (build from scratch)
2. **fast.ai: Practical Deep Learning** (top-down practical approach)
3. **Chip Huyen: AI Engineering** (production systems)

### "I want to understand the research" → Start here:
1. **Read "Attention Is All You Need"** (the foundation)
2. **Lilian Weng's blog** (comprehensive research summaries)
3. **Sebastian Raschka's Ahead of AI** (curated paper reviews)
4. **Stanford CS224n** (academic depth)

---

*Last updated: June 2026. All URLs verified at time of compilation.*
