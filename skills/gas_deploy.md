# Google Apps Script 自動化

利用 Google 的雲端腳本自動化寄信、處理試算表。

## 步驟 1：打開 GAS API 權限
* 請使用者用瀏覽器打開：https://script.google.com/home/usersettings
* 將「Google Apps Script API」切換為「開啟 (ON)」。

## 步驟 2：安裝 Clasp 上傳工具
* 終端機執行：`npm install -g @google/clasp`

## 步驟 3：登入 Google
* 終端機執行：`clasp login`
* 瀏覽器會自動打開，請授權登入你的 Google 帳號。

## 步驟 4：測試腳本
* AI 會為你設計一個自動化腳本，並使用 `clasp push` 上傳。
