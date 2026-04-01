import json
import os
import re

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

data = [
  {
    "name": "delorean dmc wall art silhouette",
    "url": "https://makerworld.com/en/models/1739068-delorean-dmc-wall-art-silhouette",
    "description": "DeLorean DMC can be resized or mirrored for opposite direction. Have it sized currently to fit on all printbeds including a mini. Boost Me (for free)."
  },
  {
    "name": "bambu lab p1s x1 x1c door handle bed scraper",
    "url": "https://makerworld.com/en/models/511342-bambu-lab-p1s-x1-x1c-door-handle-bed-scraper",
    "description": "Simple but effective bed scraper that will fit on the door handle of your Bambu Lab X1C, X1 or P1S. Included is a profile for common scrapers and also a profile with a 0.2mm tolerance for those with calibrated printers. Enjoy!"
  },
  {
    "name": "perfect filament clip",
    "url": "https://makerworld.com/en/models/258522-the-perfect-filament-clip",
    "description": "Finding a filament clip should be easy for such a small piece of plastic. I have tried many over the years and this is my favorite. I even created a color code and storage tray for them. Thanks."
  },
  {
    "name": "hat hanger",
    "url": "https://makerworld.com/en/models/30044-hat-hanger",
    "description": "Simple hat hanger that can be mounted with a single screw or command strip. Designed for baseball caps."
  },
  {
    "name": "photo booth simple japanese",
    "url": "https://makerworld.com/en/models/1527169-simple-photography-booth-no-support-needed",
    "description": "This simple photography booth is a compact studio enabling anyone to effortlessly capture high-quality images. Compact for storage and assembled in mere minutes. It is also designed to be printed with almost no support, so it's easy to make. I've designed it to be used with a standard LED light strip (optional)."
  },
  {
    "name": "mini banana buddy",
    "url": "https://makerworld.com/en/models/1124459-mini-banana-buddy",
    "description": ""
  },
  {
    "name": "collapsible tpu bottle 600ml",
    "url": "https://makerworld.com/en/models/1660671-collapsible-tpu-bottle-600ml",
    "description": ""
  },
  {
    "name": "pinewood derby axle alignment guide jig v2",
    "url": "https://makerworld.com/en/models/151323",
    "description": ""
  },
  {
    "name": "crocodile bag clip with lock print in place",
    "url": "https://makerworld.com/en/models/1163143",
    "description": ""
  },
  {
    "name": "pinewood derby inspection box",
    "url": "https://makerworld.com/en/models/203403",
    "description": ""
  }
]

def main():
    os.chdir(REPO_ROOT)
    for item in data:
        folder = item['name'].replace(' ', '-')
        
        # Determine the file path
        path = f"verified-downloads/{folder}/README.md"
        if not os.path.exists(path):
            path = f"remixes/{folder}/README.md"
            if not os.path.exists(path):
                print(f"File not found for {folder}")
                continue
                
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the published URL to include the deep link
        # Before: [Search on MakerWorld](https://makerworld.com/en/search/models?keyword=...) 
        # Or before: MakerWorld — search by Model ID `US...`
        
        # We replace the entire line for Published URL, since now we want ultimate flexibility!
        # The user requested: You could even include the url via search and then the url va the deep link once we find it for ultimate flexibility
        
        def url_replacer(match):
            existing = match.group(1) # existing link or string
            return f"Published URL | {existing}<br>Deep Link: [{item['url']}]({item['url']})"

        content = re.sub(
            r'Published URL\s*\|\s*(.*)',
            url_replacer,
            content,
            count=1
        )
        
        # Update description if it is missing
        if item['description']:
            # Replace whatever is between ## Description and ## Details
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
