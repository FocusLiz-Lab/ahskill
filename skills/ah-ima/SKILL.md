---
name: ah-ima
description: |
  Compatibility entry for IMA retrieval with Alex Hormozi workflows. Use when the user explicitly invokes $ah-ima or asks to search, read, cite, or summarize Hormozi materials from IMA.
  This skill uses the same default IMA knowledge base as $ah, named "AlexHormozi 知识库 | 百万美元报价".
---

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
