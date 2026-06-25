from mcp.server.fastmcp import FastMCP
import json
import os
import subprocess
import urllib.request
import webbrowser
from datetime import datetime

# 初始化 MetaMCP 聚合伺服器
mcp = FastMCP("CKB-Hub")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATUS_FILE = os.path.join(BASE_DIR, "status.json")

# 記憶體內的 Session 狀態 (結合全域與專案專屬狀態)
session_status = {}

def load_global_status():
    """讀取 CKB-Hub 網頁控制台設定的全域技能開關狀態"""
    if os.path.exists(STATUS_FILE):
        try:
            with open(STATUS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {}

def is_skill_enabled(skill_id: str) -> bool:
    """檢查技能是否啟用 (全域開啟 或 專案專屬開啟)"""
    global session_status
    if not session_status:
        session_status = load_global_status()
    return session_status.get(skill_id, False)

@mcp.tool()
def init_project(project_name: str, project_type: str, required_skills: list[str], base_path: str = ".") -> str:
    """
    初始化全新專案 (當使用者說「啟動專案」、「建立專案」時呼叫此工具)。
    
    Args:
        project_name: 專案資料夾名稱 (英數字，例如 'my-web-app')
        project_type: 專案類型 (例如 '靜態網頁', 'Node.js', 'Python', '文件筆記', '其他')
        required_skills: 這個專案需要預設掛載的 CKB-Hub 技能清單 (例如 ['obsidian_sync', 'netlify_deploy'])
        base_path: 建立專案的基準目錄
    """
    project_path = os.path.join(base_path, project_name)
    try:
        os.makedirs(project_path, exist_ok=True)
        
        # 1. 建立專案專屬記憶檔 (.ckb_config.json)
        config_path = os.path.join(project_path, ".ckb_config.json")
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump({"auto_load_skills": required_skills}, f, indent=4, ensure_ascii=False)
            
        # 2. 建立基礎管理檔案
        with open(os.path.join(project_path, "PROJECT.md"), 'w', encoding='utf-8') as f:
            f.write(f"# {project_name} 專案進度表\n\n## 待辦事項\n- [ ] 初始化專案\n")
            
        return f"[SUCCESS] 專案 [{project_name}] 初始化成功！\n[MAGIC] 已自動產生 .ckb_config.json 並綁定技能：{', '.join(required_skills)}。\n使用者未來在此資料夾只要說「開工」，就會自動掛載這些能力！"
    except Exception as e:
        return f"[WARNING] 專案初始化失敗: {e}"

@mcp.tool()
def manage_project_skills(action: str, skills: list[str], project_path: str = ".") -> str:
    """
    管理專案的 CKB-Hub 技能 (當使用者說「新增技能」、「移除技能」或「調整掛載」時呼叫此工具)。
    
    Args:
        action: 'add' (新增), 'remove' (移除), 或 'set' (覆寫全部)
        skills: 要操作的技能清單 (例如 ['obsidian_sync', 'netlify_deploy'])
        project_path: 專案目錄
    """
    config_path = os.path.join(project_path, ".ckb_config.json")
    try:
        current_skills = []
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                current_skills = json.load(f).get("auto_load_skills", [])
        
        if action == 'add':
            for s in skills:
                if s not in current_skills:
                    current_skills.append(s)
        elif action == 'remove':
            current_skills = [s for s in current_skills if s not in skills]
        elif action == 'set':
            current_skills = skills
            
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump({"auto_load_skills": current_skills}, f, indent=4, ensure_ascii=False)
            
        return f"[SUCCESS] 專案技能設定成功！目前掛載的技能有：{', '.join(current_skills)}。"
    except Exception as e:
        return f"[WARNING] 技能設定失敗: {e}"

@mcp.tool()
def open_ckb_hub_ui() -> str:
    """
    打開 CKB-Hub 視覺化網頁介面。
    當使用者說「打開控制台」、「開啟網頁」、「查看有什麼技能」時呼叫此工具。
    """
    try:
        # 檢查 UI 是否已經在運行
        try:
            urllib.request.urlopen("http://127.0.0.1:8000", timeout=1)
        except Exception:
            # 如果沒有回應，在背景啟動 main.py (設定 DETACHED_PROCESS 以確保脫離父行程)
            DETACHED_PROCESS = 0x00000008
            subprocess.Popen(["python", "main.py"], cwd=BASE_DIR, creationflags=DETACHED_PROCESS)
            
        # 由於背景執行緒無法強制在前景彈出視窗，改為回傳魔法連結讓使用者點擊
        return "[SUCCESS] CKB-Hub 伺服器已在背景啟動！請告訴使用者：「✅ 伺服器已準備就緒，請點擊這個連結開啟控制台： [👉 點我開啟 CKB-Hub](http://127.0.0.1:8000) 」"
    except Exception as e:
        return f"[WARNING] 開啟網頁失敗: {e}"

@mcp.tool()
def run_project_assistant(command: str, project_path: str = ".") -> str:
    """
    執行點哥專案助理功能 (開工/收工/日常記錄)
    當使用者說出「開工」或「收工」時，必須呼叫此工具，並傳入當前的工作目錄 (project_path)。
    """
    global session_status
    
    response = f"[SUCCESS] 點哥專案助理已成功啟動！(收到指令：{command})\n"
    
    # 實作：專案專屬記憶 (Project-Level Auto-Loading) 與舊專案偵測
    if project_path and os.path.exists(project_path):
        config_file = os.path.join(project_path, ".ckb_config.json")
        project_file = os.path.join(project_path, "PROJECT.md")
        
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    project_config = json.load(f)
                    auto_load_skills = project_config.get("auto_load_skills", [])
                    
                    if auto_load_skills:
                        session_status = load_global_status()
                        for skill in auto_load_skills:
                            session_status[skill] = True
                        
                        response += f"[MAGIC] [智慧管家] 已為此專案自動掛載專屬裝備：{', '.join(auto_load_skills)}。\n"
                        response += "[ACTION] [給 AI 的指令]: 請主動告訴使用者，若未來想新增或移除技能，只要對你說「新增 xxx 技能」或「調整掛載」，你就會幫他處理！\n"
            except Exception as e:
                response += f"[WARNING] 讀取專案設定檔失敗: {e}\n"
        elif os.path.exists(project_file):
            response += "\n[WARNING] 【系統提示】發現這是一個舊版專案 (缺少 .ckb_config.json)。\n"
            response += "[ACTION] [給 AI 的指令]: 請你現在用親切的語氣主動詢問使用者：「點哥，我發現這是一個舊專案。請問你要趁這個機會，把它綁定 CKB-Hub 專屬裝備（例如 Netlify 或 Obsidian）嗎？」\n"
            response += "[ACTION] 若使用者回答需要，請直接呼叫 manage_project_skills(action='add') 工具幫他設定。\n"
        else:
            response += "\n[INFO] (提示: 本目錄似乎尚未初始化為專案。若要建立新專案，請使用者說「啟動專案」。)\n"

        # 讀取 PROJECT.md 提供上下文給 AI
        if os.path.exists(project_file):
            with open(project_file, 'r', encoding='utf-8') as f:
                project_content = f.read()
            
            if "開工" in command:
                response += f"\n📖 以下是目前 `PROJECT.md` 的專案進度：\n\n---\n{project_content}\n---\n"
                response += "\n[ACTION] [給 AI 的指令]: 請根據上述進度，向使用者總結目前的狀況，並提議今天的開發計畫。"
            elif "收工" in command:
                response += "\n[ACTION] [給 AI 的指令]: 請引導使用者完成收工流程：\n"
                response += "1. 幫使用者總結今天完成的事項，並更新 PROJECT.md。\n"
                response += "2. 詢問使用者是否需要呼叫 backup_to_github 備份到雲端。\n"

    return response

@mcp.tool()
def backup_to_github(commit_message: str, project_path: str = ".") -> str:
    """
    將目前的專案進度安全地備份到 GitHub。
    不需要手動下 git 指令，直接呼叫此 API 即可。
    
    Args:
        commit_message: Git commit 的訊息內容
        project_path: 專案目錄 (預設為當前目錄)
    """
    if not is_skill_enabled("github_backup"):
        return "[WARNING] 【錯誤】GitHub 自動備份尚未在 CKB-Hub 中啟用。請提醒使用者先到網頁控制台打開開關，或將其加入專案的 .ckb_config.json 中。"
    
    if not os.path.exists(os.path.join(project_path, ".git")):
        return "[WARNING] 【錯誤】此目錄尚未初始化為 Git 專案，無法備份。"
    
    try:
        # Git Add
        subprocess.run(["git", "add", "."], cwd=project_path, check=True, capture_output=True)
        
        # Git Commit
        commit_process = subprocess.run(["git", "commit", "-m", commit_message], cwd=project_path, capture_output=True, text=True)
        
        if "nothing to commit" in commit_process.stdout:
            return "[INFO] 目前沒有任何變更需要備份。"
            
        # Git Push
        push_process = subprocess.run(["git", "push"], cwd=project_path, capture_output=True, text=True)
        
        return f"[SUCCESS] GitHub 備份成功！\nCommit: {commit_message}\nPush 狀態: {push_process.stderr or push_process.stdout}"
    except subprocess.CalledProcessError as e:
        return f"⚠️ Git 操作失敗。\n錯誤訊息: {e.stderr}"
    except Exception as e:
        return f"⚠️ 發生未知的錯誤: {e}"

@mcp.tool()
def deploy_to_netlify() -> str:
    """
    一鍵部署靜態網頁到 Netlify。
    """
    if not is_skill_enabled("netlify_deploy"):
        return "⚠️ 【錯誤】Netlify 部署功能尚未在 CKB-Hub 中啟用。請提醒使用者先到網頁控制台打開開關，或將其加入專案的 .ckb_config.json 中。"
    
    return "✅ Netlify 部署準備就緒！(請呼叫 Netlify 官方 MCP 或執行 npx netlify deploy --prod)"

if __name__ == "__main__":
    # 使用 stdio 啟動 MCP 伺服器 (供 AI 編輯器串接)
    mcp.run()
