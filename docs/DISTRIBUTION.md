# Distribution Playbook

This playbook defines how to distribute the daily Anthropic brief beyond the website.

## Channels

1. Website dashboard: `https://omrigotlieb.github.io/awesome-anthropic/`
2. News feed page: `docs/NEWS.md`
3. RSS feed: `rss.xml`
4. Telegram channel: `scripts/notify_telegram.py`
5. Discord channel webhook: `scripts/notify_discord.py`
6. Email newsletter (Buttondown): `scripts/email_digest.py`
7. Manual social posting: `data/distribution/latest_social_posts.md`

## Daily Flow

1. Refresh news and changelog.
2. Regenerate RSS, sitemap, and README preview.
3. Generate channel-specific social copy:
   - `python3 scripts/generate_social_posts.py`
4. Push automated outbound messages:
   - `python3 scripts/notify_telegram.py`
   - `python3 scripts/notify_discord.py`
   - `python3 scripts/email_digest.py`

`scripts/run_daily.sh` now includes these steps and handles missing credentials gracefully.

## Credentials

- Telegram:
  - `TELEGRAM_BOT_TOKEN`
  - `TELEGRAM_CHANNEL_ID`
- Discord:
  - `DISCORD_WEBHOOK_URL`
- Buttondown:
  - `BUTTONDOWN_API_KEY`

## Distribution Quality Rules

- Promote official Anthropic and Claude Code updates first.
- Keep community stories, but cap low-signal topics in top slots.
- Keep cross-channel copy concise and link back to:
  - Dashboard
  - RSS feed
  - Source story URLs

## Success Metrics

- RSS subscribers growth.
- Telegram and Discord post engagement.
- Newsletter open and click rates.
- Returning visits to dashboard and `docs/NEWS.md`.
