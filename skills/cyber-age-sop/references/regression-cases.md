# Cyber-Age SOP Regression Cases

Use these cases when auditing a future revision. The evaluator must not edit the skill while testing it.

## Behavioral Regression Cases

| Case | Input Pressure | Expected Behavior |
|---|---|---|
| Trivial change | One README typo with known check | Use trivial fast path; no full brief or external report |
| Vague idea | Early project idea with no clear scope | Ask one plain-language scope-changing question; do not dump the anchor template |
| Cannot answer | User cannot answer after 2 exploration rounds | Offer 3-5 candidate anchors to pick from; classify the block type |
| Stable brief | Thought Brief with goal, scope, non-goals, acceptance, evidence boundary | Treat as authoritative; ask only for missing decision-changing facts |
| Live field work | Real router or infrastructure change | Require target, authorization, backup, rollback, recovery, timeout, stop, and pass/fail evidence before action |
| Guided facilitation request | Request for 大师级引导 or layered questioning | Hand off to `guided-thinking`; do not imitate or auto-run facilitation |
| Runtime UI claim | Claim about browser rendering, interaction, or live state | Require browser evidence or mark the claim `Not verified` |
| Technical choice | Non-technical user faces "use database A or B" | Translate to product consequences with recommendation, switch cost, and source; never neutral menu |
| Routing conflict | "I want AI to draw a brand" | Recognize collision with huashu-design/meigen; route to domain-specific skill |

## Triggering Test Cases

### Should Trigger (3 positive)

1. "我想做一个能帮我记帐的东西，但不知道要做成 App 还是网页"
2. "I have this idea for a tool but I don't know how to explain what I want to an engineer"
3. "Can you help me figure out what my MVP should include and what to cut?"

### Should NOT Trigger (3 negative)

1. "我连我要做什么都还不太清楚，你帮我理一理" → `guided-thinking`
2. "给我一些解决这个问题的创意方案" → `brainstorming`
3. "帮我设计一个品牌视觉" → `huashu-design` or `meigen`

## v0.3 Specific Acceptance

- [ ] Description uses situation-triggered language, not method names
- [ ] Description explicitly excludes guided-thinking and brainstorming
- [ ] Handles "cannot answer" with candidate anchors, not just "blocked"
- [ ] Technical translation includes recommendation + reasoning + switch cost
- [ ] MVP framing includes "core invariant" and floor condition
- [ ] Decision authority (product vs implementation) is explicit in Non-Negotiables
- [ ] All 6 triggering test cases pass correctly

## Review Questions

- Did the skill choose the smallest safe path?
- Did it keep project SOP separate from facilitation?
- Did it distinguish local, build, field, and long-running evidence?
- Did it prevent scope expansion and repository artifact pollution?
- Did it leave a concrete report and follow-up boundary?
- For non-technical users, can they explain back why they chose an option?
