import os
import re

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

data = [
  {
    "name": "simple display stand parametric fully customizable",
    "url": "https://makerworld.com/en/models/479988-simple-display-stand-parametric-fully-customizable",
    "description": "This parametric, fully customizable display stand is designed for 3D printing to hold items like photos, cards, books, or Hueforges. It allows full customization of height, length, width, and angles (backing/legs) via OpenSCAD or MakerLab's Parametric Model Maker for a perfect fit. Key features include customizable parameters for scaling from small coin stands to larger tablet displays, high stability design optimized for printing flat, and functional versatility for various display needs."
  },
  {
    "name": "gridfinity coin and bullion storage",
    "url": "https://makerworld.com/en/models/1289077-gridfinity-coin-and-bullion-storage",
    "description": "Gridfinity Coin and Bullion Storage provides modular, 3D-printable, stackable containers designed for organizing coins and bullion within the Gridfinity system. These storage solutions typically offer horizontal tray-style storage for viewing coins or vertical tubes to securely store rolls. Key features include a modular design that fits gridfinity standards, specific formats for items like 1oz silver coins or US coin rolls, labeling options for denominations, and magnet-ready bases for secure stacking."
  },
  {
    "name": "p1s prick plug",
    "url": "https://makerworld.com/en/models/501481-p1s-prick-plug",
    "description": "The P1S Prick Plug is a specialized 3D printing accessory designed for the Bambu Lab P1S printer. It serves as a protective or functional plug for specific openings in the printer's frame or purge area, preventing debris buildup or improving air management. The design is optimized for a precise friction fit and is easy to print without supports."
  },
  {
    "name": "articulated snowy axolotl",
    "url": "https://makerworld.com/en/models/1970117-snowy-axolotl-flexi",
    "description": "The Snowy Axolotl Flexi is a highly detailed, articulated 3D model of an axolotl featuring a 'snowy' or winter-themed texture. This model is designed for print-in-place functionality, meaning no assembly is required after printing. It features multiple joints for lifelike movement and is optimized for high-quality aesthetic results with either single or multi-color 3D printing."
  },
  {
    "name": "cross bookmark",
    "url": "https://makerworld.com/en/models/1586137-cross-bookmark",
    "description": "The Cross Bookmark is a simple, elegant 3D-printable model designed for use in books, bibles, or journals. Its thin, flat profile ensures it does not damage book bindings while remaining securely in place. It is an ideal quick-print project for gifts or personal use, often customized with different colors or textures to suit individual preferences."
  },
  {
    "name": "pinewood derby car tray v2",
    "url": "https://makerworld.com/en/models/1521889-pinewood-derby-car-tray",
    "description": "The Pinewood Derby Car Tray is a functional storage and display solution for Pinewood Derby cars. Version 2 improves upon the original with better structural support and recesses for wheels, ensuring the car remains stable and the axles are protected from pressure during transport. It is a must-have for scouts and hobbyists looking to keep their cars in peak condition between races."
  },
  {
    "name": "miniature baby bottle",
    "url": "https://makerworld.com/en/models/120680-miniature-baby-bottle",
    "description": "This miniature baby bottle is a detailed, small-scale model designed for dollhouses, dioramas, or as a decorative item. The model features a multi-part design that allows for printing the bottle, cap, and nipple in different colors for a realistic look. It is scaled precisely for common miniature standards (e.g., 1:12) but can be easily resized as needed."
  },
  {
    "name": "pinewood derby axle alignment guide jig",
    "url": "https://makerworld.com/en/models/1218521-pinewood-derby-axle-alignment-tool",
    "description": "The Pinewood Derby Axle Alignment Tool is a precision jig designed to ensure that car axles are perfectly straight and parallel. This is critical for reducing friction and ensuring the car tracks straight down the lane. The tool features slots and guides for standard axle diameters and helps in both the insertion and adjustment of axles."
  },
  {
    "name": "universal cardboard spool adapter ring",
    "url": "https://makerworld.com/en/models/1187157-universal-cardboard-spool-adapter-ring",
    "description": "The Universal Cardboard Spool Adapter Ring is a utility model designed to make cardboard filament spools compatible with various AMS (Automatic Material System) units or spool holders. It snaps onto the rim of cardboard spools to provide a smoother rolling surface and prevent cardboard dust from entering sensitive components. The 'universal' design includes multiple variations or a flexible geometry to fit different spool brands."
  },
  {
    "name": "locking pocket knife with frame lock v3592691",
    "url": "https://makerworld.com/en/models/1711046-pocket-folding-knife-fidget-frame-lock",
    "description": "The Pocket Folding Knife Fidget with Frame Lock is a safe, 3D-printed interpretation of a classic folding knife mechanism. It utilizes a functional frame lock to keep the 'blade' in the open position and provides a satisfying tactile experience for fidgeting. Optimized for fast printing with minimal material (approx. 20g), it requires no supports and is designed for smooth, reliable action."
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
    os.system("git add . && git commit -m 'docs: apply deep links and full descriptions for batch 5 (10 models)'")

if __name__ == "__main__":
    main()
