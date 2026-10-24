# Decision Brief Template

A standalone file a non-technical user can save, share, and reread months later to see why a decision was made.

Produce it after Discovery, Technical Translation, and MVP Framing, once the user picks a direction (including "not now"). Skip it only if the user says they don't want a file. Preserve the user-specified or existing location; otherwise default outside the repository. Durable project documents may live in the repository only under its conventions and user approval; see [Storage Policy](lifecycle-traceability.md#storage-policy).

## Minimal version

Use for short conversations or small projects.

```markdown
# Decision Brief — [Project]

**Problem**: [one sentence, user's words]
**Recommended**: [option] because [reason]
**Not doing**: [non-goals]
**Next step**: [one concrete action]
```

Leave a field empty rather than filling it with boilerplate.

For a standard or large project, add the full Next-Step Card from the template below after the metadata. Omit it for the trivial fast path.

## Full version

```markdown
# Decision Brief — [Project]

Date: YYYY-MM-DD
Status: build / validate first / postponed / not doing
Decision state: proposed / user-approved / simulation-approved / controller-authorized / deferred / rejected
Decision source: who decided which scope and where it is recorded. user-approved requires an actual human's explicit decision, not an API role, controller message or simulation; it does not mean product acceptance.

## Next-Step Card

**目前工作項目**: [用日常語言寫的當前工作]；進度：[待開始 / 進行中 / 受阻 / 待驗收 / 已驗收]（`Task ID`: [可選]）
**開始條件**: [本項需要的輸入；若有前置任務，寫出其已驗收的輸出／證據]
**這一輪要交付**: [本輪唯一主要產物或可觀察結果]
**這一輪不做**: [明確不包含的工作]
**使用者需要決定**: [需要使用者批准的事項；沒有就寫「無」]
**Agent 現在可以做**: [在上述條件下允許的動作]
**完成時要看見的證據**: [使用者或檢查者可以核對的具體證據]
**若遇阻或證據不符**: [停止條件，以及下一個安全動作]

`待驗收` 表示 Agent 已交付但證據尚未核對；只有指定證據被核對後才能標 `已驗收`。依賴任務不得在前置任務仍為 `待驗收`、`待開始` 或 `受阻` 時開始。

在對話中展示卡片時也保留這八個固定欄位；沒有內容的欄位寫「無」，不要用縮寫刪掉欄位。

## 1. What I'm solving
> [user's own words]

Problem in one sentence:
Who uses it, and when:

## 2. Facts vs assumptions
Confirmed:
- 
Unverified (check before building):
- [assumption] — how to check:

## 3. Recommendation
Recommended:
Why (in product terms):
This is the wrong choice if:
Time: [estimate] — [查证 / 经验估算 / 未查证估算], [date]
Money: [estimate] — [source label], [date]
Maintenance: [concrete, e.g. "check logs weekly"]
Switching later means redoing: [what, roughly how much]

## 4. Version 1 scope
Core invariant: the user wants to change [X]; this version must not swap it for [Y].
In:
- [feature] (user would notice immediately if removed)
Out:
- [feature] — lost: [capability], acceptable because [reason]
Floor: version 1 must touch [the user's problem] in a real situation.

## 5. How we'll know
| Evidence | Proves | Doesn't prove |
|---|---|---|
| | | |
Success signal:
Stop condition:

## 6. Next steps
1. [action] — cost, time, which assumption it tests
   - if [A] → continue; if [B] → change direction
2. Hand-off: [developer / Agent / another skill], with Agent Brief below if building

Saved at:
Review on:

## Appendix: Agent Brief
[only if the decision is to build]
```

For dependent work, changed requirements, versioned delivery, or session recovery, the engineering appendix carries the [minimum SPEC and trace links](lifecycle-traceability.md). Keep the user-facing Brief and Card short; do not duplicate the engineering record in every field.

`Recommended` is the Agent's proposal, not evidence of user approval. Use `proposed` until the user accepts, rejects, or defers the direction.

## Checklist

- User's wording kept, not rewritten into product jargon
- Facts and assumptions separated
- One recommendation, plus when it's wrong
- Every estimate has a source label and date
- Core invariant and the cost of each cut written down
- Next step is something the user can do this week
- Standard／large projects have one current-work Next-Step Card; trivial fast path does not
- Dependent work names a checked predecessor output or evidence as its start condition
- `待驗收` and `已驗收` are not conflated
- Saved location follows user intent, project conventions, and approval; raw or sensitive evidence is separate

## Anti-patterns

- Rewriting "I want to know if I ate too much today" as "caloric intake monitoring"
- Presenting a menu instead of a recommendation
- Next steps like "consider a prototype" instead of "use MyFitnessPal for 3 days to see if you keep logging"
- Leaving the decision only in the chat
