import os
import re

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

data = [
  {
    "name": "ams hygrometer simple mounting base",
    "url": "https://makerworld.com/en/models/203403-simple-temperature-hygrometer-holder",
    "description": "Simple standing hygrometer mount which fits inside the AMS in between the feeders. Fits for the standard round hygrometers you get everywhere (aliexpress, amazon, …)."
  },
  {
    "name": "low poly fox",
    "url": "https://makerworld.com/en/models/63396-low-poly-fox",
    "description": "Low poly fox model, printed without supports. Original design by mcgybeer. A simple yet elegant articulated fox sculpture."
  },
  {
    "name": "ender 3 s1 pro cable holder ribbon cable mount",
    "url": "https://makerworld.com/en/models/503497-ender-3-sprite-pro-cable-holder",
    "description": "Simple cable holder for the Sprite ribbon cable. Mounted at the old bowden extruder motor location. Ender 3 S1 Pro hotend cable holder designed to prevent cable strain and snagging."
  },
  {
    "name": "articulated lizard v2",
    "url": "https://makerworld.com/en/models/13862-articulated-lizard-v2",
    "description": "Just like the v1, no supports or assembly required. Just slice and print! This is the official v2 version by mcgybeer featuring improved joints and durability."
  },
  {
    "name": "b 17 flying fortress kit card",
    "url": "https://makerworld.com/en/models/1634582-b-17-flying-fortress-plane-kit-card",
    "description": "Print, build, and honor one of the most famous bombers in aviation history! All four propellers spin, just like on the real aircraft – perfect for display or play. Designed by Nakozen."
  },
  {
    "name": "bambu lab a1 mini poop bin",
    "url": "https://makerworld.com/en/models/719278",
    "description": "Bambu Lab A1 Mini Poop Bin. Perfectly fitting for the A1M. Designed to catch purge material efficiently. Boosts are appreciated!"
  },
  {
    "name": "articulated dragon",
    "url": "https://makerworld.com/en/models/19316-articulated-dragon",
    "description": "My best design so far (at least my favourite one). Fully articulated and printed in one piece, obviously without supports. Design by mcgybeer."
  },
  {
    "name": "edc friendly lightweight utility knife ii",
    "url": "https://makerworld.com/en/models/1403670-edc-friendly-lightweight-utility-knife-ii",
    "description": "A simple, lightweight, and compact utility knife that uses standard utility blades. Designed for EDC and light duty tasks by Trent Studio."
  },
  {
    "name": "bambu lab ams dry box desiccant",
    "url": "https://makerworld.com/en/models/1508459-ams-dry-box-desiccant-box",
    "description": "The AMS Dry Box is designed to provide optimal ventilation with all six sides featuring breathable grids. The box is printed flat for easy assembly and fits perfectly in the AMS."
  },
  {
    "name": "lucky 13 printable jointed figure",
    "url": "https://makerworld.com/en/models/183755-lucky-13-printable-jointed-figure",
    "description": "Lucky 13 is a fully printable and jointed figure. This is the official version of the popular articulated action figure designed by Soozafone."
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
    os.system("git add . && git commit -m 'docs: apply deep links and full descriptions for batch 4 (10 models)'")

if __name__ == "__main__":
    main()
