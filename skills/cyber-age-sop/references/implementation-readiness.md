# Implementation Readiness for Integrations

Use this reference when a task crosses a platform, tenant, SaaS product, HRIS, identity provider, API, or production boundary. It separates a useful project plan from a verified implementation contract without requiring every project detail before safe discovery can begin.

## Handoff Levels

Assign the narrowest level that describes the next authorized task:

| Level | Meaning | Allowed next work |
|---|---|---|
| `decision-ready` | The user can choose or reject a direction; implementation facts may be unknown | Decision, scope, or bounded discovery planning |
| `discovery-ready` | Target, allowed inspection, permissions, outputs, and stop condition are explicit | Read-only documentation/configuration inventory or sandbox inspection |
| `prototype-ready` | Path is selected and synthetic/test data plus interface assumptions are available | Reversible prototype in an isolated environment |
| `build-ready` | Interfaces, identity, data boundaries, behavior, validation, and authorization are verified | Scoped implementation in the named environment |
| `field-ready` | Build is verified and all live-operation prerequisites in Gate 5 are satisfied | Authorized deployment or field change |

A higher-level plan may be decision-ready while its first subtask is discovery-ready. Do not label the entire project build-ready when only a discovery task is ready.

## Readiness Matrix

For multi-system or sensitive-data projects, track each MVP capability separately:

| Capability / user outcome | System of record | Platform path | Verified interface and source | Identity / role / field scope | Normal and failure behavior | Validation evidence | Owner and status |
|---|---|---|---|---|---|---|---|
| [outcome] | [system or unknown] | [selected or undecided] | [actual interface, documentation, date, or unknown] | [verified scope or unknown] | [expected result and fallback] | [test and expected result] | [owner; decision/discovery/build-ready] |

Use explicit values such as `unknown`, `decision needed`, `tenant discovery`, or `blocked`. Do not replace them with guessed implementation details.

## Integration Contract

Before a task that reads or writes external business data is `build-ready`, record the information that changes its safety or behavior:

- **Product path:** selected product, app type, tenant/environment, and any required tenant tier or feature entitlement.
- **Source of truth:** authoritative system and owner for each field or workflow state.
- **Identity:** how the signed-in user maps to a business identity; how employee, manager, HR, and admin roles are derived and revalidated.
- **Permissions:** app/user identity, approved scopes, data range, field sensitivity, approver, and prohibited data.
- **Interface:** actual documented or tenant-verified endpoint/event, version, request/response schema, freshness, rate/size limits, and known deprecation status.
- **Behavior:** user-visible success, missing/unknown, denied, stale, conflict, timeout, retry, duplicate, and human-handoff behavior.
- **Evidence:** representative test cases, expected results, acceptance threshold and how it is measured.
- **Operations:** logs and sensitive-data handling, owners, alerts, support path, rollback/compensation, and stop condition where relevant.

An example endpoint or pseudo-schema may help communicate a concept, but label it illustrative. It is not an implementation dependency until checked against current official documentation or the named tenant.

## Discovery-Only Handoff

If build prerequisites are unknown, write a discovery Agent Brief instead of guessing or blocking all progress:

```markdown
## Readiness
Level: discovery-ready

## Goal
[Which implementation-changing facts this task must establish]

## Target and authorization
[Named documentation source, sandbox, tenant owner, and authorization boundary]

## Allowed inspection
- [Read-only sources or configuration]

## Prohibited actions
- No production writes, permission changes, real-person data exports, or deployment

## Required outputs
- [Readiness Matrix rows updated]
- [Sources and verification date]
- [Unknowns, owner, and next decision]

## Completion criteria
- [Observable evidence that answers the discovery question]

## Stop condition
- [Missing authorization, sensitive data, or unavailable source that stops inspection]
```

Do not ask an implementation Agent to bypass an unavailable tenant/API by inventing a mock contract. A prototype may use clearly labeled synthetic data after the user accepts that evidence boundary.

## Build-Ready Agent Brief

For each implementation slice, state:

- the selected path and exact target environment;
- the capability and allowed files/configuration;
- verified interfaces, schemas, identity mapping, and permission scopes;
- accepted product decisions and non-goals;
- normal and failure behavior;
- tests, expected results, and evidence tier;
- data and mutation boundaries;
- reporting location and follow-up discoveries.

Split work by independently verifiable capability, for example policy retrieval, authenticated self-status read, or human handoff. Do not combine a tenant discovery, production integration, and rollout into one Agent Brief.
