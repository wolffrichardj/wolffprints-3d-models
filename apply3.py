import os
import re

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

data = [
  {
    "name": "heart",
    "url": "https://makerworld.com/en/models/1517865-organic-heart",
    "description": "A very realistic organic heart, designed for medical classes. Highly detailed and accurate representation of human anatomy, suitable for educational purposes and detailed 3D printing."
  },
  {
    "name": "pinewood derby car",
    "url": "https://makerworld.com/en/models/1051515-pinewood-derby-car",
    "description": "Standard pinewood derby car design, optimized for 3D printing. Compatible with official Boy Scouts of America (BSA) pinewood derby rules, featuring proper axle spacing and weight distribution."
  },
  {
    "name": "century script",
    "url": "https://makerworld.com/en/models/2591781-customizable-3d-font-century-gothic",
    "description": "Customizable 3D font set based on the Century Gothic/Script family. Ideal for creating custom signs, nameplates, and decorative text projects. Each letter is individually crafted for clarity and ease of printing."
  },
  {
    "name": "pinewood derby car tray",
    "url": "https://makerworld.com/en/models/1521889-pinewood-derby-car-tray",
    "description": "Functional tray designed to hold a pinewood derby car during assembly and painting. Features specialized slots for wheels and body placement to prevent damage and keep the workspace organized."
  },
  {
    "name": "not my circus not my monkey 2 funny sign",
    "url": "https://makerworld.com/en/models/1123139-not-my-monkey-not-my-circus-sign",
    "description": "A humorous sign expressing the classic sentiment 'Not my circus, not my monkey'. Designed for office environments or as a fun gift. Part of a series of 'funny signs' for coworkers meant to express passive-aggressive thoughts."
  },
  {
    "name": "universal stand",
    "url": "https://makerworld.com/en/models/710009-universal-stand",
    "description": "Compact and versatile stand suitable for mobile phones, small tablets, or photos. Features a 13.5mm wide slot designed for stability across various devices and streamlined aesthetics."
  },
  {
    "name": "wire stripper",
    "url": "https://makerworld.com/en/models/2025355-wago-compact-wire-stripper",
    "description": "Compact and efficient wire stripping tool designed for WAGO connectors and general electrical work. Ergonomic design for easy handling and precise stripping of common wire gauges."
  },
  {
    "name": "porsche 914 gt",
    "url": "https://makerworld.com/en/models/1810087-porsche-914gt",
    "description": "Detailed silhouette of the classic Porsche 914GT. Perfect for wall art or desk display. Captures the iconic lines of the vehicle in a minimalist and stylish format designed by yakup29."
  },
  {
    "name": "cute bald eagle articulated",
    "url": "https://makerworld.com/en/models/1806795-cute-bald-eagle-articulated",
    "description": "Articulated, print-in-place bald eagle model. Needs no supports. Features realistic wing movement and high detail, making it a great specimen for multi-color printing or display. 3MF Multicolor file available."
  },
  {
    "name": "universal stand 3 v0",
    "url": "https://makerworld.com/en/models/2052163-universal-stand-3-0",
    "description": "Ideal presentation base for car silhouettes and similar decorative vehicle contours. Version 3.0 offers improved stability and a modern aesthetic, perfectly showcasing any vehicle design or silhouette with customizable text parameters."
  }
]

def main():
    os.chdir(REPO_ROOT)
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

    # Commit
    os.system("git add . && git commit -m 'docs: apply deep links and full descriptions for batch 3 (10 models)'")

if __name__ == "__main__":
    main()
