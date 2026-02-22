# YanHui Debug AI - GitHub Action

> **One Claw debugs, all Claws benefit.**
> CI fails? YanHui remembers every bug ever solved across all users. Get instant fixes from a shared AI knowledge base.

## How it works

```
CI fails  -->  YanHui checks 194+ known bugs (4ms)
          -->  Not found? Sonnet 4.6 analyzes ($0.05)
          -->  Fix saved to KB for everyone
          -->  Next person with same bug = instant fix ($0.02)
```

## Quick Start

```yaml
# .github/workflows/ci.yml
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

      - name: YanHui Debug AI
        if: steps.build.outcome == 'failure'
        uses: washinmura/yanhui-ci@v1
        with:
          claw-id: ${{ secrets.YANHUI_CLAW_ID }}

      - name: Fail if build failed
        if: steps.build.outcome == 'failure'
        run: exit 1
```

## With test errors

```yaml
      - name: Run tests
        id: test
        run: npm test 2>&1 | tee /tmp/test-output.log
        continue-on-error: true

      - name: YanHui Debug AI
        if: steps.test.outcome == 'failure'
        uses: washinmura/yanhui-ci@v1
        with:
          claw-id: ${{ secrets.YANHUI_CLAW_ID }}
          # Auto-detects /tmp/test-output.log — no config needed!
```

## With custom error text

```yaml
      - name: Build
        id: build
        run: npm run build 2>&1 | tee /tmp/build.log
        continue-on-error: true

      - name: Capture error
        if: steps.build.outcome == 'failure'
        id: capture
        run: |
          ERROR=$(tail -50 /tmp/build.log)
          echo "error<<EOF" >> $GITHUB_OUTPUT
          echo "$ERROR" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: YanHui Debug AI
        if: steps.build.outcome == 'failure'
        uses: washinmura/yanhui-ci@v1
        with:
          claw-id: ${{ secrets.YANHUI_CLAW_ID }}
          error-log: ${{ steps.capture.outputs.error }}
```

## With PR comments

```yaml
      - name: YanHui Debug AI
        if: failure()
        uses: washinmura/yanhui-ci@v1
        with:
          claw-id: ${{ secrets.YANHUI_CLAW_ID }}
          comment: 'true'  # Posts fix as PR comment (updates on re-run)
```

## Inputs

| Input | Required | Default | Description |
|-------|----------|---------|-------------|
| `claw-id` | Yes | - | Your Claw ID for billing |
| `error-log` | No | auto-capture | Custom error text |
| `auto-fix` | No | `false` | Create PR with fix (coming soon) |
| `comment` | No | `true` | Post fix as PR comment |
| `api-url` | No | production | Custom API endpoint |
| `language` | No | `en` | Response language (en/zh/ja) |
| `github-token` | No | `github.token` | Token for PR comments |

## Outputs

| Output | Description |
|--------|-------------|
| `status` | `knowledge_hit`, `analyzed`, or `error` |
| `fix` | Full JSON response with fix details |
| `source` | `knowledge_base`, `sonnet_4.6`, or `opus_local` |
| `cost` | Cost in USD |
| `entry-id` | KB entry ID (for feedback) |

## Use outputs in subsequent steps

```yaml
      - name: YanHui Debug AI
        id: yanhui
        if: failure()
        uses: washinmura/yanhui-ci@v1
        with:
          claw-id: ${{ secrets.YANHUI_CLAW_ID }}

      - name: Check if KB hit
        if: steps.yanhui.outputs.status == 'knowledge_hit'
        run: echo "Found in KB! This bug was solved before."
```

## Pricing

| Scenario | Cost | Speed |
|----------|------|-------|
| KB hit (someone solved this before) | $0.02 | ~4ms |
| New analysis (Sonnet 4.6) | $0.05 | ~6s |
| New analysis (Opus 4.6) | $0.07 | ~8s |
| Search only | Free | ~150ms |

## Get a Claw ID

1. Add [YanHui MCP](https://api.washinmura.jp/mcp/debug) to Claude Code:
   ```
   claude mcp add yanhui-debug --transport http https://api.washinmura.jp/mcp/debug -s user
   ```
2. Tell Claude: "Use debug_hello to onboard" - free 10 credits!
3. Add your Claw ID to GitHub Secrets: `Settings > Secrets > YANHUI_CLAW_ID`

## How the shared KB works

Every bug solved by any user goes into the shared knowledge base. When you hit the same bug, you get the fix instantly for $0.02 instead of $0.05.

```
User A: CI fails with "ENOENT" → Sonnet analyzes ($0.05) → Fix saved to KB
User B: Same "ENOENT" error → KB hit ($0.02, 4ms) → Instant fix!
User C: Similar error → KB hit ($0.02, 4ms) → Instant fix!
```

The more users, the stronger the KB. Your bugs help everyone.

## Auto-detected log files

YanHui auto-captures errors from these locations (no config needed):

| File | When to use |
|------|-------------|
| `/tmp/build-error.log` | `npm run build 2>&1 \| tee /tmp/build-error.log` |
| `/tmp/test-output.log` | `npm test 2>&1 \| tee /tmp/test-output.log` |
| `/tmp/ci-error.log` | General CI errors |
| `/tmp/lint-output.log` | Linter output |

Or use the `error-log` input for full control.

## Security & Privacy

- **Secret filtering**: API keys, tokens, passwords, and emails are automatically redacted before sending
- **No source code**: Only error messages and stack traces are sent
- **Claw ID masking**: Your Claw ID is never printed in CI logs
- **Minimal data**: Only the last 50 lines of error output are captured
- **Your Claw ID** is used only for billing

## License

MIT
