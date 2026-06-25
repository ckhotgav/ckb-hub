# CKB Hub (點哥專案助理)

CKB Hub 是一個專為「無程式基礎新手 (初學者)」設計的輕量級 MCP (Model Context Protocol) 聚合管理工具。
它提供了一個極度簡化的視覺化介面，讓使用者可以一鍵開關各種 AI 技能，並透過 `mcp_stdio.py` 讓 AI 助理自動感知目前專案的狀態（開工/收工）。

## 核心設計理念 (The "Beginner-First" Approach)

1. **零設定門檻**：無需安裝 Docker 或複雜的伺服器環境。只需 Python 即可運行。
2. **極簡 UI**：只提供必要的開關與提示，隱藏底層的「端點(Endpoint)」、「命名空間(Namespace)」等工程師概念。
3. **無縫整合**：完美對接現有的 `.ckb_config.json` 與 `PROJECT.md` 工作流，讓 AI 成為真正的專案管家。

---

## 未來擴充指南：向官方 MetaMCP 升級 (Future-Proofing)

隨著使用者的成長，或者當你需要將此工具部署給「專業的軟體開發團隊」使用時，現有的 CKB-Hub 可能會面臨擴充性（如：權限控管、多伺服器負載平衡、雲端同步）的瓶頸。

屆時，你可以選擇無痛遷移至**官方的 MetaMCP 架構** (`metatool-ai/metamcp`)。

### 升級評估：何時該升級？

- 當你需要雲端部署或團隊協作功能時。
- 當使用者具備 Docker 安裝與操作能力時。
- 當你需要極度複雜的安全驗證 (OAuth) 與中間件 (Middleware) 時。

### 升級步驟草案 (Migration Plan)

如果你決定走向官方航空母艦版，請參考以下步驟進行架構轉換：

1. **環境切換**：
   - 捨棄目前的 `main.py` (FastAPI 網頁前端)，改由安裝並運行官方的 Docker 容器 (`docker run ... metatool-ai/metamcp`)。
2. **橋接核心邏輯**：
   - 保留 `mcp_stdio.py`，但將其註冊為官方 MetaMCP 下的一個子伺服器。
   - 修改 `init_project` 工具：原本是寫入本地 `.ckb_config.json`，改為發送 HTTP API 請求至官方的 MetaMCP API (`POST /api/workspaces`)，透過官方介面動態生成專案環境。
3. **使用者教育**：
   - 引導使用者使用官方的 `http://localhost:3000` 專業介面進行高階管理。

### 總結

目前的架構是「以最小阻力換取最大價值」的最佳解。我們保留了升級的彈性，當未來的需求超過這艘「快艇」的極限時，隨時可以將引擎搬移到「航空母艦」上。
