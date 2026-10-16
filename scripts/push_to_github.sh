#!/usr/bin/env bash
# Push the PMC complaints heatmap project to GitHub.
# Run from anywhere:  bash scripts/push_to_github.sh
set -euo pipefail

REPO_URL="https://github.com/kunalbavdhane9922/PMC-DATA-ANALYSIS-HEATMAP-PROJECT.git"
BRANCH="main"

cd "$(dirname "$0")/.."

# Safety: the raw CSV must never be committed
if ! grep -qx '\*.csv' .gitignore 2>/dev/null; then
  echo "ERROR: .gitignore must contain '*.csv' (raw data has personal info and exceeds 100 MB)"; exit 1
fi

[ -d .git ] || git init -b "$BRANCH"

git remote get-url origin >/dev/null 2>&1 \
  && git remote set-url origin "$REPO_URL" \
  || git remote add origin "$REPO_URL"

git add .gitignore docs scripts
git status --short

if git diff --cached --quiet; then
  echo "Nothing new to commit."
else
  git commit -m "Add PMC complaints heatmaps, docs and build scripts"
fi

git branch -M "$BRANCH"
# If the remote already has commits (e.g. a README), merge them first
git pull origin "$BRANCH" --rebase --allow-unrelated-histories 2>/dev/null || true
git push -u origin "$BRANCH"
