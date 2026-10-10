# Cyber-Age SOP

[English](README.md) · [繁體中文](README.zh-TW.md)

Cyber-Age SOP 是一套輕量的項目生命週期流程，用來把個人 software、hardware、
UI、documentation、Skill、Docker 或 automation 想法，整理成範圍清楚、證據邊界
明確、可以交接和驗證的工作。

這個 repository 是個人開源項目，不是 OpenAI、Codex、Obsidian 或 GitHub 的官方項目。

## 兩個層次

- `skills/cyber-age-sop/`：給 Agent runtime 使用的 Skill，負責項目錨定、任務
  Profile、交付、驗證和復盤。
- `project-sop/`：可長期保存的項目類型、呈現方式和完整鏈路文件，可放入
  Obsidian 或其他知識庫。

## 它解決什麼問題

這套流程針對幾種常見問題：

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

## 目錄

```text
skills/cyber-age-sop/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── acceptance-and-evidence.md
    ├── regression-cases.md
    └── task-profiles.md

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
支援的格式調整。Skill 本身不需要網路、外部帳戶、現場設備或秘密。

Skill 會把引導和 coaching 保持為獨立能力，不會自動模擬它們。如果使用者明確要求
分層提問、深入引導或反思，應交給相應的專用工具處理。

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
- 公開包內的 Obsidian-style links；
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

目前 repository release 是 `0.1.3`：

- Runtime Skill version：`0.2`
- Project SOP document version：`0.1`
- Repository release version：`0.1.3`

如果修改路由、證據邊界或安全閘門，應同步更新 regression cases 和 CHANGELOG。

## 貢獻

提交 Pull Request 前請先閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)。保持修改範圍
清楚，不要加入私人 transcript、credential、設備識別資料或本地絕對路徑。

## 授權

除非文件另有說明，本 repository 使用 Apache License 2.0。詳見 [LICENSE](LICENSE)。

