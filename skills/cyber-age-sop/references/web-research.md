# Web Research for Decision Quality

## Purpose

Verify technical feasibility, obtain cost estimates, and fact-check constraints through web research when it would improve decision quality.

## Core Principle

**Web research is optional, triggered by user request or agent suggestion with confirmation.**

- User asks directly → research immediately
- Agent identifies uncertainty → **suggest** and wait for confirmation
- User declines or provides answer → use existing info, skip research

## When User Asks Directly (No Confirmation Needed)

If user says any of these, research immediately:

- "查一下 XX"
- "帮我看看 XX 的文档"
- "最新价格是多少"
- "能搜一下 XX API 的限制吗"
- "看看这个 [URL] 说了什么"

→ **Use `tavily-search` or `tavily-extract` immediately, no need to ask for confirmation**

---

## When Agent Should Suggest (Requires Confirmation)

### 1. Uncertain Feasibility (不确定可行性)

**Identify when:**
- You need to say `我不知道` about technical capability
- User asks "这个能做吗？" and you're unsure
- User mentions a specific technology/API you're not certain supports their need
- You're about to say `确定不可行` but lack a verified source

**Suggestion template:**
```
我不确定 XX 是否支持这个功能，我可以查一下官方文档，要吗？
```

**Example scenario:**
```
User: "Chrome 插件能在后台一直运行吗？"

Agent: "我不确定 Chrome Extension Manifest V3 是否支持持续后台运行，
        我可以查一下官方文档，要吗？"

[Wait for user response]

If user says "查吧" / "好" / "要":
→ tavily-search("Chrome Extension Manifest V3 background script limitations")

If user says "不用" / "我知道" / "先不查":
→ Continue with: "那我基于现有信息继续。根据一般限制，后台脚本通常有时间限制..."
```

---

### 2. Cost Estimation (成本估算)

**Identify when:**
- User asks "要多少钱？" or "成本大概多少？"
- You mention a third-party service (Firebase, Stripe, AWS, etc.) without knowing current pricing
- You need to provide `有条件可行` with cost as a condition
- User is deciding between options where cost is a key factor

**Suggestion template:**
```
成本涉及 XX 服务的最新价格，我可以查一下，需要吗？
```

**Example scenario:**
```
User: "用 Firebase 大概要多少钱？"

Agent: "成本涉及 Firebase 的最新价格，我可以查一下，需要吗？"

[Wait for user response]

If user says "查吧":
→ tavily-search("Firebase pricing 2026")

If user says "我预算是 $50/月，你看够不够":
→ Use user's budget as constraint, continue without research
```

---

### 3. Specific Tool Mentioned (用户提到具体工具)

**Identify when:**
- User says "用 [工具名]" (e.g., "用 Firebase", "用 Stripe", "用 Notion API")
- User is deciding between specific tools and needs comparison
- You need to know tool limitations to give accurate Technical Translation

**Suggestion template:**
```
你提到 XX，我可以查一下它的限制和定价，帮你判断合不合适，要吗？
```

**Example scenario:**
```
User: "我想用 Notion API 做个数据同步工具"

Agent: "你提到 Notion API，我可以查一下它的速率限制和数据结构，
        帮你判断合不合适，要吗？"

[Wait for user response]

If user says "好，查吧":
→ tavily-search("Notion API rate limits data structure 2026")

If user says "不用，我自己看过了":
→ Continue with: "好的。那我们基于 Notion API 继续设计..."
```

---

### 4. Need Evidence for `确定不可行` (需要证据标注)

**Identify when:**
- You believe something is infeasible but don't have a verified source
- You need to apply certainty label `确定不可行` which requires source + date
- User's requirement conflicts with what you think is a platform limitation
- You want to avoid saying `我不知道` when verification is possible

**Suggestion template:**
```
这个看起来不可行，但我想查证一下官方文档确认，可以吗？
```

**Example scenario:**
```
User: "微信小程序能直接读取手机通讯录吗？"

Agent: "这个看起来不可行（涉及隐私权限），但我想查证一下官方文档确认，可以吗？"

[Wait for user response]

If user says "查一下吧":
→ tavily-search("微信小程序 通讯录 API 权限限制")
→ Use result to provide `确定不可行` with source + date

If user says "不用了，那就不做这个功能":
→ Continue without research, remove feature from scope
```

---

## How to Use Tavily Skills

### tavily-search: Quick fact-finding

**When to use:**
- General questions ("Firebase 最新价格", "Chrome Extension API 限制")
- Comparison ("Notion vs Airtable API")
- Latest updates ("React 19 新特性")

**Example:**
```bash
/tavily-search Firebase Realtime Database pricing free tier limits 2026
```

**Returns:** Optimized snippets with relevance scores, URLs, published dates

---

### tavily-extract: Get content from specific URLs

**When to use:**
- User provides a URL: "看看这个文档 [URL]"
- You found a relevant doc URL from search results
- Need full content from official documentation

**Example:**
```bash
/tavily-extract https://firebase.google.com/pricing
```

**Returns:** Clean markdown of the page content, LLM-optimized

---

### When to use which

| Scenario | Use |
|---|---|
| User asks "XX 的价格是多少" | `tavily-search` |
| User gives URL "看看这个 [URL]" | `tavily-extract` |
| You found doc URL from search | `tavily-extract` on that URL |
| General "XX 有什么限制" | `tavily-search` |
| Need official API reference | `tavily-search` first → extract top result |

---

## Citation Format

### Three Evidence Quality Levels

Match the format from `references/technical-translation.md`:

#### 1. 查证 (Verified)

**When:** You researched and found official documentation or reliable source

**Format:**
```
查证：根据 [来源名称](URL) (YYYY-MM-DD 验证)，...
```

**Example:**
```
查证：根据 Firebase 官方定价页 (https://firebase.google.com/pricing) (2026-10-12 验证)，
Realtime Database 免费配额是 1GB 存储 + 10GB/月 下载流量。
```

---

#### 2. 经验估算 (Experience-based estimate)

**When:** Based on your knowledge of similar projects, but not fact-checked for this specific case

**Format:**
```
经验估算：基于类似项目经验，... (未查证)
```

**Example:**
```
经验估算：基于类似项目经验，一个简单的 Chrome 插件开发通常需要 1-2 周时间 (未查证)。
```

---

#### 3. 未查证估算 (Unverified estimate)

**When:** You're making an educated guess but could be significantly wrong

**Format:**
```
未查证估算：可能..., 需要进一步确认
```

**Example:**
```
未查证估算：可能需要 $20-50/月的云服务费用，需要进一步确认实际用量和定价。
```

---

## Important Rules

### 1. Wait for Confirmation

When you suggest research, **always wait** for user to say:
- ✅ "查吧" / "好" / "要" / "可以" → Research
- ❌ "不用" / "先不查" / "我知道" → Skip
- ⚠️ User provides answer directly → Use their info, skip research

**Example of user providing answer:**
```
Agent: "成本涉及 Firebase 最新价格，我可以查一下，需要吗？"
User: "我预算只有 $10/月"

→ Don't research, use $10/月 as constraint
```

### 2. State Uncertainty First

When suggesting research, **always** acknowledge uncertainty before offering solution:

✅ **Right:**
```
"我不确定 XX 是否支持..."  (state uncertainty)
"我可以查一下..."        (offer solution)
"要吗？"                  (wait for confirmation)
```

❌ **Wrong:**
```
"我去查一下 XX..."       (assumes user wants you to research)
"让我搜索一下..."        (already decided to research)
```

### 3. Use Research Results Properly

After getting research results:

**Always include:**
- Source URL
- Verification date (YYYY-MM-DD)
- Specific fact extracted (don't just link, quote key point)

**Example:**
```
查证：根据 Chrome Extension 官方文档 
(https://developer.chrome.com/docs/extensions/develop/migrate/to-service-workers)
(2026-10-12 验证)，Manifest V3 的 background service worker 最多运行 5 分钟后会被终止。
```

### 4. Handle Research Failures Gracefully

If research returns no useful results:

```
我查了一下但没找到明确信息，建议：
1. 直接查阅 [官方文档链接]
2. 或者我们基于一般限制做 conservative estimate

你想怎么处理？
```

Don't pretend you found something when you didn't.

---

## When NOT to Research

❌ **Don't suggest research when:**

### 1. User Already Provided Information

```
User: "我预算是 $50/月，能用什么云服务？"

→ Don't suggest "我可以查一下云服务价格，要吗？"
→ User already set budget constraint, work within it
```

### 2. General Knowledge (Not Time-Sensitive)

```
User: "React 是什么？"

→ Don't research, this is general knowledge
→ Answer directly from your knowledge
```

### 3. User Explicitly Said "不用查"

```
User: "大概了解就行，不用查具体的"

→ Respect user's preference for speed over precision
```

### 4. Research Won't Change Decision

```
User: "无论多少钱我都要做"

→ Cost research won't change decision, skip it
```

### 5. User Is Exploring, Not Deciding

```
User: "我随便问问，Firebase 好用吗？"

→ Casual question, provide general answer
→ Don't suggest "我可以查一下最新评测，要吗？"
```

---

## Integration with Certainty Labels

Research directly supports the three certainty labels from `references/failure-path.md`:

### `确定不可行` Requires Research

If you say `确定不可行`, you **must** have:
- Source (URL or official doc name)
- Date (YYYY-MM-DD)
- Specific reason

**Example:**
```
确定不可行：根据微信小程序官方文档 
(https://developers.weixin.qq.com/miniprogram/dev/api/)
(2026-10-12 验证)，小程序无法访问设备通讯录（隐私限制）。

替代方案：可以让用户手动输入联系人信息。
```

### `我不知道` Can Become `查证` via Research

**Before research:**
```
我不知道：需要确认 Firebase 免费配额是否满足你的需求（预计 100 用户/天）。
```

**After research (if user agrees):**
```
查证：根据 Firebase 官方定价 (URL) (2026-10-12 验证)，
免费配额支持 10GB/月 下载流量，按你的预估（100 用户/天 × 10KB/用户 = 30GB/月）
会超出免费限额，需要付费计划（约 $25/月）。
```

### `有条件可行` Needs Cost/Limit Research

When conditions involve cost or limits, research improves accuracy:

**Before research:**
```
有条件可行：如果你能接受云服务费用（未查证估算：约 $20-50/月）
```

**After research (if user agrees):**
```
有条件可行：如果你能接受以下条件：
- 每月 $25 Heroku Hobby 方案（查证：https://heroku.com/pricing, 2026-10-12 验证）
- 每周 1 小时维护时间
```

---

## Example Conversations

### Example 1: User asks directly

```
User: "能查一下 Stripe 的手续费是多少吗？"

Agent: [Researches immediately without asking]

/tavily-search Stripe payment processing fees 2026

[After getting results]

查证：根据 Stripe 官方定价 (https://stripe.com/pricing) (2026-10-12 验证)，
标准费率是 2.9% + $0.30 每笔交易（美国国内卡）。
```

---

### Example 2: Agent suggests, user accepts

```
Agent: "你提到用 Firebase，我可以查一下它的限制和定价，帮你判断合不合适，要吗？"

User: "好啊，查吧"

Agent: /tavily-search Firebase Realtime Database pricing free tier limits 2026

查证：根据 Firebase 官方定价 (https://firebase.google.com/pricing) (2026-10-12 验证)：
- 免费配额：1GB 存储 + 10GB/月 下载流量
- 超出后：$5/GB 存储, $1/GB 流量

按你预估的使用量（50 用户 × 100KB/用户/天 = 150MB/天 ≈ 4.5GB/月），
会在免费配额内。
```

---

### Example 3: Agent suggests, user declines

```
Agent: "成本涉及 AWS Lambda 的最新价格，我可以查一下，需要吗？"

User: "不用了，我预算只有 $10/月，你看够不够就行"

Agent: "好的。AWS Lambda 免费套餐通常包括 100 万次请求/月（经验估算，未查证），
       按你的使用量应该在免费范围内。
       
       如果需要确切价格，建议之后查阅 AWS 官方定价页。"
```

---

### Example 4: Agent suggests, user provides answer

```
Agent: "我不确定 Notion API 的速率限制是多少，我可以查一下，要吗？"

User: "我看过了，是每秒 3 个请求"

Agent: "好的，那按每秒 3 个请求的限制，我们来设计..."

[Uses user's info, skips research]
```

---

### Example 5: Research to support `确定不可行`

```
User: "小程序能直接读取用户的微信好友列表吗？"

Agent: "这个看起来不可行（涉及隐私），但我想查证一下官方文档确认，可以吗？"

User: "查一下吧"

Agent: /tavily-search 微信小程序 好友列表 API 权限

确定不可行：根据微信小程序官方 API 文档 
(https://developers.weixin.qq.com/miniprogram/dev/api/) (2026-10-12 验证)，
小程序无法访问用户的微信好友列表（隐私保护限制）。

可选替代方案：
- 让用户手动邀请好友（生成邀请链接）
- 通过小程序内的社交功能建立好友关系（不依赖微信好友）
```

---

## Quality Checklist

Before suggesting research, confirm:

- [ ] Uncertainty is genuine (not general knowledge)
- [ ] Research would improve decision quality (not just nice-to-have)
- [ ] Stated uncertainty first ("我不确定...")
- [ ] Offered research as optional ("我可以查...要吗？")
- [ ] Ready to handle both acceptance and decline

After completing research, confirm:

- [ ] Included source URL
- [ ] Included verification date (YYYY-MM-DD)
- [ ] Quoted specific fact (not just "according to XX, it's possible")
- [ ] Applied correct evidence quality label (查证 / 经验估算 / 未查证估算)
- [ ] If `确定不可行`, also provided alternative solution

---

## Summary

**Web research improves decision quality when used selectively.**

- User-driven: always honor user's explicit request or decline
- Agent-suggested: offer when uncertainty exists, wait for confirmation
- State uncertainty first: "我不确定..." before "我可以查..."
- Use correct citation format: source + date + specific fact
- Integrate with certainty labels: `确定不可行` requires verified source

**The goal is to ground decisions in facts, not to research everything.**
