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

log "Updating DAILY_Anthropic.md run log..."
python3 scripts/update_daily_anthropic.py 2>&1 | tee -a "$LOG"

# Pull latest changes first
git pull --rebase --quiet 2>&1 | tee -a "$LOG"

log "Fetching news..."
python3 scripts/fetch_news.py 2>&1 | tee -a "$LOG"

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

# Commit and push if anything changed
git add DAILY_Anthropic.md docs/DAILY_ANTHROPIC.md docs/NEWS.md docs/CHANGELOG.md README.md data/ rss.xml
if [ -f "sitemap.xml" ]; then
  git add sitemap.xml
fi
if ! git diff --staged --quiet; then
    git commit -m "chore(bot): daily update $(date -u +%Y-%m-%d)"
    git push
    log "Pushed update to GitHub."
else
    log "No changes to commit."
fi

log "Done."
