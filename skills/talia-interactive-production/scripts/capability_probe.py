#!/usr/bin/env python3
"""Report local production-tool availability without reading credentials."""

from __future__ import annotations

import json
import os
import shutil
import sys


TOOLS = ["python3", "node", "npm", "ffmpeg", "ffprobe", "talia", "git", "curl"]


def main() -> int:
    found = {name: shutil.which(name) for name in TOOLS}
    report = {
        "schema_version": 1,
        "platform": sys.platform,
        "cwd_writable": os.access(os.getcwd(), os.W_OK),
        "executables": {
            name: {"available": path is not None, "path": path}
            for name, path in found.items()
        },
        "requires_explicit_test": {
            "image_vision": "Inspect a real local image and report testable details.",
            "image_generation": "Generate one disposable image with the configured tool.",
            "video_understanding": "Inspect a short disposable video or extracted frames.",
            "audio_understanding": "Transcribe or listen to a short disposable clip.",
            "browser_upload": "Upload a disposable file without changing production data.",
            "persistent_login": "Repeat a read-only authenticated request in a new process.",
            "talia_permissions": "Run whoami/projects/validate only.",
        },
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
