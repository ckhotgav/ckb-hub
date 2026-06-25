import os
import json
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="CKB-Hub 點哥AI萬用工具箱")

# 設定目錄
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
STATUS_FILE = os.path.join(BASE_DIR, "status.json")

if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

# 預設狀態
default_status = {
    "project_assistant": False,
    "github_backup": False,
    "netlify_deploy": False,
}

def load_status():
    if os.path.exists(STATUS_FILE):
        try:
            with open(STATUS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return default_status

def save_status(status_dict):
    with open(STATUS_FILE, 'w', encoding='utf-8') as f:
        json.dump(status_dict, f, indent=4)

skill_status = load_status()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    """回傳首頁 UI"""
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return HTMLResponse("<h1>找不到 index.html</h1>")

@app.get("/api/status")
async def get_status():
    """取得目前的技能啟用狀態"""
    return load_status()

@app.post("/api/toggle/{skill_id}")
async def toggle_skill(skill_id: str, enable: bool):
    """切換特定技能的狀態，並同步 MCP 設定"""
    current_status = load_status()
    if skill_id not in current_status:
        return {"status": "error", "message": "找不到該技能"}
    
    current_status[skill_id] = enable
    save_status(current_status)
    
    action = "掛載" if enable else "卸載"
    print(f"\n[系統] 正在 {action} 技能: {skill_id}")
    
    return {"status": "success", "skill_id": skill_id, "enabled": enable}

if __name__ == "__main__":
    print("==================================================")
    print(" 啟動 CKB-Hub 伺服器...")
    print(" 請在瀏覽器打開: http://127.0.0.1:8000")
    print("==================================================")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
