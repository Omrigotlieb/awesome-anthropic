#!/usr/bin/env bash
# setup_launchd.sh — installs a macOS launchd job to run run_daily.sh every morning.
#
# Usage:
#   bash scripts/setup_launchd.sh          # install (runs at 09:00 local time daily)
#   bash scripts/setup_launchd.sh remove   # uninstall

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LABEL="com.awesome-anthropic.daily"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
RUNNER="$REPO_DIR/scripts/run_daily.sh"
PYTHON="$(which python3)"

if [ "$1" = "remove" ]; then
    launchctl unload "$PLIST" 2>/dev/null || true
    rm -f "$PLIST"
    echo "Uninstalled $LABEL."
    exit 0
fi

chmod +x "$RUNNER"

cat > "$PLIST" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$LABEL</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>$RUNNER</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>WorkingDirectory</key>
    <string>$REPO_DIR</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/opt/homebrew/bin:/Users/$(whoami)/.local/bin:/usr/bin:/bin</string>
        <key>HOME</key>
        <string>$HOME</string>
    </dict>

    <key>StandardOutPath</key>
    <string>$REPO_DIR/logs/launchd.log</string>

    <key>StandardErrorPath</key>
    <string>$REPO_DIR/logs/launchd.log</string>

    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
EOF

launchctl unload "$PLIST" 2>/dev/null || true
launchctl load "$PLIST"

echo "Installed: $LABEL"
echo "Runs daily at 09:00 local time."
echo "Logs: $REPO_DIR/logs/launchd.log"
echo ""
echo "To run now:   bash $RUNNER"
echo "To uninstall: bash $0 remove"
