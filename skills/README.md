# 技能指令放置區 (Skills Prompts)

這裡是開發者（點哥）專用的「AI 規則儲藏室」。

當初學者在網頁控制台上把某個技能打開時，系統會自動來這裡尋找對應的 `.md` 檔案，並且把裡面的內容偷偷塞進 AI 的腦袋裡。

## 如何掛載舊工具包的指令？

非常簡單！假設你要掛載 **Google Apps Script 部署 (gas_deploy)** 的超長規則：
1. 在這個資料夾底下建立一個名為 `gas_deploy.md` 的檔案。
2. 把你舊工具包裡寫好的那一大坨 Prompt、Clasp 指令、對話守則，全部貼進這個檔案裡面。
3. 存檔！

搞定了！下次初學者在網頁點擊開啟 GAS 部署時，AI 就會瞬間獲得你寫的這份神級秘笈！

## 目前支援的技能檔名對應表：

- `netlify_deploy.md`
- `env_setup.md`
- `cloudflare_deploy.md`
- `gas_deploy.md`
- `custom_deploy.md`
- `ftp_hosting.md`
- `ftp_php.md`
- `supabase_setup.md`
- `firebase_setup.md`
- `notebooklm.md`
- `gemini_api.md`
- `obsidian_sync.md`
- `knowledge_guide.md`
- `project_doctor.md`
- `pkg_upgrade.md`
- `troubleshoot.md`

*(如果沒有建立這些檔案，系統會安全地退回使用簡短的預設提示詞)*
