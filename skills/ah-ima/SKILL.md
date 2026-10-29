---
name: ah-ima
description: |
  Compatibility entry for IMA retrieval with Alex Hormozi workflows. Use when the user explicitly invokes $ah-ima or asks to search, read, cite, or summarize Hormozi materials from IMA.
  This explicit IMA retrieval skill uses the IMA knowledge base "AlexHormozi 知识库 | 百万美元报价" unless the user names another IMA knowledge base.
---

## 手动更新路由

用户明确要求“更新 skill / 检查更新 / 同步最新原子库”时，先执行此路由。使用当前 SKILL.md 所在目录解析脚本绝对路径：

```text
python "{skillDir}/tools/update_skill.py"
```

只检查时加 `--check`。脚本从 GitHub main 的固定提交同步本仓库整套 skill 和原子资料，覆盖前备份，写入失败回滚；不需要 Git 或 GitHub 登录。根据脚本实际结果报告当前提交、更新状态与失败原因。普通业务问题不自动更新。更新后重新读取相关 SKILL.md。


# ah-ima

Use this skill as a thin compatibility entry for users who explicitly ask for IMA retrieval.

Default IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

For the actual workflow, follow `$ah`:

```text
IMA search/read -> evidence summary -> Hormozi framework selection -> final answer
```

Required dependency:

- `ima-skill/SKILL.md`
- `ima-skill/knowledge-base/SKILL.md`

Rules:

- Use the default knowledge base unless the user explicitly names another IMA knowledge base.
- Do not expose internal `knowledge_base_id`, `media_id`, or `folder_id`.
- Do not claim to have read IMA content unless retrieval actually happened.
- Use IMA as the retrieval source. Do not add non-IMA fallback instructions to this skill.
- If IMA credentials are missing, explain setup and do not silently use unverified materials.

Output a compact version of the `$ah` template:

```markdown
## IMA 检索摘要
- 知识库：
- 检索词：
- 命中的材料：
- 可用证据：
- 不确定/缺失：

## 处理结果

## 下一步
```
## Hormozi Methodology First

Every answer must use Alex Hormozi methodology as the primary reasoning layer. For /ah requests, first ground the diagnosis, framing, and recommendation in Alex Hormozi sources or workflow principles:

1. Prefer the local expert atom library and packaged method notes by default. Use the IMA knowledge base `AlexHormozi 知识库 | 百万美元报价` only when the user explicitly asks to search/read/cite/troubleshoot IMA.
2. If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or local fallback is needed, use the local Alex Hormozi expert atom library and auto-bootstrap it when missing.
3. Only after the Alex Hormozi layer is established, add commercial cases when the question would benefit from proof, benchmarks, platform/channel examples, monetization examples, acquisition examples, or Chinese-market context.
4. Commercial cases are supporting evidence only. Do not let commercial cases replace Alex Hormozi methodology, and do not answer purely from the commercial case library unless no Alex Hormozi source is available; if that happens, label the answer as case-supported inference rather than Alex Hormozi-grounded.
5. In final answers, keep the distinction clear: Hormozi 方法论 for the core principle and 商业案例支撑 for examples.

## Dependency Auto-Bootstrap

If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or the user explicitly wants local/offline retrieval, ensure the local Alex Hormozi expert atom library exists before answering. GitHub installs should include it when bundled; also check ~/.agents/skills/ah/知识库/原子库/atoms.jsonl and ~/.agents/skills/ah-download-atoms/知识库/原子库/atoms.jsonl. If both are missing, treat this as a light/partial install and call $ah-download-atoms or run python tools/download_full_atoms.py from the installed ah-download-atoms skill directory. Do not ask the user whether to download; do it automatically when local fallback is required.

If the request involves acquisition, traffic, channel choice, platform choice, Xiaohongshu/小红书, WeChat Official Account/公众号, private domain/私域, conversion, lead generation, product launch, business examples, benchmark projects, case studies, monetization examples, 生财有术案例, or any answer would benefit from case evidence, use $commercial-case-library automatically before answering. Do not ask the user whether to download it.
