//
// Stylized printable bust
// Based on user-provided photos
// Target: Bambu Lab P1S
// Recommended print: PLA, 0.16 or 0.12 layer height, 3 walls
//

$fn = 72;

// ---------- Global scale ----------
target_height_mm = 120;
model_height_units = 118;
global_scale = target_height_mm / model_height_units;

// ---------- Helpers ----------
module ellipsoid(x=10,y=10,z=10){
    scale([x/2,y/2,z/2]) sphere(r=1);
}

module rounded_box(size=[10,10,10], r=1.5){
    x=size[0]; y=size[1]; z=size[2];
    hull(){
        for(ix=[-1,1], iy=[-1,1], iz=[-1,1]){
            translate([ix*(x/2-r), iy*(y/2-r), iz*(z/2-r)])
                sphere(r=r);
        }
    }
}

module tapered_cylinder(h=10, r1=10, r2=8){
    cylinder(h=h, r1=r1, r2=r2);
}

module mirrored_x(){
    children();
    mirror([1,0,0]) children();
}

// ---------- Main ----------
scale(global_scale)
    bust_model();

module bust_model(){

    union(){

        pedestal();
        torso();
        neck();
        head();
        ears();
        facial_planes();
        nose();
        lips();
        beard_mass();
        hair_mass();
        glasses();
    }
}

// ---------- Pedestal ----------
module pedestal(){
    union(){
        translate([0,0,0])
            cylinder(h=8, r=24);

        translate([0,0,8])
            cylinder(h=6, r1=22, r2=19);

        translate([0,0,14])
            cylinder(h=4, r1=19, r2=17);
    }
}

// ---------- Torso / jacket ----------
module torso(){
    union(){

        // Upper chest block
        translate([0,0,28])
            hull(){
                translate([0,0,0]) ellipsoid(34,24,20);
                translate([0,0,10]) ellipsoid(32,22,16);
            }

        // Shoulders
        hull(){
            translate([-16,0,36]) ellipsoid(16,13,10);
            translate([ 16,0,36]) ellipsoid(16,13,10);
            translate([0,3,33])   ellipsoid(28,18,10);
        }

        // Jacket drape
        difference(){
            hull(){
                translate([0,2,28])  ellipsoid(36,24,18);
                translate([0,4,46])  ellipsoid(30,18,12);
            }

            // shirt opening / V cut
            translate([0,12,43])
                rotate([65,0,0])
                rounded_box([18,16,20], r=2.5);
        }

        // Lapels
        translate([-5.8,8.0,39])
            rotate([18,0,26])
            rounded_box([3.2,10,14], r=0.9);

        translate([5.8,8.0,39])
            rotate([18,0,-26])
            rounded_box([3.2,10,14], r=0.9);

        // Shirt collar
        translate([0,6.0,41.5])
            difference(){
                hull(){
                    translate([-5,0,0]) ellipsoid(6,5,5);
                    translate([ 5,0,0]) ellipsoid(6,5,5);
                    translate([0,-2,3]) ellipsoid(12,7,4);
                }
                translate([0,4.8,41.6-41.5])
                    rotate([65,0,0])
                    cube([8,10,8], center=true);
            }
    }
}

// ---------- Neck ----------
module neck(){
    union(){
        translate([0,0,43])
            hull(){
                translate([0,0,0]) ellipsoid(13.5,12,14);
                translate([0,0,10]) ellipsoid(12,11,9);
            }

        // slight back neck support blend
        hull(){
            translate([0,-4,41]) ellipsoid(16,10,8);
            translate([0,-6,50]) ellipsoid(15,9,8);
        }
    }
}

// ---------- Head ----------
module head(){
    difference(){
        union(){

            // Main skull
            translate([0,0,67])
                ellipsoid(28,24,34);

            // Jaw / lower face
            hull(){
                translate([0,1,60]) ellipsoid(22,20,18);
                translate([0,1,51]) ellipsoid(18,18,12);
            }

            // Forehead extension
            hull(){
                translate([0,2.5,75]) ellipsoid(20,18,12);
                translate([0,1.5,83]) ellipsoid(17,15,8);
            }

            // Back of head
            hull(){
                translate([0,-4.5,69]) ellipsoid(25,22,25);
                translate([0,-7.0,66]) ellipsoid(21,18,18);
            }
        }

        // Under chin flattening for printability
        translate([0,8,49])
            rotate([18,0,0])
            rounded_box([18,12,7], r=1.2);
    }
}

// ---------- Ears ----------
module ears(){
    mirrored_x()
    translate([13.6,-1.8,66.8])
        rotate([0,18,0])
        difference(){
            ellipsoid(6.3,4.2,11.5);
            translate([0.9,0.7,0])
                ellipsoid(3.0,2.2,6.2);
        }
}

// ---------- Facial planes ----------
module facial_planes(){
    union(){

        // Brow ridge
        hull(){
            translate([-6.8,8.2,71.7]) ellipsoid(7,4,3.4);
            translate([ 6.8,8.2,71.7]) ellipsoid(7,4,3.4);
        }

        // Cheek planes
        mirrored_x()
        hull(){
            translate([7.8,8.0,64.3]) ellipsoid(6,4.5,7);
            translate([5.5,6.8,59.5]) ellipsoid(5.5,4.8,7);
        }

        // Chin block
        hull(){
            translate([0,8.8,53.2]) ellipsoid(8.5,6.5,5.5);
            translate([0,7.2,49.5]) ellipsoid(7.2,5.8,4.2);
        }
    }
}

// ---------- Nose ----------
module nose(){
    union(){

        // bridge
        hull(){
            translate([0,9.0,69.8]) ellipsoid(3.6,3.2,9);
            translate([0,11.2,62.8]) ellipsoid(4.2,4.0,8);
        }

        // tip
        translate([0,12.8,61.8])
            ellipsoid(6.4,5.5,5.6);

        // nostril / wing mass
        hull(){
            translate([-2.3,11.8,60.8]) ellipsoid(2.6,2.6,2.8);
            translate([ 2.3,11.8,60.8]) ellipsoid(2.6,2.6,2.8);
            translate([0,12.4,60.3])    ellipsoid(4.8,3.8,2.6);
        }
    }
}

// ---------- Mouth ----------
module lips(){
    union(){

        // moustache shelf / philtrum region
        hull(){
            translate([0,10.1,58.0]) ellipsoid(8.5,3.0,2.4);
            translate([0,9.2,56.3])  ellipsoid(7.2,2.6,1.8);
        }

        // upper lip
        hull(){
            translate([-2.8,10.2,55.5]) ellipsoid(3.2,1.8,1.5);
            translate([ 2.8,10.2,55.5]) ellipsoid(3.2,1.8,1.5);
        }

        // lower lip
        hull(){
            translate([0,9.6,53.8]) ellipsoid(6.4,2.2,1.8);
            translate([0,9.0,52.9]) ellipsoid(5.2,2.1,1.4);
        }
    }
}

// ---------- Beard ----------
module beard_mass(){
    union(){

        // Full beard envelope
        difference(){
            hull(){
                translate([0,5.5,58]) ellipsoid(23,18,20);
                translate([0,4.8,50]) ellipsoid(20,17,16);
                translate([0,2.5,46]) ellipsoid(16,15,10);
            }

            // remove upper cheeks / eye area
            translate([0,9.5,67])
                rotate([10,0,0])
                rounded_box([30,12,12], r=2);

            // open front of nose / mouth slightly
            translate([0,14.2,60])
                rounded_box([10,7,8], r=1.5);
        }

        // moustache fullness
        hull(){
            translate([-4.0,10.0,57.3]) ellipsoid(4.5,2.5,2.4);
            translate([ 4.0,10.0,57.3]) ellipsoid(4.5,2.5,2.4);
            translate([0,9.1,56.2])     ellipsoid(9.5,2.5,2.3);
        }

        // beard under jaw
        hull(){
            translate([0,4.5,49.5]) ellipsoid(15,13,8);
            translate([0,2.0,45.5]) ellipsoid(12,12,7);
        }

        // sideburn connection
        mirrored_x()
        hull(){
            translate([10.8,4.2,64.5]) ellipsoid(5.5,3.5,9.5);
            translate([8.8,5.2,58.0])  ellipsoid(5.5,4.0,10.5);
        }
    }
}

// ---------- Hair ----------
module hair_mass(){
    union(){

        // Main hair cap
        difference(){
            hull(){
                translate([0,-1.5,78.2]) ellipsoid(27.5,23,12);
                translate([0,-4.5,71.0]) ellipsoid(25.5,22,16);
            }

            // front recession / hairline shaping
            translate([0,10.2,76.8])
                rotate([20,0,0])
                rounded_box([26,10,8], r=2.5);
        }

        // top part / swept front
        hull(){
            translate([-3.0,7.5,79.3]) ellipsoid(12,7,5);
            translate([ 5.0,6.3,78.8]) ellipsoid(11,7,4.5);
            translate([ 1.5,4.8,81.0]) ellipsoid(10,6,3.8);
        }

        // side taper
        mirrored_x()
        hull(){
            translate([11.5,-1.5,73.0]) ellipsoid(6,5,11);
            translate([11.0,-2.0,67.0]) ellipsoid(5.5,5,10);
        }
    }
}

// ---------- Glasses ----------
module glasses(){
    union(){

        // Left lens frame
        translate([-7.3,11.1,69.6])
            rotate([84,0,0])
            linear_extrude(height=1.8, center=true)
                offset(r=0.7)
                difference(){
                    square([12.5,7.8], center=true);
                    offset(delta=-1.4)
                        square([12.5,7.8], center=true);
                }

        // Right lens frame
        translate([7.3,11.1,69.6])
            rotate([84,0,0])
            linear_extrude(height=1.8, center=true)
                offset(r=0.7)
                difference(){
                    square([12.5,7.8], center=true);
                    offset(delta=-1.4)
                        square([12.5,7.8], center=true);
                }

        // bridge
        hull(){
            translate([-1.8,11.0,69.4]) ellipsoid(2.0,1.5,1.4);
            translate([ 1.8,11.0,69.4]) ellipsoid(2.0,1.5,1.4);
        }

        // brow bar emphasis
        hull(){
            translate([-11.5,11.0,72.2]) ellipsoid(3,1.3,1.6);
            translate([ 11.5,11.0,72.2]) ellipsoid(3,1.3,1.6);
        }

        // temples, thickened for printability
        mirrored_x()
        hull(){
            translate([13.0,9.4,69.6]) ellipsoid(1.8,1.4,1.6);
            translate([18.0,4.2,69.0]) ellipsoid(2.0,1.6,1.8);
            translate([20.5,-0.5,68.2]) ellipsoid(2.1,1.7,1.8);
        }
    }
}