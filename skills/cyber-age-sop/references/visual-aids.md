# Shape Readback for Project Discovery

## Purpose

Help the owner see and correct what the Agent understood before agreeing to an execution plan. Use a small provisional drawing when text leaves product shape or behavior unclear. Do not wait for the user to know the words "wireframe" or "architecture".

Ordinary local text or ASCII sketches do not need a separate permission round. Respect an explicit request to skip drawings, and omit a drawing that adds no clarity. External image services, uploads and live system changes still require their applicable authority.

## Choose the useful shape

| Project | Useful readback |
|---|---|
| App / plugin UI | What the owner sees, enters and clicks, including an important empty/error state |
| Program / CLI | Input → checks/processing → output, with failure behavior |
| Skill / Agent workflow | Trigger → question/readback → agreed action → result/check |
| Multi-role system | Who can see or change which information; only relevant modules/data flows |

Use the host's native preview if available. Otherwise show a short text diagram directly in the conversation. Do not promise interactive cards or a rendered canvas the host does not supply. Label assumptions and avoid adding unrequested features.

## Example: provisional plugin layout

```text
草圖，尚待你修正：
[網頁標題與網址]
[你選取的段落]
主題：[自己輸入]   [保存]

[依主題找回] → [檢視原文與來源] → [匯出 Markdown]
```

Explain what the drawing makes visible in one or two sentences. Invite a meaningful correction, such as whether this matches how they want to collect and reuse material. A sketch is not a substitute for the owner's substantive confirmation of purpose and scope.

## Example: program behavior

```text
指定的 JSONL 檔 → 逐行讀取與驗證 → 按原順序輸出 Markdown
                       ↓ 有錯
                回報原始行號，不輸出部分成功內容
```

This shows behavior; it does not establish that code or tests exist. If tool or format details remain unknown, keep them explicit rather than drawing an invented interface.

## Keep it focused

- Show one concept at a time, using the owner's language.
- Prefer a compact drawing with only relationships needed to make a decision.
- Distinguish provisional understanding, agreed design, actual implementation and tested behavior.
- After a material change, revise only the affected part and confirm the new meaning before changing the execution Card.
- For a previously confirmed project, reuse its existing diagram where applicable; do not redraw just to fulfill a step.

## Review

Check that the drawing appeared inline, made an ambiguity easier to discuss, and did not silently enlarge scope. A text diagram being present proves neither that a human understood it nor that the host can render a native UI. Record those limits when evaluating it.
