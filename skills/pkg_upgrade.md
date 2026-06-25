---
name: 15-upgrade
description: 一鍵升級工具 — 更新 npm、pip 以及各種已安裝的 CLI 工具。
---

# 技能 15：一鍵升級工具

將本機所有的 CLI 套件一鍵更新至最新版本。

## 執行流程
對 AI 助理說「幫我更新所有工具」，AI 助理會自動在終端機運行以下升級指令：
1. NPM 全域套件更新：`npm install -g npm`，以及更新 `@bitbonsai/mcpvault`。
2. PIP 套件更新：`pip install --upgrade notebooklm-mcp-cli`。
3. 重新執行健康檢查 (Doctor)，向你回報更新後的版本。
