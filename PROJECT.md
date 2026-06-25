# ckb-hub 專案進度表

## 🎯 目前開發進度

### ✅ 已完成
- [x] 初始化 CKB-Hub 核心環境與介面 (A+B 混合架構)
- [x] 成功載入並配置 18 項精選核心 AI 技能開關
- [x] **實作 `skills/` 動態讀卡機架構，讓 MCP 動態讀取 `.md` 提示詞注入 AI**
- [x] **完成舊版 15 項 `.md` 技能提示詞的自動化搬運與 YAML Frontmatter 清理**
- [x] 解決背景執行程序衝突，實作安全關閉機制 (Taskkill)
- [x] 撰寫 CKB-Hub 詳細使用手冊

- [x] **實作「全自動外掛尋找模式」 (Auto-Discovery Plugin Architecture)**
  - 取消寫死的陣列，將所有 `.md` 技能檔注入 YAML 身分證（包含 ID, 標題與分類）。
  - 後端 (`main.py`) 啟動時自動解析 YAML，動態產生 `/api/skills`。
  - 網頁 UI 動態渲染分類與開關，並確保「點哥專案助理」與其分類置頂。
  - `mcp_stdio.py` 在啟動瞬間全自動向 MCP 註冊所有的技能 API。
- [x] 撰寫初學者專屬的「點哥 AI 萬用工具箱：新手完全制霸手冊」與流程圖。
- [ ] 考慮未來擴充雲端技能市集 (Skill Marketplace)。

---

## 📝 開發里程碑與技術細節
* **2026-06-25 專案初始化**：
  * 建立 `.ckb_config.json` 綁定全域技能。
* **2026-06-25 完成 MVP 與 18 技能擴充**：
  * 確立了 FastAPI + MCP 的混合架構。
  * 移除了冗餘技能，導入 Cloudflare 部署等高價值工具。
  * 完善了使用者流程（新增「安全關閉」按鈕避免程序殘留）。
* **2026-06-25 實作動態讀卡機與自動化搬運**：
  * 發現「舊版長篇提示詞未掛載」之痛點，緊急開發 `skills/` 資料夾架構。
  * 撰寫 Python 腳本自動搬運舊版 `ckhotgav-agy-tools` 內 15 項資料夾中的 `SKILL.md`，並重新命名對應。
  * 開發正則腳本，深度清除舊版 YAML Frontmatter (`name: 09-xxx`) 與數字標題，確保 Prompt 純淨度。
* **2026-06-25 系統架構究極進化：全自動模組化外掛架構**：
  * 重新為所有的 `skills/*.md` 檔案注入標準化的 **YAML 身分證** (包含 `id`, `title`, `description`, `tooltip`, `category`)。
  * 移除前端 HTML 與後端 Python 中所有寫死的技能架構，打通 `/api/skills` 讓系統能**全自動掃描並生成按鈕與 API**，達成完美的熱插拔體驗。
  * 解決 Uvicorn `reload=True` 導致的雙程序殘留問題，實作徹底追殺 Parent PID 的關閉機制。
  * 擴充技能：將 Gemini API 擴展為 `free_llm_api` (加入 Groq)，並打通專案導讀 (`knowledge_guide`) 與 Obsidian 知識庫的自動同步機制。
  * 產出給初學者的「新手完全制霸手冊」與系統運作流程圖。
