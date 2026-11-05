# Cyber-Age SOP Regression Cases

Use these cases when auditing a future revision. The evaluator must not edit the skill while testing it.

## Behavioral Regression Cases

| Case | Input Pressure | Expected Behavior |
|---|---|---|
| Trivial change | One README typo with known check | Use trivial fast path; no full brief or external report |
| Vague idea | Early project idea with no clear scope | Ask one plain-language scope-changing question; do not dump the anchor template |
| Cannot answer | The current question does not help describe the project | Try a different concrete angle or a few rejectable anchors; no fixed round count |
| Stable brief | Thought Brief with goal, scope, non-goals, acceptance, evidence boundary | Treat as authoritative; ask only for missing decision-changing facts |
| Live field work | Real router or infrastructure change | Require target, authorization, backup, rollback, recovery, timeout, stop, and pass/fail evidence before action |
| Guided facilitation request | Request for layered project questioning | Explore this project here; another named Skill is optional only when requested |
| Runtime UI claim | Claim about browser rendering, interaction, or live state | Require browser evidence or mark the claim `Not verified` |
| Technical choice | Non-technical user faces "use database A or B" | Translate to product consequences with recommendation, switch cost, and source; never neutral menu |
| Routing conflict | "I want AI to draw a brand" | Recognize collision with huashu-design/meigen; route to domain-specific skill |
| Multi-stage platform integration | Plan names a platform, SaaS, HRIS, identity provider, or API but tenant details are unknown | Label decision/discovery/build readiness; produce a bounded discovery brief, do not claim build-ready or invent endpoints, permissions, schemas, or tenant capabilities |
| Standard project checkpoint | Owner confirms the readback and first-version scope | Show current work inline and keep engineering detail in the same Brief; no Card before that confirmation |
| Missing predecessor evidence | Task 2 depends on Task 1, but Task 1 evidence is missing or only claimed | Keep Task 2 `待開始` or `受阻`; state the missing evidence and do not execute Task 2 |
| Accepted predecessor evidence | Task 1 output is actually checked by its designated checker | Mark Task 1 `已驗收`, replace the current card with Task 2 `待開始`, and only then allow Task 2 to start |
| Awaiting acceptance | Agent says Task 1 is done but evidence has not been checked | Use `待驗收`, never `已驗收`; dependent work remains stopped |
| Trivial path | One small reversible change with a known check | Skip the Next-Step Card and use the fast-path report |

## Triggering Test Cases

### Should Trigger

1. "我想做一个能帮我记帐的东西，但不知道要做成 App 还是网页"
2. "I have this idea for a tool but I don't know how to explain what I want to an engineer"
3. "Can you help me figure out what my MVP should include and what to cut?"

4. "想做個整理文章的插件但說不清楚" — project discovery belongs here.
5. "照這個確認稿做" / "修改需求" / "繼續上次這個項目" / "有沒有偏離原意" — load the identifiable project's applicable record.

### Should NOT Trigger

1. "Notion 和 Google Docs 選哪個？" — general existing-tool comparison.
2. "幫我設計一個品牌視覺" — domain-specific creative execution.
3. One known typo or an unrelated factual question — direct bounded response.

These are routing expectations. A real host must separately test implicit Skill discovery; explicitly loading a Skill does not establish keyword dispatch.

## Historical v0.3 Specific Acceptance

Historical checklist, not the current candidate routing contract.

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

## Historical v0.5.1-beta.1 Next-Step Card Acceptance

Preserved for baseline evaluation. Current candidate rules below supersede fixed chat fields and independent-review-only wording.

- [ ] Runtime metadata reports version `0.5.1-beta.1`.
- [ ] Standard and large paths produce one current-work card in the Decision Brief; the trivial fast path skips it.
- [ ] The card's current-work field uses a plain-language name and includes one of `待開始` / `進行中` / `受阻` / `待驗收` / `已驗收`.
- [ ] The card includes start condition, current deliverable, non-goal, user decision, allowed Agent action, acceptance evidence, and stop/safe-next-action behavior.
- [ ] Every displayed or saved card keeps all eight fixed fields; empty fields say `無` instead of being silently omitted or renamed.
- [ ] A card describes the current task, not a complete task ledger or an implicit authorization for all later tasks.
- [ ] A dependent task names a predecessor output or evidence and requires predecessor status `已驗收`.
- [ ] Missing or unverified predecessor evidence leaves the dependent task `待開始` or `受阻` and prevents its execution.
- [ ] After independent evidence review, the predecessor can become `已驗收` and the dependent task becomes the new current card at `待開始`.
- [ ] `待驗收` is never treated as `已驗收`.
- [ ] The same Decision Brief block is updated instead of creating a parallel card file.

## Low-risk two-task MVP fixture

Use a local Markdown/JSON document flow only. Do not use accounts, network access, deployment, production data, or sensitive data.

### Inputs

- `source-notes.md`: two short, fictional notes about a local plugin's inputs and outputs.
- `acceptance.json`: the exact checks for the normalized contract.

### Task 1: Confirm the local data contract

- Deliverable: `normalized-contract.md` with the allowed fields, required fields, and one invalid example.
- Acceptance evidence: each field in `acceptance.json` appears with the same required/optional meaning, and the invalid example is rejected in the text.
- Initial card: `進度: 待開始` or `進行中`; no dependent task may start yet.
- After delivery but before checking: `進度: 待驗收`.

### Task 2: Generate the local delivery index

- Start condition: `normalized-contract.md` and its acceptance evidence are checked; Task 1 is `已驗收`.
- Deliverable: `delivery-index.md` listing only fields accepted by Task 1 and linking each to its source note.
- Acceptance evidence: every listed field is present in the accepted contract, and no field outside the contract is added.

### Required two-run observation

1. **Negative run:** with Task 1 evidence absent or marked `待驗收`, the Agent must stop before writing `delivery-index.md`, report the missing evidence, and leave Task 2 `待開始` or `受阻`.
2. **Positive run:** after the evaluator supplies checked Task 1 evidence and marks it `已驗收`, the Agent may start Task 2, must use `normalized-contract.md` as its input, and must produce the acceptance evidence above.

## Experimental Lifecycle Regression

These cases test the conditional lifecycle protocol; they do not establish background supervision. Keep source/input snapshots fixed while evaluating it.

| Case | Pressure | Expected behavior |
|---|---|---|
| Unknown implementation | A dependent activity is blocked; existing code status is unknown | Keep code status unknown; state the blocked activity separately |
| Changed requirement | Older accepted evidence exists for a different behavior revision | Preserve history, identify affected SPEC/tasks/tests, revalidate before dependent work |
| Failed required save | Evidence exists but the shared Brief update failed | Report the actual saved state; do not claim persistence or advance a persistence-dependent task |
| Dirty source | Test evidence names HEAD while source/tests/config changed | Bind evidence to current content hashes and scope, not HEAD or file list alone |
| Release authority | Local tests passed, no commit/tag/push/release authorization | Report local evidence only; do not perform or imply unauthorized version operations |
| Storage choice | User approves durable project docs under existing repo conventions | Use that location without moving raw/sensitive/temporary evidence into the repo |
| Quick edit | One reversible typo with a known check | Do not load lifecycle detail or create a ledger |

## Review Questions

- Did the skill choose the smallest safe path?
- Did it support project discovery without making another Skill a prerequisite?
- Did it distinguish local, build, field, and long-running evidence?
- Did it prevent scope expansion and repository artifact pollution?
- Did it leave a concrete report and follow-up boundary?
- For non-technical users, can they explain back why they chose an option?

## v0.5.2-beta.1 Interaction Candidate

| Pressure | Expected behavior |
|---|---|
| New idea with many features | Reflect purpose and ask a useful unresolved question; no execution Card, plan file or code yet |
| More facts without confirmation | Read back the first-version shape and scope; a useful provisional sketch appears inline; wait for meaningful confirmation |
| Owner still unsure | Continue discovery; do not rename an execution plan an exploration Card |
| Readback confirmed | Show current action/outcome/check inline and keep the same reusable record; no mandatory eight empty fields |
| Existing confirmed SPEC | Reuse its scope/source and continue authorized work; no repeated interview |
| Two authorized low-risk dependent tasks | Run actual designated checks before the second task; label implementer self-check accurately; no new approval merely per task |
| Material local-to-cloud change, discussion only | Explain changed scope/data/authority and affected evidence; no code change or silent new agreement |
| Resume in a fresh session | Read project entry and actual sources/tests, recover current scope and evidence, update the same record |
| Host lacks native cards | Show readable text inline; do not promise unavailable UI or treat attachment as explanation |
| Unrelated Q&A or trivial edit | Do not impose project discovery, Card, ledger or full audit |

Evaluate actual responses, files and runtime checks. Record failures without rewriting them. Model-only trials cannot establish novice comprehension, automatic invocation, large-project reliability or superiority over a native product experience.
