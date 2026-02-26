# Claude Code Ecosystem

> The definitive developer reference for Claude Code — Anthropic's agentic coding environment available in your terminal, IDE, desktop app, and browser. Last updated February 2026.

---

## What is Claude Code?

Claude Code is an AI-powered coding assistant that understands your entire codebase and can work autonomously across multiple files and tools to build features, fix bugs, write tests, and automate development tasks. It is not a chat-style autocomplete tool — it is an agentic system that reads your codebase, edits files, runs commands, and integrates with your development tools.

### Key differentiators vs. other coding assistants

| Feature | Claude Code | GitHub Copilot | Cursor |
|---|---|---|---|
| **Architecture** | Agentic — plans, executes, verifies | Inline autocomplete + chat | Fork of VS Code with chat |
| **Multi-file reasoning** | Full codebase understanding | Limited to open files | Limited to open files |
| **CLI-first** | Terminal, IDE, Desktop, Web | IDE-only | IDE-only |
| **MCP integration** | Native, 100s of servers | None | None |
| **Custom automation** | Hooks, Skills, Subagents | None | None |
| **Remote sessions** | Remote Control (mobile/browser) | None | None |
| **Multi-agent** | Native subagent orchestration | None | Limited |
| **Extensibility** | Plugin marketplace, open standard skills | Extensions only | Extensions only |

### Install Claude Code

```bash
# macOS / Linux / WSL (recommended — auto-updates)
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# Homebrew (does not auto-update)
brew install --cask claude-code

# WinGet
winget install Anthropic.ClaudeCode
```

Then start Claude Code in any project:

```bash
cd your-project
claude
```

Official documentation: [code.claude.com/docs](https://code.claude.com/docs/en/overview)

---

## Remote Control (New — February 2026)

Launched February 24, 2026, Remote Control lets you continue a local Claude Code session from your phone, tablet, or any browser. Start a task at your desk, put your laptop in a bag, and keep full control from your phone.

### How it works

Remote Control is a synchronization layer that bridges your local terminal with the Claude mobile app and web interface. Your session keeps running on your local machine — your filesystem, MCP servers, tools, and project configuration all stay available. The web and mobile interfaces are just a window into that local process.

Claude Code makes outbound HTTPS requests only and never opens inbound ports. All traffic travels through the Anthropic API over TLS. The connection uses multiple short-lived credentials, each scoped to a single purpose.

### Setup

```bash
# Start a new remote session from your project directory
claude remote-control

# Or, from an existing session, use the slash command
/remote-control
# alias: /rc
```

- The terminal displays a session URL and a QR code (press spacebar to toggle the QR display).
- Scan the QR code with your phone to open the session in the Claude iOS or Android app.
- Open [claude.ai/code](https://claude.ai/code) in any browser to connect via the session URL.

### Enable for all sessions automatically

Run `/config` inside Claude Code and set **Enable Remote Control for all sessions** to `true`.

### What you can do remotely

- See exactly what Claude is doing in real-time
- Approve or reject file changes
- Provide additional instructions or redirect the work
- Send messages interchangeably from terminal, browser, and phone — the conversation stays in sync
- Survive interruptions: the session reconnects automatically if your laptop sleeps or your network drops

### Availability and limitations

| Item | Detail |
|---|---|
| **Availability** | Research preview on Max plans; Pro plan support coming soon |
| **API keys** | Not supported — requires claude.ai subscription login |
| **Concurrent connections** | One remote connection per Claude Code instance |
| **Terminal** | Must stay open — closing the terminal ends the session |
| **Network timeout** | ~10-minute outage before session times out |

### Remote Control vs. Claude Code on the web

| | Remote Control | Claude Code on the Web |
|---|---|---|
| **Where it runs** | Your local machine | Anthropic cloud infrastructure |
| **Local filesystem** | Available | Not available |
| **MCP servers** | Your local servers available | Cloud-configured only |
| **Use when** | Continuing local work from another device | Starting fresh tasks without local setup |

Official documentation: [code.claude.com/docs/en/remote-control](https://code.claude.com/docs/en/remote-control)

---

## MCP Servers (Model Context Protocol)

The Model Context Protocol (MCP) is an open standard for connecting AI tools to external data sources and services. With MCP, Claude Code can read your design docs in Figma, update tickets in Jira, pull data from Slack, query your database, or use your own custom tooling.

Official MCP site: [modelcontextprotocol.io](https://modelcontextprotocol.io)
MCP server registry: [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
Anthropic tools repo: [github.com/anthropics/anthropic-tools](https://github.com/anthropics/anthropic-tools)

### Popular MCP servers

| Name | Description | Install command |
|---|---|---|
| **GitHub** | Create issues, review PRs, manage repos | `claude mcp add --transport http github https://api.githubcopilot.com/mcp/` |
| **Sentry** | Debug production errors and stack traces | `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp` |
| **Notion** | Read and write Notion docs and databases | `claude mcp add --transport http notion https://mcp.notion.com/mcp` |
| **Asana** | Manage tasks and projects | `claude mcp add --transport sse asana https://mcp.asana.com/sse` |
| **Stripe** | Query payments, customers, subscriptions | `claude mcp add --transport http stripe https://mcp.stripe.com` |
| **HubSpot** | CRM contacts, deals, and pipelines | `claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic` |
| **PayPal** | Payments and transaction data | `claude mcp add --transport http paypal --scope project https://mcp.paypal.com/mcp` |
| **PostgreSQL / DBHub** | Query any SQL database naturally | `claude mcp add --transport stdio db -- npx -y @bytebase/dbhub --dsn "postgresql://..."` |
| **Filesystem** | Read/write local files with controlled access | `claude mcp add --transport stdio filesystem -- npx -y @modelcontextprotocol/server-filesystem /path` |
| **Airtable** | Read/write Airtable bases | `claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable -- npx -y airtable-mcp-server` |
| **Playwright** | Browser automation and UI testing | `claude mcp add --transport stdio playwright -- npx -y @playwright/mcp@latest` |

### Installing MCP servers

**HTTP server (recommended for cloud services):**
```bash
claude mcp add --transport http <name> <url>

# With authentication header
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

**Local stdio server (for tools needing system access):**
```bash
claude mcp add --transport stdio --env KEY=value <name> -- npx -y <package>
```

**OAuth authentication:**
```bash
# After adding the server, authenticate inside Claude Code
/mcp
# Follow browser prompts to log in
```

### MCP installation scopes

| Scope | Flag | Where stored | Who can use it |
|---|---|---|---|
| `local` (default) | `--scope local` | `~/.claude.json` | You, in this project |
| `project` | `--scope project` | `.mcp.json` (commit to git) | Everyone on the team |
| `user` | `--scope user` | `~/.claude.json` | You, in all projects |

### Managing your servers

```bash
claude mcp list          # List all configured servers
claude mcp get github    # Details for a specific server
claude mcp remove github # Remove a server

# Inside Claude Code
/mcp                     # View status and authenticate
```

### Using MCP from Claude.ai

If you log into Claude Code with a Claude.ai account, MCP servers configured at [claude.ai/settings/connectors](https://claude.ai/settings/connectors) are automatically available in Claude Code.

### Advanced: MCP Tool Search

When you have many MCP servers, their tool definitions can consume large portions of your context window. Claude Code automatically enables Tool Search when MCP tool descriptions exceed 10% of the context window, dynamically loading tools on demand rather than preloading all of them.

Control this behavior with the `ENABLE_TOOL_SEARCH` environment variable:
- `auto` (default): activates when tools exceed 10% of context
- `auto:5`: custom 5% threshold
- `true`: always enabled
- `false`: disabled

---

## Skills and Slash Commands

Skills extend what Claude can do. Create a `SKILL.md` file and Claude adds it to its toolkit — using it automatically when relevant, or you can invoke it directly with `/skill-name`.

Claude Code skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools.

### Built-in commands

| Command | Description |
|---|---|
| `/help` | Show available commands and shortcuts |
| `/compact` | Compact conversation to free context space |
| `/compact <instructions>` | Compact with custom focus (e.g., `/compact Focus on API changes`) |
| `/clear` | Reset context window |
| `/mcp` | View MCP server status and authenticate |
| `/hooks` | Interactive hook configuration menu |
| `/agents` | Manage subagents interactively |
| `/memory` | Open and edit memory files |
| `/init` | Generate a starter CLAUDE.md for your project |
| `/permissions` | View and configure permission settings |
| `/config` | Open Claude Code settings |
| `/model` | Switch model for this session |
| `/remote-control` or `/rc` | Start a Remote Control session |
| `/desktop` | Hand off session to the Desktop app |
| `/rewind` | Open checkpoint rewind menu |
| `/rename` | Give the current session a descriptive name |
| `/resume` | Resume a previous session |

### Creating custom skills

Skills live in `SKILL.md` files in a skill directory.

```
~/.claude/skills/my-skill/SKILL.md    # Personal skill (all projects)
.claude/skills/my-skill/SKILL.md      # Project skill (this project)
```

**Example: `/fix-issue` skill**

```yaml
# .claude/skills/fix-issue/SKILL.md
---
name: fix-issue
description: Fix a GitHub issue by number
disable-model-invocation: true
---

Analyze and fix GitHub issue $ARGUMENTS:

1. Use `gh issue view $ARGUMENTS` to get the issue details
2. Understand the problem described
3. Search the codebase for relevant files
4. Implement the fix
5. Write and run tests to verify
6. Create a descriptive commit and open a PR
```

Invoke with: `/fix-issue 1234`

### Frontmatter reference

| Field | Description |
|---|---|
| `name` | Slash command name (e.g., `name: review-pr` → `/review-pr`) |
| `description` | When Claude should use the skill automatically |
| `disable-model-invocation` | Set `true` to require manual invocation only |
| `user-invocable` | Set `false` to hide from the `/` menu (background knowledge) |
| `allowed-tools` | Tools Claude can use without asking when this skill is active |
| `model` | Model to use when this skill is active |
| `context` | Set to `fork` to run in an isolated subagent context |
| `argument-hint` | Autocomplete hint (e.g., `[issue-number]`) |

### Skill invocation control

| Setting | You can invoke | Claude can invoke |
|---|---|---|
| (default) | Yes | Yes |
| `disable-model-invocation: true` | Yes | No |
| `user-invocable: false` | No | Yes |

### Community skill collections

- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — 21k+ stars, curated skills, hooks, and commands
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) — practical skills for common workflows
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — skills for Claude.ai, Claude Code, and the API
- [obra/superpowers](https://github.com/obra/superpowers) — battle-tested skill library: TDD, debugging, collaboration patterns

---

## Hooks and Automation

Hooks are user-defined shell commands (or LLM-evaluated prompts) that execute automatically at specific points in Claude Code's lifecycle. Unlike CLAUDE.md instructions which are advisory, hooks are deterministic — they guarantee the action happens every time.

### Hook events

| Event | When it fires | Can block? |
|---|---|---|
| `SessionStart` | Session begins or resumes | No |
| `UserPromptSubmit` | When you submit a prompt | Yes (exit 2) |
| `PreToolUse` | Before a tool call executes | Yes (exit 2) |
| `PermissionRequest` | When a permission dialog appears | Yes |
| `PostToolUse` | After a tool call succeeds | Yes (exit 2) |
| `PostToolUseFailure` | After a tool call fails | No |
| `Notification` | When Claude needs your attention | No |
| `SubagentStart` | When a subagent is spawned | No |
| `SubagentStop` | When a subagent finishes | No |
| `Stop` | When Claude finishes responding | Yes (exit 2 continues) |
| `PreCompact` | Before context compaction | No |
| `ConfigChange` | When a config file changes during session | Yes |
| `WorktreeCreate` | When a worktree is being created | Yes |
| `WorktreeRemove` | When a worktree is being removed | No |
| `SessionEnd` | When a session terminates | No |

### Hook configuration

Hooks are configured in `settings.json` files:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
          }
        ]
      }
    ]
  }
}
```

### Matchers

Matchers filter when a hook fires. They are regex patterns matched against the relevant field for each event type.

| Event | Matcher filters |
|---|---|
| `PreToolUse`, `PostToolUse` | Tool name (e.g., `Bash`, `Edit\|Write`, `mcp__github__.*`) |
| `SessionStart` | Session source: `startup`, `resume`, `clear`, `compact` |
| `SessionEnd` | Exit reason: `clear`, `logout`, `prompt_input_exit`, `other` |
| `Notification` | Type: `permission_prompt`, `idle_prompt`, `auth_success` |
| `SubagentStart/Stop` | Agent type name (e.g., `Explore`, `Plan`, custom names) |
| `PreCompact` | Trigger: `manual`, `auto` |
| `ConfigChange` | Source: `user_settings`, `project_settings`, `skills` |

### Exit codes

| Exit code | Behavior |
|---|---|
| `0` | Action proceeds. Stdout (if any) is added to Claude's context. |
| `2` | Action is blocked. Stderr message is fed back to Claude as feedback. |
| Other | Action proceeds. Stderr is logged but not shown to Claude. |

### Example hook: desktop notification when Claude needs input

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

### Example hook: auto-format after file edits

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
          }
        ]
      }
    ]
  }
}
```

### Example hook: block writes to protected files

```bash
#!/bin/bash
# .claude/hooks/protect-files.sh

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
PROTECTED_PATTERNS=(".env" "package-lock.json" ".git/")

for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$FILE_PATH" == *"$pattern"* ]]; then
    echo "Blocked: $FILE_PATH matches protected pattern '$pattern'" >&2
    exit 2
  fi
done

exit 0
```

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/protect-files.sh" }]
      }
    ]
  }
}
```

### Hook storage locations

| File | Scope |
|---|---|
| `~/.claude/settings.json` | All your projects |
| `.claude/settings.json` | This project (commit to git) |
| `.claude/settings.local.json` | This project, not committed |
| Skill/agent frontmatter `hooks:` | While that skill/agent is active |

### Hook types

Claude Code supports three hook types:

- **`type: "command"`** — Runs a shell command (most common)
- **`type: "prompt"`** — Sends a prompt to a Claude model (Haiku by default) for judgment-based decisions. Returns `{"ok": true}` or `{"ok": false, "reason": "..."}`
- **`type: "agent"`** — Spawns a subagent with tool access for verification tasks that require reading files or running commands

Official documentation: [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide)

---

## IDE Integrations

Claude Code's underlying engine is shared across all surfaces — your `CLAUDE.md` files, settings, and MCP servers work everywhere.

### VS Code (Official)

Install: [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) or run `ext install anthropic.claude-code`

Also works in [Cursor](cursor:extension/anthropic.claude-code) and other VS Code forks.

**Requirements:** VS Code 1.98.0 or higher.

**Key features:**
- Inline diffs with side-by-side change review
- Plan mode — Claude describes what it will do and waits for approval before making changes
- `@`-mentions to reference files, folders, and specific line ranges
- Conversation history with search and resume
- Multiple conversations in separate tabs or windows
- Checkpoints — hover any message to rewind code and/or conversation to that point
- Resume remote sessions from Claude.ai directly in VS Code
- Browser automation via `@browser` with the Claude Chrome extension
- Automatic selection context sharing

**Keyboard shortcuts:**
| Shortcut | Action |
|---|---|
| `Cmd+Esc` / `Ctrl+Esc` | Toggle focus between editor and Claude |
| `Cmd+Shift+Esc` / `Ctrl+Shift+Esc` | Open new conversation as tab |
| `Option+K` / `Alt+K` | Insert `@`-mention for current selection |
| `Cmd+N` / `Ctrl+N` | New conversation (when Claude is focused) |

Docs: [code.claude.com/docs/en/vs-code](https://code.claude.com/docs/en/vs-code)

### JetBrains (Official)

Plugin: [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)

**Supported IDEs:** IntelliJ IDEA, PyCharm, WebStorm, PhpStorm, GoLand, Android Studio

**Key features:**
- Interactive diff viewing in the IDE diff viewer
- Automatic selection context sharing with Claude
- File reference shortcuts (`Cmd+Option+K` / `Alt+Ctrl+K`)
- Diagnostic error sharing (lint, syntax errors shared automatically)
- Quick launch with `Cmd+Esc` / `Ctrl+Esc`

**Usage:**
```bash
# Run Claude from your IDE's integrated terminal
claude
# Or connect an external terminal session to your IDE
claude
/ide
```

Docs: [code.claude.com/docs/en/jetbrains](https://code.claude.com/docs/en/jetbrains)

### Neovim (Community)

The Neovim community has built plugins that implement the same WebSocket-based MCP protocol used by the official VS Code extension, providing feature-equivalent integration.

| Plugin | Stars | Description |
|---|---|---|
| [coder/claudecode.nvim](https://github.com/coder/claudecode.nvim) | Active | Full IDE integration, reverse-engineered from VS Code extension |
| [greggh/claude-code.nvim](https://github.com/greggh/claude-code.nvim) | Active | Seamless Neovim integration for Claude Code |

### Emacs (Community)

| Package | Description |
|---|---|
| [manzaltu/claude-code-ide.el](https://github.com/manzaltu/claude-code-ide.el) | Native IDE integration via MCP, bidirectional bridge |
| [stevemolitor/claude-code.el](https://github.com/stevemolitor/claude-code.el) | Emacs interface for Claude Code CLI |

Presented at [EmacsConf 2025](https://emacsconf.org/2025/talks/claude-code/).

---

## Multi-Agent Workflows

Claude Code has a native multi-agent system for orchestrating specialized AI assistants that work in isolated contexts.

### Subagents

Subagents are specialized AI assistants defined in Markdown files with YAML frontmatter. Each runs in its own context window with a custom system prompt, specific tool access, and independent permissions.

**Built-in subagents:**

| Agent | Model | Purpose |
|---|---|---|
| `Explore` | Haiku (fast) | Read-only codebase search and analysis |
| `Plan` | Inherits | Research for plan mode (read-only) |
| `general-purpose` | Inherits | Complex multi-step tasks with full tool access |
| `Bash` | Inherits | Running terminal commands in separate context |

**Creating custom subagents:**

```markdown
# .claude/agents/security-reviewer.md
---
name: security-reviewer
description: Reviews code for security vulnerabilities. Use proactively after code changes.
tools: Read, Grep, Glob, Bash
model: opus
---

You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.
```

**Subagent frontmatter fields:**

| Field | Description |
|---|---|
| `name` | Unique identifier (lowercase letters and hyphens) |
| `description` | When Claude should delegate to this agent |
| `tools` | Allowed tools (inherits all if omitted) |
| `disallowedTools` | Tools to deny |
| `model` | `sonnet`, `opus`, `haiku`, or `inherit` |
| `permissionMode` | `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | Maximum agentic turns before stopping |
| `skills` | Skills to preload into agent context at startup |
| `memory` | Persistent memory scope: `user`, `project`, or `local` |
| `background` | Set `true` to always run as background task |
| `isolation` | Set `worktree` to run in an isolated git worktree |

**Subagent scopes:**

| Location | Scope | Priority |
|---|---|---|
| `--agents` CLI flag | Current session only | 1 (highest) |
| `.claude/agents/` | This project | 2 |
| `~/.claude/agents/` | All your projects | 3 |
| Plugin's `agents/` directory | Where plugin is enabled | 4 (lowest) |

### Parallel patterns

**Parallel research:**
```
Research the authentication, database, and API modules in parallel using separate subagents
```

**Writer / Reviewer pattern:**
```
Use a subagent to implement the rate limiter, then use the security-reviewer
subagent to audit the implementation before committing
```

**Chain subagents:**
```
Use the code-reviewer subagent to find performance issues, then use the
optimizer subagent to fix them
```

### Agent Teams

For sustained parallelism across independent sessions, [Agent Teams](https://code.claude.com/docs/en/agent-teams) coordinate multiple Claude Code processes with shared tasks, messaging, and a team lead. Each worker gets its own independent context window, avoiding the context accumulation problem of single-session subagents.

### Persistent memory for agents

Subagents can maintain persistent memory across sessions:

```yaml
---
name: code-reviewer
description: Reviews code for quality and best practices
memory: user
---

You are a code reviewer. Update your memory with patterns and conventions
you discover. This builds institutional knowledge across conversations.
```

Memory locations:
- `user` → `~/.claude/agent-memory/<name>/` (all projects)
- `project` → `.claude/agent-memory/<name>/` (shareable via git)
- `local` → `.claude/agent-memory-local/<name>/` (not committed)

Official documentation: [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)

---

## Tips and Power Features

### CLAUDE.md — Persistent instructions

`CLAUDE.md` is a markdown file that Claude reads at the start of every session. Use it for project conventions, build commands, code style, and architectural decisions that Claude cannot infer from code alone.

**File locations:**

| Location | Scope |
|---|---|
| `~/.claude/CLAUDE.md` | All your projects |
| `./CLAUDE.md` or `./.claude/CLAUDE.md` | This project (commit to git) |
| `./CLAUDE.local.md` | This project, private (auto-gitignored) |
| `./.claude/rules/*.md` | Modular rules, optionally scoped to file paths |
| `/Library/Application Support/ClaudeCode/CLAUDE.md` | macOS organization-wide (managed by IT) |

Bootstrap a CLAUDE.md for your project:
```
/init
```

**What to include vs. exclude:**

| Include | Exclude |
|---|---|
| Bash commands Claude can't guess | Things Claude can infer from code |
| Code style rules differing from defaults | Standard language conventions |
| Testing instructions and preferred runners | Detailed API docs (link instead) |
| Branch naming and PR conventions | Information that changes frequently |
| Architectural decisions | File-by-file codebase descriptions |
| Required environment variables | Self-evident practices |

**CLAUDE.md imports:**
```markdown
See @README.md for project overview and @package.json for npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
- Personal overrides: @~/.claude/my-project-instructions.md
```

**Modular rules with `.claude/rules/`:**
```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API Development Rules
- All endpoints must include input validation
- Use standard error response format
```

### Extended thinking

Extended thinking lets Claude spend additional time reasoning through complex problems before responding. Enable it in the VS Code command menu (`/`) or include the word `ultrathink` anywhere in a skill's content.

Best used for:
- Complex architectural decisions
- Hard bugs requiring multi-step reasoning
- Mathematical or algorithmic problems
- Security analysis

### Plan Mode

Plan Mode lets Claude explore your codebase and propose what it will do before making any changes. Claude reads files and answers questions without writing code until you approve the plan.

```bash
# In VS Code: click the mode indicator at bottom of prompt box
# In CLI: Ctrl+Shift+H or run /plan
```

Workflow:
1. Enter Plan Mode — Claude reads and explores, no changes
2. Ask Claude to create an implementation plan
3. Edit the plan if needed (`Ctrl+G` opens plan in your editor)
4. Switch to Normal Mode to execute

### Headless / scripted mode

Run Claude Code non-interactively for CI pipelines and automation:

```bash
# One-off query
claude -p "Explain what this project does"

# Structured JSON output
claude -p "List all API endpoints" --output-format json

# Streaming JSON
claude -p "Analyze this log file" --output-format stream-json

# Pipe data in
cat error.log | claude -p "Summarize the errors and suggest fixes"

# Fan out across files
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue" --allowedTools "Edit,Bash(git commit *)"
done
```

### Checkpoints and rewinding

Every action Claude takes creates a checkpoint. Double-tap `Escape` or run `/rewind` to open the rewind menu with three options:

- **Fork conversation from here** — new branch, keep code as-is
- **Rewind code to here** — revert file changes, keep full history
- **Fork conversation and rewind code** — new branch + revert files

Checkpoints persist across sessions, so you can close your terminal and still rewind later.

### Git worktrees for parallel sessions

Run multiple isolated Claude Code sessions on the same repo simultaneously:

```bash
# Start Claude in an isolated worktree
claude --worktree feature-auth

# Each worktree has its own files and branch,
# but shares git history with the main repo
```

The Desktop app and Claude Code on the web also support parallel sessions with visual management.

### Web search

Claude Code can fetch web content and documentation during sessions. Use `/permissions` to allowlist frequently-used domains for seamless access without repeated prompts.

### Auto memory

Claude Code automatically saves useful context across sessions — project patterns, build commands, debugging insights, and your preferences. Toggle it with `/memory` → auto-memory toggle.

Auto memory stores notes at: `~/.claude/projects/<project>/memory/MEMORY.md`

The first 200 lines of `MEMORY.md` are loaded into every session. Detailed notes go into topic files (`debugging.md`, `patterns.md`) that Claude reads on demand.

Ask Claude to save specific things:
```
Remember that we use pnpm, not npm
Save to memory that the API tests require a local Redis instance
```

### Prompt caching

Claude Code automatically uses Anthropic's prompt caching to reduce costs and latency on repeated context. CLAUDE.md content, system prompts, and frequently-accessed files are cached automatically — no configuration needed.

### Sandbox mode

Enable OS-level isolation that restricts Claude's filesystem and network access:

```bash
# Start a sandboxed session
claude --sandbox

# Or from within a session
/sandbox
```

Sandboxing lets Claude work more freely within defined boundaries without bypassing all permission checks.

### Context management

Context is your primary constraint — performance degrades as the context window fills.

```bash
/compact                          # Compact with auto-summary
/compact Focus on the API changes # Compact with custom focus
/clear                            # Full reset between unrelated tasks
```

Monitor context usage with a custom status line:
```bash
/statusline
```

---

## Community Resources

### Official

| Resource | Link |
|---|---|
| Documentation | [code.claude.com/docs](https://code.claude.com/docs/en/overview) |
| Claude Code homepage | [code.claude.com](https://code.claude.com) |
| GitHub (issues, examples) | [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code) |
| Anthropic Discord | [discord.gg/anthropic](https://www.anthropic.com/discord) |
| MCP Protocol site | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| Anthropic Tools repo | [github.com/anthropics/anthropic-tools](https://github.com/anthropics/anthropic-tools) |
| Agent Skills standard | [agentskills.io](https://agentskills.io) |

### Community collections

| Resource | Stars | Description |
|---|---|---|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 21k+ | The canonical awesome list: skills, hooks, commands, agents, plugins |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Active | Practical skills for common workflows |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Active | Skills for Claude.ai, Claude Code, and the API |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Active | Curated MCP server directory |
| [obra/superpowers](https://github.com/obra/superpowers) | Active | Battle-tested core skills library |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Official | Official MCP server implementations |

### Discussion communities

| Community | Link |
|---|---|
| Reddit r/ClaudeAI | [reddit.com/r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) |
| Reddit r/anthropic | [reddit.com/r/anthropic](https://www.reddit.com/r/anthropic/) |
| GitHub Discussions | [github.com/anthropics/claude-code/discussions](https://github.com/anthropics/claude-code/discussions) |

### Tutorials and guides

- [Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices) — official Anthropic guide with patterns from internal teams
- [How to Write a Good CLAUDE.md](https://www.builder.io/blog/claude-md-guide) — builder.io deep dive
- [Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) — HumanLayer guide
- [Claude Code Remote Control Guide](https://code.claude.com/docs/en/remote-control) — official Remote Control documentation
- [Common Workflows](https://code.claude.com/docs/en/common-workflows) — official step-by-step recipes
- [ClaudeLog](https://claudelog.com/) — community docs, guides, and tutorials

---

*Page maintained as part of the [Awesome Anthropic](https://github.com/anthropics/awesome-anthropic) resource collection. Content sourced from official Anthropic documentation at [code.claude.com/docs](https://code.claude.com/docs) and verified against live sources as of February 2026.*
