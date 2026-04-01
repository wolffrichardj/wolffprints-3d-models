import os
import re

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

data = [
  {
    "name": "ice cream chapstick holder keychain",
    "url": "https://makerworld.com/en/models/1081541-ice-cream-chapstick-holder-keychain",
    "description": "Ice cream cone style keychain for holding ChapStick or lip balm. Works great on lanyards as well. Now with two cone designs. Update 4/9/25: New plate has been added to the print profile that includes a new ice cream STL. The original is still included. Supports are no longer needed for this one as I have tapered the overhang inside the ice cream. Update 5/4/25: New ice cream swirl design has been added. This will work with existing cones."
  },
  {
    "name": "steering blocks for traxxas rustler",
    "url": "https://makerworld.com/en/models/870482-traxxas-rustler-steering-blocks",
    "description": "This is a steering block I remixed from Sidpatchy's model. I made the piece that attaches to the steering assembly a little bit thicker to make it more durable. Compatibility: Traxxas Bandit, Traxxas Drag Slash, Traxxas Nitro Slash, Traxxas Rustler 2wd, Traxxas Slash 2wd, Traxxas Stampede 2wd. Make sure to follow us so you get notified when we upload a new model!"
  },
  {
    "name": "zelda tissue box",
    "url": "https://makerworld.com/en/models/1166233-zelda-tissue-box",
    "description": "Zelda Monster Chest Tissue Box: This highly detailed model is styled after the monster chests found in Breath of the Wild. Features: Includes a hidden 'key' in the base that illuminates LED lights in the chest's eyes. Capacity: Designed for tissues roughly 150mm x 100mm. Required Hardware: Requires specific springs, an M2 nut/screw, magnets, and 10.6mm magnetic LED lights. Compatibility: Can be printed on a Bambu Lab A1 mini."
  },
  {
    "name": "kingroon silica gel holder",
    "url": "https://makerworld.com/en/models/473741-kingroon-spool-dry-cap-lids-silicagel-dry-box",
    "description": "Kingroon spool dry cap / lids silicagel dry box. Print two lids (cap) and you have a cheap dry box for Kingroon spool. This is a remix of 3Dcrabi's design. It allows you to keep your filament dry while stored on the spool. Compatible with Bambu Lab AMS units."
  },
  {
    "name": "mini us state license plate key tags customizable",
    "url": "https://makerworld.com/en/models/445898-mini-us-state-license-plate-key-tags-customizable",
    "description": "Customize your own US State License Plate Keychain Tags! This model is fully compatible with the Bambu Lab Customizer. Choose your state, enter your text, and create realistic miniature license plate key tags. More states and styles will be added as requested. If your favorite state is not there, leave a comment!"
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

if __name__ == "__main__":
    main()
