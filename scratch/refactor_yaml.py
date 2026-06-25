import os
import re

base_dir = "d:/ANTI 課程AI整理區/AGY-2/ckb-hub"
html_path = os.path.join(base_dir, "static/index.html")
skills_dir = os.path.join(base_dir, "skills")

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 找出所有的 Category
categories = re.split(r'<h2 class="category-title">(.*?)</h2>', html)

current_category = ""
for i in range(1, len(categories), 2):
    cat_title = categories[i].strip()
    # 我們只需要中文名稱，去除英文如 (Base Settings & Assistant)
    cat_title = re.sub(r'\s*\(.*?\)', '', cat_title)
    
    cat_content = categories[i+1]
    
    # 在這個 category block 中尋找所有的 skill-card
    cards = re.findall(r'<h3>(.*?)<div.*?<p>(.*?)</p>.*?id="(.*?)"', cat_content, re.DOTALL)
    
    for title, desc, skill_id in cards:
        # 清理字串
        title = title.strip()
        desc = desc.strip()
        skill_id = skill_id.strip()
        
        file_path = os.path.join(skills_dir, f"{skill_id}.md")
        
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 如果已經有 YAML frontmatter，就跳過
            if content.startswith("---"):
                continue
                
            yaml = f"---\nid: {skill_id}\ntitle: {title}\ndescription: {desc}\ncategory: {cat_title}\n---\n"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(yaml + content)
            print(f"Added YAML to {skill_id}.md")
        else:
            print(f"Warning: {skill_id}.md not found")

print("YAML frontmatter injection complete.")
