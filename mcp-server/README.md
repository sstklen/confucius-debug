# Confucius Debug MCP Server 🦞

> *"不貳過" — Never repeat a mistake.* (Confucius, Analects 6.3)

AI debugging assistant backed by the **YanHui Knowledge Base** — 6,800+ scraped issues and 980+ verified fixes from real AI agent projects.

## Quick Start

### Option 1: Remote URL (Recommended)

For clients that support HTTP MCP (Claude Code, etc.):

```json
{
  "mcpServers": {
    "confucius-debug": {
      "url": "https://api.washinmura.jp/mcp/debug"
    }
  }
}
```

### Option 2: stdio proxy (via npx)

For clients that only support stdio (Claude Desktop, Cursor, etc.):

```json
{
  "mcpServers": {
    "confucius-debug": {
      "command": "npx",
      "args": ["-y", "confucius-debug-mcp"]
    }
  }
}
```

## Tools

| Tool | Cost | Description |
|------|------|-------------|
| `debug_search` | FREE | Search 980+ verified fixes instantly |
| `debug_analyze` | FREE | AI-powered root cause analysis |
| `debug_contribute` | FREE | Share your fix to help others |
| `debug_hello` | FREE | Build your local YanHui KB + earn 10U credits |

## How It Works

```
You hit a bug
    ↓
1. debug_search (FREE, instant)
    ↓
   Found? → Use the fix directly
   Not found? ↓
2. debug_analyze (FREE)
    ↓
   Fix saved to KB → Next person gets it FREE
```

## Links

- **GitHub**: [sstklen/confucius-debug](https://github.com/sstklen/confucius-debug)
- **API Docs**: [api.washinmura.jp/confucius](https://api.washinmura.jp/confucius)
- **By**: [Washin Village](https://washinmura.jp) — animal sanctuary, Boso Peninsula, Japan

## License

MIT
