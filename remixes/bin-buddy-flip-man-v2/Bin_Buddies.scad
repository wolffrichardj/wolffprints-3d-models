// Bin Buddies v2, original characters for Richard Wolff, 2026-10-28.
// Mechanical donor: Bindicator by user_1770727599, CC BY-NC 4.0.
// https://makerworld.com/en/models/2889779-bindicator
// Keep the complete original collar and lid-contact arm; replace the paddle.

mode = "model"; // model, front, presentation, preservation_check
style = "helper"; // helper: hard hat / buddy: tilted cap and overalls
$fn = 64;
thickness = 4.6;
figure_x = 22.9;
axis_z = 17.5;
cut_y = -7.8;
protected_y = -9.0;
recess = 0.55;

module pill(a,b,r) {
    hull() { translate(a) circle(r=r); translate(b) circle(r=r); }
}
module rounded_box(c,s,r) {
    hull() for (sx=[-1,1], sy=[-1,1])
        translate([c[0]+sx*(s[0]/2-r),c[1]+sy*(s[1]/2-r)]) circle(r=r);
}
module heart(c,s=1) {
    translate(c) scale([s,s]) union() {
        translate([-1.05,0.55]) circle(r=1.5);
        translate([1.05,0.55]) circle(r=1.5);
        polygon([[-2.35,0.0],[2.35,0.0],[0,-2.6]]);
    }
}
module helmet() {
    // A broad, rounded dome and a chunky brim read in a single filament.
    intersection() {
        translate([0,37.5]) scale([1.08,1]) circle(r=11.5);
        translate([-15,38.8]) square([30,15]);
    }
    rounded_box([0,39.0],[27,3.4],1.6);
}
module cap() {
    translate([0,38.7]) rotate(-9) translate([0,-38.7]) union() {
        intersection() {
            translate([0,37.0]) scale([1.04,0.94]) circle(r=11.6);
            translate([-14,38.2]) square([28,14]);
        }
        rounded_box([3.0,38.7],[28.0,3.0],1.45);
        translate([-0.4,47.4]) circle(r=1.5);
    }
}
module silhouette() {
    union() {
        // Short legs and big boots; soles overlap the retained neck.
        rounded_box([-7.8,-5.35],[12.3,5.7],2.6);
        rounded_box([7.8,-5.35],[12.3,5.7],2.6);
        pill([-6.6,-2.8],[-5.0,6.3],3.9);
        pill([6.6,-2.8],[5.0,6.3],3.9);
        // Soft pear-shaped body, little shoulders, tucked-in neck.
        hull() {
            translate([0,8.5]) scale([1.10,1]) circle(r=9.2);
            translate([0,18.0]) scale([1.12,0.90]) circle(r=7.1);
        }
        pill([0,21.0],[0,25.1],4.7);
        // Big cheeks and ears, with a slight head tilt.
        translate([0,32.0]) rotate(-5) scale([1,0.98]) circle(r=11.2);
        translate([-10.5,31.5]) circle(r=2.4);
        translate([10.5,31.5]) circle(r=2.4);
        if (style=="helper") helmet(); else cap();
        // A bent wave with a mitten, rather than a long straight stick arm.
        pill([-7.5,19.7],[-16.2,25.2],3.5);
        pill([-16.2,25.2],[-19.7,35.0],3.2);
        translate([-20.0,38.6]) scale([0.94,1.16]) circle(r=3.65);
        pill([-17.9,36.3],[-16.3,38.6],1.8);
        // The other elbow makes a rounded, relaxed hand-on-hip pose.
        pill([7.6,19.7],[13.0,14.3],3.25);
        pill([13.0,14.3],[11.0,9.0],3.1);
        translate([9.7,8.7]) circle(r=3.7);
    }
}
module face() {
    translate([0,32.0]) rotate(-5) translate([0,-32.0]) {
        // Large friendly eyes, a tiny nose, cheek dimples, open smile.
        for (u=[-3.55,3.55]) translate([u,33.2]) scale([1,1.17]) circle(r=1.15);
        pill([-0.15,30.4],[0.35,30.25],0.45);
        for (u=[-7.0,7.0]) pill([u-0.5,29.7],[u+0.5,29.7],0.55);
        intersection() {
            translate([0,29.7]) scale([1,0.86]) circle(r=3.9);
            translate([-4.5,25.2]) square([9,4.45]);
        }
    }
}
module clothing() {
    // Rounded overall bib, wide shoulder straps, big buttons.
    pill([-5.3,19.7],[-4.7,13.5],0.65);
    pill([5.3,19.7],[4.7,13.5],0.65);
    pill([-4.7,13.5],[4.7,13.5],0.65);
    for (u=[-4.8,4.8]) translate([u,17.6]) circle(r=0.8);
    if (style=="buddy") {
        rounded_box([0,7.2],[8.8,6.2],1.5);
        // The heart remains raised inside the recessed pocket.
    } else {
        // Vest reflection stripes retain a workwear cue without tiny text.
        pill([-7.1,9.9],[-3.9,9.9],0.65);
        pill([3.9,9.9],[7.1,9.9],0.65);
        rounded_box([0,6.0],[10.6,1.3],0.5);
    }
    // Boot seams and the mitten cuff.
    pill([-12.0,-4.2],[-4.0,-4.2],0.45);
    pill([4.0,-4.2],[12.0,-4.2],0.45);
    pill([-22.0,34.6],[-17.5,35.6],0.48);
}
module details() {
    face();
    if (style=="helper") {
        heart([0,44.5],0.76);
        clothing();
    } else {
        // A raised heart in the pocket is robust and visible in gray PETG.
        difference() { clothing(); heart([0,7.0],0.81); }
        pill([-7.1,41.7],[-7.8,44.6],0.52);
    }
}
module face_extrusion(x,d) {
    translate([x,0,axis_z]) rotate([0,90,0]) linear_extrude(height=d) children();
}
module mechanism() {
    intersection() {
        import("source/Bindicator_Original_Geometry.stl");
        translate([-1000,-1000,-1]) cube([2000,1000+cut_y,100]);
    }
}
module buddy() {
    difference() {
        union() {
            mechanism();
            face_extrusion(figure_x,thickness) silhouette();
        }
        face_extrusion(figure_x-0.1,recess+0.1) details();
        face_extrusion(figure_x+thickness-recess,recess+0.1) details();
    }
}
module protected_region() {
    intersection() {
        children();
        translate([-1000,-1000,-1]) cube([2000,1000+protected_y,100]);
    }
}
module preservation_check() {
    union() {
        difference() {
            protected_region() import("source/Bindicator_Original_Geometry.stl");
            protected_region() buddy();
        }
        difference() {
            protected_region() buddy();
            protected_region() import("source/Bindicator_Original_Geometry.stl");
        }
    }
}
if (mode=="model") buddy();
else if (mode=="front") difference() { silhouette(); details(); }
else if (mode=="presentation") rotate([90,0,0]) buddy();
else if (mode=="preservation_check") preservation_check();
