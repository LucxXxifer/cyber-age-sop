---
vault: Cyber-Age
note_type: reference_project_template
scope: cross-project-presentation
reference_project_id: CA-0001
reference_project_name: ArkBridge
reference_sop_version: "0.2"
reference_profile: ui-doc
reuse_mode: structure-only
status: active
updated: 2026-10-11
privacy: public-reference
---

# ArkBridge 參考樣板

這一頁只保存 `CA-0001 ArkBridge` 已經示範過的**呈現方法、證據語意和文件組織方式**。
它不是 ArkBridge 的技術摘要，也不是下一個項目的內容模板。跨項目使用時，必須重新讀取
目標項目的原始材料、選擇目標 Profile，再填入新的事實和證據。

## 1. 可以借用什麼

### 敘事順序

一個項目主頁可以按以下順序幫讀者建立理解：

```text
我遇到的具體場景
→ 使用者真正不方便的地方
→ 我想改變什麼
→ 我做過哪些關鍵決定
→ 方法或技術如何支持決定
→ 實際看見了什麼
→ 哪些仍然沒有被證明
```

這是一種閱讀順序，不是要求所有項目都使用相同標題或相同頁數。

### 設計者與使用者同時出現

- 用第一人稱保存設計者的原始動機、取捨和改變。
- 同時說明使用者在正常、缺資料和失敗狀態下要完成什麼。
- 技術只在能解釋使用體驗、風險或邊界時出現。
- 不把後來的 Agent 推理改寫成設計者當時的意圖。

### 決定與證據分開

每個重要決定最好都能回答：

```text
當時的場景：
使用者的問題：
人的決定：
放棄或延後的方案：
實現如何支持這個決定：
結果：
還缺什麼證據：
```

### 證據分層

同一個項目可以同時有不同證據，但不能把它們合併成一個模糊的「已完成」：

| 證據層 | 可以說什麼 | 不可以推出什麼 |
|---|---|---|
| Code / fixture | 某個版本中的行為、測試或契約 | 真實設備或使用者已接受 |
| Build / release | 構建物產生、發布檢查通過 | 已部署或在所有環境可用 |
| Field | 獲授權環境中觀察到的結果 | 其他拓撲、所有使用者或長期穩定 |
| Long-running | 在指定窗口內保持的行為 | 未觀察環境的相同結果 |

### 歷史與當前分開

項目主頁要明確區分：

- 歷史測試或部署曾經發生過什麼；
- 本輪文檔整理重新核對了什麼；
- 當前狀態是否真的重新測試；
- 仍然只是推測或待確認的內容。

## 2. 參考的閱讀層次

ArkBridge 示範了以下閱讀層次。其他項目可以採用相同邏輯，但不必複製檔名：

| 閱讀層 | 要回答的問題 | 可替換的項目 |
|---|---|---|
| 項目主頁 | 這是什麼，為什麼值得理解 | `README.md` |
| 起點與問題 | 哪個具體場景促成了項目 | `01-起點與問題.md` |
| 使用與角色 | 誰使用、在哪裡使用、怎樣知道狀態 | `02-使用與角色.md` |
| 決定與轉折 | 哪些取捨真正改變了方向 | `03-關鍵決定與轉折.md` |
| 方法與邊界 | 方法怎樣工作，不能做什麼 | `04-方法與實現.md` |
| 結果與里程碑 | 看到了什麼，走過哪些狀態 | `05-結果與里程碑.md` |
| 外部生態 | 發布、依賴、社區或使用入口 | `06-外部生態.md` |
| 證據附錄 | 原始來源、測試、矛盾和未決事項 | `90-證據附錄/` |

小項目可以只用主頁、結果頁和證據附錄；大型項目才拆成完整閱讀層。

## 3. 明確不能借用什麼

下列內容必須由目標項目重新提供，不能因為它出現在 ArkBridge 中就帶入新項目：

- 設備、品牌、硬件型號、主機名稱、拓撲或現場環境；
- 任何具體技術、命令、套件、架構、版本、release 或數字；
- ArkBridge 的日期、里程碑、測試結果、部署觀察和現場結論；
- ArkBridge 的原話、失敗經過、圖表、圖片或外部鏈接，除非只是明確標示的引用來源；
- ArkBridge 的項目規模、文件數量、成熟度或社區狀態；
- 「已部署」「已驗證」「可用」等結論，除非目標項目有自己的證據；
- `CA-0001`。目標項目必須使用自己的 Project ID；
- ArkBridge 的 `ui-doc` Profile。這只是本參考項目的 Profile，不是全局預設。

## 4. 跨項目調用方式

開始整理新項目前，先把以下欄位寫入新項目的 Anchor 或 Agent Brief：

```yaml
reference_project: CA-0001
reference_name: ArkBridge
reference_sop_version: "0.2"
reference_profile: ui-doc
reuse:
  - first-person project narrative
  - designer and user viewpoints
  - decision-to-evidence structure
  - evidence-tier wording
  - category -> project home -> evidence appendix navigation
do_not_reuse:
  - ArkBridge devices, topology, technologies, dates, versions
  - ArkBridge field conclusions or test outcomes
  - ArkBridge project identity or Project ID
target_profile:
target_project_id:
```

`target_profile` 和 `target_project_id` 必須由新項目重新決定；空白時不能直接開始
套用 ArkBridge 的頁面內容。

## 5. 參考頁驗收

套用這個樣板後，至少確認：

- 主頁先說明目標項目的場景，而不是先堆技術名稱；
- 設計者原話、Agent 建議、程式結果和現場觀察有不同標記；
- 每個重要結論都能回到目標項目的來源或驗證記錄；
- 目標項目沒有出現 ArkBridge 專屬資料；
- 目標項目使用自己的 Project ID、分類和 Profile；
- 未驗證內容明確寫成 `Not verified` 或「尚未驗證」；
- 小項目沒有被迫建立 ArkBridge 同等數量的頁面；
- 項目主頁、分類頁和證據附錄之間的鏈接可用。

## 6. 與 Cyber-Age SOP 的關係

這一頁是參考材料，不取代流程判斷：

```text
ArkBridge 參考樣板
→ 借用呈現結構和證據語意
→ 讀取目標項目材料
→ 由 cyber-age-project-sop 選擇 Profile 和交付深度
→ 由 cyber-age-sop.skill 執行錨定、交付、驗證和復盤
```

需要理解這個關係時，先看：

- [[cyber-age-project-sop类型定义|cyber-age-project-sop 類型定義]]
- [[cyber-age-project-sop完整鏈路|cyber-age-project-sop 完整鏈路]]
