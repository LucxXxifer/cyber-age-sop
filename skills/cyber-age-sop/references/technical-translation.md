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
| Implementation detail (library choice, file structure, algorithm) | **Agent proposes** | Must disclose choice, user can veto |

## Estimate Quality Markers

Mark all estimates with source and date:
- `查证` (verified): from pricing page, documentation, or quote; include URL and check date
- `经验估算` (experience-based): from past similar work; state basis
- `未查证估算` (unverified): educated guess; mark as such

Never present unverified estimates as facts. Non-technical users will treat them as commitments.

## Example (Good)

```markdown
## Technical Translation

### User's Original Need
"我想随时能在手机上查看这些数据"

### Recommended Approach
**Option: Shared spreadsheet (Google Sheets or Airtable)**
**Why:** Changes appear instantly on all devices, no server to maintain, can share view-only links
**Don't choose this if:** You need more than 10,000 rows, or the data is highly sensitive
**Switch cost:** If you need custom app later, export to CSV takes ~1 hour, data structure stays the same

---

### Alternative Options

#### Option B: Custom mobile app
- **Form:** App on iPhone/Android
- **Estimated time:** 4-6 weeks for MVP — 经验估算, based on similar 2-screen apps, 2026-10-12
- **Monthly cost:** $0-25/month (hosting) — 查证: Firebase free tier → Blaze plan, https://firebase.google.com/pricing, 2026-10-12
- **Maintenance burden:** Weekly: check crash reports; Monthly: OS update testing
- **Main risk:** App store review can take 1-7 days; if rejected, public launch delays
- **Switch cost:** Complete rebuild if changing platform (iOS → Android or vice versa); ~50% of original dev time
- **Breakage point:** Free tier ends at 10GB stored + 50K reads/day

### Not Recommended Now
**Native phone app with offline mode:** Adds 3-4 weeks for sync logic, overkill if WiFi always available
**Closer alternative:** Start with spreadsheet; if offline becomes blocking, revisit in 3 months

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
