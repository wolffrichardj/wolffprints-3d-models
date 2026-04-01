import os
import re

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

data = [
  {
    "name": "link's ultrahand rings zelda tears of the kingdom",
    "url": "https://makerworld.com/en/models/210769-link-s-ultrahand-rings-zelda-tears-of-the-kingdom",
    "description": "This is a digital 3D printable model of Link's Ultrahand Rings from the game Zelda Tears of the Kingdom. The model was created by 3Demon. Props & Cosplays > Costumes. This set includes all the rings you need to complete your Link cosplay."
  },
  {
    "name": "brick plug for x1 p1 printers easy fit remix",
    "url": "https://makerworld.com/en/models/172006-brick-block-style-dust-plug-for-x1-and-p1-printers",
    "description": "If you love famous Bricks / Blocks, then you probably need this dust plug for your printer. This is an easy-fit remix by Lumpy3D of the original Brick Block Style Dust Plug. It prevents dust and debris from entering the printer's unused ports and adds a fun, aesthetic touch to your Bambu Lab printer."
  },
  {
    "name": "arrow of light w border cross over cub scouts bsa",
    "url": "https://makerworld.com/en/models/2379343-arrow-of-light-w-border-cross-over-cub-scouts-bsa",
    "description": "Arrow of Light logo with a border around it. 3D printed and glued onto a plaque for the Arrow of Light Award at Blue and Gold this year. Gives the plaque a little more color than just a laser engraved plaque. This could also be customized to add a youth's name, Pack, etc. Designed by Paul."
  },
  {
    "name": "back to the future coaster updated version",
    "url": "https://makerworld.com/en/models/1182751-back-to-the-future-coaster-updated-version",
    "description": "Back to the Future Coaster (updated version). This is an updated version of the previous Back to the Future coaster. This version has a more basic image of the DeLorean, giving a better finish with less details in the wheels. Perfect for fans of nostalgic films. Would look great in a home cinema or man cave."
  },
  {
    "name": "3rd gen tacoma center console organizer",
    "url": "https://makerworld.com/en/models/215682-3rd-gen-tacoma-center-console-organizer",
    "description": "3rd generation Toyota Tacoma center console organizer. This model is designed to fit perfectly into the center console of a 3rd gen Tacoma (2016-2023). It provides a better way to organize small items in the large console, such as coins, pens, and tools. Robust design meant for everyday use."
  },
  {
    "name": "desiccant container for bambu lab spool",
    "url": "https://makerworld.com/en/models/973318-desiccant-container-for-bambu-lab-spool",
    "description": "This Spool desiccant container is designed specifically for the Bambu Lab filament spool. It fits perfectly in the center of the spool to keep your filament dry in storage or during printing. Features an easy-to-use screw-on lid and optimized airflow holes for maximum effectiveness."
  },
  {
    "name": "mechanical counter all printed parts",
    "url": "https://makerworld.com/en/models/153170-mechanical-counter-all-printed-parts",
    "description": "A fully mechanical counter where all parts are 3D printed. No screws or bearings are needed. It can count up to 999. Features a satisfying mechanical click and is a great demonstration of 3D printed mechanisms. Ideal for manual counting tasks or as a desktop toy."
  },
  {
    "name": "slip flip slide basketball fidget toy 37 mins",
    "url": "https://makerworld.com/en/models/1759633-slip-flip-slide-basketball-fidget-toy-37-mins",
    "description": "Slip Flip Slide Basketball Fidget Toy (37 mins). SpacedOut. This is a remix of the Peanut Slide and Flip Fidget. It's a fun and addictive fidget toy that can be printed in approximately 37 minutes. Features a basketball theme and provides multiple ways to fidget through sliding and flipping."
  },
  {
    "name": "bambu x1c p1s p1p poop chute v2",
    "url": "https://makerworld.com/en/models/1107679-bambu-x1c-p1s-p2s-p1p-poop-chute-v2",
    "description": "Overview: A clean and tidy way to manage filament poops and a necessity for all P1S, P2S, X1C and P1P owners! I've designed this on bench with a balance of aesthetics, functionality, print time and filament in mind. Prints in 2-3 hours depending on profile and uses less than 90g of filament. Slide the poop chute into the printer and enjoy the tidy result."
  },
  {
    "name": "bambulab ams desiccant tray w oem lid",
    "url": "https://makerworld.com/en/models/459881-bambulab-ams-desiccant-tray-w-oem-lid",
    "description": "I made a desiccant tray that snaps with the original desiccant cover for the Bambu Lab AMS. I simply used PLA and .2mm standard settings for printing. This should fit just perfect in your ams if it's the same as mine. To install the original cover on the desiccant tray, join the part closest to you by first lining up the pimples with the holes on the tray."
  }
]

def main():
    os.chdir(REPO_ROOT)
    for item in data:
        # Some custom namings that contain quotes or distinct characters
        name_clean = item['name'].replace("'", "").replace(" ", "-")
        
        # We need to find the correct folder
        # Just use wildcard search if necessary or replace spaces
        folder = item['name'].replace(' ', '-')
        if item['name'] == "link's ultrahand rings zelda tears of the kingdom":
            folder = "link-s-ultrahand-rings-zelda-tears-of-the-kingdom"
        folder2 = folder.replace("'", "")
        folder3 = item['name'].replace("'", "").replace(" ", "-")
        
        path = None
        for cand in [folder, folder2, folder3]:
            for pre in ["verified-downloads", "remixes"]:
                test_path = f"{pre}/{cand}/README.md"
                if os.path.exists(test_path):
                    path = test_path
                    break
            if path:
                break
                
        if not path:
            print(f"File not found for {item['name']}")
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
            def desc_replacer(m):
                return m.group(1) + item["description"] + m.group(2)
            content = re.sub(
                r'(## Description\n\n).*?(\n\n## Details)',
                desc_replacer,
                content,
                flags=re.DOTALL
            )
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {item['name']}")

    # Commit
    os.system("git add . && git commit -m 'docs: apply deep links and full descriptions for batch 6 (10 models)'")

if __name__ == "__main__":
    main()
