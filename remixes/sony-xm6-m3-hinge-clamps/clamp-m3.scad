// Minimal M3 bore-only prototype, 2026-10-18.
// Original: Viktor @Viktor_2298956, CC BY 4.0
// https://www.printables.com/model/1465791-sony-xm6-headphone-hinge-repair
// Entire original curved body, collar opening, slot and recesses retained.
// Only change: enlarge coaxial ~1.965 mm holes to 3.4 mm clearance.
// M3 head/nut do NOT fit inside original recesses. Trial external hardware
// with flat washers spanning recesses. Richard selected M3 x 12 mm
// screws for the full kit on 2026-10-18; detailed installed assembly unrecorded.
$fn=96;
pair=false;
bore_d=3.4;
cx=11.278; cy=0.0019865; cz=4.525;
module clamp() {
 difference() {
  import("../../verified-downloads/sony-xm6-hinge-repair/XM6_Hinge_Clamp_Rev3.stl",convexity=10);
  translate([cx,cy-15,cz]) rotate([-90,0,0]) cylinder(d=bore_d,h=30);
 }
}
if(pair) for(x=[-20,20]) translate([x,0,0]) clamp();
else clamp();
