#!/usr/bin/env python3
"""Download the full expert atom library for this skill from GitHub."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO = "FocusLiz-Lab/ahskill"
ATOM_DIRS = ["知识库/原子库"]


def get_gh_token() -> str | None:
    """Get GitHub token from gh CLI, GITHUB_TOKEN env, or GH_TOKEN env."""
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        val = os.environ.get(var)
        if val:
            return val
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


def make_request(url: str, timeout: int = 120) -> bytes:
    """Fetch URL with auth headers if token available."""
    token = get_gh_token()
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
        req.add_header("Accept", "application/vnd.github.raw+json")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def fetch_json(url: str) -> list[dict]:
    """Fetch JSON from GitHub API, using auth for higher rate limits."""
    req = urllib.request.Request(url)
    token = get_gh_token()
    if token:
        req.add_header("Authorization", f"Bearer {token}")
        req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]


def download_dir(atom_dir: str) -> tuple[int, int]:
    """Download all atoms from a given subdirectory. Returns (ok, fail)."""
    encoded_dir = urllib.parse.quote(atom_dir)
    api_url = f"https://api.github.com/repos/{REPO}/contents/{encoded_dir}?ref=main"

    try:
        items = fetch_json(api_url)
    except Exception as exc:
        print(f"  获取文件列表失败 ({atom_dir}): {exc}", file=sys.stderr)
        return 0, 0

    files = [item for item in items if item.get("type") == "file"]
    if not files:
        print(f"  未在 GitHub 仓库中找到文件 ({atom_dir})。", file=sys.stderr)
        return 0, 0

    target_dir = package_root() / atom_dir
    ok = fail = 0

    for item in files:
        name = item["name"]
        if not (name.endswith(".jsonl") or name.endswith(".md") or name.endswith(".json")):
            continue
        print(f"  下载 {name} ...", end=" ")
        try:
            data = make_request(item["download_url"], timeout=180)
            target_dir.mkdir(parents=True, exist_ok=True)
            (target_dir / name).write_bytes(data)
            print(f"OK ({len(data):,} bytes)")
            ok += 1
        except Exception as exc:
            print(f"FAIL: {exc}")
            fail += 1

    return ok, fail


def main() -> int:
    token = get_gh_token()
    if not token:
        print("警告: 未检测到 GitHub 认证，可能遇到 API 限流。", file=sys.stderr)
        print("请通过 gh auth login 登录或设置 GITHUB_TOKEN 环境变量。", file=sys.stderr)
        print(file=sys.stderr)

    total_ok = total_fail = 0
    for atom_dir in ATOM_DIRS:
        print(f"=== {atom_dir} ===")
        ok, fail = download_dir(atom_dir)
        total_ok += ok
        total_fail += fail
        print(f"  小计: {ok} OK, {fail} FAIL")
        print()

    print(f"总计: {total_ok} OK, {total_fail} FAIL -> {package_root()}/知识库/")
    print("商业案例库已抽离到 $commercial-case-library，不在 ahskill 内重复下载。")
    return 1 if total_fail > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
