// Dummy topper + stem tester for dance bag base v3 through-slot
// Print flat on the bed.

$fn = 48;

// =========================
// STEM THAT MATCHES THE BASE SLOT TARGET
// =========================
stem_w   = 10.0;
stem_t   = 4.0;
stem_len = 10.0;    // length through the base roof

// =========================
// TOPPER TO EXPOSE TILT
// =========================
name_w = 100.0;     // try 80 / 100 / 120
name_h = 18.0;
name_t = 4.0;

// centered stem by default
stem_offset_x = 0.0;

// small fillet-ish gusset dimensions at stem junction
use_gussets = true;
gusset_w = 18.0;
gusset_h = 6.0;

// =========================
// MAIN
// =========================
translate([0, 0, stem_len + name_t])
    rotate([180, 0, 0])
        dummy_topper();

module dummy_topper() {
    union() {
        // name bar
        translate([-name_w/2, -name_t/2, stem_len])
            cube([name_w, name_t, name_h]);

        // main stem
        translate([stem_offset_x - stem_w/2, -stem_t/2, 0])
            cube([stem_w, stem_t, stem_len + 0.02]);

        if (use_gussets) {
            // front gusset
            hull() {
                translate([stem_offset_x - gusset_w/2, -name_t/2, stem_len])
                    cube([gusset_w, 0.02, gusset_h]);
                translate([stem_offset_x - stem_w/2, -stem_t/2, stem_len - gusset_h])
                    cube([stem_w, 0.02, 0.02]);
            }

            // back gusset
            hull() {
                translate([stem_offset_x - gusset_w/2, name_t/2 - 0.02, stem_len])
                    cube([gusset_w, 0.02, gusset_h]);
                translate([stem_offset_x - stem_w/2, stem_t/2 - 0.02, stem_len - gusset_h])
                    cube([stem_w, 0.02, 0.02]);
            }
        }
    }
}
