# Technical Translation Reference

## Purpose

Help non-technical users make informed technical decisions by translating options into product consequences, time, cost, and risk.

## Translation Protocol

Always provide:
1. **One recommendation** with clear reasoning
2. **Switch cost** for each option (what happens if we need to change later)
3. **Source and date** for all estimates
4. Remove vague "适合什么时候" — use concrete criteria instead

## Template

```markdown
## Technical Translation

### User's Original Need
[Quote their exact words]

### Recommended Approach
**Option: [name]**
**Why:** [reason in product terms, not technical terms]
**Don't choose this if:** [concrete condition that makes this wrong]
**Switch cost:** If you need to change in [timeframe], [what has to be redone]

---

### Alternative Options

#### Option B: [name]
- **Form:** [what the user will interact with]
- **Estimated time:** [range] — source: [where this estimate comes from], [date]
- **Monthly cost:** [amount] — source: [pricing page/quote/estimate], [date]
- **Maintenance burden:** [concrete description: "check logs daily" not "moderate"]
- **Main risk:** [what can go wrong in product terms]
- **Switch cost:** [what has to be redone if changed]
- **Breakage point:** [when this option stops working or becomes too expensive]

#### Option C: [name]
[same structure]

### Not Recommended Now
**[Option X]:** [concrete reason why not at MVP stage]
**Closer alternative:** [what gets closer to their goal with lower risk]

### Decision Point
[Exactly one question whose answer determines which option fits]
[Frame in product impact terms, not technical preference]
```

## Decision Authority

| Type | Who Decides | Agent's Role |
|---|---|---|
| Product-visible consequence (user experience, cost, maintenance, data ownership) | **User decides** | Recommend with reasoning, user can veto |
| Implementation detail (library choice, file structure, algorithm) | **Agent resolves within delegated scope** | Keep material choices traceable in the existing Brief and open to correction; explain product consequences in conversation |

## Estimate Quality Markers

Mark all estimates with source and date:
- `查证` (verified): from pricing page, documentation, or quote; include URL and check date
- `经验估算` (experience-based): from past similar work; state basis
- `未查证估算` (unverified): educated guess; mark as such

Never present unverified estimates as facts. Non-technical users will treat them as commitments.

## Example (Good)

Illustrative layout only, not a researched recommendation, quote, product quota or verified schedule. Replace assumptions and placeholders with project-specific evidence; do not copy the example's estimates as facts.

```markdown
## Technical Translation

### User's Original Need
"我想随时能在手机上查看这些数据"

### Recommended Approach
**Option: Shared spreadsheet (Google Sheets or Airtable)**
**Why:** Can provide mobile access and sharing without maintaining a custom server; verify the chosen service's actual access and data rules
**Don't choose this if:** The actual data volume exceeds the checked plan limits, or its handling does not meet the project's sensitivity requirements
**Switch cost:** A later custom app needs export, data-shape and integration checks; migration effort remains unknown until that work is scoped

---

### Alternative Options

#### Option B: Custom mobile app
- **Form:** App on iPhone/Android
- **Estimated time:** [range] — 经验估算; record actual comparable work and assumptions, or mark unknown
- **Monthly cost:** [amount or unknown] — cite the actual service/plan, usage assumption and verification date only after checking
- **Maintenance burden:** Weekly: check crash reports; Monthly: OS update testing
- **Main risk:** The target store's review and rejection handling can delay launch; check its actual current requirements rather than promise a duration
- **Switch cost:** Changing platforms can require replacing platform-specific code; estimate only after checking which modules are reusable
- **Breakage point:** [verified quota or cost threshold for the specific service and billing item; unknown until checked]

### Not Recommended Now
**Native phone app with offline mode:** Adds synchronization and conflict handling that may be unnecessary if offline use is outside the confirmed scope
**Closer alternative:** Start with the scoped online option; revisit if actual offline use becomes a blocker

### Decision Point
How often will you check the data when you have no internet connection?
- Never/rarely → spreadsheet sufficient
- Daily → need offline-capable solution
```

## Common Traps to Avoid

1. **Circular descriptions**: "适合想要快速启动的场景" — this doesn't help the user decide
2. **Undefined adjectives**: "维护量：中等" — what does that mean in hours per week?
3. **Missing source**: "每月成本：$20" — from where? When checked?
4. **Hidden switch cost**: Option looks cheap upfront but locks you into expensive migration
5. **Technical jargon in decision criteria**: "选择 A 如果你需要 ACID guarantees" — translate to product impact

## Non-Technical User Checklist

After writing translation, verify:
- [ ] Can the user repeat back *why* they're choosing this option?
- [ ] Do they know what happens if they're wrong?
- [ ] Are time/cost estimates sourced and dated?
- [ ] Is the "don't choose this if" condition concrete and checkable?
- [ ] Does switch cost describe effort in user-understandable terms (hours, rework scope)?
