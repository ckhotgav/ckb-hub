---
name: 01-env-setup
description: 基礎環境建置 — 安裝 Node.js 與 Python 並配置 PowerShell 權限。
---

# 基礎環境建置

在開始使用 AI 開發之前，需要先安裝基礎的「底座工具」。

## 步驟 1：PowerShell 權限解除 (僅限 Windows)
> ⚠️ 重要：必須由使用者在系統管理員權限的 PowerShell 執行：
* 搜尋 `PowerShell` -> 右鍵「以系統管理員身分執行」
* 貼上並執行：`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
* 輸入 `Y` 並按下 Enter。

## 步驟 2：安裝 Node.js (JavaScript 執行環境)
* **Windows** (AI 助理在終端機執行)：`winget install --id OpenJS.NodeJS.LTS -e --source winget`
* **macOS** (AI 助理在終端機執行)：`brew install node`

## 步驟 3：安裝 Python
* **Windows**：引導使用者前往 [Python 官網](https://www.python.org/downloads/) 下載並安裝。**安裝時第一步一定要勾選「Add Python to PATH」**。
* **macOS** (AI 助理在終端機執行)：`brew install python`

## 驗證方式
重啟編輯器後，終端機執行：
* `node --version`
* `npm --version`
* `python --version`
確認皆能顯示版本號。
