<p align="center">
  <h1 align="center">🦞 Confucius Debug — AI Debugging That Never Repeats a Mistake</h1>
  <p align="center"><strong>Search 1,100+ solved AI agent bugs instantly. No match? AI fixes it and saves to KB — next person gets it free.</strong></p>
</p>

<p align="center">
  <a href="https://github.com/sstklen/confucius-debug/actions"><img src="https://img.shields.io/badge/GitHub_Action-Marketplace-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Action"/></a>
  <a href="https://github.com/sstklen/confucius-debug/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License"/></a>
  <a href="#mcp-server"><img src="https://img.shields.io/badge/MCP-Server-brightgreen?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6bTAgMThjLTQuNDIgMC04LTMuNTgtOC04czMuNTgtOCA4LTggOCAzLjU4IDggOC0zLjU4IDgtOCA4eiIvPjwvc3ZnPg==" alt="MCP Server"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/YanHui_KB-1,143_solutions-blue?style=for-the-badge" alt="1143 Solutions"/>
  <img src="https://img.shields.io/badge/Search-FREE_·_~150ms-green?style=for-the-badge" alt="Search Free"/>
  <img src="https://img.shields.io/badge/AI_Fix-$0.05_·_~6s-orange?style=for-the-badge" alt="AI Fix"/>
  <img src="https://img.shields.io/badge/Accuracy-9/9_confirmed-brightgreen?style=for-the-badge" alt="9/9 Confirmed"/>
</p>

<p align="center">
  <a href="#mcp-server"><strong>MCP Server →</strong></a>
  &nbsp;·&nbsp;
  <a href="#github-action"><strong>GitHub Action →</strong></a>
  &nbsp;·&nbsp;
  <a href="#openclaw-skill"><strong>OpenClaw Skill →</strong></a>
  &nbsp;·&nbsp;
  <a href="#api"><strong>REST API →</strong></a>
</p>

---

## The Philosophy

> **「不貳過」** — *Never repeat a mistake.* (Confucius on his student Yan Hui, Analects 6.3)

[Yan Hui (顏回)](https://en.wikipedia.org/wiki/Yan_Hui) was Confucius's favorite student — praised for never making the same mistake twice. We named our Knowledge Base after him: the **YanHui KB (不貳過知識庫)**.

**Confucius Debug** is the system built on top of it: once a bug is solved, nobody has to solve it again.

---

## How It Works

```
Your AI agent hits a bug
       │
       ▼
  Search YanHui KB ──── Found! → Instant fix (FREE, ~150ms)
       │
       Not found
       ▼
  Confucius AI analyzes ($0.05, ~6s)
       │
       ▼
  Fix saved to KB → Next person gets it FREE
```

**Your bugs help everyone. Everyone's bugs help you.**

---

## What Makes It Different

Most debug tools **wait for you to ask**. Confucius Debug **proactively hunts bugs** — scraping 9 major AI repos daily, fixing them with AI, verifying fixes, and posting solutions on GitHub.

| What we do | Numbers |
|------------|---------|
| Daily automated scraping | 9 repos (OpenClaw, Claude Code, MCP SDK, Anthropic SDK, Aider, Codex...) |
| Knowledge Base | **1,143** verified solutions (growing ~100/day) |
| Platform specialties | **12** (MCP, Telegram, Docker, OpenAI, Ollama, Discord...) |
| Fix quality (A-rate) | **80-100%** across all 12 platforms |
| GitHub replies posted | **280** |
| Confirmed correct | **9/9 = 100%** (0 corrections) |
| Notable | OpenClaw creator [verified our fix](https://github.com/openclaw/openclaw/issues/2019) and closed the issue |

**By the time you hit a bug, there's a good chance we already have the fix.**

---

## Install

### MCP Server (Recommended) {#mcp-server}

For **Claude Code**, **Claude Desktop**, or any MCP-compatible client:

```bash
claude mcp add confucius-debug --transport http https://api.washinmura.jp/mcp/debug -s user
```

Or add to your MCP config:

```json
{
  "mcpServers": {
    "confucius-debug": {
      "url": "https://api.washinmura.jp/mcp/debug"
    }
  }
}
```

Then tell your AI: *"Use debug_hello to set up"* — you get **10 free credits**.

### GitHub Action {#github-action}

```yaml
- name: Confucius Debug AI
  if: failure()
  uses: sstklen/confucius-debug@v1
  with:
    lobster-id: ${{ secrets.CONFUCIUS_LOBSTER_ID }}
```

4 lines. When CI fails, Confucius posts the fix on your PR.

### OpenClaw Skill {#openclaw-skill}

```
"Help me install the Confucius Debug skill"
```

See [`skills/confucius-debug/SKILL.md`](skills/confucius-debug/SKILL.md) for full details.

### REST API {#api}

```bash
# Search (always free)
curl -X POST https://api.washinmura.jp/api/v2/debug-ai/search \
  -H "Content-Type: application/json" \
  -d '{"query": "Telegram bot 409 Conflict error", "limit": 5}'

# AI analysis (when search returns nothing, $0.05)
curl -X POST https://api.washinmura.jp/api/v2/debug-ai \
  -H "Content-Type: application/json" \
  -d '{"error_description": "...", "lobster_id": "your-id"}'
```

---

## 4 Tools

| Tool | What it does | Cost |
|------|-------------|------|
| `debug_search` | Search YanHui KB for existing solutions | **Free** |
| `debug_analyze` | No match? AI solves it, saves to KB | $0.05 |
| `debug_contribute` | Share your own solutions back | **Free** |
| `debug_hello` | Scan your bug history, bulk-import to KB | **Free** + 10 credits |

**Workflow:** `debug_hello` (once) → `debug_search` (always free) → `debug_analyze` (only if needed)

---

## Platform Coverage

The YanHui KB specializes in AI agent bugs across 12 platforms:

| Platform | Solutions | Quality (A-Rate) |
|----------|-----------|-------------------|
| Anthropic / Claude | 392 | 80% |
| MCP (Model Context Protocol) | 261 | 87% |
| Telegram | 101 | 97% |
| Memory / RAG / Vector DB | 94 | 87% |
| Browser / WebSocket | 73 | 92% |
| OpenAI / GPT | 54 | 87% |
| Docker / K8s | 51 | 84% |
| Discord | 40 | 93% |
| Cron / Scheduler | 37 | 92% |
| WhatsApp | 16 | 94% |
| Google / Gemini | 15 | 100% |
| Ollama / Local LLM | 14 | 93% |

**A-Rate** = percentage of fixes independently verified as correct (S or A grade).

---

## How the KB Grows

An automated pipeline runs daily:

```
scrape (GitHub Issues) → verify → fix (AI analysis)
    → import (vector KB) → reply (GitHub) → track → learn
```

| Stage | What happens |
|-------|-------------|
| **Scrape** | Pull new issues from 9 AI repos |
| **Verify** | Grade existing solutions for quality |
| **Fix** | AI generates fixes for unsolved bugs |
| **Import** | Good fixes go into the YanHui KB (vector database) |
| **Reply** | Post solutions on GitHub with smart filtering |
| **Track** | Monitor community responses |
| **Learn** | Extract lessons from corrections to improve |

The KB grows by ~100 entries per day, automatically.

---

## Pricing

| Action | Cost |
|--------|------|
| Search KB | **Free** |
| Contribute to KB | **Free** |
| AI analysis (Sonnet/Opus) | **$0.05** |
| Onboarding (debug_hello) | **Free** + 10 credits gift |

---

<details>
<summary><b>GitHub Action — Full Setup Guide</b></summary>

### Quick Start (2 minutes)

#### 1. Get a free Lobster ID

```bash
claude mcp add confucius-debug --transport http https://api.washinmura.jp/mcp/debug -s user
```
Tell Claude: *"Use debug_hello to onboard"* → 10 free credits.

#### 2. Add to GitHub Secrets

Repo → `Settings` → `Secrets` → Add `CONFUCIUS_LOBSTER_ID`

#### 3. Add to workflow

```yaml
name: CI
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build
        id: build
        run: npm run build 2>&1 | tee /tmp/build-error.log
        continue-on-error: true

      - name: Confucius Debug AI
        if: steps.build.outcome == 'failure'
        uses: sstklen/confucius-debug@v1
        with:
          lobster-id: ${{ secrets.CONFUCIUS_LOBSTER_ID }}

      - name: Fail if build failed
        if: steps.build.outcome == 'failure'
        run: exit 1
```

### Inputs

| Input | Required | Default | Description |
|-------|----------|---------|-------------|
| `lobster-id` | Yes | - | Your Lobster ID |
| `error-log` | No | auto-capture | Custom error text |
| `comment` | No | `true` | Post fix as PR comment |
| `language` | No | `en` | Response language (en/zh/ja) |

### Outputs

| Output | Description |
|--------|-------------|
| `status` | `knowledge_hit`, `analyzed`, or `error` |
| `fix` | Full JSON response with fix details |
| `source` | `knowledge_base`, `sonnet`, or `opus` |
| `cost` | Cost in USD |

</details>

<details>
<summary><b>Security & Privacy</b></summary>

### What leaves your machine
Only the error description and error message you provide. No source code, no file contents, no environment variables.

### What's stored
Error descriptions and fixes in the YanHui KB. No PII beyond your chosen lobster-id.

### Automatic redaction
API keys, tokens, and passwords are filtered before sending.

### Data retention
Contributions are permanent — that's the point. Never repeat a mistake.

</details>

---

## Related Projects

| Project | What it does |
|---------|-------------|
| [112 Claude Code Skills](https://github.com/sstklen/washin-claude-skills) | Battle-tested coding patterns |
| [Zero Engineer](https://github.com/sstklen/zero-engineer) | How a non-engineer built all of this with AI |

---

<p align="center">
  <b>「不遷怒，不貳過。」</b><br>
  <i>"Never redirect anger, never repeat a mistake."</i><br><br>
  Built at <a href="https://washinmura.jp">Washin Village (和心村)</a> — an animal sanctuary in Japan, 28 cats & dogs 🐾<br>
  Powered by Claude (Anthropic) + the Confucius philosophy.<br><br>
  🦞 <i>The bigger the Knowledge Base, the stronger Confucius becomes.</i>
</p>
