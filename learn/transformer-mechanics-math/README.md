# 🧮 Transformer Mechanics & Math

> How transformers actually work — self-attention, positional encoding, KV caching, scaling laws. The math that powers all modern AI.

---

## 1. THE TRANSFORMER ARCHITECTURE

The Transformer (Vaswani et al., 2017) is the architecture behind GPT, Claude, Gemini, Llama, and every other modern LLM.

### Core Components

```
Input Tokens → Token Embeddings + Positional Encoding
    → [Transformer Block] × N layers
        → Multi-Head Self-Attention
        → LayerNorm
        → Feed-Forward Network (MLP)
        → LayerNorm
    → Output Logits → Softmax → Next Token Prediction
```

### Key Papers
- **"Attention Is All You Need"** (Vaswani et al., 2017) — The original paper — https://arxiv.org/abs/1706.03762
- **"The Illustrated Transformer"** (Jay Alammar) — Best visual explanation — https://jalammar.github.io/illustrated-transformer/
- **"Formal Algorithms for Transformers"** (DeepMind, 2023) — Complete mathematical formalization — https://arxiv.org/abs/2207.09238
- **3Blue1Brown: "Attention in transformers, visually explained"** — https://www.youtube.com/watch?v=eMlx5fFNoYc
- **Andrej Karpathy: "Let's build GPT from scratch"** — https://www.youtube.com/watch?v=kCc8FmEb1nY

---

## 2. SELF-ATTENTION MECHANISM

### The Math

Given input sequence **X** ∈ ℝ^(n×d):

```
Q = X·W_Q    (Queries)
K = X·W_K    (Keys)  
V = X·W_V    (Values)

Attention(Q, K, V) = softmax(Q·K^T / √d_k) · V
```

Where:
- **Q·K^T** computes pairwise similarity between all token positions
- **√d_k** scaling prevents softmax from saturating (gradient vanishing)
- **softmax** converts similarities to attention weights (probability distribution)
- Multiplication by **V** produces weighted combination of value vectors

### Multi-Head Attention

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) · W_O
where head_i = Attention(Q·W_Qi, K·W_Ki, V·W_Vi)
```

Multiple heads allow attending to different relationship types simultaneously (syntactic, semantic, positional, etc.).

### Complexity

Standard self-attention is **O(n²)** in sequence length — the main bottleneck for long contexts. This is why efficient attention variants exist.

---

## 3. POSITIONAL ENCODING

Transformers have no inherent notion of position — positional encoding adds this information.

### Sinusoidal (Original)
```
PE(pos, 2i) = sin(pos / 10000^(2i/d))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d))
```
Fixed, no learnable parameters. Can theoretically extrapolate to longer sequences.

### Learned Absolute Embeddings
- Used in GPT-2, BERT
- Learnable embedding per position
- Cannot extrapolate beyond training length

### RoPE (Rotary Position Embedding)
- Used in: **Llama, Qwen, Mistral, most modern open LLMs**
- Encodes position by rotating query/key vectors in 2D subspaces
- Key insight: relative position becomes the angle between rotated vectors
- Naturally supports relative positioning
- Paper: https://arxiv.org/abs/2104.09864
- **"RoPE is a rotation"** — best intuitive explanation: https://blog.eleuther.ai/rotary-embeddings/

### ALiBi (Attention with Linear Biases)
- Used in: BLOOM, MPT
- Adds linear bias to attention scores based on distance
- No learned parameters, trains at short length, infers at long
- Paper: https://arxiv.org/abs/2108.12409

### YaRN (Yet another RoPE extensioN)
- Extends RoPE context length without retraining
- Used to scale Llama-2 from 4K → 128K context
- Paper: https://arxiv.org/abs/2309.00071

---

## 4. KV CACHING

### What It Is

During autoregressive generation, the model generates one token at a time. Without KV caching, every new token would require recomputing attention over ALL previous tokens from scratch.

**KV Cache stores the Key and Value matrices from all previous tokens** so each new token only computes its own Q, then attends to the cached K/V.

### Memory Math

```
KV Cache Size = 2 × n_layers × n_heads × head_dim × seq_len × precision_bytes
```

For a 70B model (Llama 3.3 70B) with 128K context at FP16:
```
= 2 × 80 × 64 × 128 × 128,000 × 2 bytes
≈ 167 GB just for KV cache!
```

This is why long-context models need so much VRAM.

### KV Cache Optimization Techniques

| Technique | Description | Paper/Resource |
|-----------|-------------|---------------|
| **GQA (Grouped-Query Attention)** | Share KV heads across query heads (used in Llama 2+). Reduces KV cache by N×. | https://arxiv.org/abs/2305.13245 |
| **MQA (Multi-Query Attention)** | Extreme version — 1 KV head for all queries | https://arxiv.org/abs/1911.02150 |
| **PagedAttention** (vLLM) | Paginates KV cache like OS virtual memory — eliminates fragmentation | https://arxiv.org/abs/2309.06180 |
| **Quantized KV Cache** | FP8/INT4 KV cache with minimal quality loss | Various implementations |
| **Sliding Window Attention** | Only attend to last W tokens (Mistral) | https://arxiv.org/abs/2004.05150 |
| **Ring Attention** | Distribute long sequences across devices | https://arxiv.org/abs/2310.01889 |

---

## 5. EFFICIENT ATTENTION VARIANTS

| Method | Complexity | Used In | Paper |
|--------|-----------|---------|-------|
| **Flash Attention 1** | O(n²) but IO-aware (2-4× faster) | Everything modern | https://arxiv.org/abs/2205.14135 |
| **Flash Attention 2** | Further optimized, 2× over FA1 | Standard in 2025+ | https://arxiv.org/abs/2307.08691 |
| **Flash Attention 3** | Hopper GPU specific, FP8 support | Latest GPUs | https://arxiv.org/abs/2407.08691 [?] |
| **Sliding Window** | O(n·w) where w = window | Mistral, Gemma | Part of architecture |
| **Sparse Attention** | O(n√n) | GPT-3 training | https://arxiv.org/abs/1904.10509 |
| **Linear Attention** | O(n) | Research | Various |
| **Mamba (S4/SSM)** | O(n) state space | Mamba, Jamba | https://arxiv.org/abs/2312.00752 |

### Flash Attention — Why It Matters
Standard attention materializes the full N×N attention matrix in HBM (slow GPU memory). Flash Attention:
1. Tiles the computation to fit in SRAM (fast on-chip memory)
2. Never materializes the full attention matrix
3. Fuses softmax + matmul into one kernel
4. Result: same exact output, 2-4× faster, uses O(N) memory instead of O(N²)

**Repo:** https://github.com/Dao-AILab/flash-attention (⭐ 15,000+)

---

## 6. SCALING LAWS

### Chinchilla Scaling Law (Hoffmann et al., 2022)
- **Key finding:** Models should be trained on ~20× more tokens than parameters
- A 70B model needs ~1.4T tokens for compute-optimal training
- Paper: https://arxiv.org/abs/2203.15556
- This is why Llama 3 trained on 15T tokens (overtraining for inference efficiency)

### Kaplan Scaling Laws (OpenAI, 2020)
- Loss scales as power law with compute, data, and parameters
- L(C) ∝ C^(-0.050) — loss decreases predictably with more compute
- Paper: https://arxiv.org/abs/2001.08361

### Inference Scaling (2025-2026)
- "Test-time compute" — spending more compute at inference (chain-of-thought, search)
- o1/o3/R1 models: scale inference compute for harder problems
- Paper (DeepSeek): https://arxiv.org/abs/2501.12948 [?]

---

## 7. KEY ARCHITECTURAL INNOVATIONS (2023-2026)

| Innovation | What It Does | Used In |
|-----------|-------------|---------|
| **Mixture of Experts (MoE)** | Only activate subset of parameters per token → bigger model, same compute | Mixtral, GPT-4, DeepSeek V3 |
| **SwiGLU Activation** | Better MLP activation (replaces ReLU/GELU) | Llama, Mistral, most modern |
| **RMSNorm** | Faster normalization (replaces LayerNorm) | Llama, Qwen |
| **Grouped-Query Attention** | Fewer KV heads → less memory | Llama 2+, Mistral |
| **Rotary Embeddings (RoPE)** | Relative position via rotation | Almost all modern LLMs |
| **State Space Models (Mamba)** | Linear-time alternative to attention | Mamba, Jamba, Zamba |
| **Differential Attention** | Subtract two attention maps for noise cancellation | Research (2024) |
| **Native Multimodality** | Process images/audio as tokens alongside text from training | Gemini, GPT-4o+ |

---

## 8. LEARNING RESOURCES

### Courses
- **Andrej Karpathy: Neural Networks: Zero to Hero** — https://karpathy.ai/zero-to-hero.html
- **Stanford CS224N: NLP with Deep Learning** — https://web.stanford.edu/class/cs224n/
- **Umar Jamil: Attention/Transformer videos** — https://www.youtube.com/@uloammar

### Visual Explainers
- **Jay Alammar's Blog** — Best visual ML explanations — https://jalammar.github.io/
- **The Illustrated Transformer** — https://jalammar.github.io/illustrated-transformer/
- **The Illustrated GPT-2** — https://jalammar.github.io/illustrated-gpt2/
- **3Blue1Brown: Neural Networks** — https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
- **Lilian Weng's Blog** — Deep technical posts — https://lilianweng.github.io/

### Implementations
- **nanoGPT** (Karpathy) — Minimal GPT implementation for learning — https://github.com/karpathy/nanoGPT (⭐ 38,000+)
- **minGPT** (Karpathy) — Even more minimal — https://github.com/karpathy/minGPT
- **llm.c** (Karpathy) — GPT-2 training in pure C/CUDA — https://github.com/karpathy/llm.c (⭐ 30,000+)
- **labml.ai Annotated Implementations** — Every paper annotated in PyTorch — https://nn.labml.ai/ (⭐ 57,000+)
- **x-transformers** — Clean transformer building blocks — https://github.com/lucidrains/x-transformers (⭐ 5,000+)

---

*Last updated: June 2026.*
