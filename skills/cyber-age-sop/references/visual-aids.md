# Visual Aids for Non-Technical Users

## Purpose

Help non-technical users **see** their product structure through simple ASCII diagrams when verbal description becomes ambiguous or complex.

## Core Principle

**Visual aids are optional tools, not mandatory steps.**

- User asks directly → generate immediately
- Agent identifies complexity → **suggest** and wait for confirmation
- User declines or ignores → continue without diagrams

## When User Asks Directly (No Confirmation Needed)

If user says any of these, generate visual aid immediately:

- "能画个图吗？"
- "帮我画个流程图"
- "我想看看架构是什么样的"
- "能用图示说明一下吗？"
- "画出来我可能更容易理解"

→ **Generate diagram immediately, no need to ask for confirmation**

---

## When Agent Should Suggest (Requires Confirmation)

### 1. Complex Flow (复杂流程)

**Identify when:**
- User describes 3+ sequential steps
- User mentions branching logic ("如果...那么...")
- User describes different paths for different scenarios
- User mentions error handling or fallback paths

**Suggestion template:**
```
听起来流程有几个分支，我可以画个简单流程图帮你看清楚，要吗？
```

**Example scenario:**
```
User: "用户先登录，如果密码对就进主页，密码错就显示错误，
       然后如果错3次就锁定账号，需要管理员解锁"

Agent: "听起来流程有几个分支，我可以画个简单流程图帮你看清楚，要吗？"

[Wait for user response]

If user says "好" / "要" / "画吧":
→ Generate flow diagram

If user says "不用" / "先不要" / "我理解了":
→ Continue without diagram
```

---

### 2. Multi-Role Interaction (多角色交互)

**Identify when:**
- User mentions different user types ("管理员"、"普通用户"、"访客")
- User describes different permissions or capabilities for different people
- User says "不同人看到不同东西" or "有权限控制"

**Suggestion template:**
```
涉及不同角色的权限，我可以画个图说明谁能做什么，需要吗？
```

**Example scenario:**
```
User: "管理员可以看所有人的数据，普通用户只能看自己的，
       访客只能看公开的部分"

Agent: "涉及不同角色的权限，我可以画个图说明谁能做什么，需要吗？"

[Wait for user response]
```

---

### 3. Multi-Module System (多模块系统)

**Identify when:**
- User mentions "前端"、"后端"、"数据库"
- User says "分几个部分" or "系统有几块"
- User describes data flow between components
- User mentions API, server, client, or service boundaries

**Suggestion template:**
```
系统有几个模块，我可以画个架构图展示它们的关系，要不要？
```

**Example scenario:**
```
User: "前端是个手机App，后端是API服务器，数据存在云数据库里，
       还要对接微信支付"

Agent: "系统有几个模块，我可以画个架构图展示它们的关系，要不要？"

[Wait for user response]
```

---

### 4. Interface Layout (界面布局)

**Identify when:**
- User describes page structure ("页面分成几块")
- User mentions spatial relationships ("左边...右边..." / "上面...下面...")
- User describes navigation or tab structure
- User says "有个菜单" or "分几个区域"

**Suggestion template:**
```
可以用简单布局图展示页面结构，需要吗？
```

**Example scenario:**
```
User: "页面顶部是导航栏，左边是菜单，右边是主要内容区，
       底部是版权信息"

Agent: "可以用简单布局图展示页面结构，需要吗？"

[Wait for user response]
```

---

## Three Types of ASCII Diagrams

### Type 1: Flow Diagram (流程图)

**Use for:** Sequential steps, branching logic, decision points

**Template:**
```
[开始] → [步骤1] → [判断] → [步骤2] → [结束]
                      ↓
                   [错误处理]
```

**Example 1: Simple linear flow**
```
用户登录流程：

[用户输入账号密码] → [验证身份] → [显示主页]
                          ↓ (验证失败)
                      [显示错误提示]
```

**Example 2: Branching flow**
```
订单处理流程：

[用户下单] → [检查库存] → [库存充足] → [生成订单] → [通知发货]
                  ↓
              [库存不足] → [通知用户] → [推荐替代品]
```

**Example 3: Multiple error paths**
```
支付流程：

[用户选择商品] → [进入支付页面] → [调用支付API]
                                      ↓
                 成功 ←────────── [支付结果] ──────────→ 失败
                  ↓                                      ↓
            [显示成功页面]                          [显示失败原因]
                  ↓                                      ↓
            [发送确认邮件]                          [允许重试]
```

**Symbols:**
- `[ ]`: 步骤或状态
- `→`: 流程方向
- `↓`: 向下流转
- `(条件)`: 判断条件说明

---

### Type 2: Architecture Diagram (架构图)

**Use for:** System components, data flow, module relationships

**Template:**
```
┌─────────┐    ┌─────────┐
│ 模块A   │───→│ 模块B   │
└─────────┘    └────┬────┘
                    ↓
               ┌─────────┐
               │ 模块C   │
               └─────────┘
```

**Example 1: Simple 3-tier architecture**
```
系统架构：

┌─────────────┐
│  手机App    │ (用户界面)
└──────┬──────┘
       │ HTTPS
       ↓
┌─────────────┐
│  后端API    │ (业务逻辑)
└──────┬──────┘
       │ SQL
       ↓
┌─────────────┐
│  数据库     │ (数据存储)
└─────────────┘
```

**Example 2: Multi-component system**
```
团队协作系统架构：

┌──────────┐          ┌──────────┐
│ Web前端  │─────────→│ API服务器│
└──────────┘          └─────┬────┘
                            │
┌──────────┐                ├─────→ ┌──────────┐
│ 手机App  │───────────────→│       │ 数据库   │
└──────────┘                │       └──────────┘
                            │
                            └─────→ ┌──────────┐
                                    │ 文件存储 │
                                    └──────────┘
```

**Example 3: External service integration**
```
支付系统集成：

┌─────────┐    ┌─────────┐    ┌──────────┐
│ 用户App │───→│ 你的后端│───→│ 微信支付 │
└─────────┘    └─────────┘    └──────────┘
                    │
                    ↓
              ┌─────────┐
              │ 订单数据库│
              └─────────┘
```

**Symbols:**
- `┌─┐ └─┘`: 模块边框 (box drawing)
- `→`: 数据流向或调用方向
- `↓`: 向下依赖
- `(说明)`: 模块功能说明

---

### Type 3: Interface Layout (界面布局)

**Use for:** Page structure, navigation layout, screen zones

**Template:**
```
┌────────────────────┐
│   区域1            │
├────────────────────┤
│ 区域2 │ 区域3      │
└────────────────────┘
```

**Example 1: Standard dashboard layout**
```
主页面布局：

┌─────────────────────────────┐
│   顶部导航栏 (Logo + 菜单)   │
├────────┬────────────────────┤
│ 左侧   │                    │
│ 菜单   │   主要内容区        │
│        │                    │
│ - 首页 │   (显示数据/表单)   │
│ - 设置 │                    │
│ - 帮助 │                    │
└────────┴────────────────────┘
```

**Example 2: Mobile app screen**
```
手机App界面：

┌───────────────┐
│ 顶部标题栏    │
├───────────────┤
│               │
│   搜索框      │
│               │
├───────────────┤
│               │
│   列表项1     │
│   列表项2     │
│   列表项3     │
│   ...         │
│               │
├───────────────┤
│ 底部导航栏    │
│ [首页][我的]  │
└───────────────┘
```

**Example 3: Form layout**
```
用户注册表单：

┌─────────────────────┐
│ 注册新账号          │
├─────────────────────┤
│                     │
│ 用户名: [_______]   │
│                     │
│ 密码:   [_______]   │
│                     │
│ 确认:   [_______]   │
│                     │
│ 邮箱:   [_______]   │
│                     │
│     [  注册  ]      │
│                     │
└─────────────────────┘
```

**Symbols:**
- `┌─┐ ├─┤ └─┘`: 区域边框
- `│`: 垂直分隔
- `[___]`: 输入框
- `[按钮]`: 可点击按钮

---

## When NOT to Use Diagrams

❌ **Don't suggest diagrams when:**

1. **User already understands clearly**
   ```
   User: "就是一个简单的登录页面，输入账号密码然后点登录"
   
   → No need for diagram, description is already clear
   ```

2. **Single linear path with no branches**
   ```
   User: "用户点击按钮，然后显示成功消息"
   
   → Too simple for a diagram
   ```

3. **User explicitly declines**
   ```
   Agent: "我可以画个流程图，要吗？"
   User: "不用，我自己理解了"
   
   → Don't insist, continue without diagram
   ```

4. **User changes topic instead of responding**
   ```
   Agent: "我可以画个架构图，需要吗？"
   User: "对了，这个系统要支持多少人同时用？"
   
   → User ignored suggestion, treat as "不用"
   ```

5. **Diagramming would slow down a clear conversation**
   ```
   User: "我想快速确认一下技术方案，别画图了，直接说"
   
   → Respect user's preference for speed
   ```

---

## Important Rules

### 1. Wait for Confirmation

When you suggest a diagram, **always wait** for user to say:
- ✅ "好" / "要" / "画吧" / "可以" → Generate
- ❌ "不用" / "先不要" / "我理解了" → Skip
- ⚠️ No response / changes topic → Treat as "不用"

**Never generate a diagram without user confirmation when you suggested it.**

### 2. Keep It Simple

- Use only ASCII characters (no Unicode art beyond box-drawing)
- Keep diagrams under 20 lines when possible
- Label clearly in Chinese (or user's language)
- One diagram per concept (don't combine flow + architecture)

### 3. Explain After Showing

After generating a diagram, add 1-2 sentences explanation:

```
这个流程图展示了用户从登录到进入主页的三种可能路径：
成功、密码错误、以及账号被锁定的情况。
```

### 4. Don't Over-Design

Visual aids are for **understanding**, not **documentation**.

❌ Wrong (too detailed):
```
完整的系统架构（包含所有模块、所有API端点、所有数据表...）
[50 lines of complex diagram]
```

✅ Right (focused on key relationships):
```
系统的三个主要部分：

┌─────────┐    ┌─────────┐    ┌─────────┐
│ 前端    │───→│ 后端API │───→│ 数据库  │
└─────────┘    └─────────┘    └─────────┘
```

---

## Example Conversations

### Example 1: User asks directly

```
User: "能画个图吗？我想看看这个流程是什么样的"

Agent: [Generates flow diagram immediately]

用户注册流程：

[填写表单] → [提交] → [验证邮箱格式] → [创建账号] → [发送确认邮件]
                          ↓ (格式错误)
                      [显示错误提示]

这个流程展示了用户注册的主要步骤和邮箱格式验证失败时的处理。
```

### Example 2: Agent suggests, user accepts

```
Agent: "听起来流程有几个分支，我可以画个简单流程图帮你看清楚，要吗？"

User: "好啊，画吧"

Agent: [Generates flow diagram]

订单处理流程：

[用户下单] → [检查库存] → [充足] → [生成订单] → [通知发货]
                  ↓
              [不足] → [通知用户] → [推荐替代品]

这个图展示了库存充足和不足两种情况的不同处理路径。
```

### Example 3: Agent suggests, user declines

```
Agent: "系统有几个模块，我可以画个架构图展示它们的关系，要不要？"

User: "不用了，我自己清楚"

Agent: "好的。那我们继续讨论技术选型..."

[Continues without diagram]
```

### Example 4: Agent suggests, user ignores

```
Agent: "可以用简单布局图展示页面结构，需要吗？"

User: "对了，这个页面要支持手机访问吗？"

Agent: [User changed topic, treat as declined]

"需要。我们来确认一下响应式设计的要求..."

[Continues without diagram]
```

---

## Box-Drawing Characters Reference

For consistent diagram appearance, use these Unicode box-drawing characters:

```
┌───┬───┐    ┏━━━┳━━━┓
│   │   │    ┃   ┃   ┃
├───┼───┤    ┣━━━╋━━━┫
│   │   │    ┃   ┃   ┃
└───┴───┘    ┗━━━┻━━━┛

→  ←  ↑  ↓  (arrows)
```

**Recommended set (most compatible):**
- Corners: `┌ ┐ └ ┘`
- Lines: `─ │ ├ ┤ ┬ ┴ ┼`
- Arrows: `→ ↓ ←`

---

## Quality Checklist

Before generating a visual aid, confirm:

- [ ] User asked for it OR Agent suggested and user confirmed
- [ ] Diagram adds clarity (not just repeating what was already clear)
- [ ] Kept simple (under 20 lines, focused on key relationships)
- [ ] Labels in user's language (Chinese by default)
- [ ] Includes 1-2 sentence explanation after diagram
- [ ] Symbols are consistent (don't mix arrow styles)

If any checkbox fails → reconsider whether diagram is needed.

---

## Summary

**Visual aids are powerful but optional.**

- User-driven: always honor user's explicit request or decline
- Agent-suggested: offer when complexity justifies, wait for confirmation
- Keep simple: clarity over completeness
- Explain briefly: diagram + 1-2 sentences

**The goal is to help users SEE their product, not to create documentation.**
