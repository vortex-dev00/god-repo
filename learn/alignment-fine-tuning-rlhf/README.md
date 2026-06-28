# 🎯 Alignment & Fine-Tuning (RLHF/DPO/KTO)

> How models go from "predicts next token" to "helpful, harmless, and honest" — instruction tuning, preference optimization, and alignment techniques.

---

## 1. THE ALIGNMENT PIPELINE

Modern LLMs follow a multi-stage training pipeline:

```
Stage 1: Pre-training (next-token prediction on internet text)
    ↓ Base model (knows everything, follows nothing)
Stage 2: Supervised Fine-Tuning (SFT) on instruction/response pairs
    ↓ Instruction-following model
Stage 3: Preference Optimization (RLHF / DPO / KTO)
    ↓ Aligned model (helpful, safe, honest)
Stage 4: (Optional) Red-teaming & Constitutional AI refinement
    ↓ Production-ready model
```

---

## 2. SUPERVISED FINE-TUNING (SFT)

### What It Is
Train the base model on curated (instruction, response) pairs to teach it to follow instructions and produce useful outputs.

### Key Datasets

| Dataset | Size | Description | Link |
|---------|------|-------------|------|
| **OpenHermes 2.5** | 1M samples | High-quality synthetic instruction data | https://huggingface.co/datasets/teknium/OpenHermes-2.5 |
| **Dolly 15K** (Databricks) | 15K | Human-written instruction pairs | https://huggingface.co/datasets/databricks/databricks-dolly-15k |
| **FLAN Collection** (Google) | 1.8K tasks | Multi-task instruction tuning mixture | https://github.com/google-research/FLAN |
| **SlimOrca** | 518K | Cleaned and filtered from OpenOrca | https://huggingface.co/datasets/Open-Orca/SlimOrca |
| **UltraChat** | 1.5M | Multi-turn synthetic conversations | https://huggingface.co/datasets/stingning/ultrachat |
| **Evol-Instruct** (WizardLM) | 250K | Complexity-evolved instructions | https://github.com/nlpxucan/WizardLM |
| **Magpie** | — | Self-synthesis: LLM generates its own SFT data | https://github.com/magpie-align/magpie [?] |

### SFT Tools

| Tool | Description | Link |
|------|-------------|------|
| **Unsloth** | 2-5× faster fine-tuning, 80% less VRAM. Supports Llama, Mistral, Qwen, Gemma. The standard for efficient SFT in 2026. ⭐ 25,000+ | https://github.com/unslothai/unsloth |
| **Axolotl** | Full-featured fine-tuning framework. Supports LoRA, QLoRA, full fine-tune, many architectures. ⭐ 8,500+ | https://github.com/axolotl-ai-cloud/axolotl |
| **TRL (Transformer Reinforcement Learning)** | HuggingFace's official alignment library — SFT, DPO, PPO, KTO all in one. ⭐ 10,500+ | https://github.com/huggingface/trl |
| **LLaMA-Factory** | No-code fine-tuning GUI + CLI. 100+ models, all methods. ⭐ 45,000+ | https://github.com/hiyouga/LLaMA-Factory |
| **torchtune** (Meta) | PyTorch-native fine-tuning for Llama models | https://github.com/pytorch/torchtune |
| **OpenPipe** | SFT-as-a-service — upload data, get fine-tuned model | https://openpipe.ai/ |

---

## 3. RLHF (Reinforcement Learning from Human Feedback)

### The Process
1. **Collect comparisons:** Human raters rank multiple model outputs for the same prompt
2. **Train reward model:** Learn a scalar reward function from the preference data
3. **Optimize with PPO:** Use the reward model as the environment, optimize the LLM policy with Proximal Policy Optimization while constraining divergence from SFT model (KL penalty)

### Key Papers
- **"Training language models to follow instructions with human feedback"** (InstructGPT, OpenAI 2022) — https://arxiv.org/abs/2203.02155
- **"Learning to summarize from human feedback"** (OpenAI, 2020) — https://arxiv.org/abs/2009.01325
- **"Proximal Policy Optimization"** (Schulman et al., 2017) — https://arxiv.org/abs/1707.06347

### Limitations of RLHF
- Expensive (requires reward model training + PPO)
- Unstable training (reward hacking, mode collapse)
- Requires careful hyperparameter tuning
- This led to simpler alternatives (DPO, KTO, ORPO)...

---

## 4. DPO (Direct Preference Optimization)

### The Breakthrough
DPO eliminates the reward model entirely. It directly optimizes the LLM from preference pairs using a clever mathematical reformulation.

**Key insight:** The optimal RLHF policy has a closed-form solution relating the reward to the log-ratio of policy vs reference model probabilities.

### The Math (simplified)
```
L_DPO = -E[log σ(β · (log π(y_w|x)/π_ref(y_w|x) - log π(y_l|x)/π_ref(y_l|x)))]
```
Where:
- y_w = preferred response ("winner")
- y_l = dispreferred response ("loser")  
- π = policy model, π_ref = reference (frozen SFT) model
- β = temperature controlling deviation from reference

### Why DPO Won
- No reward model needed
- No RL training loop (just supervised loss)
- Stable training
- Equivalent to RLHF at optimum
- Much simpler to implement

### Paper
**"Direct Preference Optimization: Your Language Model is Secretly a Reward Model"** (Rafailov et al., 2023) — https://arxiv.org/abs/2305.18290

---

## 5. BEYOND DPO — Modern Variants

| Method | Key Innovation | When to Use | Paper |
|--------|---------------|-------------|-------|
| **DPO** | Direct preference optimization without reward model | Default choice, most stable | https://arxiv.org/abs/2305.18290 |
| **KTO (Kahneman-Tversky Optimization)** | Works with just thumbs-up/down (no paired comparisons needed) | When you only have binary feedback | https://arxiv.org/abs/2402.01306 |
| **IPO (Identity Preference Optimization)** | Fixes DPO's overfitting to length | When DPO produces verbose outputs | https://arxiv.org/abs/2310.12036 |
| **ORPO (Odds Ratio Preference Optimization)** | Combines SFT + alignment in one step | Saves compute (no separate SFT stage) | https://arxiv.org/abs/2403.07691 |
| **SimPO** | Simpler reference-free preference optimization | When you want simplicity | https://arxiv.org/abs/2405.14734 |
| **SPIN (Self-Play Fine-Tuning)** | Model generates its own losing responses | When you lack human preference data | https://arxiv.org/abs/2401.01335 |
| **RLAIF (Constitutional AI)** | AI generates the feedback (no humans) | Anthropic's approach for Claude | https://arxiv.org/abs/2212.08073 |
| **Online DPO / Iterative DPO** | Continuously generate new pairs during training | Best results, more compute | Various |

---

## 6. PARAMETER-EFFICIENT FINE-TUNING (PEFT)

### LoRA (Low-Rank Adaptation)
Instead of updating all model weights, inject small low-rank matrices:
```
W' = W + α·(B·A)    where B ∈ ℝ^(d×r), A ∈ ℝ^(r×d), r << d
```
- Only trains r×(d+d) parameters instead of d×d
- Typical rank: r = 8-64 (vs d = 4096-8192)
- Reduces trainable params by 1000×+
- Paper: https://arxiv.org/abs/2106.09685

### QLoRA
- Quantize base model to 4-bit (NF4)
- Apply LoRA adapters in FP16/BF16
- Train a 70B model on a single 48GB GPU
- Paper: https://arxiv.org/abs/2305.14314

### DoRA (Weight-Decomposed LoRA)
- Decomposes weight into magnitude and direction
- Better than LoRA at same rank
- Paper: https://arxiv.org/abs/2402.09353

---

## 7. PREFERENCE DATASETS

| Dataset | Type | Size | Link |
|---------|------|------|------|
| **UltraFeedback** | Multi-aspect preference ratings | 64K | https://huggingface.co/datasets/openbmb/UltraFeedback |
| **HH-RLHF** (Anthropic) | Helpfulness + Harmlessness comparisons | 161K | https://huggingface.co/datasets/Anthropic/hh-rlhf |
| **Nectar** (Berkeley) | Ranked responses from multiple models | 183K | https://huggingface.co/datasets/berkeley-nest/Nectar |
| **Chatbot Arena Conversations** | Real user preference votes | Growing | https://huggingface.co/datasets/lmsys/chatbot_arena_conversations |
| **Argilla DPO Pairs** | Community-curated DPO datasets | Various | https://huggingface.co/argilla |

---

## 8. PRACTICAL GUIDE — "I Want to Fine-Tune a Model"

### Easiest Path (2026)
1. **Pick base model:** Llama 3.3 8B/70B or Qwen 2.5
2. **Pick method:** QLoRA + DPO (best quality/cost ratio)
3. **Pick tool:** Unsloth (fastest) or LLaMA-Factory (most features)
4. **Get data:** 1K-10K high-quality examples for SFT, 5K-50K preference pairs for DPO
5. **Compute:** Single 24GB GPU (RTX 4090) handles 8B QLoRA; 48GB (A6000) for 70B QLoRA
6. **Deploy:** Merge adapters → GGUF quantize → Ollama serve

### Cost Estimates
| What | Hardware | Time | Cost |
|------|----------|------|------|
| 8B LoRA SFT (1K examples) | RTX 4090 | ~30 min | ~$0.20 (cloud) |
| 8B QLoRA DPO (10K pairs) | RTX 4090 | ~2 hrs | ~$0.80 |
| 70B QLoRA SFT | A100 80GB | ~4 hrs | ~$8-12 |
| 70B Full fine-tune | 8× H100 | ~24 hrs | ~$500+ |

---

*Last updated: June 2026.*
