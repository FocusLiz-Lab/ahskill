#!/usr/bin/env python3
"""Download the full atom libraries for this skill from GitHub."""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO = "FocusLiz-Lab/ahskill"
DOWNLOAD_DIRS = ("知识库/原子库", "知识库/商业案例库")


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]


def fetch_json(url: str):
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def download(url: str, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as response:
        target.write_bytes(response.read())


def download_dir(remote_dir: str) -> int:
    encoded_dir = urllib.parse.quote(remote_dir)
    api_url = f"https://api.github.com/repos/{REPO}/contents/{encoded_dir}?ref=main"
    files = [item for item in fetch_json(api_url) if item.get("type") == "file"]
    if not files:
        print(f"未在 GitHub 仓库中找到 {remote_dir} 文件。", file=sys.stderr)
        return 0

    target_dir = package_root() / remote_dir
    count = 0
    for item in files:
        name = item["name"]
        if not (name.endswith(".jsonl") or name.endswith(".json") or name.endswith(".md")):
            continue
        print(f"下载 {remote_dir}/{name} ...")
        download(item["download_url"], target_dir / name)
        count += 1
    return count


def main() -> int:
    count = 0
    for remote_dir in DOWNLOAD_DIRS:
        count += download_dir(remote_dir)
    if count == 0:
        print("未下载到任何原子库文件。", file=sys.stderr)
        return 1
    print(f"完成：已下载 {count} 个文件到 {package_root() / '知识库'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
