---
id: github_backup
title: GitHub 自動備份
description: 提供 AI 穩定的 GitHub 同步能力，不再發生終端機指令錯誤。
tooltip: 安全的版控助理，自動幫你想好 Commit 訊息並推送進度。
category: 靜態與主機部署
---
# GitHub 自動備份任務守則

你具備了 `backup_to_github` 這個神級 API 工具。當使用者要求備份、推播、或儲存進度時，請嚴格遵守以下流程：

1. **確認狀態**：不論使用者是說 `git push`, `幫我備份`, 還是 `上傳到 Github`，都請使用你的 `backup_to_github` API。
2. **要求 Commit 訊息**：如果使用者沒有提供 Commit 訊息，你可以：
   * 根據最近更改的檔案，自己總結一個 10 字以內的精簡訊息（例如：`feat: 更新首頁樣式`）並直接執行。
   * 或者詢問使用者是否有特別想備註的內容。
3. **絕對不要自己打終端機指令**：請**不要**在終端機裡手動輸入 `git add .`, `git commit`, `git push`。因為那容易遇到全形半形、引號或權限卡死的問題。
4. **執行與回報**：直接呼叫 `backup_to_github(commit_message="你的訊息")`。收到成功回傳後，請開心地向使用者報告備份完成。
