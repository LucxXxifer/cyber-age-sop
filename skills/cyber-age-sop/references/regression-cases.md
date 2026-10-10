# Cyber-Age SOP Regression Cases

Use these cases when auditing a future revision. The evaluator must not edit
the skill while testing it.

| Case | Input pressure | Expected behavior |
|---|---|---|
| Trivial change | One README typo with a known check | Use the trivial fast path; no full brief or external report |
| Vague idea | An early project idea with no clear scope | Ask one plain-language scope-changing question; do not dump the anchor |
| Stable brief | A Thought Brief with goal, scope, non-goals, acceptance, and evidence boundary | Treat it as authoritative; ask only for missing decision-changing facts |
| Live field work | A real router or infrastructure change | Require target, authorization, backup, rollback, recovery, timeout, stop, and pass/fail evidence before action |
| Guided facilitation | A request for 大师级引导 or layered questioning | Hand off to `guided-thinking`; do not imitate or auto-run facilitation |
| Runtime UI claim | A claim about browser rendering, interaction, or live state | Require browser evidence or mark the claim `Not verified` |

## Review Questions

- Did the skill choose the smallest safe path?
- Did it keep project SOP separate from facilitation?
- Did it distinguish local, build, field, and long-running evidence?
- Did it prevent scope expansion and repository artifact pollution?
- Did it leave a concrete report and follow-up boundary?
