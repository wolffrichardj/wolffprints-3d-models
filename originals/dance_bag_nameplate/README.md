# Dance Bag Nameplate Base

## Description

A clip-on nameplate holder that saddles over a dance bag bar. v3 uses a through-slot instead of a blind mortise so the base prints flat on the bed with no supports. A companion stem tester prints quickly and lets you dial in the fit before printing the full nameplate.

## Details

| Field | Value |
|---|---|
| Category | originals |
| Version | v3 |
| Source / Origin | Original design |
| Published URL | — |
| Status | Active / in progress |

## File inventory

| File | Description |
|---|---|
| `dance_bag_base_v3_through_slot.scad` | OpenSCAD source — main base body |
| `dummy_name_through_slot_tester.scad` | OpenSCAD source — stem and topper fit tester |
| `dummy_name_through_slot_tester.stl` | Exported STL of the fit tester (print this first) |

## Changes made

N/A — original design. v3 replaced the blind mortise from earlier versions with a through-slot for supportless printing.

## Printing notes

Set `print_flipped = true` in the SCAD to orient the model correctly (top face on bed). Adjust `clear_w` / `clear_h` tolerance variables if the saddle cavity is too tight or loose for your bag bar. `$fn = 48` for smooth curves.

## Assembly / use notes

1. Print `dummy_name_through_slot_tester` first to verify stem fit.
2. Slide the nameplate stem (10.0 mm × 4.0 mm target) through the slot from the top of the base.
3. The saddle cavity is sized for a 27.07 mm × 29.91 mm bag bar cross-section.
