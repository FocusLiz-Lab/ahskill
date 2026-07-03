---
name: ah-download-atoms
description: 下载或更新 Alex Hormozi / ahskill 的全量本地专家原子库。用于用户安装 SkillHub 轻量包后，需要从 GitHub 拉取完整 `知识库/原子库/atoms.jsonl` 和按年份/季度拆分的 `atoms_*.jsonl`。商业案例库已抽离为共享依赖 `$commercial-case-library`，不要在本 skill 内重复下载。
---

# ah-download-atoms 全量专家原子库下载

当用户要求下载、补全、更新或修复 ahskill 本地原子库时，运行：

```powershell
python tools/download_full_atoms.py
```

下载完成后，原子库应位于：

```text
知识库/原子库/atoms.jsonl
```

以及同目录下的 `atoms_*.jsonl` 文件。

如果用户需要商业案例、案例拆解、对标案例、变现案例或生财有术案例，改用：

```text
$commercial-case-library
```
