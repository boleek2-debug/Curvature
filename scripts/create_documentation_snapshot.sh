#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
OUTPUT_FILE="${HOME}/curvature-documentation-current.zip"

cd "$REPO_ROOT"

rm -f "$OUTPUT_FILE"

python - "$REPO_ROOT" "$OUTPUT_FILE" <<'PY'
from __future__ import annotations

import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

repo_root = Path(sys.argv[1]).resolve()
output_file = Path(sys.argv[2]).resolve()

excluded_parts = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

excluded_names = {
    "curvature-documentation-current.zip",
}

documentation_files: set[Path] = set()

# All Markdown documentation in the repository.
for path in repo_root.rglob("*.md"):
    relative = path.relative_to(repo_root)

    if any(part in excluded_parts for part in relative.parts):
        continue

    if path.name in excluded_names:
        continue

    if path.is_file():
        documentation_files.add(relative)

# Include repository configuration files useful for documentation review.
optional_files = (
    Path("requirements.txt"),
    Path("environment.yml"),
    Path("pyproject.toml"),
    Path(".gitignore"),
)

for relative in optional_files:
    absolute = repo_root / relative
    if absolute.is_file():
        documentation_files.add(relative)

files = sorted(
    documentation_files,
    key=lambda item: item.as_posix(),
)

commit = subprocess.run(
    ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
    check=True,
    capture_output=True,
    text=True,
).stdout.strip()

branch = subprocess.run(
    ["git", "-C", str(repo_root), "branch", "--show-current"],
    check=True,
    capture_output=True,
    text=True,
).stdout.strip()

status = subprocess.run(
    ["git", "-C", str(repo_root), "status", "--short", "--branch"],
    check=True,
    capture_output=True,
    text=True,
).stdout.rstrip()

snapshot_info = "\n".join(
    [
        "Project Curvature documentation snapshot",
        "",
        f"Created UTC: {datetime.now(timezone.utc).isoformat()}",
        f"Repository: {repo_root}",
        f"Branch: {branch}",
        f"Commit: {commit}",
        "",
        "Git status:",
        status or "(clean)",
        "",
        f"Included files: {len(files)}",
        "",
        "Files:",
        *(f"- {path.as_posix()}" for path in files),
        "",
    ]
)

with zipfile.ZipFile(
    output_file,
    mode="w",
    compression=zipfile.ZIP_DEFLATED,
    compresslevel=9,
) as archive:
    archive.writestr("SNAPSHOT_INFO.txt", snapshot_info)

    for relative in files:
        archive.write(
            repo_root / relative,
            arcname=relative.as_posix(),
        )

print(f"Created: {output_file}")
print(f"Included files: {len(files)}")
PY

echo
ls -lh "$OUTPUT_FILE"
echo
echo "Documentation snapshot ready:"
echo "$OUTPUT_FILE"
