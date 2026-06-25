---
id: firebase_setup
title: Firebase 服務
description: 串接 Firebase Firestore 資料庫與身份認證。
tooltip: 引導初始化 Firebase SDK，並確保資料庫存取規則安全。
category: 雲端資料庫
---
# Firebase 雲端資料庫

Google 提供的即時 NoSQL 資料庫。

## 步驟 1：安裝 Firebase 工具
* 終端機執行：`npm install -g firebase-tools`

## 步驟 2：登入 Firebase
* 終端機執行：`firebase login`
* 在瀏覽器中完成你的 Google 帳號授權登入。

## 步驟 3：初始化與實戰
* 前往 https://firebase.google.com 建立專案。
* 告訴 AI 專案名稱，AI 會協助執行 `firebase init firestore` 並撰寫串接程式碼。
