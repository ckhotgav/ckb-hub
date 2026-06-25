---
name: 11-obsidian
description: Obsidian 本地筆記連結 — 安裝 mcpvault，詢問筆記庫路徑後自動修改 mcp_config.json 註冊 mcpServers。
---

# Obsidian 本地筆記連結

將你的本地筆記庫「第二大腦」與 AI 助理直接打通。

## 步驟 1：下載安裝 Obsidian
* 請前往 https://obsidian.md/ 下載並安裝。建立一個 Vault 資料夾，例如 `D:\Obsidian`。

## 步驟 2：安裝 MCPVault 工具
* 終端機執行：`npm install -g @bitbonsai/mcpvault`

## 步驟 3：自動設定 mcpServers 區塊
* 將你的 Obsidian Vault 路徑（例如 `D:\Obsidian`）告訴 AI。
* AI 助理會自動讀取並編輯 `C:\Users\user\.geminintigravity\mcp_config.json`。
* AI 將會把 Obsidian 以正確格式寫入 `"mcpServers"` 中：
  ```json
  "obsidian": {
    "command": "npx.cmd",
    "args": ["-y", "@bitbonsai/mcpvault", "你的Obsidian路徑"]
  }
  ```
  *(在 Mac 系統上 command 會自動設定為 `"npx"`)*

## 步驟 4：重啟編輯器
設定更新後，重啟編輯器。你可以對 AI 說：「幫我讀取 Obsidian 裡的最新筆記」，測試連線是否成功。

## 💡 額外功能：14 天筆記整理自動追蹤
連線 Obsidian 後，搭配「知識管理」與「專案助理 (開工)」，AI 將會自動追蹤你筆記庫的整理狀態，每 14 天主動提醒你進行知識重整，確保第二大腦井井有條！
