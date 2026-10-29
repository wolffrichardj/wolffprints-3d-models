# Bindicator

Trash-bin pickup indicator prepared for Richard's Bambu Lab P1S, with the original model retained at 100% scale.

Richard subsequently requested a waving little figure like the original social reference. The [Bin Buddy Flip Man remix](../../remixes/bin-buddy-flip-man/README.md) keeps this smaller collar and the long lid-contact arm, replaces the upper paddle with an original worker figure, and includes a separate sliced project for review.

## Source and attribution

- Model: [Bindicator on MakerWorld](https://makerworld.com/en/models/2889779-bindicator).
- Creator: [user_1770727599](https://makerworld.com/en/@user_1770727599).
- License shown on the source: [Creative Commons Attribution-NonCommercial 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
- Downloaded: 2026-10-27.
- Category: verified download. Both test coupons completed printing; Richard reported the smaller original-size coupon was a perfect fit on the household bin. The full indicator's fit and pickup behavior remain to be checked after printing.

## Prepared print

- Printer: Bambu Lab P1S, 0.4 mm nozzle.
- Material: Generic PETG. The active full-size project uses gray PETG, verified and mapped to AMS A1 in Bambu Studio.
- Plate: Textured PEI, 70 C.
- Nozzle: 255 C; maximum volumetric speed 8 mm3/s.
- Layers: 0.16 mm, 219 layers, four walls, 5% gyroid infill.
- Supports: disabled. The original part is a vertical extrusion from the bed; all mesh vertices occupy the bottom or top Z plane.
- Brim: automatic.
- Speed: Standard 100%, including M220 S100 in startup G-code.
- Original geometry: approximately 103 x 88 x 35 mm. No scaling or shape changes to the full part.
- Bambu Studio 02.08.02.61 slice: success, return code 0, no plate/model warnings.
- Estimate: 1h27m11s total, 27.48 g PETG.

The author's project included ten filament entries and support settings. The prepared project uses one PETG filament, a previously verified P1S machine/filament setup, and the author's layer height, wall count, and infill percentage. Machine-preset lookup notices in the CLI log are separate from the successful plate result and do not represent geometry warnings.

## Fit and use

### Handle comparison, checked 2026-10-27

- The downloaded MakerWorld model does not publish a nominal handle diameter. Measuring its actual profile gives approximately **25.1 mm maximum rigid circular clearance** inside the irregular clip pocket. This is a geometric measurement, not a guarantee of clearance after printing or a published handle specification.
- The alternative [Universal Full / Empty Flag on Printables](https://www.printables.com/model/771018-universal-full-empty-flag-for-trash-can-recycle-bi) explicitly specifies a **32 mm default handle diameter**. That is a different design and does not establish that this MakerWorld clip fits a 32 mm handle.
- The comparison is recorded in `handle-fit-analysis.json` and `images/handle-fit-comparison.png`. The original full-size indicator remains unchanged.
- A second test coupon scales the original opening in XY to approximately **32.6 mm circular clearance**, allowing 0.6 mm over a nominal 32 mm circular handle. Its width remains 6 mm. This is a separate derived test, not the downloaded Printables model.
- `fit-test-slice/Bindicator_Fit_Tests_P1S_PETG_Sliced.3mf` contains both coupons on one plate: original approximately 25.1 mm on the left and enlarged approximately 32.6 mm on the right. The slice passed with no plate/model warnings: **23m35s total, 5.31 g PETG, 37 layers**.

1. Richard confirmed that the smaller, original-size test coupon was a perfect fit on the household bin. Use the unchanged original opening for the full indicator. The exact cart model remains unidentified.
2. `Fit_Check.stl` is an optional low-material test of the unchanged handle opening. It is only 6 mm wide and has shortened arms, so it flexes more easily than the full 35 mm wide part. A successful coupon fit does not prove that the full part will snap on equally easily.
3. The full clip must rotate freely around the handle. Do not force a tight or cracked clip into service.
4. Install near the lid as in the source photos. Set its armed position only after placing the bin at the curb.
5. Open the lid and simulate a pickup before relying on the indicator. Confirm that it changes position, remains visible, and does not obstruct the lid. Opening the lid manually may also change the indicator.
6. Bright paint or reflective tape on one arm can improve visibility if using dark PETG. Keep the rotating/contact surfaces clear.

The model's source description is minimal. The smaller coupon's fit is confirmed; full-width fit, lid clearance, and pickup behavior need checking after the full indicator prints.

Loose G-code is omitted from the repository because the sliced 3MF projects already contain it. Detailed local printer-control records and screenshots are also omitted; public summaries are in `fit-test-gray/dispatch-summary.json` and `full-gray/dispatch-summary.json`.

## Files and status

- `Bindicator_Original.3mf`: unmodified MakerWorld download.
- `Bindicator_P1S_PETG_Prepared.3mf`: prepared single-filament project.
- `Bindicator_P1S_PETG_Sliced.3mf`: validated full-part project with embedded G-code.
- `full-gray/Bindicator_Full_Original_Size_Gray_PETG_P1S.3mf`: active full indicator at the successful smaller size, with gray PETG and embedded G-code.
- `full-gray/`: full-indicator project, slice result, and public dispatch summary.
- `Bindicator.stl`: unchanged source mesh, translated so its bottom is at Z=0.
- `Fit_Check.scad` / `Fit_Check.stl`: optional narrow fit coupon, derived from the source mesh.
- `Fit_Check_32_6mm.scad` / `Fit_Check_32_6mm.stl`: larger comparison coupon.
- `Bindicator_Fit_Tests_P1S_PETG_Prepared.3mf`: both handle-size tests on one plate.
- `fit-test-slice/`: sliced two-coupon project, G-code, result, and log.
- `handle-fit-analysis.json` / `images/handle-fit-comparison.png`: measured opening and comparison with the alternative design.
- `result.json`: full-part Bambu slice result.
- `mesh-validation.json`: original mesh topology and dimensions.
- `images/`: model and slicer previews.

The Mac was initially locked, then became accessible during the follow-up. Richard authorized one test print if the checks support it. Live Bambu Studio showed printer finished/idle, gray PETG in A1, black PETG in A2, blue PETG in A3, and black PLA in A4. Gray A1 was selected for the fit tests for visibility. The send dialog verified the P1S 0.4 mm printer, gray PETG mapped to A1, timelapse off, and auto bed leveling on. The GUI estimate is 23m26s / 5.31 g; the small timing difference from CLI is immaterial.

One gray PETG fit-test job was sent at approximately **2026-10-27 19:36 CDT** to the P1S, using A1, auto bed leveling on, and timelapse off. Live Bambu Studio later showed the fit tests **finished at 37/37 layers**. Richard reported that the **smaller size was perfect for the household bin**.

### Full indicator follow-up

Richard then authorized preparation of the full indicator at that smaller size and automatic printing if the estimate was under two hours. The original mesh and build transforms were verified unchanged. The full gray PETG slice passed without model/plate warnings: approximately 103 x 88 x 35 mm, 219 layers, four walls, 5% gyroid infill, no supports, 255 C nozzle, 70 C textured PEI bed, and 8 mm3/s maximum flow.

The CLI estimate was **1h27m11s / 27.48 g**; the Bambu Studio send dialog showed **1h26m / 27.48 g**, passing the two-hour authorization gate. The selected printer was the P1S, gray PETG mapped to A1, auto bed leveling on, and timelapse off. One full-indicator job was sent at approximately **20:10 CDT**. The printer showed download at 100%, then **0/219 layers, waiting for the heatbed to reach target temperature**, with estimated finish at **21:37 CDT**. Printer acceptance and preparation are verified. Bambu Studio showed this plain indicator finished at 219/219 layers before the centered character was sent on 2026-10-28. Full-width installation and flipping remain unverified. No duplicate full-indicator job was sent.

## Plano cart research, 2026-10-27

- [Plano Residential Trash](https://www.plano.gov/residential-trash) lists 95 gallons as the standard trash and recycling cart and 68 gallons as the smaller trash option.
- [Plano's cart purchasing recap](https://plano.novusagenda.com/agendapublic/AttachmentViewer.ashx?AttachmentID=15749&ItemID=7019) and [December 7, 2021 council record](https://plano.novusagenda.com/agendapublic/DisplayAgendaPDF.ashx?MinutesMeetingID=668) identify Rehrig Pacific as the selected trash/recycling cart supplier. This supports Rehrig as a plausible manufacturer; it does not identify Richard's individual cart or establish that every older Plano cart is the same model.
- Rehrig's [95-gallon EnviroGuard page](https://www.rehrigpacific.com/waste-and-recycling/products/95-gallon-enviroguard-roll-out-cart) and [July 2026 manufacturer sheet](https://www.rehrigpacific.com/download_file/force/feb735be-aa3e-4edb-bc97-2911282d1eec/394) give overall depth 33.3 in, width 29.2 in, and height 43.5 in.
- Rehrig's [95-gallon Nestable Bar sheet](https://www.rehrigpacific.com/download_file/force/2f8b645c-685c-4ea0-823a-97fbd250abc8/394) gives overall depth 33.7 in, width 28.7 in, and height 45.1 in for that configuration. Lid variants change overall height.
- The reviewed manufacturer sheets describe a continuous one-piece molded handle but do not give its grip cross-section. Overall cart dimensions and gallon capacity do not establish a 25 mm or 32 mm handle. Do not confuse a published **cart gripping diameter** for truck arms, wheel axle diameter, catch-bar diameter, or handle height with the handgrip's cross-section.
- Some rotational looseness is useful for this indicator. It must still remain captured around the handle, clear nearby ribs/hinges, and engage the lid through a simulated pickup. A looser coupon can be an acceptable fit, but it does not by itself verify the full mechanism.
