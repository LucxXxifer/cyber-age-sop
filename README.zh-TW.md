# Cyber-Age SOP

[English](README.md) · [繁體中文](README.zh-TW.md)

Cyber-Age SOP 是一套用來深度挖掘設計者／項目負責人需求、釐清假設和邊界，
再輔佐 Agent 交付的流程框架。它可以處理 software、hardware、UI、
documentation、Skill、Docker、automation、藝術、AI 媒體或遊戲想法。

**v0.4.5（2026-10-15）：Integration Readiness Gate。** Decision Brief 現在會區分
Agent 的建議和使用者已確認的決定。涉及平台、租戶、API、身份或敏感資料時，Skill 會標示
就緒層級；未知的整合條件會轉成有邊界的只讀盤點任務，而不是猜測可直接建置的契約。

**v0.4.4（2026-10-13）：Decision Brief。** 完成需求探索和技術翻譯後，Skill 會在
repository 外寫一份 Decision Brief，讓不會寫程式的使用者可以保存、分享，或直接交給
開發者／Agent。

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
→ 獨立驗證
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

大型項目不會被壓成一張超大的 Brief，而是拆成：

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
和價格；沒有時就用模型知識回答，並標明知識截止日期。

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

推送 `v*` tag 時，release workflow 會重新驗證、產生 `.tar.gz` 源碼包，並附加到
GitHub Release。

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

目前 repository release 是 `0.4.5`：

- Runtime Skill version：`0.4.5`
- Project SOP document version：`0.1`
- Repository release version：`0.4.5`

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

