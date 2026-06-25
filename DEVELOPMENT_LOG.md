# CKB-Hub 開發與架構決策日誌 (Development & Architecture Log)

## 📌 專案背景與初衷
本專案（CKB-Hub，又稱點哥 AI 萬用工具箱）的誕生，是為了解決舊版「紙本說明書模式 (Prompt-based)」工具箱的痛點。
在舊版中，使用者的 21 個 AI 技能是以 `.md` 文字檔的形式存在。這種做法導致 AI 常常需要自行憑空拼湊終端機指令（如 `netlify deploy`），出錯率極高，且初學者難以安裝與管理。

為此，我們決定引入 **MCP (Model Context Protocol)** 架構，將文字說明書進化為「實體的 API 遙控器」。

---

## 📅 開發歷程與重大決策

### 階段一：PoC 概念驗證與核心架構建立 (The Foundation)
* **設計理念**：打造一個「背景 Python 伺服器 (MCP)」搭配「直覺網頁前端 (GUI)」的架構。
* **技術選型**：
  * **前端**：純 HTML + CSS + JS (Vanilla)，追求最極致的輕量化與零安裝門檻。
  * **後端**：FastAPI 提供 Web API，負責讀寫 `status.json`，讓前端能視覺化管理技能開關。
  * **MCP 層**：使用 `fastmcp` 開發 `mcp_stdio.py`。這是與 AI 溝通的橋樑，將所有複雜的指令（如 Git 備份、初始化專案）封裝成 Python 函數。
* **無縫升級機制**：開發了 `migration.py`，能在一秒內將使用者的舊版 Markdown 技能備份，並將新的 `mcp_stdio.py` 自動寫入系統的全局 MCP 設定檔中。

### 階段二：A+B 混合架構的抉擇 (The Crossroads)
* **面臨問題**：使用者發現了開源社群官方的 `metatool-ai/metamcp`（一個極其強大的 Docker-based MCP 聚合器），並提議是否能將我們的自動化工作流與官方框架結合（A+B 融合）。
* **架構辯論**：
  * **官方 MetaMCP 的優點**：企業級架構、未來擴充性極強、內建 Inspector。
  * **官方 MetaMCP 的致命傷**：強烈依賴 Docker，對於沒有程式基礎的「初學者」來說，安裝門檻極高；且管理介面過於工程師導向（需設定 Namespace, Environment Variables 等）。
* **最終決策 (The Beginner-First Approach)**：
  回歸到使用者的初衷：「這套工具箱必須讓沒有程式基礎的新手初學者也能輕鬆使用」。因此，我們**拒絕了強迫安裝 Docker 的官方路線**，選擇保留並優化我們自主開發的「極簡版 CKB-Hub」。我們用最低的阻力（只需 Python），實現了與官方系統 80% 相同的核心聚合功能。
* **未來防護網**：我們撰寫了 `README.md` 的擴充指南。若未來受眾轉變為專業開發團隊，隨時能將 `mcp_stdio.py` 無縫掛載至官方的 Docker 容器中。

### 階段三：極致的 AI 語音遙控器 (The Ultimate Magic)
* **情境最佳化**：為了解決 Windows 環境下背景子處理程序隱藏視窗的問題，以及達成完全不需要動手點擊的完美體驗，我們賦予了 AI 自我管理的能力。
* **功能實作**：
  1. **動態技能管理 (`manage_project_skills`)**：AI 可以直接透過 MCP 工具讀寫專案目錄下的 `.ckb_config.json`。使用者只要說「幫我新增 Netlify 技能」，AI 就能瞬間完成配置。
  2. **魔法控制台連結 (`open_ckb_hub_ui`)**：考慮到 Windows 背景執行的權限隔離（子程序無法強制彈出前景視窗），我們改由 AI 確保伺服器在背景穩定運行（使用 `DETACHED_PROCESS`），並在對話框中回傳可點擊的專屬連結 (`http://127.0.0.1:8000`)，巧妙且優雅地解決了系統限制。
  3. **智慧管家 (`run_project_assistant`)**：當使用者在任何資料夾喊「開工」，AI 會自動偵測是否為舊專案並詢問是否升級，或是自動讀取該專案專屬的掛載設定。

---

## 🛠️ 目前已實作的核心模組與功能
1. **`main.py`**：輕量級 FastAPI 網頁伺服器，負責提供前端 UI。
2. **`mcp_stdio.py`**：核心 MCP 伺服器，負責與 AGY-2 編輯器溝通。目前已內建的工具 API 包含：
   * `init_project`: 初始化全新專案目錄。
   * `manage_project_skills`: 語音動態增刪專案專屬技能。
   * `open_ckb_hub_ui`: 啟動背景伺服器並提供控制台魔法連結。
   * `run_project_assistant`: 處理日常「開工/收工」流程與進度總結。
   * `backup_to_github`: 封裝好的 Git 備份指令。
   * `deploy_to_netlify`: 封裝好的部署準備指令。
3. **`static/index.html`**：初學者友善的零門檻開關控制台。
4. **`utils/migration.py`**：一鍵升級腳本。

### 階段四：18 技能完全體與使用者體驗優化 (The Final Polish)
* **核心擴充**：成功將剩餘的 18 個核心技能（包含 Cloudflare 網頁部署、Supabase, Obsidian 知識庫等）全部遷移至 `mcp_stdio.py`。
* **介面翻新**：在 `static/index.html` 中實作了乾淨俐落的六大分類，讓「初學者」能像逛 App Store 一樣輕鬆挑選需要的 AI 技能。
* **安全與流程防護**：
  1. **Git 防護機制**：建立嚴格的 `.gitignore`，確保 `status.json` 等本地開關狀態或環境變數不會被上傳到 GitHub。
  2. **安全關閉機制 (Taskkill)**：解決了 Windows 環境下 Uvicorn `reload=True` 產生的「總管與工人」雙程序殘留問題。透過在網頁新增紅色的「關閉控制台」按鈕，實作了對父程序的 `taskkill`，確保伺服器能被瞬間且徹底地拔除。

### 階段五：真正的動態讀卡機架構 (The Real Dynamic Bridge)
* **核心挑戰**：使用者點出了一個盲點：「我們的系統只有開關，但舊版那些長篇大論的 Markdown 神級提示詞到底在哪裡被讀取？」
* **架構重構 (Prompt-as-a-Tool)**：
  1. **建立專屬知識庫 (`skills/`)**：新增 `skills/` 資料夾，作為使用者（點哥）專屬的「AI 規則儲藏室」。
  2. **動態讀取引擎 (`check_skill`)**：在 `mcp_stdio.py` 實作了 `check_skill(skill_id)` 函數。當網頁上的開關被打開時，AI 呼叫對應的 API（如 `gas_deploy`），`mcp_stdio.py` 會瞬間潛入 `skills/` 資料夾尋找對應的 `.md` 檔案，並將其內容原封不動地注入 MCP 訊號回傳給 AI。
* **自動化搬運與無縫對接**：
  1. 撰寫 Python 腳本，將舊工具包中 15 項以數字資料夾命名的技能（如 `05-gas/SKILL.md`），自動複製並更名為對應的新 ID（如 `gas_deploy.md`）。
  2. **深度資料淨化**：寫了一支正則表達式腳本，一秒內拔除舊檔案中遺留的 YAML Frontmatter（如 `name: 09-gemini`）以及標題殘留的數字編號（如 `# 19-FTP`），讓注入給 AI 的提示詞達到最純淨、無干擾的狀態。
* **哲學突破**：這確立了 CKB-Hub 的核心價值——我們不寫底層串接的「工程級 MCP」，我們打造的是「Prompt 注入型 MCP」。用 1% 的安裝難度，達成真正 MCP 95% 的自動化威力，完美實現對新手的「降維打擊」。

### 階段六：終極模組化與全自動外掛架構 (The Auto-Discovery Plugin Architecture)
* **核心挑戰**：為了達成「把檔案丟進去，網頁與 MCP 就自動生出按鈕與 API」的最高境界，我們移除了寫死在 HTML 與 Python 中的擴充架構。
* **YAML 身分證 (Self-Contained Plugins)**：
  1. 我們設計了 `SKILL_TEMPLATE.md` 標準格式樣板。
  2. 將所有的 `.md` 規則檔案，頂部加入了 `YAML Frontmatter`（包含 `id`, `title`, `description`, `category`）。讓檔案自帶身分證，完全不需額外的清單。
* **雙端動態重構**：
  1. **後端 API (`main.py`)**：新增 `/api/skills`，啟動時自動掃描 `skills/` 資料夾的 Markdown 檔案並解析 YAML。
  2. **前端 UI (`index.html`)**：完全移除寫死的 HTML，改由 JavaScript 讀取 API，動態產生分類面板與開關。
  3. **動態工具註冊 (`mcp_stdio.py`)**：透過迴圈讀取技能型錄，使用 `mcp.add_tool()` 在啟動瞬間全自動註冊所有的 MCP API。
* **漏洞填補**：為原本只有 Python 腳本的「點哥專案助理 (`project_assistant`)」與「GitHub 備份 (`github_backup`)」補齊了專屬的 `.md` 對話守則與規則說明書，確保 AI 引導初學者的體驗滴水不漏。

---

## 🛠️ 目前已實作的核心模組與功能
1. **`main.py`**：輕量級 FastAPI 網頁伺服器，負責提供前端 UI、動態讀取技能型錄 (`/api/skills`) 與處理安全關閉 (`/api/shutdown`)。
2. **`mcp_stdio.py`**：核心 MCP 伺服器，負責與 AI 編輯器溝通。能在啟動時**動態註冊**所有的技能工具。
3. **`static/index.html`**：初學者友善的零門檻開關控制台（完全動態渲染，支援一鍵安全關閉）。
4. **`使用手冊.md`**：詳細記載技能的用途與「加掛新技能」的擴充指南。
5. **`skills/` 目錄**：外掛技能的集中營，每個技能都是一個獨立且帶有 YAML 身分證的 `.md` 檔案。

## 🚀 未來發展計畫 (Roadmap)
* **多模型切換與高階設定 GUI**：
  未來可將控制台進一步擴充，讓使用者能在網頁上輸入自己的 API Keys，並自動產生 `.env`。
* **雲端技能市集 (Skill Marketplace)**：
  讓網頁具備一鍵從 GitHub 下載其他大神撰寫的 `.md` 技能並瞬間啟用的功能。
