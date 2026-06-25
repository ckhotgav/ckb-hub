import os
import json
import shutil
from datetime import datetime

# 路徑定義
USER_PROFILE = os.environ.get('USERPROFILE', 'C:\\Users\\user')
GEMINI_DIR = os.path.join(USER_PROFILE, '.gemini')
SKILLS_DIR = os.path.join(GEMINI_DIR, 'config', 'skills')
MCP_CONFIG_PATH = os.path.join(GEMINI_DIR, 'antigravity', 'mcp_config.json')
CKB_HUB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def backup_old_skills():
    """將舊版 Markdown 技能備份，避免與新版 MCP 衝突"""
    if not os.path.exists(SKILLS_DIR):
        print("[升級機制] 未偵測到舊版技能資料夾，跳過備份。")
        return
    
    # 檢查是否已經備份過
    backup_dir_name = f"skills_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path = os.path.join(os.path.dirname(SKILLS_DIR), backup_dir_name)
    
    # 這裡我們只針對特定舊版工具箱的名稱做備份，或是全備份
    # 為了安全與無痛升級，我們將整個 skills 資料夾改名備份，並建立一個空的 skills
    try:
        shutil.move(SKILLS_DIR, backup_path)
        os.makedirs(SKILLS_DIR, exist_ok=True)
        print(f"[升級機制] ✅ 成功將舊版技能備份至: {backup_dir_name}")
    except Exception as e:
        print(f"[升級機制] ⚠️ 備份舊版技能失敗: {e}")

def register_ckb_hub_mcp():
    """將 CKB-Hub 註冊到 mcp_config.json 中"""
    config_dir = os.path.dirname(MCP_CONFIG_PATH)
    if not os.path.exists(config_dir):
        os.makedirs(config_dir, exist_ok=True)
        
    config = {}
    if os.path.exists(MCP_CONFIG_PATH):
        try:
            with open(MCP_CONFIG_PATH, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    config = json.loads(content)
        except Exception as e:
            print(f"[升級機制] 讀取現有 mcp_config.json 失敗，將建立新檔: {e}")
            
    if "mcpServers" not in config:
        config["mcpServers"] = {}
        
    # 註冊 ckb-hub
    mcp_script_path = os.path.join(CKB_HUB_DIR, 'mcp_stdio.py').replace('\\', '/')
    
    config["mcpServers"]["ckb-hub"] = {
        "command": "python",
        "args": [mcp_script_path]
    }
    
    try:
        with open(MCP_CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        print(f"[升級機制] ✅ 成功將 CKB-Hub 註冊至 mcp_config.json")
    except Exception as e:
        print(f"[升級機制] ⚠️ 寫入 mcp_config.json 失敗: {e}")

def run_migration():
    print("==================================================")
    print(" 開始執行 CKB-Hub 無痛升級與接管程序...")
    backup_old_skills()
    register_ckb_hub_mcp()
    print(" 升級完成！舊版設定已安全清理，新版大腦已連線。")
    print("==================================================")

if __name__ == "__main__":
    run_migration()
