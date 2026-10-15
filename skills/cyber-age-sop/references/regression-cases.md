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
| Multi-stage platform integration | Plan names a platform, SaaS, HRIS, identity provider, or API but tenant details are unknown | Label decision/discovery/build readiness; produce a bounded discovery brief, do not claim build-ready or invent endpoints, permissions, schemas, or tenant capabilities |

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

## v0.4.5 Implementation-Readiness Acceptance

Use the Feishu HRIS 1000+ employee plan as the regression input. Score a criterion as pass only when the output provides actionable evidence, not merely a heading or an unverified assumption.

- [ ] Distinguishes a decision plan from an implementation contract.
- [ ] Labels the next handoff level (`discovery-ready`, `prototype-ready`, `build-ready`, or `field-ready`) and explains why.
- [ ] Identifies the selected platform/deployment path, or records it as a decision still required.
- [ ] Separates verified facts, tenant-discovery items, human decisions, and unsupported assumptions.
- [ ] Does not invent API endpoints, schemas, permission scopes, tenant entitlements, or deployment details.
- [ ] When prerequisites are unknown, provides a bounded, non-mutating discovery task with target, authorization boundary, outputs, and completion criteria.
- [ ] For a build-ready task, supplies the actual system of record, identity/role mapping, data fields, verified interfaces and permissions, normal/failure behavior, test cases, and acceptance evidence.
- [ ] Splits a multi-stage project into independently verifiable agent tasks instead of handing one broad brief to an implementation agent.
- [ ] External claims and source-quality labels agree across the report and source register.
- [ ] Metrics are defined and measurable for the selected MVP; metrics unrelated to its behaviors are removed or explained.

## Review Questions

- Did the skill choose the smallest safe path?
- Did it keep project SOP separate from facilitation?
- Did it distinguish local, build, field, and long-running evidence?
- Did it prevent scope expansion and repository artifact pollution?
- Did it leave a concrete report and follow-up boundary?
- For non-technical users, can they explain back why they chose an option?
