#!/usr/bin/env python3
"""Return ffprobe media facts as stable JSON for production QA."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: inspect_media.py FILE [FILE ...]", file=sys.stderr)
        return 2
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        print(json.dumps({"ok": False, "error": "ffprobe not found"}))
        return 2
    results = []
    failed = False
    for item in sys.argv[1:]:
        path = Path(item).resolve()
        proc = subprocess.run(
            [
                ffprobe,
                "-v", "error",
                "-show_entries", "format=duration,size,format_name:stream=index,codec_type,codec_name,width,height,sample_rate,channels",
                "-of", "json",
                str(path),
            ],
            text=True,
            capture_output=True,
        )
        if proc.returncode:
            failed = True
            results.append({"path": str(path), "ok": False, "error": proc.stderr.strip()})
        else:
            payload = json.loads(proc.stdout)
            results.append({"path": str(path), "ok": True, **payload})
    print(json.dumps({"ok": not failed, "files": results}, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
