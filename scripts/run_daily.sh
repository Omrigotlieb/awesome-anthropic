#!/usr/bin/env bash
# run_daily.sh — runs locally (or via launchd) to update the repo daily.
#
# Uses your Claude Code Max subscription via the `claude` CLI.
# No GitHub Actions, no secrets needed.
#
# Setup (one-time):
#   chmod +x scripts/run_daily.sh
#   bash scripts/setup_launchd.sh   # installs macOS daily scheduler
#
# Manual run:
#   bash scripts/run_daily.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$REPO_DIR/logs/run_daily.log"
mkdir -p "$REPO_DIR/logs"

log() { echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] $*" | tee -a "$LOG"; }

log "=== awesome-anthropic daily update ==="
cd "$REPO_DIR"

DEFAULT_BRANCH="$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##')"
if [ -z "$DEFAULT_BRANCH" ]; then
  DEFAULT_BRANCH="main"
fi

log "Ensuring run executes on ${DEFAULT_BRANCH}..."
git checkout "$DEFAULT_BRANCH" 2>&1 | tee -a "$LOG"

log "Pulling latest changes from origin/${DEFAULT_BRANCH}..."
if git pull --rebase --quiet origin "$DEFAULT_BRANCH" 2>&1 | tee -a "$LOG"; then
  log "Pull completed."
else
  log "Pull failed (likely offline). Continuing with local daily generation."
fi

log "Updating DAILY_Anthropic.md run log..."
python3 scripts/update_daily_anthropic.py 2>&1 | tee -a "$LOG"

log "Fetching news..."
python3 scripts/fetch_news.py 2>&1 | tee -a "$LOG"

log "Refreshing DAILY_Anthropic.md + daily docs after fetch..."
python3 scripts/update_daily_anthropic.py 2>&1 | tee -a "$LOG"

log "Generating RSS feed..."
python3 scripts/generate_rss.py 2>&1 | tee -a "$LOG"

if [ -f "scripts/generate_sitemap.py" ]; then
  log "Generating sitemap..."
  python3 scripts/generate_sitemap.py 2>&1 | tee -a "$LOG"
else
  log "Skipping sitemap generation (scripts/generate_sitemap.py not found)."
fi

log "Checking changelog..."
python3 scripts/check_changelog.py 2>&1 | tee -a "$LOG"

log "Updating README..."
python3 scripts/update_readme.py --section ALL 2>&1 | tee -a "$LOG"

log "Generating multi-channel social copy..."
python3 scripts/generate_social_posts.py 2>&1 | tee -a "$LOG"

log "Running distribution channels (skip automatically if credentials are missing)..."
python3 scripts/notify_telegram.py 2>&1 | tee -a "$LOG" || true
python3 scripts/notify_discord.py 2>&1 | tee -a "$LOG" || true
python3 scripts/email_digest.py 2>&1 | tee -a "$LOG" || true

# Commit and push if anything changed
git add DAILY_Anthropic.md docs/DAILY_ANTHROPIC.md docs/DAILY_BLOG.md docs/NEWS.md docs/CHANGELOG.md README.md data/ rss.xml
if [ -f "sitemap.xml" ]; then
  git add sitemap.xml
fi
if ! git diff --staged --quiet; then
    git commit -m "chore(bot): daily update $(date -u +%Y-%m-%d)"
    git push origin "$DEFAULT_BRANCH"
    log "Pushed update to GitHub."
else
    log "No changes to commit."
fi

log "Done."
