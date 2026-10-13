# Web Research Protocol

## Purpose

Verify technical feasibility, cost estimates, and constraints through web research when it improves decision quality.

---

## Core Principle

**Web research is optional and user-controlled.**

- User asks directly → research immediately
- Agent identifies uncertainty → suggest and wait for confirmation
- User declines → use model knowledge, continue without research

---

## When to Suggest Research

### Trigger Conditions

Suggest research when you encounter:

1. **Uncertain feasibility** — "我不確定 XX 是否支持..."
2. **Cost estimation** — third-party service pricing unknown
3. **Specific tool verification** — user mentions a tool/API you need to verify
4. **Evidence for `確定不可行`** — need verified source + date

### Suggestion Template

```
我不確定 [具體問題]，我可以查一下 [來源]，要嗎？
```

**Wait for user response:**
- ✅ "查吧" / "好" / "要" → research immediately
- ❌ "不用" / "先不查" → skip, use model knowledge
- User provides answer → use their info, skip research

---

## Fallback Strategy

### Step 1: Try Available Tools (if user approves)

```yaml
Priority order:
  1. tavily-search skill (best for general queries)
  2. tavily-extract skill (for specific URLs)
  3. WebSearch tool (Claude Code, US-only)
  4. WebFetch tool (for known URLs)
  
Check availability:
  - Look for installed skills: /tavily-search
  - Try WebSearch if available
  - If user provided URL, try WebFetch
```

### Step 2: Use Model Knowledge (if tools unavailable or user declines)

```yaml
When to use:
  - No research tools available
  - User declined research
  - Research returned no useful results

Format:
  "基於模型知識（截至 2026-06），[答案]。
   建議查閱最新資訊: [URL]"

Key points:
  ✅ State knowledge cutoff date
  ✅ Provide likely documentation URL (model knows common doc sites)
  ✅ Suggest user verify if precision matters
  ❌ Don't maintain static URL lists in this skill
  ❌ Don't maintain experience answer database
```

### Step 3: Graceful Failure (if truly uncertain)

```yaml
When nothing works:
  - State limitation clearly
  - Provide research directions
  - Offer to continue with assumptions

Format:
  "我無法確認 [問題]，建議：
   1. 查閱 [官方文檔 URL]
   2. 或基於一般限制做保守估計
   
   你想怎麼處理？"
```

---

## Citation Format

### Three Evidence Quality Levels

#### 1. 查證 (Verified)
**When:** Researched and found source

```
查證：根據 [來源名稱](URL) (YYYY-MM-DD 驗證)，[具體事實]。
```

#### 2. 經驗估算 (Experience-based)
**When:** Based on model knowledge, not fact-checked

```
經驗估算：基於類似專案經驗，[估算] (未查證)。
```

#### 3. 未查證估算 (Unverified)
**When:** Educated guess with uncertainty

```
未查證估算：可能..., 需要進一步確認。
```

---

## Integration with Certainty Labels

From `references/failure-path.md`:

### `確定不可行` Requires Verification

Must include:
- Source (URL or official doc)
- Date (YYYY-MM-DD)
- Specific reason

```
確定不可行：根據 [官方文檔](URL) (2026-10-12 驗證)，
[具體限制]。

替代方案：[建議]
```

### `我不知道` Can Become `查證`

**Before research:**
```
我不知道：需要確認 [問題]
```

**After research (if user agrees):**
```
查證：根據 [來源](URL) (2026-10-12 驗證)，[具體答案]
```

---

## When NOT to Research

❌ Don't suggest research when:

1. **User already provided information** — use their constraint
2. **General knowledge** — not time-sensitive, answer from model knowledge
3. **User said "不用查"** — respect preference for speed
4. **Won't change decision** — research is irrelevant
5. **User is exploring casually** — not in decision phase

---

## Example: Complete Flow

```
User: "Chrome 插件能在後台一直運行嗎？"

Agent: "我不確定 Chrome Extension Manifest V3 是否支持持續後台運行，
        我可以查一下官方文檔，要嗎？"

[User: "查吧"]
→ Use tavily-search or WebSearch

[Research succeeds]
查證：根據 Chrome Extension 官方文檔 
(https://developer.chrome.com/docs/extensions/develop/migrate/to-service-workers)
(2026-10-13 驗證)，Manifest V3 的 service worker 最多運行 5 分鐘後會被終止。

[User: "不用"]
→ 基於模型知識（截至 2026-06），Chrome Extension Manifest V3 將 background 
   scripts 改為 service workers，通常有運行時間限制。
   建議查閱官方文檔確認: https://developer.chrome.com/docs/extensions/mv3/

[Research fails or tool unavailable]
→ 我無法確認最新的限制，建議查閱 Chrome Extension 官方文檔
   (https://developer.chrome.com/docs/extensions/mv3/)。
   
   或者我可以基於一般限制給個保守估計，你想怎麼處理？
```

---

## Quality Checklist

**Before suggesting research:**
- [ ] Uncertainty is genuine (not general knowledge)
- [ ] Research would improve decision quality
- [ ] Stated uncertainty first ("我不確定...")
- [ ] Offered as optional ("我可以查...要嗎？")

**After research:**
- [ ] Included source URL
- [ ] Included verification date (YYYY-MM-DD)
- [ ] Quoted specific fact
- [ ] Applied correct evidence label (查證/經驗估算/未查證估算)

---

## Summary

**Web research improves decision quality when used selectively.**

- **User-controlled**: honor explicit request or decline
- **Tool detection**: try available tools, fallback to model knowledge
- **Model knowledge**: valid fallback with clear timestamp
- **No static database**: don't maintain URL lists or experience answers
- **Graceful degradation**: always provide useful output, even without research
