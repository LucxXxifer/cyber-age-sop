# Cyber-Age SOP

[English](README.md) · [繁體中文](README.zh-TW.md)

Cyber-Age SOP 是一套用來深度挖掘設計者／項目負責人需求、釐清假設和邊界，
再輔佐 Agent 交付的流程框架。它可以處理 software、hardware、UI、
documentation、Skill、Docker、automation、藝術、AI 媒體或遊戲想法。

**公開測試版：[v0.5.3-beta.1](https://github.com/LucxXxifer/cyber-age-sop/releases/tag/v0.5.3-beta.1)（2026-11-09）。**
本 Skill 指示 Agent 在明確要求增強項目提示詞時，展示原話、可修改的改稿與重要理由，支援局部採用或返回原文，並將只改提示詞與執行任務分開。
重要提問會簡述答案影響什麼，呈現依用途選草圖、表格或 SVG／HTML，重點仍在對話，視圖沿用同一 Brief／SPEC 修訂。
使用者實質確認共同理解後才有第一張行動卡。實際表現仍取決於宿主有否載入及模型遵循程度。詳見[變更、驗證與限制](docs/releases/v0.5.3-beta.1.md)。

上一測試版 [v0.5.2-beta.1](https://github.com/LucxXxifer/cyber-age-sop/releases/tag/v0.5.2-beta.1) 仍可下載。
跨模型穩定性、小白可用性與大型專案效益尚未驗證；本版不提供原生增強按鈕、保證模型切換、自動觸發或背景監督。

**穩定版仍為 [v0.4.5](https://github.com/LucxXxifer/cyber-age-sop/releases/tag/v0.4.5)。** 測試版不取代穩定版。

## 試用測試版

1. 在測試版 Release 下載 **`cyber-age-sop-v0.5.3-beta.1.zip`**，不要混用 GitHub 整庫源碼 ZIP。安裝包內只有一個 `cyber-age-sop/` 目錄，包含 `SKILL.md`、references 和授權聲明。
2. 按所用 Agent／IDE 的 Skill 安裝方式放入該目錄。本機 Codex 可放在 `~/.codex/skills/cyber-age-sop/`。升級前備份舊版，以整個目錄替換，避免版本混雜；安裝後開啟新 session。
3. 在 Codex 呼叫 `$cyber-age-sop`，或按宿主的 Skill 機制明確載入，描述一個真的想做的小工具、程式、插件或 Skill。不必先懂技術棧；執行、搜尋和繪圖能力由所用 Agent／IDE、工具與模型提供。
4. 記下有幫助或看不懂的位置，使用[雙語回饋指南](docs/beta-feedback.md)或 [GitHub 回饋表](https://github.com/LucxXxifer/cyber-age-sop/issues/new?template=beta-feedback.md)。

例如：「用 cyber-age-sop 幫我做一個本機 Markdown 連結檢查工具。我不懂技術需求怎麼寫，請先釐清第一版範圍，確認大致結構，再在同意範圍內實作和測試。」

只改文字可說：「幫我增強這段項目提示詞，先不要執行。保留原話，展示重要差異與理由，未知保持未知。」可以只採用一處或用回原文；之後要開始項目再說明，仍按已確認範圍與實際權限執行。

先選本機、可恢復的工作。安裝測試版不代表授權存取真實帳號或正式服務；如需退回穩定版，以穩定版的整個 Skill 目錄替換即可。

它不是項目管理平台，也不是任何領域的解決方案；不會取代 software engine、
生成工具、遊戲引擎、媒體工具或專業審核。

這個 repository 是個人開源項目，不是 OpenAI、Codex 或 GitHub 的官方項目。

## 兩個層次

- `skills/cyber-age-sop/`：給 Agent runtime 使用的 Skill，負責項目錨定、任務
  Profile、交付、驗證和復盤。
- `project-sop/`：可長期保存的項目類型、呈現方式和完整鏈路文件，可放入任何知識庫。

## 它解決什麼問題

這套框架先幫設計者把意圖、假設和邊界說清楚，並針對幾種常見問題：

- 小修改被擴展成沒有邊界的大重寫；
- 模糊想法被轉成冗長問卷；
- 本地測試被誤寫成現場驗收；
- 構建成功被誤寫成部署成功；
- 沒有 runtime 證據就宣稱 UI 或文檔「已驗證」；
- 額外發現悄悄變成本輪實施範圍；
- 引導、反思和項目執行混在一起。

核心鏈路如下：

```text
真實場景或已有材料
→ Project Anchor
→ Task Profile
→ 必要時加入 Research／Shape／Decision
→ Agent Brief
→ 實現／構建／部署／發布
→ 指定查核（低風險自測須標明；需要時獨立查核）
→ 項目記錄與證據附錄
→ Project Review 與 SOP 反饋
```

流程會按風險和範圍裁剪。單一錯字可以使用 `trivial fast path`；多文件、
UI/runtime、構建發布或現場任務才使用較完整的交付契約。

## 怎樣套用

只要工作可以按以下方式整理，就可以使用這個框架：

```text
理解意圖
→ 暴露假設
→ 釐清邊界
→ 作出設計決定
→ 交接有範圍的工作
→ 驗證證據實際能證明什麼
```

## 適用場景

Cyber-Age SOP 不只適合小型 coding 任務。大型系統、藝術設計、AI 媒體和 AI
遊戲，只要使用者需要先釐清需求與邊界，也可以套用：

| 規模或領域 | SOP 負責協調什麼 |
|---|---|
| 小型任務 | 有邊界的修改、一次相關檢查和簡短報告 |
| 標準項目 | Anchor、Profile、Agent Brief、驗證和項目記錄 |
| 大型系統 | 工作流、依賴、架構決定、里程碑、發布閘門和整合證據 |
| 多項目計畫 | 上層目標、子項目、共享決定、跨項目風險和分階段交付 |
| System／Infrastructure | 架構、環境、權限、備份、rollback、恢復和長期證據 |
| 藝術與設計 | Creative Brief、參考素材、方向、迭代、選稿標準和來源記錄 |
| AI 生圖／動畫／音訊 | Prompt 或製作版本、資產、審核閘門、輸出檢查和權利邊界 |
| AI 遊戲 | Game Design、核心循環、可玩 Vertical Slice、Playtest、平台矩陣和發布證據 |

以上是概念套用方式。Runtime 提供 Brief／Task／Evidence 記錄與依賴閘門，沒有 Program／Workstream 管理器，大型項目效益仍未驗證。大型工作可按需要拆成：

```text
Program
→ Workstream
→ Project
→ Task
→ Evidence
```

目前 runtime Skill 直接提供 `code`、`ui-doc` 和 `field` 三個主要 Task Profile。
Project-SOP 層另外描述 `skill-agent-workflow`、`docker-service` 和
`experiment-tool`。`system-architecture`、`creative-production`、
`media-generation` 和 `game-development` 是可擴展方向，不代表目前 runtime
已經內置這些領域的專用邏輯。

## 它能做什麼，不能做什麼

### 它能協助

- 把模糊想法整理成有範圍的 Project Anchor；
- 按風險和範圍選擇小路徑或完整路徑；
- 透過 Agent Brief 把已確認的決定交給 Agent；
- 釐清專用工具需要接收什麼，但不冒充專用工具本身；
- 分開 code、build/release、field 和 long-running 證據；
- 在項目負責人選擇使用時，把大型工作拆成工作流、Task、里程碑和審核閘門；
- 區分生成資產、人工審核資產和正式接受的生產結果；
- 在知識庫留下項目主頁和證據附錄。

### 它不能做

- 取代 software、game、rendering、audio、image 或 animation engine；
- 自動判斷作品是否美、音樂是否好聽、遊戲是否好玩；
- 保證所有 Agent runtime 都會完全相同地解讀 Skill；
- 把本地測試或生成文件變成現場驗收；
- 自己提供現場操作所需的授權、備份、rollback 或恢復能力；
- 保證長期穩定性、兼容性、作品質量或使用者採用；
- 取代領域專家、人工審美、權利檢查或 production QA。

對 AI 創意工作，SOP 可以協助釐清製作鏈路，但不是代替人做審美判斷：

```text
創意 Brief
→ 參考素材與權利邊界
→ Prompt／模型／資產版本
→ 小型 Vertical Slice
→ 生成與後期
→ 人工審核
→ 輸出與播放檢查
→ 發布或歸檔
```

## 目錄

```text
skills/cyber-age-sop/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── acceptance-and-evidence.md
    ├── decision-brief-template.md
    ├── failure-path.md
    ├── implementation-readiness.md
    ├── lifecycle-traceability.md
    ├── prompt-enhancement.md
    ├── regression-cases.md
    ├── task-profiles.md
    ├── technical-translation.md
    ├── visual-aids.md
    └── web-research.md

project-sop/
├── README.md
├── reference-project-template.md
├── cyber-age-project-sop类型定义.md
└── cyber-age-project-sop完整鏈路.md

.github/workflows/
├── validate.yml
└── release.yml

scripts/
├── validate_public_package.py
└── validate_implementation_readiness.py
```

參考項目文件只作「結構參考」。公開包沒有加入任何項目的設備、拓撲、實現細節、
私人證據或現場結論。

## 使用 Skill

Skill 位於：

```text
skills/cyber-age-sop/
```

可以把這個目錄複製到你的 Agent runtime 所使用的 Skill 目錄，或按目標 runtime
支援的格式調整。

**網路依賴：** 不強制需要。runtime 有搜尋或網頁讀取工具時，Skill 可用來查證可行性
和價格；沒有時按模型知識作有條件回答，標明實際已知截止日，未知則如實說明。

**引導原則：** Skill 在 Discovery 階段內建了引導式探索（先承接、邀請描述、逐層區分），
借鑒自引導與 coaching 實務，但不取代專門的引導或 coaching skill，也不會自動轉介到
其他 skill。

## Project SOP 文件

`project-sop/` 保存可跨 session 使用的項目層：

- `reference-project-template.md`：說明可以借用哪些呈現結構，以及哪些內容不可複製。
- `cyber-age-project-sop类型定义.md`：定義項目類型、Task Profile、metadata、
  證據契約和最小記錄。
- `cyber-age-project-sop完整鏈路.md`：從 Anchor、交付到驗證、項目主頁和復盤的
  完整流程。

這些文件不依賴任何特定硬件、repository、部署環境或現場結果。

## GitHub Actions

GitHub Actions 會檢查：

- Skill frontmatter；
- Markdown code fence 是否成對；
- 公開包內的 Markdown 內部連結；
- 常見秘密和本地路徑模式；
- 可重現的 source archive。

推送 `v*` tag 時，release workflow 會重新驗證，產生 `.tar.gz` 源碼包、可安裝 Skill
`.zip` 和 SHA-256 校驗值，附加到 GitHub Release。帶測試後綴的 tag 會標為
Pre-release，不取代最新穩定版。

這是一個 Markdown/YAML 文件包，因此這裡的「編譯」指結構驗證和打包，不是生成二進制
程序。

## 證據邊界

repository checks 通過，只能證明指定 commit 的公開包結構有效，不能證明：

- 所有 Agent runtime 都會完全相同地解讀每一條指令；
- 某個項目可以安全部署到真實環境；
- 某個使用者設備、網路或服務已經驗收；
- 現場操作已經成功；
- 長時間運行一定穩定。

報告結果時，請使用 `acceptance-and-evidence.md` 中的證據層級。

## 版本

目前公開測試版為 `0.5.3-beta.1`（2026-11-09），最新穩定版仍為 `0.4.5`：

- Runtime Skill version：`0.5.3-beta.1`（公開測試版）
- Project SOP document version：`0.1`
- Repository prerelease version：`0.5.3-beta.1`

### v0.5.3-beta.1 的變更

- 內建可逆提示詞增強，無須先安裝 `prompt-refiner`；原話、改稿、差異、未知與新增建議分清。
- 局部採納或返回原文會影響後續內容；只認可改稿不會自動執行，也不等於未定範圍已獲確認。
- 有用的提問／能力選擇附一句具體理由，不反覆列調用回執。
- 按用途選草圖、比較表與自包含 SVG／HTML；同一來源修訂、對話內重點及實際畫面查核。
- 不增加 runtime dependency、server、hook、排程器或模型路由服務。詳見[本版說明](docs/releases/v0.5.3-beta.1.md)。

### v0.5.2-beta.1 的變更

- 探索 → 暫定草圖／回述 → 使用者實質確認 → 第一張對話內行動卡；不規定提問輪數。
- 已確認需求可直接接續實作、修改與恢復，實際檢查及來源身分保存在同一記錄。
- 已授權低風險工作可使用指定的確定性自測，仍分開獨立查核與真人驗收。
- 有限本機比較中，三組均通過同組 12 項程式與 4 項插件核心檢查；三組續做均未增加功能。這不證明編程品質較高或真人更容易理解。
- 詳見[本版說明](docs/releases/v0.5.2-beta.1.md)及 [CHANGELOG](CHANGELOG.md)；以下保留歷史版本內容。

### v0.5.1-beta.1 的變更（歷史版本）

- 項目範圍釐清後，顯示一張固定八欄的 Next-Step Card；瑣碎修改跳過。
- 用日常工作名稱說明現況，分開實作、測試、驗收與未知狀態。
- 依賴工作引用直接前置的實際證據；沒有自動任務排程器。
- 按需加入最小 SPEC、任務／證據索引、版本身分與人工恢復核對。
- 符合使用者批准與 repo 規範時，可版本化長期項目文件；私人與原始證據分開保存。
- 補充雙語安裝、回饋和已知限制。

本地 `0.5.0` 與後續候選快照屬開發基線，沒有補稱為已公開的穩定版本。
結構檢查通過不代表真人理解或端到端可靠度已驗證，詳見[測試版說明](docs/releases/v0.5.3-beta.1.md)及 [CHANGELOG](CHANGELOG.md)。

### v0.4.5 的新特徵（2026-10-15）

- 新增 `decision-ready`、`discovery-ready`、`prototype-ready`、`build-ready`、
  `field-ready` 五級交接成熟度；
- 把 Agent 推薦與使用者已批准的決策分開；
- 對平台、租戶、API、身份和敏感資料整合要求 Readiness Matrix；
- 未知的租戶或接口條件改成有界限的只讀盤點，不再猜測 endpoint、schema 或權限；
- 多系統項目拆成可獨立驗證的 Agent Brief；
- 新增整合就緒回歸案例和 validator。

這一版只澄清交接成熟度，不會自動選平台、授權租戶訪問，也不會在沒有證據時宣稱
整合已經可以建置。

各版本變更見 [CHANGELOG.md](CHANGELOG.md)。

如果修改路由、證據邊界或安全閘門，應同步更新 regression cases 和 CHANGELOG。

## 貢獻

提交 Pull Request 前請先閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)。保持修改範圍
清楚，不要加入私人 transcript、credential、設備識別資料或本地絕對路徑。

## 授權

除非文件另有說明，本 repository 使用 Apache License 2.0。詳見 [LICENSE](LICENSE)。

