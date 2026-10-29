// Bin Buddy Flip Man, a personal-use remix for Richard Wolff.
// Mechanical donor: Bindicator by user_1770727599, CC BY-NC 4.0.
// https://makerworld.com/en/models/2889779-bindicator
// The tested original collar and long lid-contact arm are retained.
// Only the upper indicator paddle is replaced with this original character.

mode = "model"; // model, presentation, figure_front, preservation_check
$fn = 64;

figure_thickness = 2.8;
figure_x = 23.1;
handle_axis_center_z = 17.5;
old_paddle_cut_y = 18.5;
protected_y = 14.9;
engraving_depth = 0.65;

module capsule(a, b, r) {
    hull() { translate(a) circle(r=r); translate(b) circle(r=r); }
}

module rounded_rect_at(center, size, r) {
    hull() for (sx=[-1,1], sy=[-1,1])
        translate([center[0]+sx*(size[0]/2-r),
                   center[1]+sy*(size[1]/2-r)]) circle(r=r);
}

// Coordinates here are left/right and height on the character's face.
// The final face is perpendicular to the original collar's radial plane,
// so the little worker can be seen across the back of the bin.
module worker_silhouette() {
    union() {
        // Broad, rounded boots overlap the retained paddle root.
        rounded_rect_at([-10.6,18.3],[11.0,5.4],2.2);
        rounded_rect_at([10.6,18.3],[11.0,5.4],2.2);
        capsule([-9.3,21.0],[-5.3,35.8],3.1);
        capsule([9.3,21.0],[5.3,35.8],3.1);
        // One continuous torso, neck and round head.
        offset(r=1.2) polygon([[-6.8,33.0],[6.8,33.0],[9.0,48.6],
                              [6.4,52.4],[-6.4,52.4],[-9.0,48.6]]);
        capsule([0,50.5],[0,57.8],3.5);
        translate([0,63.8]) circle(r=9.1);
        // Rounded hard hat. No brittle separate brim or tiny fingers.
        intersection() {
            translate([0,65.5]) circle(r=10.2);
            translate([-12,66.1]) square([24,12]);
        }
        rounded_rect_at([0,66.8],[23.0,2.8],1.2);
        // Raised waving arm and a mitten with a rounded thumb.
        capsule([-7.6,49.6],[-14.3,58.0],2.7);
        capsule([-14.3,58.0],[-14.7,73.7],2.4);
        translate([-14.2,75.8]) circle(r=2.9);
        capsule([-12.5,74.9],[-10.3,77.2],1.3);
        // Other hand rests on the hip.
        capsule([8.0,49.0],[13.0,43.7],2.6);
        capsule([13.0,43.7],[11.8,37.9],2.6);
        capsule([11.8,37.9],[8.8,37.2],2.9);
    }
}

module worker_details() {
    // Eyes and a smile are shallow recesses on both faces.
    for (u=[-3.1,3.1]) translate([u,62.8]) circle(r=0.95);
    intersection() {
        difference() {
            translate([0,61.1]) circle(r=3.25);
            translate([0,61.1]) circle(r=2.15);
        }
        translate([-4.0,56.8]) square([8.0,4.3]);
    }
    // Reflective-vest style V and waist stripe.
    capsule([-5.3,48.5],[0,42.5],0.6);
    capsule([0,42.5],[5.3,48.5],0.6);
    rounded_rect_at([0,37.6],[12.4,1.2],0.4);
    // A small hard-hat ridge gives the cap definition in one-color PETG.
    capsule([0,69.4],[0,73.8],0.55);
}

module face_extrusion(x_start, depth) {
    translate([x_start,0,handle_axis_center_z])
        rotate([0,90,0]) linear_extrude(height=depth) children();
}

module retained_mechanism() {
    intersection() {
        import("source/Bindicator_Original_Geometry.stl");
        translate([-1000,-1000,-1]) cube([2000,1000+old_paddle_cut_y,37]);
    }
}

module flip_man() {
    difference() {
        union() {
            retained_mechanism();
            face_extrusion(figure_x,figure_thickness) worker_silhouette();
        }
        face_extrusion(figure_x-0.1,engraving_depth+0.1) worker_details();
        face_extrusion(figure_x+figure_thickness-engraving_depth,
                       engraving_depth+0.1) worker_details();
    }
}

module protected_region() {
    intersection() {
        children();
        translate([-1000,-1000,-1]) cube([2000,1000+protected_y,37]);
    }
}

module preservation_check() {
    // Expected result: EMPTY. Both original and remixed solids are identical
    // through the complete handle collar and long lid-contact arm.
    union() {
        difference() {
            protected_region() import("source/Bindicator_Original_Geometry.stl");
            protected_region() flip_man();
        }
        difference() {
            protected_region() flip_man();
            protected_region() import("source/Bindicator_Original_Geometry.stl");
        }
    }
}

if (mode=="model") flip_man();
else if (mode=="presentation") color([0.72,0.76,0.80]) rotate([90,0,0]) flip_man();
else if (mode=="figure_front") difference() { worker_silhouette(); worker_details(); }
else if (mode=="preservation_check") preservation_check();
