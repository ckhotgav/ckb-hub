# CKB-Hub 開發與架構決策日誌 (Development & Architecture Log)

## 📌 專案背景與初衷
本專案（CKB-Hub，又稱點哥 AI 萬用工具箱）的誕生，是為了解決舊版「紙本說明書模式 (Prompt-based)」工具箱的痛點。
在舊版中，使用者的 21 個 AI 技能是以 `.md` 文字檔的形式存在。這種做法導致 AI 常常需要自行憑空拼湊終端機指令（如 `netlify deploy`），出錯率極高，且小白使用者難以安裝與管理。

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
  * **官方 MetaMCP 的致命傷**：強烈依賴 Docker，對於沒有程式基礎的「小白使用者」來說，安裝門檻極高；且管理介面過於工程師導向（需設定 Namespace, Environment Variables 等）。
* **最終決策 (The Beginner-First Approach)**：
  回歸到使用者的初衷：「這套工具箱必須讓沒有程式基礎的新手小白也能輕鬆使用」。因此，我們**拒絕了強迫安裝 Docker 的官方路線**，選擇保留並優化我們自主開發的「極簡版 CKB-Hub」。我們用最低的阻力（只需 Python），實現了與官方系統 80% 相同的核心聚合功能。
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
3. **`static/index.html`**：小白友善的零門檻開關控制台。
4. **`utils/migration.py`**：一鍵升級腳本。

## 🚀 下一步計畫 (Next Steps)
完成目前的架構後，接下來的工作是「填補血肉」。我們計畫將舊版工具箱中剩餘的 18 個技能（包含 Supabase, Obsidian 知識庫等）逐一遷移，為每一個技能在 `mcp_stdio.py` 中撰寫對應的 `@mcp.tool()`，最終打造出完整的 21 技能完全體。
