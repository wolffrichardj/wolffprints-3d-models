# Sony XM6 original-shape M3 bore-only prototype

Original design: **Viktor (@Viktor_2298956)**, [Sony XM6 headphone hinge repair](https://www.printables.com/model/1465791-sony-xm6-headphone-hinge-repair), **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**. M3 remix by Wolff Prints, October 18, 2026. Original Rev3 files retained in `../../verified-downloads/sony-xm6-hinge-repair/`. No endorsement implied.

## What changed

**Only the two coaxial bolt passages are enlarged from approximately 1.965 mm to 3.4 mm.** A negative cylinder follows the original bolt axis. The original curved outer body, collar opening, 2.86 mm slot, bolt location and 5.05 mm recesses are retained. No added material, enlarged tabs, blocks, bosses or whole-body scaling. Outer dimensions remain 29.5904 × 20.5144 × 8.25 mm per clamp, within STL export rounding (less than 0.00005 mm).

`clamp-m3.scad` retains the editable negative-cylinder operation. The STL and Bambu project contain its baked result so both print the same geometry. Earlier enlarged-body experiments were rejected and are not the files in this folder.

## Hardware trial, not a validated retail kit

Richard's photo shows M3 socket-head kits with plain nuts, flat washers and short screws including 16, 18 and 20 mm. Earlier M2-stock and M3×10 recessed-kit assumptions are superseded.

**The standard M3 socket head and nut do not fit inside the original 5.05 mm recesses.** The minimal-body prototype instead needs a trial with head and nut outside, with flat washers spanning the recesses. Start with **one M3×18 screw, two flat M3 washers and one plain M3 nut per clamp**; use the shortest stocked screw that fully engages the nut and leaves a small visible thread beyond it at the installed clamp position. Two clamps therefore need two screws, four flat washers and two nuts. Do not use split lock washers against PETG. Do not force M3 bolts into the previous M2 prints.

Nominal reference dimensions: [M3 socket cap head 5.5 mm](https://www.accu.co.uk/metric-cap-head-screws/10638-SSC-M3-55-A2), [plain M3 nut 5.5 mm across flats / 2.4 mm thick](https://www.accu.co.uk/hexagon-nuts/7888-HPN-M3-A2), [M3 Form A washer 7 mm OD / 0.55 mm thick](https://www.accu.co.uk/metric-flat-washers/72482-HPW-M3-A2). These describe standard hardware, not measurements of Richard's actual kit. Approximate sampled contact span for 7 mm washers is 12.382 mm; assumed washer/nut stack gives about 2.1 mm of thread beyond an 18 mm screw before any clamp closure. This is an estimate, not verified seating.

**Acceptance requires a hand test:** shaft slides freely, washers seat stably rather than rocking or cutting into curved PETG, nut fully engages, and hardware clears the headphones throughout adjustment/folding. Tighten gently; do not use screw force to correct poor fit. If washers cannot seat stably, stop and revise the recesses locally. Load/endurance and headphone fit remain untested. Assembly required; no tools are promised in a retail kit.

## Print a prototype pair

Open `XM6_M3_Pair_Black_PETG_P1S_Prototype.3mf`: **two clamps on one plate**, one object with two closed shells. Black Generic PETG, P1S 0.4 mm nozzle, textured PEI, 0.20 mm layers, four walls, 99% cubic, five top/bottom layers, 255°C nozzle / 70°C bed. Automatic tree support on build plate enabled; this slice generated no support paths. Native Bambu 02.08.02.61 loaded and sliced the final original-shape version, **17m57s / 3.50g / 41 layers**, without a warning banner. Saved with native Save Project As. CLI slice also succeeds; result retained in `qa/`.

Single STL: 3,916 vertices / 7,836 triangles, one shell. Pair STL: 15,672 triangles, two shells. Both have zero boundary/nonmanifold edges, inconsistent-winding edges or degenerate triangles. See `qa/geometry-validation.json`. Digital checks do not validate hardware seating, clamp strength or headphone fit. **No M3 print dispatched.** The previously dispatched M2 pair separately showed Finished, 41/41 layers, in Bambu on October 18.

Files: editable SCAD, single STL, paired STL, native paired PETG 3MF, QA records, actual CAD/native previews and SHA256SUMS. Keep unpublished until hardware and headphone testing, actual product photos and packed shipping measurements are complete. Earlier M2 listing graphics/copy must be replaced before sale.
