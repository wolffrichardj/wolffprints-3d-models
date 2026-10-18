# Sony WH-1000XM6 hinge-ring reinforcement clamps — pair

Design: **Viktor (@Viktor_2298956)**, [Sony XM6 headphone hinge repair](https://www.printables.com/model/1465791-sony-xm6-headphone-hinge-repair), **CC BY 4.0** ([license](https://creativecommons.org/licenses/by/4.0/)). Original source Rev3 retained unchanged in `source/`. Commercial use verified on source page October 18, 2026. No endorsement implied.

## Print one pair

Open `XM6_Hinge_Repair_Pair_Black_PETG_P1S.3mf` in Bambu Studio and slice. It contains **two clamps on one plate**, as two disconnected shells of one object. One run = one pair. The single and pair STLs are retained at millimeter scale. Changes from source: geometry exported to STL, centered/grounded and duplicated by translation only; PETG/P1S setup added.

P1S, 0.4mm nozzle, textured PEI, black Generic PETG, 0.20mm layers, four walls, 99% cubic, five top/bottom layers, 255°C nozzle / 70°C bed, flow 0.95, max volumetric speed 12mm³/s. Auto tree support on build plate is enabled; native slice generated no supports or warnings. Estimated **17m53s / 3.55g / 41 layers**. Model is 8.25mm tall; final layer top is 8.20mm due layer quantization.

## Three checks before dispatch

1. Source closed/manifold mesh, consistent winding, zero degenerate triangles; 3,652 vertices / 7,308 triangles per clamp. Each 29.59044 × 20.514465 × 8.25mm. Pair STL has two shells / 14,616 triangles, size 69.59044 × 20.514465 × 8.25mm. See `geometry-validation.json`.
2. Final project reopened cleanly in native Bambu Studio 02.08.02.61 and native slice succeeded. Independent CLI slice of that native-saved file returned code 0, no warnings and identical 17m53s estimate. See `qa/native-slice-result.json` and `qa/gcode-settings.txt`. The earlier hand-built prototype was rejected and replaced, never dispatched.
3. Live P1S `3DP-01P-063` online/idle, camera showed a clear textured plate. Send dialog mapped single black PETG to **AMS A2**, bed leveling on, timelapse off. User authorized starting after the three checks. Dispatched October 18, 2026 about 13:35 CDT; printer accepted and entered preparation, layer 0/41. Physical completion/quality/fit not yet verified.

## Installation scope

External reinforcement for the broken support ring at the headband extension sleeve, **WH-1000XM6 only**. Not a full hinge replacement. Creator specifies **one M2 × 20mm bolt per clamp (two per pair)**. Bolts are not printed; verify hardware stock and fit. Tighten gently and check movement. Our PETG print has not been installation/endurance tested; source used PLA.

## Images

`images/plate_1.png` and `plate_no_light_1.png`: native Bambu model render of the actual paired project, not printed-product photos. `creator-installed-reference.png`: captured source gallery image 3, Viktor's installed example under the source CC BY 4.0 attribution; hardware/print revision can differ. `source-model-thumbnail.png`: creator source preview. Any generated installation illustration is explicitly labeled as AI illustration and must not be presented as real test evidence.

No buyer, order, account-access or printer credentials belong in this model archive. The unpublished eBay draft and stock/publication gates are tracked privately in Richard's vault.

## Kit and guide update

**Superseded hardware assumption:** Richard later corrected his stock to M3-only (kit-label photo, October 18, 2026). This original M2 geometry is retained for provenance; do not pair it with M3 bolts. See `../../remixes/sony-xm6-m3-hinge-clamps/` for the separately labeled M3 prototype. Earlier retail plan: **two PETG clamps + two bolts**, with **assembly required; tools and headphones not included**. User will test the parts and bolts before publication. Do not specify a bolt drive style or Allen-key size without verification. Historical M2 three-step listing guide is `images/installation-illustration-kit-ai.png`; it labels its AI origin and includes the bolts. The earlier `installation-illustration-ai.png` is a superseded clamps-only draft and must not be used for the kit listing. Neither illustration is physical fit or durability evidence.
