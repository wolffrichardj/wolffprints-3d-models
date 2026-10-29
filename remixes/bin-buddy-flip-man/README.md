# Bin Buddy Flip Man

A smiling, waving little trash worker replaces the plain upper indicator paddle. The smaller handle collar and the long lid-contact arm are retained from Richard's Bindicator model.

For the later rounder characters with the large plain paddle removed, see [Bin Buddies v2](../bin-buddy-flip-man-v2/README.md).

![Gray CAD preview](images/Flip_Man_Preview.png)

## Origin and license

- Mechanical donor: [Bindicator by user_1770727599](https://makerworld.com/en/models/2889779-bindicator), downloaded 2026-10-27 and retained in `source/Bindicator_Original_Geometry.stl`.
- Mechanical donor license and this remix: [Creative Commons Attribution-NonCommercial 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
- Visual reference requested by Richard: the waving human indicator in [this Instagram reel](https://www.instagram.com/reel/De3QnJYx-w1/), linked there to [Ready Eddie](https://www.amazon.com/dp/B0H4RVDFK6).
- Character: original rounded worker silhouette with hard hat, vest details, mitten, boots, and engraved smile. Created for this personal remix.
- Local design date: 2026-10-27.

## What changed

- Removed the plain upper paddle above source Y=18.5 mm and joined the figure's two boots to the retained root.
- Added a 2.8 mm thick figure, approximately 35 mm wide and 63 mm tall above its boots. Shallow face and vest details appear on both sides.
- Kept the original collar, its opening, and the complete long lid-contact arm. Richard reported the original-size fit coupon was a perfect fit on the household bin.
- Kept the original 35 mm collar width. The earlier coupon was 6 mm wide; the full-width part and the character's pickup behavior remain to be checked physically.
- Rounded the limb joints and used a mitten silhouette for the waving hand.

## Current print project

Open **`sliced/Flip_Man_P1S_PETG.3mf`** in Bambu Studio. It contains one complete, connected part and its sliced G-code.

- Printer: Bambu Lab P1S, 0.4 mm nozzle, Standard 100%.
- Material: one Generic PETG filament, gray project color. Confirm the live AMS slot before sending; the previous project used gray PETG in A1.
- Layer height: 0.20 mm, 175 layers.
- Walls/infill: four walls, 5% gyroid.
- Temperatures: 255 C nozzle, 70 C Textured PEI bed.
- Maximum volumetric flow: 8 mm3/s.
- Supports: organic/tree supports on the build plate for the head and raised arm; 0.24 mm top gap, two interface layers, 0.4 mm interface spacing.
- Brim: automatic, 5 mm.
- Final estimate: **1h43m03s total, 30.85 g PETG**, including supports and startup.
- Overall STL bounds in print orientation: approximately **103 x 122.7 x 35 mm**.

Use the supplied print orientation. The CAD preview rotates the model upright to show the character; it is a rendering of the final STL, not a photo or a physical pickup test.

## Checks completed

- The final STL is watertight, with one connected component, no non-manifold edges, and no degenerate triangles.
- An OpenSCAD symmetric-difference check was empty below source Y=14.9 mm. That region includes the complete handle collar and long lid-contact arm, proving those solids are unchanged in the CAD construction.
- Uniform-solid mass analysis estimates a 3.2 degree change in the balance direction around the assumed handle axis compared with the original. This informed the figure thickness. Actual sliced infill, friction, the installed handle, and lid motion can change the result.
- Bambu Studio 02.08.02.61 slice succeeded with return code 0 and no model/plate warnings.
- The exported 3MF archive and embedded PETG settings were checked.

## After printing

1. Let the part cool. Remove supports from around the head and arm carefully, and clear the brim from the collar.
2. Check that the full-width clip rotates freely around the handle without forcing it.
3. Set the indicator on the bin, open the lid, and simulate a pickup. Confirm that the figure flips, stays captured, and clears the lid and handle ribs.

**Status:** modeled, rendered, and sliced for review. No new print was dispatched for this remix. The full character's fit and flip behavior have not been physically verified.

## Files

- `Flip_Man.scad`: editable source. Default `mode="model"` exports the printable geometry.
- `Flip_Man.stl`: complete printable mesh.
- `Flip_Man_P1S_PETG_Prepared.3mf`: editable prepared project.
- `sliced/Flip_Man_P1S_PETG.3mf`: sliced Bambu project.
- `source/`: attributed donor geometry.
- `images/`: final STL preview, OpenSCAD render, figure outline, and slicer model preview.
- `validation/`: mesh/balance analysis and CAD-check logs.
- `sliced/result.json`: final slicing result.

To rebuild the STL with OpenSCAD:

```sh
openscad --export-format binstl -o Flip_Man.stl Flip_Man.scad
```

The preservation check intentionally produces an empty object:

```sh
openscad -D 'mode="preservation_check"' -o protected-region-difference.stl Flip_Man.scad
```

For this check, `Current top level object is empty.` and no exported STL are the expected result.

Loose G-code is omitted from the repository; it is embedded in each sliced 3MF.
