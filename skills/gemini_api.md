---
name: 09-gemini
description: Gemini 免費 API — 申請 API 金鑰，使用 @google/generative-ai SDK 寫測試程式。
---

# Gemini 免費 API 串接

直接呼叫 Google 的 AI 能力來為你的網頁進行智慧加持。

## 步驟 1：申請 API Key
* 前往 [Google AI Studio](https://aistudio.google.com/apikey)，點擊「Create API Key」。

## 步驟 2：安裝 SDK
* 終端機執行：`npm install @google/generative-ai`

## 步驟 3：寫測試程式
* 將 API 金鑰提供給 AI 助理，AI 助理會為你撰寫一個 `test-gemini.js` 檔案，自動呼叫 `gemini-1.5-flash` 模型並列印出對話結果。
