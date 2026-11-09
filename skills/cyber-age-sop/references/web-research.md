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
  1. Available search capability for general queries (for example tavily-search)
  2. Available fetch/extraction capability for known URLs (for example tavily-extract)
  3. Host search/fetch tools when exposed and usable; verify availability rather than assuming names or regional access
  
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
  "未即時查證：基於模型知識（截至[實際已知截止日；不確定則寫『截止日未知』]），[有條件的答案]。
   可再核對：[官方文件名稱或搜尋方向]。"

Key points:
  ✅ State the actual known model cutoff, or explicitly say it is unknown; never infer it from today's date
  ✅ Offer an identifiable documentation entry only if known; label an unread link as unverified and potentially changed, otherwise give search terms instead of inventing a URL
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
   1. 查閱 [可辨識的官方文件入口（未讀取，可能已變）或搜尋方向]
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
查證：根據 [本次實際讀取的來源](URL) (YYYY-MM-DD 驗證)，[具體答案]
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

Format example only; this is not a performed search or a claim about any platform's current limits.

```
User: "這個平台能一直在後台處理嗎？"

Agent: "我不確定目標版本的生命週期限制，我可以查官方文件，要嗎？"

[User: "查吧"]
→ Use an available search/fetch capability

[Research succeeds]
查證：根據 [本次實際讀取的官方來源](URL)
(YYYY-MM-DD 驗證)，[適用版本、限制與例外]。
對你的要求而言：[能支持的結論與仍未知的部分]。

[User: "不用"]
→ 未查證：可能有生命週期限制；不能據此斷言持續處理不可能。
   保留未知，按已知限制討論有條件的替代方案。

[Research fails or tool unavailable]
→ 我無法確認最新限制；提供可辨識的官方文件入口（若已知），
   但不將未讀取的連結當成已查證證據。
   
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
