import json
import os
import re
import sys

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

def main():
    if len(sys.argv) < 2:
        print("Usage: python apply_json.py <path_to_json>")
        return
        
    os.chdir(REPO_ROOT)
    
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)
        
    for item in data:
        folder = item['name'].replace(' ', '-')
        
        path = f"verified-downloads/{folder}/README.md"
        if not os.path.exists(path):
            path = f"remixes/{folder}/README.md"
            if not os.path.exists(path):
                print(f"File not found for {folder}")
                continue
                
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        def url_replacer(match):
            existing = match.group(1) 
            if 'Deep Link:' in existing:
                return f"Published URL | {existing}"
            return f"Published URL | {existing}<br>Deep Link: [{item['url']}]({item['url']})"

        content = re.sub(
            r'Published URL\s*\|\s*(.*)',
            url_replacer,
            content,
            count=1
        )
        
        if item['description']:
            content = re.sub(
                r'(## Description\n\n).*?(\n\n## Details)',
                rf'\1{item["description"]}\2',
                content,
                flags=re.DOTALL
            )
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {folder}")

if __name__ == "__main__":
    main()
