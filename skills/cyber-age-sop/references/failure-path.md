# Failure Path Protocol

## Purpose

Handle situations where the user cannot articulate their needs after facilitated exploration, while preserving the facilitation principles from guided-thinking.

## When to Apply

This protocol applies when:
- After 2 rounds of open exploration, the user still cannot describe their situation clearly
- User repeatedly responds with "I don't know" or "You decide for me"
- User asks for preset options instead of describing their own needs
- Different angles (time/problem-goal/self-others) don't help clarify

## Three-Step Escalation

### Step 1: Try a Different Angle

Before offering structured options, reframe the question to help them see it from a new perspective:

**Time perspective:**
```
"我想从另一个方向了解：你现在怎么做这件事的？如果有这个工具，会有什么不同？"
```

**Problem vs goal frame:**
```
"换个角度：现在遇到的问题是什么？希望达到什么效果？"
```

**Self vs others perspective:**
```
"或者这样想：你自己会怎么用？其他人（团队/客户）会怎么用？"
```

**Why this works:**
- Shifts cognitive frame without adding complexity
- Helps user access different mental models
- Still open-ended, not a menu

---

### Step 2: Offer Candidate Anchors

If different angles don't help, offer **3-5 candidate anchors** as exploration aids.

#### What Makes a Good Candidate Anchor

✅ **Specific and concrete:**
- Not: "A) 简单版 B) 复杂版"
- Yes: "A) Google Sheets 插件，团队 5 人用，自动记录每日任务"

✅ **Diverse coverage:**
- Different scales (个人用 vs 团队用 vs 公司级)
- Different approaches (现成工具改造 vs 从零构建)
- Different domains (if the user's need is ambiguous)

✅ **Allows rejection:**
- Always add: "或者都不太对？可以说说哪个比较接近，或者差在哪里。"
- User can reject all options without feeling they did something wrong

#### Example Format

```markdown
听起来可能是以下几种情况之一，看看哪个更接近你的需求：

A) **内部任务分配系统**：团队 5-10 人，每天分配任务，需要看到谁在做什么
B) **客户项目跟踪**：给客户看项目进度，不需要内部协作功能
C) **个人 GTD 工具**：只有你自己用，重点是快速记录和提醒

或者都不太对？可以说说哪个比较接近，或者差在哪里。
```

#### Common Patterns for Candidate Anchors

| User says | Possible anchors |
|---|---|
| "做个记账工具" | A) 个人记账 App<br>B) 家庭共享记账<br>C) 小团队报销系统 |
| "团队文档协作" | A) 实时协作编辑（类 Google Docs）<br>B) 版本管理+审批流（类 Confluence）<br>C) 知识库+搜索（类 Notion） |
| "数据可视化" | A) 静态报表（每周生成）<br>B) 实时 Dashboard（随时刷新）<br>C) 交互式探索工具 |

---

### Step 3: Generate Blocked Report

If none of the candidate anchors fit, **do not guess further**. Generate a Blocked Report and hand off.

#### Blocked Report Template

```markdown
## Blocked Report

**What we explored:**
- [列出尝试过的角度：时间视角 / 问题vs目标 / 自己vs他人]
- [列出提供过的候选锚点]

**What is still unclear:**
- [具体说明哪些关键信息仍然缺失]
- [Example: "不清楚主要使用者是谁，以及使用频率"]

**Why I cannot proceed:**
- [说明为什么这些信息对判断可行性/方向至关重要]

**Suggested next steps:**
1. **Use `guided-thinking` for deeper intent exploration**
   - 进行更深入的意图澄清和假设检验
   
2. **Try existing tools first**
   - 先用 [具体建议的现成工具]，在实际使用中明确真正需要什么
   
3. **Consult domain experts**
   - 咨询 [具体领域] 的专家，确认技术可行性和成本

**Certainty label:** `我不知道` (需要 [具体信息] 才能判断可行性)
```

#### When to Use Blocked Report

✅ **Use when:**
- Tried 2+ rounds of open exploration
- Tried different angles
- Offered candidate anchors (if applicable)
- User still cannot describe their needs or situation

❌ **Don't use when:**
- You just haven't tried different angles yet
- You could ask one more clarifying question that would resolve it
- The user is describing their needs, just slowly

---

## Certainty Labels

When you need to state feasibility, use one of these three labels explicitly:

### 1. `确定不可行`

**Meaning:** Clear, verified blocker exists (technical, cost, legal, or other constraint).

**Requirements:**
- Must cite **source** (documentation URL, API reference, expert consultation)
- Must include **date** of verification
- Must state **specific reason** (not just "不支持")

**Example:**
```
确定不可行：根据 Chrome Extension Manifest V3 规范 [链接]，
后台脚本无法持续运行超过 5 分钟（2026-10-12 验证）。
如果需要持续监控，需要改用原生应用或 Web 应用方案。
```

**When NOT to use:**
- When you haven't verified the blocker personally
- When it might be feasible with workarounds
- When feasibility depends on user's resources/choices

---

### 2. `我不知道`

**Meaning:** Feasibility depends on unknown external factors.

**Requirements:**
- State **what specific information** is needed
- Explain **why** that information determines feasibility
- Suggest **how** to obtain that information (if possible)

**Example:**
```
我不知道：需要确认以下信息才能判断：
- 你的预算范围（决定是用现成服务 $20/月，还是自建服务器）
- 团队技术背景（决定能否自己维护，还是需要托管服务）

可以先说说这两点，我再给具体方案建议。
```

**When to use:**
- Feasibility depends on user's budget, time, or technical skill
- Need to know team size, usage frequency, or data sensitivity
- External factors (API availability, legal constraints) are unknown

---

### 3. `有条件可行`

**Meaning:** Feasible, but user must accept specific prerequisites or constraints.

**Requirements:**
- List **conditions explicitly** (cost, time, ongoing maintenance, tradeoffs)
- Let user **decide** whether to accept those conditions
- Include **switch cost** if moving away from this approach later

**Example:**
```
有条件可行：如果你能接受以下条件：
- 每月 $20 云服务费用（Firebase Hosting + Firestore）
- 每周 1 小时维护时间（处理用户反馈、更新内容）
- 用户数超过 1000 人后需要升级方案（额外 $50/月）

可以用这个方案。如果后续想迁移到自建服务器，
需要重写后端代码（约 2-3 周工作量）。
```

**When to use:**
- Technical solution exists but has non-trivial costs
- Solution requires ongoing work (not one-time build)
- Solution has scale limits or future migration costs

---

## Common Mistakes to Avoid

### ❌ Guessing Feasibility Without Evidence

**Wrong:**
```
"应该可以做，不会太复杂"
"大概需要 2 周时间"
"这个功能很常见，肯定能实现"
```

**Why wrong:**
- "应该" and "大概" hide uncertainty
- User cannot tell if you verified this or just guessed
- If wrong, user wastes time on infeasible path

**Right:**
```
我不知道：需要确认 [具体信息] 才能判断是否可行。
```

---

### ❌ Offering Candidate Anchors Too Early

**Wrong sequence:**
```
User: "我想做个工具"
Assistant: "你是想做 A) XX 还是 B) YY？"
```

**Why wrong:**
- Skips open exploration
- Forces user into preset categories
- May miss what they actually need

**Right sequence:**
```
User: "我想做个工具"
Assistant: "我想先了解一下：你现在怎么做这件事的？"
[2 rounds of open exploration]
[Try different angles if still unclear]
[Only then offer candidate anchors if needed]
```

---

### ❌ Making Candidate Anchors Too Vague

**Wrong:**
```
A) 简单版
B) 复杂版
C) 中等复杂度
```

**Why wrong:**
- User doesn't know what "简单" means in this context
- No concrete details to react to
- Doesn't help them clarify their mental model

**Right:**
```
A) Google Sheets 插件，5 人团队用，自动记录每天任务
B) 独立网页，支持 50+ 人，带权限管理和报表
C) 个人命令行工具，只在本地运行，不需要服务器
```

---

### ❌ Forcing User to Pick an Option

**Wrong:**
```
"你选 A 还是 B？必须选一个我才能继续"
```

**Why wrong:**
- Violates facilitation principle: preserve user autonomy
- User may feel none of the options fit
- Creates false choice

**Right:**
```
"或者都不太对？可以说说哪个比较接近，或者差在哪里。"
```

If user rejects all options → proceed to Blocked Report.

---

## Borrowed Principles from guided-thinking

This protocol adapts guided-thinking's "when stuck" mechanism:

1. **Acknowledge confusion first**
   - "听起来现在还不太清楚..."
   - Not: "你需要回答这些问题才能继续"

2. **Don't force preset options**
   - Candidate anchors are exploration aids, not requirements
   - User can reject all of them

3. **Preserve user's autonomy**
   - User decides when to stop exploring
   - User decides whether to accept suggested next steps

4. **Make uncertainty explicit**
   - Use certainty labels (`我不知道` / `确定不可行` / `有条件可行`)
   - Never hide uncertainty with vague language

5. **Provide exit ramps**
   - Hand off to `guided-thinking` if intent is still unclear
   - Suggest trying existing tools first
   - Recommend domain expert consultation when needed

---

## Testing This Protocol

To verify this protocol works:

1. **Simulate a user who cannot describe their needs**
   - User: "我想做个工具"
   - User: [cannot answer open questions]
   - User: [rejects all candidate anchors]
   
2. **Check protocol coverage**
   - ✓ Tried different angles?
   - ✓ Offered candidate anchors?
   - ✓ Generated Blocked Report with next steps?
   
3. **Check facilitation quality**
   - ✓ Did not force user to pick preset options?
   - ✓ Acknowledged confusion with empathy?
   - ✓ Made uncertainty explicit (certainty labels)?
   - ✓ Provided clear hand-off suggestions?

If all checks pass → protocol is complete.
