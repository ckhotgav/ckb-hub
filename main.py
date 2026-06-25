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

import re

def get_skills_metadata():
    """從 skills/ 資料夾中自動掃描所有 Markdown 檔案的 YAML 身分證"""
    skills_dir = os.path.join(BASE_DIR, "skills")
    skills = []
    if not os.path.exists(skills_dir):
        return skills
        
    for filename in os.listdir(skills_dir):
        if filename.endswith(".md") and filename != "SKILL_TEMPLATE.md":
            filepath = os.path.join(skills_dir, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # 使用正則表達式解析 YAML Frontmatter
                match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
                if match:
                    yaml_content = match.group(1)
                    skill_data = {}
                    for line in yaml_content.split("\n"):
                        if ":" in line:
                            k, v = line.split(":", 1)
                            skill_data[k.strip()] = v.strip()
                    
                    # 確認身分證格式完整
                    if "id" in skill_data and "title" in skill_data:
                        skills.append(skill_data)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return skills

def load_status():
    """讀取技能開關狀態，若沒有紀錄則預設為 False"""
    status = {}
    if os.path.exists(STATUS_FILE):
        try:
            with open(STATUS_FILE, 'r', encoding='utf-8') as f:
                status = json.load(f)
        except:
            pass
            
    # 確保所有掃描到的技能都有預設狀態
    for skill in get_skills_metadata():
        skill_id = skill["id"]
        if skill_id not in status:
            status[skill_id] = False
    return status

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

@app.get("/api/skills")
async def api_get_skills():
    """取得全自動外掛系統掃描到的所有技能型錄"""
    return get_skills_metadata()

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

import asyncio

@app.post("/api/shutdown")
async def shutdown_server():
    """關閉伺服器與網頁"""
    print("\n[系統] 收到關閉指令，CKB-Hub 伺服器將在 1 秒後關閉...")
    
    async def commit_suicide():
        await asyncio.sleep(1)
        import platform
        import signal
        parent_pid = os.getppid()
        if platform.system() == "Windows":
            os.system(f"taskkill /F /PID {parent_pid} /T")
        else:
            os.kill(parent_pid, signal.SIGTERM)
        os._exit(0)
        
    asyncio.create_task(commit_suicide())
    return {"status": "success", "message": "伺服器即將關閉"}

if __name__ == "__main__":
    print("==================================================")
    print(" 啟動 CKB-Hub 伺服器...")
    print(" 請在瀏覽器打開: http://127.0.0.1:8000")
    print("==================================================")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
