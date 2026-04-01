import json
import re
import time
from duckduckgo_search import DDGS

def update_readme(path, new_url, new_desc):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update URL
    if new_url:
        content = re.sub(
            r'MakerWorld — search by Model ID `[^`]+`',
            new_url,
            content
        )

    # Update Description if needed
    if new_desc:
        match = re.search(r'## Description\n\n(.*?)\n\n## Details', content, re.DOTALL)
        if match:
            content = content.replace(match.group(1), new_desc)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    try:
        with open('/tmp/models_to_fix.json', 'r') as f:
            models = json.load(f)
    except Exception as e:
        print("Error loading models JSON:", e)
        return

    ddgs = DDGS()
    
    for m in models:
        folder_clean = m['folder'].replace('-', ' ')
        query = f"{folder_clean} site:makerworld.com"
        
        print(f"Searching: {query}")
        try:
            results = ddgs.text(query, max_results=3)
            if not results:
                # Fallback broader search
                query = f"\"{folder_clean}\" makerworld"
                results = ddgs.text(query, max_results=3)
                
            results = list(results)
            
            if results:
                url = ''
                snippet = ''
                for r in results:
                    if 'makerworld.com' in r.get('href', ''):
                        url = r['href']
                        snippet = r.get('body', '')
                        break
                
                new_url = url if url else None
                new_desc = None
                
                if m.get('truncated', False) and snippet:
                    new_desc = snippet
                    
                if new_url or new_desc:
                    update_readme(m['path'], new_url, new_desc)
                    print(f"  Fixed {m['folder']} (URL: {bool(new_url)}, Desc: {bool(new_desc)})")
                else:
                    print(f"  No usable data for {m['folder']}")
            else:
                print(f"  No results for {m['folder']}")
        except Exception as e:
            print(f"  Error searching for {m['folder']}: {e}")
            
        time.sleep(1.5)

if __name__ == "__main__":
    main()
