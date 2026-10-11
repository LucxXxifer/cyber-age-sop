---
vault: Cyber-Age
note_type: project_sop_lifecycle
scope: cyber-age-project-sop
version: "0.1"
status: pilot
updated: 2026-10-11
privacy: public-reference
---

# cyber-age-project-sop 完整鏈路

## 一張圖

```text
真實場景／已有材料
→ 路徑判斷
→ Project Anchor
→ Task Profile
→ Research／Shape／Decision 閘門
→ Agent Brief
→ 實現／構建／部署／發布
→ 獨立驗證
→ 項目主頁與證據附錄
→ Project Review
→ SOP 反饋
```

這條鏈路不是每次都完整執行。每一個閘門都要回答「它是否會改變範圍、證據或交付
方式」；不會改變時就跳過。

## 0. 路徑判斷

| 路徑 | 何時用 | 最少產物 |
|---|---|---|
| `trivial fast path` | 單一低風險、可逆、已明確的小修復 | 對話記錄、相關檢查、diff |
| `standard` | 有清楚目標，但涉及多文件、設計或一般驗證 | Anchor、Profile、Agent Brief、驗證記錄 |
| `full` | 多個證據層、研究、UI/runtime、建置發布或現場風險 | 完整鏈路與外部報告 |

如果工作在途中擴大、觸及權限或改變行為，立即從 fast path 回到 standard 或 full。

### 規模判斷

```text
fast
→ 一個小切片、一個主要驗收

standard
→ 一個項目、幾個相關產物

large
→ 多個工作流、依賴、里程碑和整合驗證

program
→ 多個項目共享上層目標、決定、風險和發布節奏
```

大項目仍然使用同一套證據邊界，但透過 Workstream 和 Task 拆開，不把所有內容
塞進一份 Agent Brief。

## 1. Project Anchor

### 輸入

- 使用者原話和具體場景；
- 已有 Thought Brief；
- 現有項目、程式碼、文檔、圖片或研究材料；
- 隱私、權限和環境限制。

### 產出

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

### 閘門

- 目標能用一句話表達；
- 至少有一個具體使用場景；
- 本輪範圍和非目標分開；
- 已知事實沒有和推測混在一起；
- 有一個可觀察的成功或停止條件。

若項目不清楚，只問一個最可能改變範圍、證據或交付方式的問題。兩輪有限探索後仍
無法形成 Anchor，就記錄阻斷原因，不繼續無限搜索。

## 2. Task Profile

先選一個主要 Profile：

```text
code
ui-doc
field
skill-agent-workflow
docker-service
experiment-tool
```

選擇依據不是項目名稱，而是本輪要改變和要證明的事情：

- 要改變 repository 行為，選 `code`；
- 要改變人看到的狀態、文案或文檔，選 `ui-doc`；
- 要操作真實環境，選 `field`；
- 要設計可重用 Agent 流程，選 `skill-agent-workflow`；
- 要運行容器服務，選 `docker-service`；
- 要驗證假設或工具可行性，選 `experiment-tool`。

一個項目可以有多個 Task，但不要把不同 Profile 的驗收混成一個「完成」。

## 3. Research 閘門

只有在外部資料可能改變決策時才做研究，例如：

- 相容性、標準、安全或法規；
- 已有社區方案或常見失敗模式；
- 技術選型和維護風險；
- 需要外部引用或公開發布；
- 本地材料不足以判斷某個重要假設。

研究產物最少要寫：

```text
研究問題：
來源分組：
各方案或案例：
對本項目的影響：
採用什麼：
排除什麼：
仍需驗證什麼：
```

文章列表本身不是研究完成；研究必須改變、支持或排除一個決定。

## 4. Shape／Decision 閘門

當架構、UI、交付方式或範圍仍未定時，補一份最小設計材料：

- 系統邊界圖；
- 使用者流程；
- 正常、缺資料、失敗和回復狀態；
- 方案比較；
- 低保真線稿或實驗設定；
- Decision Record / Pitch。

這些圖和草圖用來發現缺口，不追求美觀。事後重建的圖要標為
`retrospective_reconstruction`，不能冒充當時已有的設計稿。

Decision Record 至少說清楚：

```text
本輪要達到什麼：
投入上限或時間盒：
採用方案：
放棄或延後什麼：
主要風險：
下一個可驗證切片：
```

## 5. Agent Brief

交給 Agent 前，先把人已經決定的內容壓縮成交付契約：

```markdown
# Agent Brief

Project ID:
Project name:
Task ID:
Task profile:
Evidence tier:

## Goal
## Context
## Human decisions
## Scope
## Non-goals
## Allowed files
## Protected files
## Input material
## Constraints and permission boundary
## Evidence boundary
## Required behavior
## Failure behavior
## Validation commands
## Acceptance criteria
## Report path outside repository
## Follow-up discoveries
```

風險較高或範圍不清楚時，必須列出文件白名單和明確禁止修改的文件。
Agent 不能自行改變目標、接觸未授權設備或秘密，也不能把 Follow-up 變成實施範圍。

## 6. 執行時分開四件事

不要把以下事情寫成同一個「已完成」：

```text
實現：改變程式、文檔或配置
測試：在本地或 CI 檢查行為
構建／發布：產生可分發的版本
部署／現場：在獲授權環境實際操作和觀察
```

對 field 或 infrastructure 任務，執行前必須有：

- exact target and environment；
- authorized scope and authorization source；
- intended change；
- backup or configuration capture；
- rollback method；
- out-of-band recovery path；
- timeout and stop condition；
- pass/fail observations。

任何一項缺失都停在規劃，不執行現場命令。

## 7. 獨立驗證

執行者報告之外，由主執行器重新檢查：

1. 實際 diff 和 changed-file list；
2. repository 沒有報告、日志、cache 或生成物；
3. 最窄的檢查，再按需要執行完整檢查；
4. code、build/release、field、long-running 證據分層；
5. UI／文檔的狀態、人話和不可推論內容一致；
6. runtime、互動或 responsive claim 有 browser 證據，否則標為 `Not verified`；
7. 報告位於 repository 外，且具備固定欄位。

正常或 full 任務的報告欄位：

```markdown
## Changed
## Verified
## Not verified
## Remaining risk
## Follow-up discoveries
## SOP feedback
```

## 8. 項目主頁和證據附錄

### 項目主頁

項目主頁是給人閱讀的，不是完整日志。按目標 Profile 裁剪，但通常回答：

1. 我為什麼開始；
2. 誰在什麼場景使用；
3. 我做過哪些關鍵決定；
4. 方法或技術解決了什麼；
5. 目前有什麼結果；
6. 哪些限制和未驗證事項仍然存在。

### 證據附錄

證據附錄保存：

- 原始 thread、source map 和引用；
- 設計決定和變更記錄；
- 測試、構建、部署和長時間觀察；
- GitHub 或其他外部資料的快照日期；
- 矛盾、未決事項和隱私檢查；
- 本輪報告與復盤。

主頁可以簡化閱讀，但不能刪除能改變結論的證據邊界。

## 9. Project Review

階段結束後記錄：

```text
發現：
造成的代價：
下一次提前問什麼：
下一次增加哪項驗收：
哪些設計材料真正有用：
哪個 Profile 或 Brief 欄位需要調整：
是否更新 cyber-age-project-sop：
```

只有重複失敗或有意義的 A/B 實驗，才把一次發現提升為永久 SOP 規則。

## 10. 跨項目調用順序

建立新項目時按以下順序調用：

1. 讀 [[reference-project-template|參考項目樣板]]，只借用結構和證據語意。
2. 讀 [[cyber-age-project-sop类型定义|類型定義]]，判斷項目和本輪 Task Profile。
3. 讀本頁，按風險選 fast、standard 或 full 路徑。
4. 讀目標項目的原始材料，重新建立 Anchor。
5. 只在會改變決策時做 Research 或 Shape。
6. 產出 Agent Brief，交給 Agent 實施。
7. 按 Profile 驗證，分開寫 `Verified` 和 `Not verified`。
8. 將主頁、證據附錄和 Project Review 落回 Cyber-Age。

## 11. 最終停車點

項目可以在以下任一狀態停下，並不需要假裝完成：

- `anchored`：目標和範圍已清楚，但尚未實施；
- `designed`：方案和交付方式已確認；
- `implemented`：已有程式或文檔變更；
- `built`：已有可分發構建物；
- `field-observed`：在指定環境有現場觀察；
- `released`：已有對外或內部發布；
- `blocked`：阻斷資訊、授權或恢復條件缺失；
- `archived`：停止投入，但保留原因和證據。

狀態表示目前證據，不表示項目永久有效或所有環境都已驗收。
