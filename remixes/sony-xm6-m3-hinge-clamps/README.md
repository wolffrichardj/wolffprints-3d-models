# Sony XM6 original-shape M3 bore-only prototype

Original design: **Viktor (@Viktor_2298956)**, [Sony XM6 headphone hinge repair](https://www.printables.com/model/1465791-sony-xm6-headphone-hinge-repair), **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**. M3 remix by Wolff Prints, October 18, 2026. Original Rev3 files retained in `../../verified-downloads/sony-xm6-hinge-repair/`. No endorsement implied.

## What changed

**Only the two coaxial bolt passages are enlarged from approximately 1.965 mm to 3.4 mm.** A negative cylinder follows the original bolt axis. The original curved outer body, collar opening, 2.86 mm slot, bolt location and 5.05 mm recesses are retained. No added material, enlarged tabs, blocks, bosses or whole-body scaling. Outer dimensions remain 29.5904 × 20.5144 × 8.25 mm per clamp, within STL export rounding (less than 0.00005 mm).

`clamp-m3.scad` retains the editable negative-cylinder operation. The STL and Bambu project contain its baked result so both print the same geometry. Earlier enlarged-body experiments were rejected and are not the files in this folder.

## Kit hardware — M3 × 12 mm selected

On October 18, 2026 Richard reported the result was great and selected **M3×12 mm** for the full kit. This supersedes the earlier M2, M3×10 and provisional M3×18 suggestions. **Two black M3×12 mm socket-head screws per pair, one per clamp.** The planned full bundle also includes two plain M3 nuts and four flat M3 washers; the exact installed nut/washer arrangement has not separately been documented. Assembly required; installation tools and headphones not included.

The complete original curved body and recesses are retained. The M3 shaft clearances are 3.4 mm. [Standard M3 socket heads are 5.5 mm across](https://www.accu.co.uk/metric-cap-head-screws/10638-SSC-M3-55-A2), so they do not fully recess in the original 5.05 mm pockets. Standard plain nuts are [5.5 mm across flats / 2.4 mm thick](https://www.accu.co.uk/hexagon-nuts/7888-HPN-M3-A2); [Form A M3 washers are nominally 7 mm OD](https://www.accu.co.uk/metric-flat-washers/72482-HPW-M3-A2). These are reference specifications, not measurements of Richard's hardware. The earlier M3×18 recommendation came from an unverified open-clamp stack estimate; the user's M3×12 selection is now authoritative for kit preparation.

Richard's positive result and hardware selection do not by themselves document installation on actual headphones or a load/endurance test. Before retail release, confirm the final nut/washer arrangement, stable seating, full nut engagement, headphone movement and actual packed shipment measurements. Tighten gently; do not force M3 bolts into the previous M2 prints.

## Print a prototype pair

Open `XM6_M3_Pair_Black_PETG_P1S_Prototype.3mf`: **two clamps on one plate**, one object with two closed shells. Black Generic PETG, P1S 0.4 mm nozzle, textured PEI, 0.20 mm layers, four walls, 99% cubic, five top/bottom layers, 255°C nozzle / 70°C bed. Automatic tree support on build plate enabled; this slice generated no support paths. Native Bambu 02.08.02.61 loaded and sliced the final original-shape version, **17m57s / 3.50g / 41 layers**, without a warning banner. Saved with native Save Project As. CLI slice also succeeds; result retained in `qa/`.

Single STL: 3,916 vertices / 7,836 triangles, one shell. Pair STL: 15,672 triangles, two shells. Both have zero boundary/nonmanifold edges, inconsistent-winding edges or degenerate triangles. See `qa/geometry-validation.json`. Digital checks do not validate hardware seating, clamp strength or headphone fit. **M3 pair dispatched October 18 at 17:54 CDT, black PETG AMS A2, bed leveling on and timelapse off; printer accepted and entered preparation. Richard subsequently reported a positive result and selected M3×12 hardware.** The previously dispatched M2 pair separately showed Finished, 41/41 layers, in Bambu on October 18.

Files: editable SCAD, single STL, paired STL, native paired PETG 3MF, QA records, actual CAD/native previews and SHA256SUMS. Keep unpublished until hardware and headphone testing, actual product photos and packed shipping measurements are complete. Earlier M2 listing graphics/copy must be replaced before sale.
