---
name: 06-supabase
description: Supabase 雲端資料庫 — 安裝 Supabase CLI 並協助建立 SQL 會員資料表。
---

# 技能 06：Supabase 雲端資料庫

使用免費的 Postgres 雲端資料庫來儲存網站資料。

## 步驟 1：安裝 Supabase
* **Windows** (AI 助理執行)：`npm install -g supabase`
* **macOS** (AI 助理執行)：`brew install supabase/tap/supabase`

## 步驟 2：註冊與建立專案
* 請使用者前往：https://supabase.com
* 使用 GitHub 登入並點選「New Project」，設定密碼與伺服器區域（建議 Singapore 或 Tokyo）。

## 步驟 3：資料庫表格初始化
* 將你的 Supabase API URL 與 Key 提供給 AI 助理，AI 助理會主動幫你建立 `users` 資料表，包含 `name`, `email` 等欄位。
