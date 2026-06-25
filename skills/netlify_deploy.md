---
id: netlify_deploy
title: Netlify 一鍵部署
description: 讓 AI 具備直接將靜態網頁發布到網路上的能力。
tooltip: 目前最受歡迎的靜態網站免費發布通道，極速上線。
category: 靜態與主機部署
---
# Netlify 一鍵部署

將寫好的精美靜態網頁（HTML / CSS / JS）一鍵發布到網路上。

## 步驟 1：安裝 Netlify 工具
* 終端機執行：`npm install -g netlify-cli`

## 步驟 2：登入 Netlify
* 終端機執行：`netlify login`
* 瀏覽器會自動彈出，請登入你的 GitHub 帳號進行連結授權。

## 步驟 3：部署測試
* AI 助理會為你寫好一個簡單漂亮的個人網頁。
* AI 助理會**主動詢問**是否執行部署指令：`netlify deploy --prod`。
* 部署成功後，AI 會將產生的網址以精美的 Markdown 格式回傳給使用者。
