---
id: ftp_php
title: PHP 專案 FTP 部署
description: 安全且結構化地發布 PHP 後端至 CPanel 虛擬主機。
category: 靜態與主機部署
---
# PHP + MySQL 資料庫（進階延伸）

**先决條件**：你已經完成技能 19，擁有免費主機帳號（ProFreeHost 或 InfinityFree）、已上傳網頁、並建立了 MySQL 資料庫。

## 什麼是 PHP？

PHP 是一種讓網頁「會動」的程式語言。靜態 HTML 就像一張紙，印什麼就永遠固定；PHP 則像一個魔術師，可以從資料庫撈資料即時顯示出來。

## 什麼是 MySQL？

MySQL 是一種「資料庫」軟體，用來存放網站的資料（會員名單、文章內容、商品資訊等）。PHP 負責幫你讀取、新增、修改這些資料。

簡單來說：**PHP 是店員，MySQL 是倉庫**。

---

## 1. 準備你的資料庫連線資訊

在開始之前，先確認你手上有技能 19 建立好的這四項資訊：

- 資料庫名稱
- 資料庫使用者
- 資料庫密碼
- 資料庫主機（ProFreeHost 是 `localhost`，InfinityFree 則為控制台上顯示的主機位置，例如 `sql123.infinityfree.com`）

## 2. 讓 AI 幫你寫 PHP 程式

對你的 AI 編輯器說：
```
我有一個免費主機，已建立 MySQL 資料庫。
資料庫資訊如下：
- 資料庫名稱：[貼上你的資料庫名稱]
- 使用者：[貼上你的使用者]
- 密碼：[貼上你的密碼]
- 主機：[貼上你的資料庫主機]

請幫我做兩件事：

1. 寫一個 db.php（資料庫連線檔），用來連線到我的 MySQL 資料庫
2. 寫一個 index.php，會連線資料庫並顯示「連線成功」的訊息，
   以及一個簡單的訪客計數器（把每次瀏覽次數存到資料庫）

用 mysqli 寫法，加上錯誤處理，如果連線失敗要顯示清楚的原因。

寫完後請把程式碼給我，我會上傳到主機。
```

AI 會幫你產生 PHP 程式碼。

## 3. 上傳 PHP 檔案到主機

用 FileZilla 或 CLI，把 `db.php` 和 `index.php` 上傳到 `public_html` 資料夾。

### Windows (PowerShell)
```powershell
# 安裝 ftp-deploy 套件
npm install -g ftp-deploy

# 用指令上傳整個資料夾
npx ftp-deploy --server 你的FTP主機 --user 你的帳號 --password 你的密碼 --local-dir . --remote-dir public_html
```

### Mac
```bash
# 用 curl 上傳單一檔案
curl -T db.php ftp://你的帳號:你的密碼@你的FTP主機/public_html/db.php
curl -T index.php ftp://你的帳號:你的密碼@你的FTP主機/public_html/index.php
```

## 4. 測試你的動態網站

打開瀏覽器，輸入你註冊時選的網址再加上 `index.php`（例如 `https://你的帳號.infinityfreeapp.com/index.php`）

- 看到「資料庫連線成功」+ 訪客計數器 → 全部搞定！
- 如果出現錯誤訊息 → 把錯誤貼給 AI，請它幫你修正

## 5. 進階練習（選用）

對 AI 說：
```
我已經可以成功連線免費主機的 MySQL 資料庫了。
請幫我寫一個「留言板」PHP 程式：
- index.php：顯示所有留言 + 新增留言表單
- db.php：資料庫連線
- 留言需要名字、內容、時間
- 用 Bootstrap 簡單美化一下畫面
寫好後告訴我怎麼上傳。
```

## ✅ 完成

你已經從「只會放靜態網頁」升級到「擁有動態網站 + 資料庫」了！

隨時可以請 AI 幫你加更多功能：會員系統、文章發佈、商品展示⋯⋯
