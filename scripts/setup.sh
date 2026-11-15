#!/usr/bin/env bash
# Link the repo's skills into .claude/skills so Claude Code finds them.
# Usage: ./scripts/setup.sh            (this repo only)
#        ./scripts/setup.sh --global   (~/.claude/skills, available in every project)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [[ "${1:-}" == "--global" ]]; then DEST="$HOME/.claude/skills"; else DEST="$ROOT/.claude/skills"; fi
mkdir -p "$DEST"
for s in "$ROOT"/skills/*/; do
  name="$(basename "$s")"
  ln -sfn "$s" "$DEST/$name"
  echo "linked $name -> $DEST/$name"
done
