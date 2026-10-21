# Kreg pocket-hole jig dust shroud — Festool D27, left-hand

One dark-blue PETG test shroud for connecting the matching Kreg pocket-hole jig to a Festool D27 hose. Downloaded model with printer setup; geometry is unchanged apart from inch-to-millimeter conversion. **Prototype: physical jig retention, hose fit, support cleanup and useful airflow remain untested.** The folder category records a reviewed download, not a claim that physical fit is verified.

## Source and attribution

Original: **Festool to Kreg Dust Shroud**, **Tooltutor**, [Thingiverse 22865](https://www.thingiverse.com/thing:22865). Original left-hand STL dated May 11, 2012, retained unchanged in `source/`. Licensed [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/); commercial use is permitted with attribution. No endorsement by the creator, Kreg or Festool is implied.

The unitless original has inch-sized coordinates. `Kreg_D27_Left_Metric.stl` applies a uniform **25.4×** unit conversion, yielding approximately **50.6984 × 67.5894 × 89.5604 mm**. The Bambu project adds only rigid placement/orientation and slicer/material setup. No fit offsets, hole resizing, thickening or other shape edits. One shroud is one unit; the separate right-handed source is not included or qualified.

Source owner reports include K4 and K5 use, but also mixed hose-fit reports. This is not universal Kreg or vacuum-hose compatibility. Successful source makes do not validate this exact print.

## Print one prototype

Open `Kreg_D27_Left_Dark_Blue_PETG_P1S_Test.3mf` in Bambu Studio. It contains **one shroud on one plate**. P1S, 0.4 mm nozzle, textured PEI; **Generic PETG**, dark-blue preview `#2850E0`, 255°C nozzle / 70°C bed, flow ratio 0.95, maximum volumetric speed 12 mm³/s. This is the final user-synchronized preset; it supersedes the earlier named 10 mm³/s preparation profile. It has not been calibrated specifically to this spool. The photographed spool is PETG Basic Dark Blue, SKU NPETG019, 1.75 mm; its label specifies 230–260°C nozzle and 70–90°C bed. Preview color is illustrative, not an exact Kreg color match.

0.24 mm layers, 0.20 mm first layer, three walls, 25% grid infill. Build-plate-only automatic tree supports, 0.24 mm top/bottom gap. Bambu auto-orientation rests the source Y=0 plane on the plate; placed height 67.5894 mm. The process dropdown retains the modified Standard preset name; the saved settings above are authoritative.

Final native slice: **2h02m / 51.90 g**, including **8.31 g support**, 282 layers. Independent installed Bambu 02.08.02.61 CLI reopen/reslice: success, return 0, no warnings, **7314.06 seconds / 51.896 g**. Geometry retains 72,066 triangles with zero boundary/nonmanifold edges and no native repairs; `qa/verification.json` records checks.

## Preflight and test status

On October 21, 2026, live printer check showed the previous job finished and a clear textured plate. A3 was verified as blue PETG. Send dialog correctly mapped project filament 1 to **AMS A3**, auto bed leveling on, timelapse off. Always recheck actual loaded material and assignment before another run; a saved project color is not proof of a physical slot.

Dispatch: prepared; not yet sent at this commit.

After cooling, remove supports carefully and check that retention features remain intact. Test the exact jig and hose without forcing either connection, check ordinary hose movement and vacuum flow, and capture installed photos before any sale trial. No universal-fit, dust-elimination, static-safety or heat-proof claim.

## Files

- `Kreg_D27_Left_Dark_Blue_PETG_P1S_Test.3mf` — native Bambu project for one blue PETG prototype.
- `Kreg_D27_Left_Metric.stl` — metric printable mesh.
- `source/Festool_Kreg_DC_Shroud_Left.STL` — untouched original inch-sized source.
- `images/plate-preview.png` — native model preview, not a printed-product photograph.
- `qa/verification.json`, `qa/native-project-reslice.json` — geometry, setup and slice evidence.
- `SHA256SUMS` — retained-file checksums.

No listing or sale inventory is created by retaining this prototype.
