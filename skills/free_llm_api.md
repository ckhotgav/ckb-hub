---
id: free_llm_api
title: 免費 AI API 串接
description: 協助申請免費額度的 AI 服務 (如 Gemini, Groq 等)，並引導如何在專案中實作串接。
category: AI 工具與模型
---
# 免費 AI API 串接與實作指南

AI 助理會協助你將強大的 AI 模型整合進你的網頁或專案中。為了降低初學者的門檻，本指南重點介紹提供「**免費額度**」的優質 AI 服務供應商。

## 🤖 推薦供應商一：Google Gemini
Google 提供的 Gemini 模型，目前對開發者提供了非常優渥的免費額度 (Free Tier)，非常適合初學者與小專案使用。

### 步驟 1：申請 API Key
* 前往 [Google AI Studio](https://aistudio.google.com/apikey)。
* 登入你的 Google 帳號後，點擊畫面上的「**Create API Key**」按鈕，產生一串金鑰。

### 步驟 2：安全儲存金鑰
* 請立刻將這串金鑰告訴 AI，AI 會啟動「API 金鑰管家」，幫你安全地存入 `.env` 檔案中，避免外洩。

### 步驟 3：安裝 SDK 與實作
* AI 會引導你在終端機執行：`npm install @google/generative-ai`
* AI 會幫你寫一個簡單的 `test-gemini.js`，自動呼叫超快的 `gemini-1.5-flash` 模型來測試對話。

---

## ⚡ 推薦供應商二：Groq (極速推論)
Groq 是一家主打「超高速推論晶片 (LPU)」的公司。在他們平台上，你可以**免費**且**極速**地使用開源模型（如 Meta 的 Llama 3 或開源的 Mixtral）。這對於需要快速反應的聊天機器人非常有用。

### 步驟 1：申請 API Key
* 前往 [GroqCloud Console](https://console.groq.com/keys)。
* 註冊/登入後，點選左側選單的「**API Keys**」，然後點擊「**Create API Key**」。

### 步驟 2：安全儲存金鑰
* 同樣地，將取得的 `gsk_` 開頭金鑰貼給 AI，讓 AI 幫你安全地寫入 `.env` 中。

### 步驟 3：安裝 SDK 與實作
* Groq 的 API 完全相容於 OpenAI 格式，所以實作非常簡單！
* AI 會引導你安裝官方套件：`npm install groq-sdk`
* AI 會幫你寫好呼叫 `llama3-8b-8192` 或其他開源模型的測試程式碼。

---

## 🛠️ 給 AI 的實作守則 (AI 必讀)
1. 當使用者選擇了想要串接的廠商後，請先確保已建立 `.env` 與對應的 `.gitignore`。
2. 請根據使用者選擇的廠商，使用對應的官方 Node.js SDK 撰寫一個測試腳本，並使用 `console.log` 印出 AI 的回覆。
3. 程式碼必須要加上清楚的中文註解，解釋每一行的功用。
