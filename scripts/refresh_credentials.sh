#!/usr/bin/env bash
# refresh_credentials.sh
#
# Run this OUTSIDE of a Claude Code session to refresh your Max subscription
# credentials and push them to the GitHub Actions secret.
#
# Usage:
#   bash scripts/refresh_credentials.sh
#
# Requirements:
#   - claude CLI installed: npm install -g @anthropic-ai/claude-code
#   - gh CLI installed and authenticated: gh auth login
#   - Run from outside any active Claude Code session

set -e

REPO="Omrigotlieb/awesome-anthropic"
CREDS="$HOME/.claude/credentials.json"

echo "=== awesome-anthropic credentials refresh ==="
echo ""

# Check we're not inside Claude Code
if [ -n "$CLAUDECODE" ]; then
  echo "ERROR: This script must be run OUTSIDE of a Claude Code session."
  echo "Close Claude Code and run this from a regular terminal."
  exit 1
fi

# Trigger claude to refresh credentials
echo "Step 1: Refreshing Claude Code Max credentials..."
claude --print -p "ping" > /dev/null 2>&1 && echo "  ✓ Credentials refreshed" || {
  echo "  Running 'claude' to authenticate..."
  claude
}

# Verify credentials are fresh
EXPIRES=$(python3 -c "
import json
from datetime import datetime, timezone
d = json.load(open('$CREDS'))
o = d['claudeAiOauth']
dt = datetime.fromtimestamp(o['expiresAt']/1000, tz=timezone.utc)
now = datetime.now(tz=timezone.utc)
diff = dt - now
print(f'Expires: {dt.strftime(\"%Y-%m-%d %H:%M UTC\")}')
if diff.total_seconds() > 0:
    print(f'Valid for: {str(diff).split(\".\")[0]}')
    print('OK')
else:
    print('EXPIRED — run claude to login again')
    print('FAIL')
" 2>/dev/null)

echo "$EXPIRES"
if echo "$EXPIRES" | grep -q "FAIL"; then
  echo "Please run 'claude' manually to log in, then retry this script."
  exit 1
fi

# Upload to GitHub
echo ""
echo "Step 2: Uploading fresh credentials to GitHub Actions secret..."
gh secret set CLAUDE_CREDENTIALS \
  --repo "$REPO" \
  --body "$(cat "$CREDS")"

echo "  ✓ CLAUDE_CREDENTIALS secret updated on $REPO"
echo ""
echo "Done! GitHub Actions workflows will now use your Claude Code Max subscription."
echo "Run this script again whenever the credentials expire (roughly every few months)."
