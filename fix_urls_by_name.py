import glob, re, os

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

def main():
    os.chdir(REPO_ROOT)
    count = 0
    for f in glob.glob('verified-downloads/*/README.md') + glob.glob('remixes/*/README.md'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        folder_name = f.split('/')[-2]
        keyword = folder_name.replace('-', '+')
        
        # Replace the `keyword=US...` URL with one that searches by the actual name
        # from: [View on MakerWorld](https://makerworld.com/en/search/models?keyword=US123)
        # to:   [Search on MakerWorld](https://makerworld.com/en/search/models?keyword=mini+banana+buddy)
        
        new_content = re.sub(
            r'\[View on MakerWorld\]\(https://makerworld.com/en/search/models\?keyword=US[a-zA-Z0-9_]+\)',
            f'[Search on MakerWorld](https://makerworld.com/en/search/models?keyword={keyword})',
            content
        )
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1
            
    print(f"Updated {count} READMEs to search MakerWorld by model name instead of broken US ID.")

if __name__ == "__main__":
    main()
