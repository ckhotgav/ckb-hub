---
name: 19-ftp-hosting
description: FTP 免費主機 — 使用 ProFreeHost 或 InfinityFree 免費架設網站與建立 MySQL 資料庫。
---

# 19-FTP 免費主機（網站架設）

這個技能教你用免費主機把網頁放到網路上，讓任何人都能瀏覽。

## 什麼是網站主機？

就像在網路上「租一塊地來蓋房子」——主機就是那塊地，你的網頁檔案和資料庫都放在裡面。

## 什麼是 FTP？

FTP 就像網路的「檔案總管」，把你的電腦檔案傳送到主機上。傳上去之後，全世界都能看到你的網站。

---

## 選擇你的主機商

這個技能支援兩家免費主機，你可以選一家來用：

| 項目 | ProFreeHost | InfinityFree |
|:----|:-----------|:-------------|
| 官網 | `profreehost.com` | `infinityfree.com` |
| 免費域名 | 多種免費子網域可選（不含主公司網址） | 多種免費子網域可選（部分方案含 `.infinityfreeapp.com`） |
| FTP | ✅ 有控制台 | ✅ 有控制台 |
| MySQL | ✅ 支援 | ✅ 支援 |
| PHP | ✅ 支援 | ✅ 支援 |
| 空間 | 1GB | 5GB |
| 月流量 | 5GB | 無限 |
| 廣告 | 無（免掛廣告） | 有（掛在頁尾） |
| 同集團 | 同一家（iFastNet） | 同一家（iFastNet） |

兩家都是同個母公司，操作介面很類似。差別在 **InfinityFree 空間更大但會掛廣告**，**ProFreeHost 空間小但無廣告**。

> 不確定選哪個？預設用 **InfinityFree**（空間大、流量無限制，適合新手練習）。

---

## 1. 註冊帳號

### 選 ProFreeHost

1. 打開 [https://profreehost.com/register](https://profreehost.com/register)
2. 填入 Email 和密碼，點 Register
3. 去信箱收驗證信，點擊啟用連結
4. 登入控制台後，建立一個網站帳號
5. 在「選擇網域」步驟可以挑選免費子網域（不含 ProFreeHost 自家網址），例如：
   - `你的帳號.rf.gd`
   - `你的帳號.c1.biz`
   - 或其他可用選項
6. 設定完成後，你的網址就是 `https://你選的網域`

### 選 InfinityFree

1. 打開 [https://www.infinityfree.com](https://www.infinityfree.com)
2. 點「Get Premium Free Hosting」或「Sign Up」
3. 填入 Email 和密碼，註冊後收驗證信啟用
4. 登入後點「Create Account」建立一個免費主機帳號
5. 在「選擇網域」步驟可以看到多種免費子網域，例如：
   - `你的帳號.infinityfreeapp.com`
   - `你的帳號.rf.gd`
   - `你的帳號.c1.biz`
   - `你的帳號.a0001.net`
   - 或其他可用選項
   （`.infinityfreeapp.com` 是 InfinityFree 自家提供的選項，其他為第三方免費域名）
6. 挑一個你喜歡的，輸入帳號名稱
7. 密碼會自動產生，**記下來**（之後會用到）
8. 點「Create」完成
9. 之後登入控制台：`https://cp.infinityfree.com`（VistaPanel）

---

## 2. 找到你的 FTP 與 MySQL 資訊

### ProFreeHost 控制台

登入後：
1. 左邊選單點「FTP 帳號」(FTP Accounts)
2. 看到 FTP 主機、帳號、密碼

### InfinityFree 控制台 (VistaPanel)

登入 [https://cp.infinityfree.com](https://cp.infinityfree.com) 後：
1. 找到「FTP 帳號」(FTP Accounts) 區塊
2. 如果沒看到，點左邊的「FTP」
3. 會看到 FTP 主機（通常是 `ftp.你的帳號.infinityfreeapp.com`）、帳號、密碼
4. 點左邊的「MySQL 資料庫」(MySQL Databases) 可以管理資料庫
5. MySQL 主機位置會顯示在該頁面（通常長這樣：`sql123.infinityfree.com`）— **不是 localhost**，等等建立連線時要用這個

> ⚠️ InfinityFree 的 MySQL 主機不是 `localhost`，一定要去控制台看實際顯示的主機位置。

---

## 3. 安裝 FileZilla（圖形化上傳）

### Windows
去 [https://filezilla-project.org](https://filezilla-project.org) 下載 FileZilla Client 並安裝。

### Mac
```bash
brew install --cask filezilla
```

### 連線步驟
1. 打開 FileZilla
2. 在上方填入：
   - 主機：你的 FTP 主機
   - 使用者名稱：你的帳號
   - 密碼：你的密碼
   - 連接埠：`21`
3. 點「快速連線」
4. 右邊看到主機的檔案，就代表連線成功！

### 替代方案：用 CLI 指令上傳

### Windows (PowerShell)
```powershell
npm install -g ftp-cli
# 上傳檔案
ftp -s:upload.txt
```

### Mac
```bash
curl -T index.html ftp://你的帳號:你的密碼@你的FTP主機/htdocs/index.html
```
> InfinityFree 的網頁根目錄是 `htdocs`，ProFreeHost 是 `public_html`，上傳時注意。

---

## 4. 上傳你的第一個網頁

請 AI 幫你產生一個 `index.html`：

對你的 AI 編輯器說：
```
請幫我寫一份 index.html，內容是「點哥AI全能工具箱」的介紹頁面，
風格是深色科技風，包含：
1. 點哥AI全能工具箱是什麼的簡介
2. GitHub 連結 https://github.com/ckhotgav/ckhotgav-tools
3. 用白話解釋什麼是「網站主機」和「FTP」
4. 一段醒目的免費主機提醒：
   - 僅供練習，正式上線需購買付費主機
   - 免費主機若連續 30 天無人瀏覽，會發信警告，仍無處理將刪除帳號
5. 頁尾註明「由免費主機代管」
```

寫好後，把 `index.html` 用 FileZilla 拖曳到主機的根目錄。根目錄名稱依主機商不同：
- **ProFreeHost** → `public_html`
- **InfinityFree** → `htdocs`

### 確認網站上線

打開瀏覽器，輸入你註冊時選的網址，看到網頁就成功了！

---

## 5. 建立 MySQL 資料庫

### ProFreeHost

1. 左邊選單點「MySQL 資料庫」(MySQL Databases)
2. 在「建立新資料庫」輸入名稱（例如 `mydb`），點「建立」
3. 往下滑到「新增使用者」，輸入使用者名稱和密碼，點「建立」
4. 在「新增使用者到資料庫」把使用者加到資料庫，權限選「全部」
5. 記下以下資訊（技能 20 會用到）：
   - 資料庫名稱
   - 資料庫使用者
   - 資料庫密碼
   - 資料庫主機：`localhost`

### InfinityFree

1. 在 VistaPanel 左邊點「MySQL 資料庫」(MySQL Databases)
2. 輸入資料庫名稱（例如 `mydb`），點「建立」
3. 建立使用者，填入名稱和密碼，點「建立」
4. 把使用者加到資料庫，權限全選
5. 記下以下資訊（技能 20 會用到）：
   - 資料庫名稱
   - 資料庫使用者
   - 資料庫密碼
   - 資料庫主機：查看頁面上顯示的（例如 `sql123.infinityfree.com`）— **不是 localhost**

---

## ✅ 完成

你已經學會了：
- 註冊免費主機（ProFreeHost 或 InfinityFree）
- 用 FTP 上傳網頁
- 建立 MySQL 資料庫

下一步：安裝 **技能 20 (PHP + MySQL)** 來製作動態網站！
