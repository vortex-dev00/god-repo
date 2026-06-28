# 🔀 LLM Gateways & Routers

> Unified APIs, cost optimization, model routing, and caching solutions.

---

# 🏆 AI Tools God Repo — Exhaustive Reference (June 2026)

---

## 2. LLM GATEWAYS & ROUTERS

### Primary Gateways

| Name | Description | URL | ⭐ Stars |
|------|-------------|-----|----------|
| **LiteLLM** | Open-source Python proxy providing unified OpenAI-compatible API for 200+ LLM providers; built-in caching, rate limiting, cost tracking | https://github.com/BerriAI/litellm | ~18,000 [?] |
| **Portkey AI Gateway** | Blazing-fast AI gateway with 50+ integrated guardrails; routes to 1,600+ LLMs with single API | https://github.com/Portkey-AI/gateway | ~12,200 |
| **OpenRouter** | Managed multi-model marketplace; 300+ models via single OpenAI-compatible endpoint; 5.5% markup on credits | https://openrouter.ai | — (SaaS) |
| **Martian** | First dedicated LLM router — uses model understanding to achieve higher performance at lower cost than any single provider | https://withmartian.com | — (SaaS) |
| **Braintrust Gateway** | Unified API for OpenAI, Anthropic, Google, AWS Bedrock, Vertex AI, Azure, Mistral; supports caching, logging, load balancing | https://www.braintrust.dev/docs/deploy/gateway | — (open-source) |
| **Cloudflare AI Gateway** | Edge-native proxy between code and any AI provider; adds caching, rate limiting, spend tracking, logs with zero code changes | https://developers.cloudflare.com/ai-gateway/ | — (SaaS) |
| **Kong AI Gateway** | Enterprise API gateway extended for AI traffic; same operational model, observability, and security controls as Kong API management | https://konghq.com/products/kong-ai-gateway | — (Enterprise) |
| **Requesty** | Managed AI gateway built in Rust; 400+ models, 8ms P50 overhead, smart routing, auto-caching (60% cost savings), EU data residency | https://www.requesty.ai | — (SaaS) |
| **Helicone** | Observability-first gateway; proxy overhead provides LLM monitoring, analytics, cost tracking with free tier | https://www.helicone.ai | ~3,000 [?] |
| **Traceloop Hub** | High-scale LLM gateway written in Rust with OpenTelemetry-based observability built in | https://github.com/traceloop/hub | ~500 [?] |

### Comparison Summary (2026)

| Platform | Models | Overhead (P50) | Pricing | Self-Host | Best For |
|----------|--------|---------------|---------|-----------|----------|
| LiteLLM | 200+ | 10-20ms | Free (self-host) | ✅ | Zero markup at scale |
| Portkey | 1,600+ | 10-20ms | Per-log pricing | Gateway only | Guardrails + enterprise observability |
| OpenRouter | 300+ | 40-55ms | 5.5% on credits | ❌ | Quick model access for solo devs |
| Requesty | 400+ | 8ms | 5% markup | ❌ | Production routing with caching |
| Cloudflare | Major providers | Sub-10ms at edge | Pay-per-request | ❌ | Cloudflare-native stacks |
| Kong | Provider-dependent | Varies | Enterprise license | ✅ | Teams already on Kong |
| Braintrust | Major providers | ~15ms | Free tier + usage | ✅ | Eval + gateway combined |
