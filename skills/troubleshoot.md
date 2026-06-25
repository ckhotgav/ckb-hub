---
id: troubleshoot
title: 疑難排解大師
description: 啟用深度的除錯模式，解決卡關超過 30 分鐘的疑難雜症。
tooltip: 當卡關超過 30 分鐘必開！深度分析 Log 錯誤並提出突破方案。
category: 診斷與維護
---
# 疑難排解

整理了學生在安裝過程中常見的報錯與快速修復方式。

## 常見問題 1：NPM 安裝出現 `Permission Denied` 或 EACCES 錯誤
* **解法**：在 Windows 請以系統管理員權限打開 PowerShell 執行安裝。在 Mac 請在指令前加上 `sudo`，如：`sudo npm install -g @bitbonsai/mcpvault`。

## 常見問題 2：`Set-ExecutionPolicy` 指令無效
* **解法**：確保你打開的是 `PowerShell`，而不是舊版的 `CMD (命令提示字元)`。且必須選擇「以系統管理員身分執行」。

## 常見問題 3：MCP 無法連線，顯示 `Spawn ENOENT`
* **解法**：代表設定檔中的執行檔路徑不正確。請 AI 重新檢查你的 `mcp_config.json`，在 Windows 上請確認 `command` 指向的是 `npx.cmd` 而不是 `npx`。
