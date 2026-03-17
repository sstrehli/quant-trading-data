#!/bin/bash
# Update and push data to GitHub Pages repository

set -e  # Exit on error

# Configuration
REPO_DIR="/home/sstrehli/.openclaw/workspace-quant-guru/github-pages-data"
GIT_REPO="git@github.com:sstrehli/quant-trading-data.git"
COMMIT_MESSAGE="Auto-update: $(date '+%Y-%m-%d %H:%M:%S')"

echo "=== GitHub Pages Data Update ==="
echo "Timestamp: $(date)"
echo "Directory: $REPO_DIR"
echo ""

# Step 1: Export latest data
echo "1. Exporting latest data from Enhanced V2 API..."
cd "$REPO_DIR"
python3 export_data.py

# Step 2: Check if repository is initialized
if [ ! -d ".git" ]; then
    echo "2. Initializing Git repository..."
    git init
    git remote add origin "$GIT_REPO" || true
    git checkout -b main
fi

# Step 3: Add and commit changes
echo "3. Committing changes..."
git add *.json *.py *.sh README.md
git commit -m "$COMMIT_MESSAGE" || echo "No changes to commit"

# Step 4: Push to GitHub
echo "4. Pushing to GitHub..."
git push origin main --force

# Step 5: Verify
echo "5. Update complete!"
echo "GitHub Pages URL: https://sstrehli.github.io/quant-trading-data/"
echo "Files available at:"
echo "  - https://sstrehli.github.io/quant-trading-data/trades.json"
echo "  - https://sstrehli.github.io/quant-trading-data/signals.json"
echo "  - https://sstrehli.github.io/quant-trading-data/sessions.json"
echo "  - https://sstrehli.github.io/quant-trading-data/positions.json"
echo "  - https://sstrehli.github.io/quant-trading-data/health.json"
echo "  - https://sstrehli.github.io/quant-trading-data/summary.json"

echo ""
echo "Next update scheduled in 5 minutes."