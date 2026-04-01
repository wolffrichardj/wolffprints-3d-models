import glob, re, os

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

def main():
    os.chdir(REPO_ROOT)
    count = 0
    for f in glob.glob('verified-downloads/*/README.md') + glob.glob('remixes/*/README.md'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace the unclickable string with a markdown URL
        # from: MakerWorld — search by Model ID `US40d891ccc1c32f`
        # to:   [View on MakerWorld](https://makerworld.com/en/search/models?keyword=US40d891ccc1c32f)
        
        new_content = re.sub(
            r'MakerWorld — search by Model ID `(US[a-zA-Z0-9_]+)`',
            r'[View on MakerWorld](https://makerworld.com/en/search/models?keyword=\1)',
            content
        )
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1
            
    print(f"Updated {count} READMEs with clickable URL links.")

if __name__ == "__main__":
    main()
