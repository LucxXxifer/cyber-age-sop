# Decision Research and Approach Exploration

Development candidate / 開發候選：`0.5.4-dev.1`, 2026-11-10. Its tested behavior is retained in [v0.5.4-beta.1](../releases/v0.5.4-beta.1.md); promotion changes release identity and documentation only. The observations below refer to the frozen development candidate, not a new beta test run.

此處保存開發候選的實際驗證範圍；發布沒有追加行為變更，也不把舊版模型審計視為新版審計。

## What Changes / 本輪變更

- Research starts with the project decision and consequential unknowns. Match sources to the claim, check relevant contrary evidence for important recommendations, preserve source conflicts, and explain the effect on scope, options or acceptance.
- Reuse applicable public-research permission. Stop at a supported decision or the stated limit; keep critical unknowns conditional and propose a bounded next check.
- When purpose is understood but the approach is open, explore meaningfully different workflows or structures, compare consequences, and show a provisional shape when useful. Settled work and clear small edits skip this step.
- Existing owner confirmation, prompt-only handling, rejected suggestions and execution boundaries remain. Details load on demand; no extra search engine, model route or runtime dependency is required.

補強重點是讓查證能影響項目選擇，以及讓使用者看懂不同做法的差別。沒有固定點子數、強制多代理、全面紅隊或新增背景監督；重要資訊仍顯示在對話，已確認的工作不重啟訪談。

## Acceptance / 驗收方向

Check realistic responses for evidence-driven recommendation changes, useful alternatives, preservation of rejected ideas and lack of unnecessary ceremony on small tasks. Preserve original outputs. A synthetic evidence packet tests how evidence is interpreted; it does not measure internet coverage, live search ranking or source availability.

## Limited Validation / 有限驗證

On 2026-11-10, two fresh-context agents used the same frozen candidate for two simulated cases, each with two turns. Source excerpts and project details were fictional and local; there was no live web search. The reviewer inspected the original replies and the resulting label file.

| Check | Observation |
| --- | --- |
| Research from supplied evidence | Distinguished a documented capability from one narrow benchmark and identified a second report as a republication, not independent testing |
| New contrary evidence | Withdrew the earlier recommendation after a version limit and unsupported older version were revealed; preserved the owner's local-only goal and left the replacement conditional |
| Unsettled interaction design | Presented different entry flows and their burdens as provisional; retained the existing file picker and did not invent a filter capability |
| Adopted direction followed by a tiny fix | Applied only the requested label correction, preserved the other lines and did not restart discovery or build the deferred GUI |

The public-package and implementation-readiness checks and Skill frontmatter validator passed. Relative references resolve. The entrypoint decreased from 527 to 508 lines. Existing files retain baseline Markdown lint findings; excluding the repository's long-line style, no lint rule count increased and new files passed. This is not a claim of a clean full-repository lint run.

這是兩個模擬案例、四輪原文的有限檢查，沒有現版／候選對照，不能據此聲稱品質提升幅度。真人理解、學習轉移、即時搜尋品質、跨模型穩定性、自然觸發與大型項目效益仍未驗證。

## Method References / 方法參考

The wording in this candidate is purpose-specific. Useful comparisons include [Superpowers approach comparison](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md), [BMAD decision research](https://github.com/bmad-code-org/BMAD-METHOD/blob/a867e1604b365d48ea03cbd109da1066ba0c84bc/skills/bmad-deep-recon/SKILL.md), [GSD technical research](https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/agents/gsd-phase-researcher.md), and [Design Council's Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/history-of-the-double-diamond). These are method references, not dependencies or evidence of this candidate's effectiveness.
