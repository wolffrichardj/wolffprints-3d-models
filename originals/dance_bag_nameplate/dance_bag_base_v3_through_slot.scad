// Dance bag name plate base - v3
// Supportless version using a through-slot instead of a blind mortise.
// Recommended print orientation: print_flipped = true

$fn = 48;

// =========================
// BAG BAR MEASUREMENTS
// =========================
bar_w = 27.07;   // front-to-back of bag bar
bar_h = 29.91;   // top-to-bottom of bag bar
clear_w = 0.00;  // tuned from fit tests
clear_h = 0.00;

// =========================
// BASE GEOMETRY
// =========================
base_len   = 52.0;   // along the bar
side_wall  = 4.0;    // left/right wall thickness
top_wall   = 10.0;   // material above saddle cavity
edge_bevel = 0.8;    // small outer top-edge bevel

// =========================
// THROUGH-SLOT / STEM FIT
// =========================
slot_w          = 10.2;  // snug section width for 10.0 mm stem
slot_t          = 4.2;   // snug section thickness for 4.0 mm stem
slot_fit_depth  = 5.0;   // straight, fit-critical section near top surface
relief_w        = 13.0;  // wider lower relief into cavity
relief_t        = 6.0;   // thicker lower relief into cavity
entry_chamfer   = 0.6;   // light top lead-in

// true = model already flipped for print (top face on bed)
print_flipped = true;

// =========================
// DERIVED
// =========================
inner_w = bar_w + clear_w;
inner_h = bar_h + clear_h;

outer_w = inner_w + 2 * side_wall;
outer_h = inner_h + top_wall;

relief_top_z = inner_h + (top_wall - slot_fit_depth);

// =========================
// MAIN
// =========================
if (print_flipped) {
    translate([0, 0, outer_h])
        rotate([180, 0, 0])
            base_v3();
} else {
    base_v3();
}

// =========================
// MODULES
// =========================
module base_v3() {
    difference() {
        outer_block();

        // saddle cavity
        translate([-0.05, side_wall, -0.05])
            cube([base_len + 0.10, inner_w, inner_h + 0.10]);

        // through-slot system
        through_slot();
    }
}

module outer_block() {
    difference() {
        cube([base_len, outer_w, outer_h]);

        // front top bevel (cosmetic only)
        translate([-0.1, -0.1, outer_h - edge_bevel])
            rotate([45, 0, 0])
                cube([base_len + 0.2, 2 * edge_bevel, 2 * edge_bevel]);

        // back top bevel
        translate([-0.1, outer_w + 0.1, outer_h - edge_bevel])
            rotate([-45, 0, 0])
                cube([base_len + 0.2, 2 * edge_bevel, 2 * edge_bevel]);
    }
}

module through_slot() {
    cx = base_len / 2;
    cy = outer_w / 2;

    union() {
        // snug upper section (straight)
        translate([cx - slot_w/2, cy - slot_t/2, relief_top_z])
            cube([slot_w, slot_t, outer_h - relief_top_z + 0.02]);

        // lower relief / taper into the cavity
        hull() {
            // top of relief matches snug section
            translate([cx - slot_w/2, cy - slot_t/2, relief_top_z])
                cube([slot_w, slot_t, 0.02]);

            // bottom of relief opens up into cavity a bit wider
            translate([cx - relief_w/2, cy - relief_t/2, inner_h - 0.02])
                cube([relief_w, relief_t, 0.02]);
        }

        // tiny lead-in chamfer at top face for easier insertion
        hull() {
            translate([cx - (slot_w + 2*entry_chamfer)/2,
                       cy - (slot_t + 2*entry_chamfer)/2,
                       outer_h - 0.02])
                cube([slot_w + 2*entry_chamfer,
                      slot_t + 2*entry_chamfer,
                      0.02]);

            translate([cx - slot_w/2,
                       cy - slot_t/2,
                       outer_h - entry_chamfer - 0.02])
                cube([slot_w, slot_t, 0.02]);
        }
    }
}
