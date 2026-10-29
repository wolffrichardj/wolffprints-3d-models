// Fit coupon derived from the original Bindicator mesh by user_1770727599.
// Source: https://makerworld.com/en/models/2889779-bindicator
// License: CC BY-NC 4.0. Geometry is cropped and narrowed only for a fit check.
// This is NOT the full indicator. Do not use it as the functioning part.
// Retains the original XY handle opening at 100% scale, with a 6 mm width.
intersection() {
    import("Bindicator.stl");
    translate([14, -50, 0]) cube([46, 43, 6]);
}
