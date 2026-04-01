import os
import re

REPO_ROOT = "/Users/richardwolff/Code/wolffprints-3d-models"

data = [
  {
    "name": "keychain container pill storage bottle",
    "url": "https://makerworld.com/en/models/155504-keychain-container-pill-storage-bottle",
    "description": "A handy little container with a threaded cap. I personally use mine for my medication for ease of use when I'm out, or as a backup in case I forget them at home, its came in perfect and handy when I've been away from home. Of course you can store and carry whatever you like. It can be resized, just make sure to resize both parts the same!"
  },
  {
    "name": "scouts knots hitches and bend reference card",
    "url": "https://makerworld.com/en/models/1380685-scouts-knots-hitches-and-bend-reference-card",
    "description": "Print this reference card and clip it to your gear when you need a quick reference while you are scouting or exploring the wilderness with a rope. There are 7 common knots: Bowline Knot (Secure Loop, easy to undo), Clove Hitch (Tie to a post, adjustable and secure), Square Knot (Reef Knot, join two ropes of equal thickness), Taut-Line Hitch (Adjustable loop for lines under tension), Two Half-Hitches (Secure a rope to a post), Sheet Bend (Join ropes of different thickness), and Figure-Eight Knot (Stopper knot, easy to identify)."
  },
  {
    "name": "link ultrahand rings little finger",
    "url": "https://makerworld.com/en/models/210769-link-s-ultrahand-rings-zelda-tears-of-the-kingdom",
    "description": "This is a digital 3D printable model of Link's Ultrahand Rings from the game, Legend of Zelda: Tears of the Kingdom. The download contains pieces of the model ready to be 3D printed on a 200 mm print bed. Includes files for the thumb, index finger, middle finger, and pinky (14.5 mm diameter)."
  },
  {
    "name": "rc car clip pull tab",
    "url": "https://makerworld.com/en/models/2213382-rc-car-body-shell-clip-pull-tabs",
    "description": "RC Car Body Clip Pull Tabs - Easy‑Print, Glove‑Friendly Design. This simple, reliable pull‑tab is designed to attach to the standard metal body clips used on most RC shells. On cold days—or anytime you're wearing gloves—those tiny clips can be a real pain to remove. These pull tabs give you a solid grip and make body removal quick and effortless."
  },
  {
    "name": "crochet hooks needles h kelnadel size 2 5 v5",
    "url": "https://makerworld.com/en/models/669915-crochet-hooks-needles-size-2-5-5",
    "description": "Crochet hooks / needles in various sizes. This model covers sizes from 2.5 to 5.0. Designed for easy printing and comfortable use. Perfect for knitting and crochet projects."
  },
  {
    "name": "ams dry kit full hygrometer reading area",
    "url": "https://makerworld.com/en/models/149506-ams-dry-kit-full-hygrometer-reading-area",
    "description": "Full silica dry pod kit for AMS. Designed with a hygrometer hole that goes through the middle pod, creating an empty area for the sensor. This ensures hygrometer readings are not distorted by silica too close to the sensor."
  },
  {
    "name": "crock pot replacement foot",
    "url": "https://makerworld.com/en/models/408401",
    "description": "Replacement rubber foot for a Crock-Pot brand slow cooker (specifically model #: CPSCVTS70LL-S). May fit other models. It requires some effort to push into the foot hole; twisting while pushing is recommended for a snug fit."
  },
  {
    "name": "edc friendly lightweight utility knife ii v2",
    "url": "https://makerworld.com/en/models/1403670-edc-friendly-lightweight-utility-knife-ii",
    "description": "Redesigned version for better internal structure and assembly. Features audible 'click' feedback during deployment, controllable resistance, and compatibility with various T-shaped blades. Designed for easy printing without glue or hardware."
  },
  {
    "name": "mini us state license plate key tags customizable v2",
    "url": "https://makerworld.com/en/models/230182-mini-us-state-license-plate-key-tags-customizable",
    "description": "Customizable license plate key tags for all 50 US states. You can customize the name, state, and color using the MakerWorld Customizer. Perfect for personalized gifts or identifying keys."
  },
  {
    "name": "pinewood derby license plates",
    "url": "https://makerworld.com/en/models/1085554-pinewood-derby-license-plates",
    "description": "Quick to-scale license plate models. Provided are two full-size plates (one generic and one '1st Place') for photo booths, along with smaller versions designed specifically for Pinewood Derby cars."
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
        folder2 = folder.replace("'", "")
        folder3 = item['name'].replace("'", "").replace(" ", "-")
        
        # handle crochet specifically because it has 2-5-v5
        if "crochet" in folder:
            folder = "crochet-hooks-needles-h-kelnadel-size-2-5-v5"
            folder2 = folder
            folder3 = folder
            
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
    os.system("git add . && git commit -m 'docs: apply deep links and full descriptions for batch 7 (10 models)'")

if __name__ == "__main__":
    main()
