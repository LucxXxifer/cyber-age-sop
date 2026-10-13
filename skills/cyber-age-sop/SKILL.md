---
name: cyber-age-sop
description: >
  Use when someone wants to BUILD/DEVELOP a custom solution (tool, plugin, internal system) 
  and needs help scoping it into a deliverable MVP. 
  
  TRIGGER when user explicitly says:
  - "build/develop/create X for my team/company"
  - "existing tools don't fit, need custom solution"
  - "help me build X from scratch"
  
  DO NOT trigger when:
  - User wants to CHOOSE between existing tools → give direct recommendation
  - User asks "should I use A or B" → tool comparison
  - User says "I want to use/find/get X" → likely looking for existing solution
  
  When unclear: ask ONE clarifying question:
  "你是想找现成的工具使用,还是要开发一个定制的?"
metadata:
  short-description: Turn fuzzy product ideas into bounded, verifiable MVP delivery
  version: "0.4.4"
  status: decision-brief
---

# Cyber-Age SOP

`cyber-age-sop.skill` helps you turn a product idea into a bounded delivery task with clear evidence criteria, then verifies what was actually delivered.

## Routing

This skill is for someone who:
- Wants to build/develop a custom solution ("我要做一个 X 给团队用")
- Has a product-shaped goal but cannot scope it
- Doesn't know how to explain requirements to an agent or engineer
- Faces technical choices but lacks the context to evaluate them
- Needs to verify what "done" actually means

**Not for:**
- Tool selection or comparison ("该用 Notion 还是 Google Docs?") → give recommendation directly
- Exploring what you want → use `guided-thinking`
- Generating options to compare → use `brainstorming`
- Visual/brand creative execution → use `huashu-design` or `meigen`
- Facilitation, coaching, or relationship work → use `guided-thinking`

## Hard Boundaries

This skill is independent from `guided-thinking`.

- Do not invoke `guided-thinking` automatically.
- Do not turn a project task into emotional, relationship, coaching, or consent-oriented facilitation.
- Borrow facilitation principles: preserve user wording, acknowledge what they said before asking, separate facts from assumptions, ask one question at a time that invites description rather than menu selection.
- If the user asks for 大师级引导、大師級引導、引导大师、引導大師, guided thinking, or layered questioning, hand off to `guided-thinking`. Resume only when they return with a Thought Brief or explicitly ask to run the project SOP.

`prompt-refiner` is an optional packaging tool, not a mandatory stage.

## Path Selection

Choose the smallest path that safely produces the requested result:

| Situation | Path |
|---|---|
| One-file typo, formatting fix, or trivial low-risk change with known check | Trivial fast path below |
| Clear bounded task, more than trivial | Create short Agent Brief and execute |
| Unclear project intent or scope | Discovery exploration → Project Anchor → Technical Translation → **Decision Brief** |
| Architecture, UI, or delivery choice unsettled | Add Shape/Decision checkpoint |
| Code, UI/documentation, or field work with different evidence needs | Load matching task profile |
| Existing brief needs conversion to executable prompt | Use `prompt-refiner` |

Do not force every project through every artifact.

**The Decision Brief (Gate 3.5) is the main artifact for non-technical users.** For a build-from-scratch project, the conversation is not the deliverable — the saved Brief is. Produce it unless the user explicitly opts out.

## Trivial Fast Path

Use only when the change is small, reversible, low-risk, and well-specified. Examples: one typo, one formatting fix, one known documentation link repair.

1. Restate the one-sentence change and the one relevant check.
2. Make the smallest change.
3. Run the relevant check and inspect the diff.
4. Report the result briefly in the conversation.

**Upgrade condition**: If the same kind of small change appears 3+ times, upgrade to full Brief path.

Skip full Project Anchor, task profile, full Agent Brief, external report file, and SOP feedback for this path. If the task expands, affects behavior, touches permissions, or has unclear evidence, return to normal gates.

## Discovery: Facilitated Exploration (before Gate 1)

When project intent or scope is unclear, create space for the user to describe their situation before filling any anchor template.

### Guiding Principles

1. **Acknowledge first, then explore**
   - Start by reflecting what the user said in their own words
   - Show you heard their uncertainty or confusion
   - Example: "你说想做一个记账工具，但不确定要做成 App 还是网页。我听到的是：你知道需要记账功能，但对实现形态还在考虑。"

2. **Ask questions that invite description, not menus**
   - ❌ Not: "你多久记一次账？A) 每次花钱 B) 每天晚上 C) 每周末"
   - ✅ Instead: "你现在是怎么记账的？或者，是什么让你觉得需要一个记账工具？"
   - Let the user tell their story; don't force them to pick from preset options

3. **One round, one open question**
   - Ask one question at a time
   - Don't chain multiple questions ("你的预算多少？用户有多少？什么时候要？")
   - Wait for the answer before deciding what to ask next

4. **Separate layers progressively**
   As the user describes, distinguish:
   - **感受/困惑**: Their uncertainty, frustration, or confusion ("不知道该怎么做")
   - **想法**: What they think might work ("可能做个 App？")
   - **意图**: What they actually want to achieve ("能方便记账")
   - **事实**: Confirmed current situation ("现在用 Excel 但经常忘记")

   Don't ask about all four layers at once. Let them emerge through natural conversation.

5. **Tone: conversational, not procedural**
   - ❌ Not: "在决定技术方案之前，我需要了解一个会影响项目范围的关键问题"
   - ✅ Instead: "在我们讨论做成什么样之前，我想先了解一下你现在的情况"

### When the User Cannot Describe Clearly

After **two rounds** of open exploration, if the project anchor is still unclear:

1. **First, try a different angle**
   - "我想从另一个方向了解：你平时在什么情况下会需要用到它？"
   - "或者这样问：设想一下，如果这个工具做好了，你会在什么时候打开它？"

2. **If still unclear, offer candidate anchors**
   - Present 3-5 possible problem anchors based on what they've said
   - Let them pick one or clarify which is closest
   - Example: "根据你说的，可能是这几个方向中的一个：1) ... 2) ... 3) ... 哪个更接近你的想法？或者都不是？"

3. **If none fit, classify and hand off**
   - "I don't know what I want yet" → hand off to `guided-thinking`
   - "I want to compare options first" → hand off to `brainstorming`
   - "Definitely not feasible at MVP stage" → state this with reasoning, suggest closer alternative
   - "I cannot determine feasibility" → mark with source and date, state what info is missing

### Discovery Output

As the conversation progresses, start filling the anchor **progressively** (not as a questionnaire):

```markdown
## Project Anchor (emerging)
- Human goal: [用户原话中的目标]
- Primary user and situation: [他们描述的使用场景]
- Problem in one sentence: [一句话总结要解决的问题]
- Confirmed facts: [用户已确认的现状]
- Unverified assumptions: [还需要验证的假设]
```

Stop discovery when you have enough to proceed to MVP Framing. Don't keep asking if the next question won't change the direction.

## Visual Aids (Optional)

Visual aids help non-technical users **see** their product structure through simple ASCII diagrams.

### When User Asks Directly

If user says "画个图" / "帮我画流程图" / "能用图说明吗", generate visual aid immediately with ASCII art.

### When to Suggest (Requires User Confirmation)

Suggest visual aids when complexity justifies it:

| Scenario | Signal | Suggestion Template |
|---|---|---|
| Complex flow | 3+ steps or "如果...那么..." branches | "听起来流程有几个分支，我可以画个简单流程图帮你看清楚，要吗？" |
| Multi-role | Mentions "管理员"/"用户"/"访客" etc. | "涉及不同角色的权限，我可以画个图说明谁能做什么，需要吗？" |
| Multi-module | Mentions "前端"/"后端"/"数据库" or "分几个部分" | "系统有几个模块，我可以画个架构图展示它们的关系，要不要？" |
| Layout | "页面分成..."/"左边...右边..." | "可以用简单布局图展示页面结构，需要吗？" |

**Important:**
- Wait for user confirmation ("好"/"要"/"画吧") before generating
- If user says "不用"/"先不要" or changes topic → skip silently
- Don't force visuals if user already understands

See `references/visual-aids.md` for diagram templates (flow/architecture/layout).

## Web Research (Optional)

Web research verifies technical feasibility, obtains cost estimates, and fact-checks constraints when it would improve decision quality.

### When User Asks Directly

If user says "查一下 XX" / "帮我看看 XX 的文档" / "最新价格是多少", research immediately using `tavily-search` or `tavily-extract`.

### When to Suggest (Requires User Confirmation)

Suggest web research when it would improve decision quality:

| Scenario | Signal | Suggestion Template |
|---|---|---|
| Uncertain feasibility | Need to say `我不知道` but can verify | "我不确定 XX 是否支持这个功能，我可以查一下官方文档，要吗？" |
| Cost estimation | User asks "要多少钱" + involves 3rd-party service | "成本涉及 XX 服务的最新价格，我可以查一下，需要吗？" |
| Specific tool mentioned | User says "用 Firebase"/"用 Stripe" etc. | "你提到 XX，我可以查一下它的限制和定价，帮你判断合不合适，要吗？" |
| Need evidence for `确定不可行` | Believe infeasible but lack source | "这个看起来不可行，但我想查证一下官方文档确认，可以吗？" |

**Important:**
- State uncertainty first ("我不确定..." / "我不知道...")
- Then offer to research ("我可以查...")
- Wait for confirmation ("查吧"/"好"/"要")
- If user provides answer directly ("我预算是 XX") → use their info, skip research
- If user says "不用"/"我知道" → continue with existing info

**Citation format:**
- `查证`：根据 [来源](URL) (YYYY-MM-DD 验证)，...
- `经验估算`：基于类似项目经验，... (未查证)
- `未查证估算`：可能...，需要进一步确认

See `references/web-research.md` for Tavily usage and citation format.

## When User Cannot Answer (After 2 Rounds)

If after 2 rounds of open exploration the user still cannot describe their situation or needs clearly:

### Step 1: Try a Different Angle

Shift the frame to help them see it differently:

**Time perspective:**
> "我想从另一个方向了解：你现在怎么做这件事的？如果有这个工具，会有什么不同？"

**Problem vs goal:**
> "换个角度：现在遇到的问题是什么？希望达到什么效果？"

**Self vs others:**
> "或者这样想：你自己会怎么用？其他人会怎么用？"

### Step 2: Offer Candidate Anchors (If Still Unclear)

If the different angle doesn't help, offer **3-5 candidate anchors** based on common patterns:

> "听起来可能是以下几种情况之一，看看哪个更接近你的需求：
> 
> A) [具体场景 1 - 包含规模/用户/频率]
> B) [具体场景 2 - 不同的方向]
> C) [具体场景 3 - 另一种可能]
> 
> 或者都不太对？可以说说哪个比较接近，或者差在哪里。"

**Important rules:**
- Make anchors **specific** (not "做个工具" but "公司内部任务分配系统，5-10人用")
- Make them **diverse** (cover different scales, approaches, or domains)
- Allow rejection (user can say "都不太对")
- These are **exploration aids**, not preset solutions

### Step 3: Generate Blocked Report (If None Fit)

If none of the candidate anchors fit, generate a **Blocked Report**:

```markdown
## Blocked Report

**What we explored:**
- [尝试过的角度 1]
- [尝试过的角度 2]
- [提供过的候选锚点]

**What is still unclear:**
- [仍不清楚的关键点 - 具体说明]

**Suggested next steps:**
1. 使用 `guided-thinking` 进行更深入的意图探索
2. 先尝试现成工具（[具体建议]），在使用中明确真正需要什么
3. 咨询 [具体领域] 的领域专家

**Certainty label:** `我不知道` (需要更多信息才能判断可行性)
```

### Certainty Labels (When Stating Feasibility)

When you need to state whether something is feasible:

| Label | Meaning | When to Use | Required Evidence |
|---|---|---|---|
| `确定不可行` | Clear blocker exists | Verified technical/cost/legal constraint | Source + date + specific reason |
| `我不知道` | Need external info | Feasibility depends on unknown factors | State what info is needed |
| `有条件可行` | Feasible if conditions met | User must decide on prerequisites | List conditions explicitly |

**Examples:**

✅ **Correct usage:**
- `确定不可行`：根据 [Chrome Extension Manifest V3 文档](URL)，无法在后台持续运行脚本（2026-10-12 验证）
- `我不知道`：需要确认你的预算范围和团队技术背景才能判断是用现成工具还是自建
- `有条件可行`：如果你能接受每月 $20 云服务费用 + 每周 1 小时维护时间，可以用 Firebase 方案

❌ **Wrong usage:**
- "应该可以"（模糊，未标注不确定性）
- "大概能做"（猜测，无证据）
- "这个很简单"（未考虑维护成本和使用者背景）

**Never guess feasibility.** If uncertain, use `我不知道` and state what information is needed to determine feasibility.

## Gate 1: Project Anchor

After discovery exploration, formalize the anchor:

```markdown
## Project Anchor
- Human goal:
- Primary user and situation:
- Problem in one sentence:
- Confirmed facts:
- Unverified assumptions:
- In scope:
- Out of scope:
- Evidence boundary:
- Deliverables:
- Stop or recovery condition:
```

Fill this progressively based on what emerged during discovery. Skip fields already clear from the user's description. Ask only when a missing fact would change scope, evidence, or delivery path.

**Certainty labels**: Use `确定不可行` (definitely not feasible) vs `我不知道` (I don't know) vs `有条件可行` (feasible with conditions). Always cite source and date for feasibility claims.

### MVP Framing Rules

Before defining MVP scope, write:

**Core Invariant** (cannot be substituted):
> "The user wants to change [X]. This version must not replace it with [Y]."

Then apply the narrowing question:
> "If we remove [feature], will the user notice immediately?"
> - Yes → include in MVP
> - No → move to non-goals

**Floor condition**: The MVP must let the user's specified problem be touched in a real scenario, not just any demonstrable slice.

For each cut, state explicitly: "This cut loses [capability/constraint]. Acceptable because [reason]."

## Thought Brief Handoff

Treat a user-provided Thought Brief as authoritative when it contains goal, scope, non-goals, acceptance signal, and evidence or permission boundary. Do not repeat questions already answered there. Ask only for a missing fact that can change scope, evidence, authorization, or delivery.

## Gate 2: Task Profile

Select one primary profile and load its reference:

- `code`: behavior, allowed files, tests, build, and diff.
- `ui-doc`: user-visible states, wording boundaries, UI/documentation parity, static/runtime checks.
- `field`: preflight, rollback, environment, observation, and long-running evidence.

Read [references/task-profiles.md](references/task-profiles.md) only for the selected profile.

## Gate 3: Technical Translation (when needed)

When technical choices affect product outcomes, translate them for the user:

Read [references/technical-translation.md](references/technical-translation.md) for the translation protocol.

**Decision authority**:
- **Product-visible consequences** → user decides, user can veto
- **Implementation details** → agent proposes, must disclose, user can veto

All agent implementation choices must be disclosed and allow veto.

## Gate 3.5: Decision Brief (可帶走的產出)

**這是本 skill 對非技術使用者的核心交付物。**

Anchor、Technical Translation、MVP 邊界的內容目前散落在對話中。對話關掉就沒有了。決策一旦形成，就必須落成一個使用者可以保存、可以給別人看、三個月後可以回頭查的檔案。

### 何時產出

- Discovery + Technical Translation + MVP Framing 完成後
- 使用者做出方向決定後（或明確選擇「先不做」）
- **一律產出**，除非使用者明確說「不用給我檔案」

### 產出位置

寫在 repository 外，由使用者指定或預設到：

```
~/<專案名>-decision-brief.md
```

不要在 repo 內建立此檔案（沿用 Non-Negotiables 的既有規則）。

### 格式

```markdown
# Decision Brief — [專案名]

**日期**: YYYY-MM-DD
**狀態**: [決定要做 / 先驗證需求 / 暫緩 / 不做]

---

## 1. 我要解決什麼（使用者原話優先）

> [直接引用使用者的關鍵原話]

**一句話問題**: [用一句話總結]

**誰會用、什麼時候用**: [使用者 + 場景]

---

## 2. 已確認的事實 vs 還沒驗證的假設

**已確認**:
- [使用者明確說過的現況]

**未驗證（做之前應該確認）**:
- [假設 1] — 驗證方式: [怎麼確認]
- [假設 2] — 驗證方式: [怎麼確認]

---

## 3. 建議方案

**推薦**: [方案名]

**為什麼**:
- [理由 1，用產品後果描述，不用技術術語]
- [理由 2]

**什麼情況下這個推薦是錯的**:
- [具體可判斷的條件]

**帶價（time / cost / maintenance）**:
- 時間: [估算] — 來源: [查證/經驗估算/未查證估算]，[日期]
- 成本: [估算] — 來源: [同上]
- 維護: [具體描述，不是「中等」]

**如果之後要換方案**:
- 需要重做: [什麼]
- 估算工作量: [多少]

---

## 4. 第一版做什麼、不做什麼

**核心不變量**（這一版不可以換掉的東西）:
> [使用者真正想改變的是 X，這一版不可以換成 Y]

**第一版包含**:
- [功能 1]（拿掉它使用者會立刻發現）
- [功能 2]

**第一版不包含**（明確的非目標）:
- [功能 3] — 拿掉不會被發現
- [功能 4]

**每一刀失去了什麼**:
- 少了 [功能 3] → 失去 [能力] → 可接受因為 [理由]

**底線條件**: 第一版必須讓使用者在真實場景碰過 [那個問題]，不是任何一個可示範的切片。

---

## 5. 我自己可以驗證的證據

| 這一層 | 能證明 | 不能證明 |
|---|---|---|
| [本地測試 / 實際使用 / 現場] | [什麼] | [什麼] |

**驗收訊號**: [什麼情況算成功]
**停止條件**: [什麼情況該放棄或換方向]

---

## 6. 下一步

**你現在可以做的事**（按建議順序）:

1. **[立即可做]** — 成本 [X]，時間 [Y]
   - 目的: 驗證 [哪個假設]
   - 如果結果是 [A] → 繼續
   - 如果結果是 [B] → 換方向

2. **[需要決定後做]** — 交給:
   - `cli-creator`（如果決定是做 CLI 工具）
   - `agents-sdk`（如果決定是做 Agent app）
   - 或其他開發者／Agent

**這個 Brief 的保存位置**: [路徑]
**建議回顧時間**: [X 週後]

---

## 附錄：Agent Brief（如果決定要做）

[若已進入實作決策，附上完整 Agent Brief]
```

### 品質檢查

產出前確認：

- [ ] 使用者原話被保留（不是被改寫成產品術語）
- [ ] 已確認事實與未驗證假設分開
- [ ] 有明確推薦，不是選單
- [ ] 每個估算都有來源標記
- [ ] 核心不變量寫下來了
- [ ] 每一刀失去什麼說清楚了
- [ ] 下一步是可執行的，不是「再想想」
- [ ] 檔案寫在 repo 外

### 最小版本

如果對話很短、專案很小，Decision Brief 可以只有：

```markdown
# Decision Brief — [專案名]

**問題**: [一句話]
**推薦**: [方案] 因為 [理由]
**不做**: [非目標]
**下一步**: [一個可執行的動作]
```

**不要為了填滿模板而填。空欄位比假內容好。**

See [references/decision-brief-template.md](references/decision-brief-template.md) for the template, checklist, and anti-patterns.

## Gate 4: Delivery Contract

Before implementation, produce an Agent Brief containing:

- `Project ID`, project name, `Task ID`, and date
- Goal and user context
- Human decisions and accepted trade-offs
- Scope and non-goals
- Input files and design material
- Constraints, permissions, dependencies, and environment boundary
- Required behavior and failure behavior
- Validation commands and expected results
- Acceptance criteria
- Reporting path outside the repository
- A `Follow-up discoveries` section for useful but out-of-scope findings

For risky or ambiguous work, list an explicit file allowlist. Do not let a follow-up discovery silently become implementation scope.

Use lightweight Brief for bounded task; full Brief only when task has multiple files, multiple evidence tiers, live access, material risk, or uncertain scope.

## Gate 5: Execute and Verify

The Agent may inspect, restate contract, implement smallest change, and run specified checks. It must not change project goal, access unauthorized devices/accounts/secrets, or claim field success from local tests.

For live field or infrastructure work, do not execute until these are explicit:

- Exact target and environment
- Authorized scope and who authorized it
- Intended change
- Backup or configuration capture
- Rollback method and out-of-band recovery path
- Timeout and stop condition
- Observations that count as pass or failure

If any item is missing, remain in planning mode and report the blocking gap.

The orchestrator independently checks the result:

1. Read actual version-control diff and changed-file list.
2. Confirm no report, log, cache, or generated artifact landed in repo.
3. Re-run narrowest relevant checks, then broader checks when required.
4. Separate code, build/release, field, and long-running evidence.
5. For UI/documentation work, check state-to-wording parity and run static syntax checks. If a claim depends on runtime rendering, interaction, or responsive layout, use real browser or mark `Not verified`.

Use [references/acceptance-and-evidence.md](references/acceptance-and-evidence.md) for audit and report contract.

## Gate 6: Review and Improve

For normal or full tasks, end with:

```markdown
## Changed
## Verified
## Not verified
## Remaining risk
## Follow-up discoveries
## SOP feedback
```

Only promote a workflow change when a repeated failure or meaningful experiment supports it. Do not add a permanent rule for one-off preference.

## Anti-Patterns (mark these in reviews)

1. **Self-justifying completion**: Claiming success by restating what was attempted, not what was verified.
2. **Evidence tier collapse**: Treating local test pass as field success.
3. **Scope drift via follow-up**: Quietly implementing out-of-scope discoveries without user decision.
4. **Menu-driven questioning**: Giving the user preset options instead of letting them describe their situation.
5. **Skipping acknowledgment**: Jumping to questions without showing you heard what they said.

## Non-Negotiables

- Smallest viable slice before generalization
- Scope and non-goals before implementation
- Evidence before completion claims
- Reports and temporary outputs outside the repository
- No live deployment, external publication, credential use, or destructive action without explicit authorization
- `no local warning` ≠ `runtime success`; local success ≠ field acceptance
- **Product-visible consequences require user decision; implementation details require disclosure and allow veto**
- **Round-trip commitment (phased)**:
  - Discovery phase: +2~3 rounds to establish direction (necessary for unclear intent)
  - After anchor clear: ≤ +1 round for Technical Translation and decision
  - Trivial tasks: skip Discovery, direct execution
  - Quality trade-off: baseline gives instant output but user cannot evaluate; this skill adds exploration rounds but user can make informed decisions
- **Acknowledge what the user said before asking; invite description, not menu selection**
