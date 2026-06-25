import base64
import urllib.request
import os

mermaid_code = """
graph TD
    A[初學者] -->|把資料夾丟給 AI| B[AI 助手]
    B -->|閱讀 AI_READ| C{自動安裝與升級}
    C -->|執行 migration 腳本| M[無腦自動升級 MCP]
    C -->|檢查並安裝 Python| D[啟動背景伺服器]
    D -->|產生網址| E[CKB-Hub 控制台網頁]
    
    A -->|點擊網頁開關| F[切換技能狀態]
    F -->|自動寫入| G[status.json]
    
    M -->|自動綁定接管| H[MCP 遙控器]
    H -->|讀取開關狀態| G
    H -->|動態載入 Markdown| S[skills 資料夾]
    S -->|注入神級指令| B
    B -->|自動完成工作| I[專案開發順利進行]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#69b3a2,stroke:#333,stroke-width:2px
    style G fill:#f39c12,stroke:#333,stroke-width:2px
    style H fill:#3498db,stroke:#333,stroke-width:2px
    style M fill:#e74c3c,stroke:#333,stroke-width:2px,color:#fff
    style S fill:#9b59b6,stroke:#333,stroke-width:2px,color:#fff
"""

# Mermaid Ink requires standard base64 or base64url encoding
# We'll use base64url encoding as per some mermaid live editor standards
encoded_bytes = base64.urlsafe_b64encode(mermaid_code.encode("utf-8"))
encoded_string = encoded_bytes.decode("utf-8")

url = f"https://mermaid.ink/img/{encoded_string}?bgColor=ffffff"

output_path = "d:/ANTI 課程AI整理區/AGY-2/ckb-hub/installation_flowchart.png"

try:
    print(f"Downloading from {url}")
    # Add a user agent to avoid getting blocked
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
        out_file.write(response.read())
    print(f"Successfully saved flowchart to {output_path}")
except Exception as e:
    print(f"Error: {e}")
