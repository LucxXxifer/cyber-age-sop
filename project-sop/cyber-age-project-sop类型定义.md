---
vault: Cyber-Age
note_type: project_sop_type_definition
scope: cyber-age-project-sop
runtime_skill: cyber-age-sop
version: "0.1"
status: pilot
updated: 2026-10-11
privacy: public-reference
---

# cyber-age-project-sop 類型定義

## 1. 它是什麼

`cyber-age-project-sop` 是 Cyber-Age 中可長期保存的**項目類型與交付契約**。
它把一個項目從「我想做什麼」整理到「怎樣交接、怎樣驗證、怎樣留下可讀記錄」。

它建立在已安裝的 `cyber-age-sop` skill 之上，但不是第二個 runtime skill：

| 層次 | 職責 |
|---|---|
| `cyber-age-sop.skill` | 在對話或執行期間做錨定、分型、交付、驗證和復盤 |
| `cyber-age-project-sop` | 在 Obsidian 保存項目類型、Profile、產物和跨項目調用規則 |
| 專用引導工具 | 只在本人明確要求引導、深挖或分層提問時使用 |
| 項目主頁 | 以讀者能理解的方式保存項目背景、決定、結果和限制 |
| 證據附錄 | 保存原始來源、測試、部署、發布和矛盾記錄 |

因此，這一頁定義「項目要怎樣被管理和保存」，不替使用者下產品方向，也不把
引導工具模擬成項目問卷。

## 2. 何時使用

適用於：

- 個人 software、hardware、UI、documentation、Skill、Docker 或 automation 項目；
- 需要從模糊想法收斂到明確任務的工作；
- 需要把人做的決定交給 Agent 實施的工作；
- 需要區分 code、build/release、field 和 long-running 證據的工作；
- 需要在 Obsidian 形成可重用項目主頁和證據鏈的工作。

不適用於：

- 單純的情緒支持、關係引導或自我反思；
- 沒有項目交付物的自由對話；
- 已明確且只涉及一個低風險錯字的 trivial fast path；
- 沒有授權卻要求操作真實設備、外部帳戶或生產環境的工作。

## 3. 三種入口

| 入口 | 先做什麼 | 主要輸入 |
|---|---|---|
| 新想法 | 建立 Project Anchor，逐步補齊範圍和證據邊界 | 使用者原話、現場描述 |
| 已有 Thought Brief | 直接把它當權威輸入，檢查是否缺阻斷資訊 | Thought Brief、設計材料 |
| 已有項目或小修復 | 判斷是否走 fast path，或直接選 Profile | 現有檔案、變更要求 |

不要因為項目存在就強迫它走完整鏈路；路徑由風險、範圍、證據和交付方式決定。

## 4. Task Profile

一個項目可以有多個 Task，但每個 Task 先選一個主要 Profile：

| Profile | 先固定什麼 | 主要驗收 | 適合的主頁重點 |
|---|---|---|---|
| `code` | 行為、允許文件、測試和 diff | targeted/full tests、lint、build、diff | 問題、決定、實現、限制 |
| `ui-doc` | 狀態、人話、不可推論內容和文件一致性 | 靜態檢查、文字契約、browser/runtime | 使用流程、狀態、決定、閱讀體驗 |
| `field` | 目標、授權、備份、rollback、恢復和停止條件 | 現場觀察、回復能力、長時間窗口 | 環境、操作、結果、限制 |
| `skill-agent-workflow` | 觸發條件、輸入、輸出、邊界和案例 | prompt/skill 測試、輸出契約、失敗案例 | 解決什麼問題、怎樣調用、不能做什麼 |
| `docker-service` | 服務拓撲、持久化、備份、恢復和部署 | image/build、啟動、持久化、恢復演練 | 服務用途、運行方式、運維邊界 |
| `experiment-tool` | 假設、設定、觀察、對照和限制 | 可重現實驗、觀察記錄、反例 | 為什麼試、怎樣試、看到了什麼 |

Profile 是任務的證據契約，不是項目的永久標籤。項目可以在不同階段拆成不同
Task，例如先做 `code`，再做 `field`，最後做 `ui-doc`。

## 5. 項目記錄的最小結構

不是每個項目都要建立完整套件。標準項目可按需要使用：

```text
<分類>/<項目>/
├── README.md
├── 01-起點與問題.md
├── 02-使用與角色.md
├── 03-關鍵決定與轉折.md
├── 04-方法與實現.md
├── 05-結果與里程碑.md
├── 06-外部生態.md
└── 90-證據附錄/
```

路徑只是建議，頁面數量按項目規模裁剪：

- `fast`：主頁加一份結果記錄；
- `standard`：主頁、決定或實現頁、證據附錄；
- `full`：完整閱讀層、Profile 產物、研究／設計／驗證／復盤記錄。

## 6. 共同元資料

項目主頁和重要子頁可以使用以下欄位：

```yaml
project_id: <target-project-id>
project_sop_type: cyber-age-project-sop
project_name:
category:
stage:
status:
task_profile:
evidence_tier:
privacy: project-defined
last_reviewed_at:
```

`<target-project-id>` 只是欄位位置；新項目必須從項目登記表取得自己的 ID。
`task_profile` 和 `evidence_tier` 描述目前這份記錄，不代表整個項目已經完成。

## 7. 交付物契約

正常項目至少要能留下：

1. **Project Anchor**：人的目標、使用者、問題、事實、假設、範圍和證據邊界。
2. **Profile decision**：為什麼選這個 Profile，哪些 Profile 暫不適用。
3. **Shape／Decision**：只有在架構、UI、研究或交付方式未定時才需要。
4. **Agent Brief**：目標、允許文件、非目標、失敗行為、驗證和報告路徑。
5. **Verification record**：實際改了什麼、驗證了什麼、沒有驗證什麼。
6. **Project home**：給人閱讀的動機、使用、決定、結果和限制。
7. **Project Review**：返工原因、下一次要提前問什麼，以及是否更新 SOP。

Trivial fast path 可以只在對話中留下變更、檢查和剩餘不確定性，不生成整套產物。

## 8. 不可跨越的邊界

- 沒有來源的推斷不能寫成使用者決定。
- 本地測試不能寫成現場成功。
- Build/release 成功不能寫成部署成功。
- 歷史觀察不能自動寫成當前狀態。
- UI 沒有 browser/runtime 證據時，必須標記 `Not verified`。
- Field 操作缺少目標、授權、備份、rollback、恢復路徑、timeout 或停止條件時，
  只能停在規劃。
- Follow-up discovery 不能自動擴大本輪範圍。

## 9. 與參考項目樣板的關係

使用參考項目樣板時只借用結構和語意：

```text
參考項目樣板
→ 目標項目重新做 Anchor
→ 選擇自己的 Task Profile
→ 產出自己的決定、實現和證據
→ 依目標項目的規模裁剪頁面
```

詳細的禁止複製清單在 [[reference-project-template|參考項目樣板]]；
整個執行順序在 [[cyber-age-project-sop完整鏈路|cyber-age-project-sop 完整鏈路]]。
