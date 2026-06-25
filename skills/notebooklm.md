---
id: notebooklm
title: 匯出至 NotebookLM
description: 將專案原始碼打包成適合 NotebookLM 閱讀的文本格式。
tooltip: 將專案所有程式碼打包成單一 Markdown 檔，方便餵給 AI 分析。
category: AI 工具與模型
---
# NotebookLM 知識庫串接

將 Google NotebookLM 的強大分析能力導入你的 AI 編輯器。

## 步驟 1：安裝 NBLM CLI
* 終端機執行：`pip install notebooklm-mcp-cli` (或 `pip3 install notebooklm-mcp-cli`)

## 步驟 2：安全登入授權
* > ⚠️ 重要：請使用者在終端機輸入：`nlm login`
* 瀏覽器會自動彈出，請登入你的 Google 帳號並允許授權。

## 步驟 3：自動綁定到 AGY2 (寫入 mcpServers)
* AI 助理會主動讀取 `C:\Users\user\.gemini\antigravity\mcp_config.json`。
* AI 將自動寫入或更新 `"mcpServers"` 區塊：
  ```json
  "notebooklm": {
    "command": "C:\\Users\\user\\.local\\bin\\notebooklm-mcp.exe",
    "args": []
  }
  ```
  *(AI 助理會根據使用者實際的路徑，將 `notebooklm-mcp.exe` 的完整路徑帶入)*。

## 步驟 4：重新啟動編輯器
設定寫入後，請重啟編輯器以加載該工具。
