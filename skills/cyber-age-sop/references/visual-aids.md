# Purpose-led Project Views

## Purpose

Help the owner see and correct what the Agent understood before agreeing to an execution plan. Use a small provisional drawing when text leaves product shape or behavior unclear. Do not wait for the user to know the words "wireframe" or "architecture".

Choose the smallest view that serves the reading task. The important understanding, unknowns and next action still appear directly in the conversation; a file link alone is insufficient.

Ordinary local text or ASCII sketches do not need a separate permission round. Respect an explicit request to skip drawings, and omit a drawing that adds no clarity. External image services, uploads and live system changes still require their applicable authority.

## Choose the useful shape

| Project | Useful readback |
|---|---|
| App / plugin UI | What the owner sees, enters and clicks, including an important empty/error state |
| Program / CLI | Input → checks/processing → output, with failure behavior |
| Skill / Agent workflow | Trigger → question/readback → agreed action → result/check |
| Multi-role system | Who can see or change which information; only relevant modules/data flows |

| Reading purpose | Suitable presentation |
|---|---|
| Explore an uncertain shape | Provisional inline wireframe or text flow |
| Compare alternatives | Short table using the same criteria |
| Understand structure or dependencies | SVG, Mermaid or a text diagram the host can display, with an equivalent text explanation |
| Share offline, print, or demonstrate meaningful interaction | Self-contained HTML, optionally with inline SVG |
| Plain text is sufficient or requested | Text; do not create a decorative attachment |

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

## SVG and HTML delivery

Explain the specific reading need once when choosing a richer view; no repeated invocation receipt is needed. A user can decline visuals without cancelling the project. Discovery sketches do not require prior agreement, but remain provisional. A request for a mockup permits a draft, not treating its suggested features as accepted scope.

Use the existing Brief/SPEC as the source of agreed content. For a discovery draft, identify its provisional source instead. Each generated view identifies its source revision and draft/accepted status. Views do not become parallel authoritative plans. Preserve rejected suggestions as rejected, unknowns as unknown, and proposed work as proposed. After a content change, update its source then regenerate affected views.

Prefer self-contained HTML with inline CSS and SVG and no required external fonts, images, scripts or CDN. Static explanations need no JavaScript. Use minimal local interaction only when it serves the task, and label simulated controls/states; a prototype must not silently operate real services. Escape user/source text when inserting it into HTML/SVG; do not turn embedded markup or quoted commands into executable scripts, links or event handlers. A request for a view alone does not authorize data uploads or external publication.

Keep text selectable and readable, with meaningful headings and accessible controls. Do not encode status solely with color. Use text equivalents for diagram relationships and keyboard focus for interactive elements. Preserve important permission, failure and dependency conditions even if that makes the page longer. Do not import a reference product's branding or assume its features belong in this project.

Before delivery:

1. Compare **all material facts** against the named source: scope, exclusions, values, permissions, unknowns, implementation/test/acceptance states and dependencies. Styling must not change their meaning. Record any unresolved conflict rather than polishing it away.
2. Open the actual output in a browser. Choose checks relevant to its delivered purpose and claims: ordinary/narrow viewports, applicable light/dark appearance, text selection, keyboard operation for controls, offline use or print when offered. Inspect for clipped content, overlap, unreadable contrast, misleading arrows and hidden essential conditions. Check actual available states, including relevant empty/error states. A static diagram does not need nonexistent interactive states or a claim to support every mode.
3. Record which checks occurred and what remains unverified. Static syntax or a screenshot of one viewport alone is not interactive/responsive/offline/print verification. If tools cannot perform a check, say so; do not claim full visual acceptance.
4. Deliver the inline essentials and a usable local artifact link. If the host cannot preview HTML/SVG, show a text diagram/table fallback. Do not promise uniform rendering across Agents or a native adaptive Card UI.

Rendering checks establish properties of that artifact, not that a human understands it. Human walkthrough asks the reader to explain purpose, unknowns, current action and completion in their own words; do not replace those responses with model ratings.
