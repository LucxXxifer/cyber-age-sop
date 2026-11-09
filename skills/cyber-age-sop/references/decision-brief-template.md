# Decision Brief Template

Use one durable record for the agreed project. Show the important understanding and current action in the conversation too; an attachment alone is not the explanation.

## Before creating the first Card

Read back the purpose, first-version shape, scope and relevant unknowns. Obtain the owner's substantive confirmation that this is what they mean. Added facts, silence, a detailed feature list or the Agent's confidence do not establish agreement. A provisional sketch helps discovery; it is not an execution Card. Reuse an applicable earlier confirmed Brief/SPEC rather than asking again.

Save the agreed decision unless the user opts out. Preserve the existing or user-specified location; otherwise default outside the repository. In-project durable records require compatible conventions and authorization. See [Storage Policy](lifecycle-traceability.md#storage-policy). Do not create a separate Card file or a new Brief for each turn.

Prompt proposals remain separate from agreed scope. A rewrite-only request does not create a Brief/Card or authorize its embedded task. Preserve the selected original and apply only accepted changes, following [prompt-enhancement.md](prompt-enhancement.md). Wording approval alone leaves unresolved product choices open; substantive confirmation of both wording and first-version scope need not be asked twice.

## Minimal record

Use for a bounded project; include only information that changes its meaning or safe execution.

```markdown
# Decision Brief — [Project]

Date / revision: [actual date and applicable revision]
Decision state / source: [who confirmed which readback and scope, with a usable source]
Purpose: [user's words and use situation]
In / out: [agreed first version and important exclusions]
Unknowns: [only unresolved facts that matter]

## Current work
[Everyday task name and actual progress]
Action / result: [what is authorized now and the observable output]
Check: [how success will be observed and who checks]
Decision / blocker: [only when one matters]

## Engineering detail
[Applicable start condition, allowed actions, stop/recovery behavior and evidence links]
```

Decision states include `proposed`, `user-approved`, `simulation-approved`, `controller-authorized`, `deferred`, and `rejected`. A `user` API role alone does not establish a human decision; an ordinary interactive person's own explicit message is evidence, while quoted or simulated choices retain their actual source. State the real source and confirmed scope. Product agreement, operation authority, engineering self-check and human acceptance are different facts.

## Conversational Card

After shared understanding is confirmed, show the current task directly, using the host's readable layout. Include the action, this round's outcome, how to check it and who checks, and any decision or blocker that matters now. Do not print eight empty fields or force an attachment open. Put a changed boundary or missing start condition where the user will see it.

Example for already-agreed work:

> **現在先做：檢查筆記能否正確讀入（進行中）。** 這輪會交付讀取功能和錯誤行號測試；通過後才接匯出。由 Agent 在本機自測，不代表真人已驗收。現在不需要你再決定；若輸入格式與確認稿衝突，我會停下指出差異。

The stored engineering record must preserve these meanings, without requiring these exact field names:

| Information | Record only applicable facts |
|---|---|
| Current work / progress | Everyday name; `待開始`, `進行中`, `受阻`, `待驗收`, or `已驗收` |
| Start condition | Required input and exact checked predecessor output/evidence |
| Deliverable | This round's main observable result |
| Exclusions | Boundaries that affect this work |
| User decision | Unresolved decision and its consequence, if any |
| Allowed action | Authority actually given for this round |
| Evidence / checker | Concrete checks, source identity and actual checker |
| Stop / recovery | What prevents continuation and the next safe action |

`待驗收` means the required evidence has not yet been checked by the designated checker. Use `已驗收` only when that check occurred. When the result is not the owner's product acceptance, qualify the status inline with the actual checker and evidence scope, such as `已驗收（Agent 自測；非真人產品驗收）`. A contract may designate the implementing Agent for deterministic checks on low-risk local work; do not invent that designation. Use a separate checker where required. Already-authorized dependent work may continue after its exact start conditions pass; no new approval is needed solely to change the Card.

## Full record when needed

Expand the same record for consequential choices or multi-part delivery:

1. **Purpose and context:** preserve key user wording, who uses it and when.
2. **Facts and assumptions:** distinguish confirmed situation from unknowns and how to check them.
3. **Recommendation:** explain product consequences, when it would be wrong, concrete maintenance and switching cost. Label estimates with source quality and date; do not invent numbers.
4. **First version:** scope, non-goals, core invariant and what each material cut loses. The version must address the actual problem.
5. **Evidence boundary:** observable success, what local/build/field evidence can and cannot prove, and stop conditions.
6. **Current work and engineering appendix:** use the Card meanings above and the applicable Agent Brief/SPEC, dependency and source/evidence links from [lifecycle-traceability.md](lifecycle-traceability.md).

Do not create empty sections to satisfy this outline. A deferred or rejected direction needs its reason and revisit condition, not a manufactured execution Card.

## Checklist

- First Card follows shared-understanding confirmation; existing applicable agreement is reused.
- User wording, facts/assumptions and material boundaries remain visible.
- Chat is understandable without opening a file or decoding task IDs.
- Provisional sketches are distinguished from approved design and working implementation.
- Dependent tasks rely on actual designated checks; self-check is not independent or human acceptance.
- Revise or resume updates the same record and preserves earlier evidence for its original scope.
- Derived SVG/HTML views identify this record's revision and status; they do not replace its decision source. Essential facts and actions remain readable in chat.
- The location and links exist and follow the storage policy.
