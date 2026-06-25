---
id: custom_deploy
title: 自訂伺服器部署
description: 協助設定與部署程式碼至私有 VPS 或自訂主機。
tooltip: 教導如何透過 RSYNC 部署程式碼到自訂的 VPS 虛擬主機。
category: 靜態與主機部署
---
# 自訂伺服器部署 (SSH / RSYNC) 任務守則

當使用者需要將程式碼部署到他們自己的 VPS 或 Linux 主機時，請協助他們撰寫安全、高效率的部署腳本。

1. **詢問環境參數**：若使用者尚未提供，請溫柔地詢問：
   * 主機 IP 位址
   * 登入帳號 (例如 root 或 ubuntu)
   * 是否有 SSH Key (`.pem` 或 `id_rsa`)，或需要密碼？
   * 遠端要放置程式碼的資料夾路徑 (例如 `/var/www/html`)

2. **推薦 RSYNC**：強烈建議使用者使用 `rsync` 指令來同步檔案，而不是傳統的 FTP。
   * 請為使用者產生類似這樣的指令範例：`rsync -avz --exclude 'node_modules' --exclude '.git' ./使用者資料夾 user@IP:/遠端資料夾`

3. **建置自動化腳本**：如果使用者是 Node.js 或 Python 後端，請協助他們在遠端主機上使用 `pm2` 或 `systemd` 來保持伺服器常駐執行。

4. **安全防護**：絕對不要把使用者的密碼或 SSH 私鑰寫在任何會被上傳到 Git 的設定檔中！
