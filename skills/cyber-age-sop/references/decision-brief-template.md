# Decision Brief Template

A standalone file a non-technical user can save, share, and reread months later to see why a decision was made.

Produce it after Discovery, Technical Translation, and MVP Framing, once the user picks a direction (including "not now"). Skip it only if the user says they don't want a file. Write it outside the repository.

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

## Full version

```markdown
# Decision Brief — [Project]

Date: YYYY-MM-DD
Status: build / validate first / postponed / not doing
Decision state: proposed / user-approved / deferred / rejected

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

`Recommended` is the Agent's proposal, not evidence of user approval. Use `proposed` until the user accepts, rejects, or defers the direction.

## Checklist

- User's wording kept, not rewritten into product jargon
- Facts and assumptions separated
- One recommendation, plus when it's wrong
- Every estimate has a source label and date
- Core invariant and the cost of each cut written down
- Next step is something the user can do this week
- File is outside the repository

## Anti-patterns

- Rewriting "I want to know if I ate too much today" as "caloric intake monitoring"
- Presenting a menu instead of a recommendation
- Next steps like "consider a prototype" instead of "use MyFitnessPal for 3 days to see if you keep logging"
- Leaving the decision only in the chat
