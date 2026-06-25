# 其他雲端部署平台

除了 Netlify 之外，你也可以使用 Vercel 或 Cloudflare 部署你的網頁專案。

## 1. Cloudflare 部署方案

Cloudflare 提供了兩種極佳的部署方案，適用於不同的開發場景：

### 方案 A：臨時部署 (Wrangler Ephemeral Deploy) — 60 分鐘免登入
適合快速預覽、AI 自動部署或不想註冊帳號的臨時測試場景。
* **前提條件**：確保未處於登入狀態（若已登入，可執行 `npx wrangler logout`）。
* **部署步驟**：
  1. 安裝 CLI 工具：`npm install -g wrangler` (建議 4.102.0 以上版本)。
  2. 在專案根目錄下執行以下指令部署靜態目錄（例如 `./dist` 或 `./assets`）：
     ```powershell
     npx wrangler deploy ./dist --temporary
     ```
  3. 執行後，Cloudflare 會自動生成一個 **臨時預覽網址** (有效時間 60 分鐘)，並提供一個 **Claim URL (認領網址)**。
  4. 如果滿意，可在 60 分鐘內點擊 Claim URL 登入並認領，將此部署永久轉移至你的個人帳戶中；若不認領，60 分鐘後該部署將被自動刪除。

### 方案 B：正常部署 (Wrangler Pages Normal Deploy) — 永久部署
適合有個人 Cloudflare 帳戶，需要長期維護專案的場景。
* **方式一：瀏覽器互動登入**
  1. 終端機執行：`npx wrangler login`，瀏覽器會自動彈出，登入你的 Cloudflare 帳戶授權。
  2. 執行 Pages 部署：
     ```powershell
     npx wrangler pages deploy ./dist --project-name=your-project-name
     ```
* **方式二：API Token 免互動登入（適合自動化/隱私環境）**
  1. 在 Cloudflare Dashboard 的「My Profile -> API Tokens」建立具有 `Cloudflare Pages -> Edit` 權限的 Token。
  2. 執行命令時帶入 Token：
     * **Windows PowerShell**:
       ```powershell
       $env:CLOUDFLARE_API_TOKEN="您的_API_TOKEN"; npx wrangler pages deploy ./dist --project-name=your-project-name
       ```
     * **macOS / Linux**:
       ```bash
       CLOUDFLARE_API_TOKEN="您的_API_TOKEN" npx wrangler pages deploy ./dist --project-name=your-project-name
       ```

---

## 2. Vercel
* **特色**：前端託管神器，特別適合 Next.js / React / Vite 網頁。
* **安裝與部署**：
  1. 安裝：`npm install -g vercel`
  2. 登入：`vercel login`
  3. 部署：專案目錄下執行 `vercel`，生產環境執行 `vercel --prod`。
