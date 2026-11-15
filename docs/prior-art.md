# Prior art: open-source competitor and product research tools

*Surveyed November 2026. Open a PR if something is missing or out of date.*

## TL;DR

Plenty of projects **find competitors and compare them**. Very few go on to answer the product-design question: **which features should we build next, and why?** This repo reuses the best parts of the projects below and adds evidence grading, review mining and a transparent prioritization step.

## The landscape

### 1. End-to-end competitor intelligence apps

| Project | What it does | Stack | What we borrow | Limits |
|---|---|---|---|---|
| [awesome-llm-apps: AI Competitor Intelligence Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps) | Finds competitor URLs from a company URL or a description (Perplexity or Exa), scrapes them, produces a comparison table and an analysis | Streamlit, Agno, OpenAI, Firecrawl, Exa | Discovery from a URL *or* a description | Single-shot; no evidence links per cell; no prioritization |
| [Comp_Intell AI Competitor Intelligence System](https://github.com/the-developer-306/Comp_Intell-AI-Competitor-Intelligence-System) | Exa discovery, Firecrawl extraction, plus RAG over your own uploaded files | Python, FAISS, HuggingFace | Ingesting your own docs alongside web research | Business-info focus rather than feature-level |
| [n8n: Automate competitor research with Exa.ai, Notion & AI agents](https://www.neura.market/workflow/automate-competitor-research-with-exaai-notion-ai-agents) | Exa finds rivals; agents pull overview, products and reviews; results land in Notion | n8n, OpenAI, SerpApi, Firecrawl | Separate agents per research facet; reviews as a source | No-code and hard to version; no scoring |

### 2. General deep-research engines

| Project | What it does | Why it matters here |
|---|---|---|
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) (Apache-2.0) | Plans sub-questions, runs parallel searches, summarizes 20+ sources, writes a cited report; also ships as a Claude skill and an MCP server | The most mature open research loop. It could serve as a pluggable research backend for phase 1 or 3. It isn't competitor- or feature-aware by itself. |

### 3. Claude Code / agent skills for PMs

| Skill | Source | What we borrow |
|---|---|---|
| `competitive-analysis-process` | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | The six-step frame: landscape → product comparison → customer needs → business baseline → positioning → strategic direction |
| `competitive-brief` | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Framing around the decision: where to differentiate vs. reach parity |
| `discover-competitive-analysis` | [product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills) | Recording sources and confidence levels for every claim |
| `competitive-analysis` | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | Output set: profiles, matrix, win/loss, recommendations |

These are prompt frameworks. They structure the thinking well, but they don't fetch, grade or score anything on their own.

### 4. Commercial reference points (not open source)

- **Kasava competitor agent**: its output is the shape we want. A feature matrix, a positioning summary, *gaps* (they have it, we don't) and *advantages* (we're ahead), refreshed on a schedule.
- **Crayon, Klue, Kompyte**: battlecard and go-to-market enablement. Sales-oriented rather than product-design-oriented.
- **Scraping/search layers** (Firecrawl, Exa, Tavily, Browse AI, Apify): building blocks, not analyses.

## The gap this repo fills

| Capability | Apps (1) | Engines (2) | Skills (3) | **product-research** |
|---|:-:|:-:|:-:|:-:|
| Discover competitors from a description | ✅ | ➖ | ➖ | ✅ |
| Accept your own competitor list or docs | ➖ | ✅ | ✅ | ✅ |
| Feature-level, evidence-linked grades | ❌ | ❌ | ➖ | ✅ |
| User-need framing (job, not checkbox) | ❌ | ❌ | ➖ | ✅ |
| Review and complaint mining per feature | ➖ | ❌ | ❌ | ✅ |
| Transparent, editable prioritization math | ❌ | ❌ | ❌ | ✅ |
| Versioned, diffable runs in git | ❌ | ❌ | ➖ | ✅ |

✅ yes · ➖ partial · ❌ no

## Ideas not yet built (good first PRs)

- A GPT Researcher backend for phase 1 and 3.
- Browser-driven UX teardowns: screenshots and step counts for a key journey (signup → first value).
- Scheduled re-runs that diff `matrix.csv` and post "what changed" to Slack.
- Surface-specific rubrics: dashboards, onboarding, billing, settings.
