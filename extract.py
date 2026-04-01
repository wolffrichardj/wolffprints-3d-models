#!/usr/bin/env python3
import glob, re, json, os

results = []
for f in glob.glob('verified-downloads/*/README.md'):
    with open(f) as file:
        t = file.read()
        match = re.search(r'## Description\n\n(.*?)\n\n## Details', t, re.DOTALL)
        if match:
            desc = match.group(1).strip()
            folder = f.split('/')[-2]
            
            # Find the maker id
            id_match = re.search(r'Model ID `(US[a-zA-Z0-9_]+)`', t)
            maker_id = id_match.group(1) if id_match else ''
            
            if desc.endswith('...'):
                results.append({'path': f, 'folder': folder, 'id': maker_id, 'truncated': True})
            else:
                # Also collect non-truncated ones that still have the bad URL format
                url_match = re.search(r'MakerWorld — search by Model ID `US', t)
                if url_match:
                    results.append({'path': f, 'folder': folder, 'id': maker_id, 'truncated': False})

with open('/tmp/models_to_fix.json', 'w') as out:
    json.dump(results, out)
    
print(f"Found {len(results)} models that need fixing.")
