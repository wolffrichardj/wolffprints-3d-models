"""Compare v2 and v3 meshes from the same orthographic viewing direction."""
import importlib.util
from pathlib import Path
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('prepare',ROOT/'scripts/prepare.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)

view=[-1,-.85,.30]
p.render(p.mesh(ROOT.parent/'bin-buddy-flip-man-v2/Overall_Buddy.stl'),ROOT/'images/Previous_Same_View.png',size=(1100,1150),view_override=view,old_orientation=True)
p.render(p.mesh(ROOT/'Overall_Buddy.stl'),ROOT/'images/Perpendicular_Same_View.png',size=(1100,1150),view_override=view)

canvas=Image.new('RGB',(2400,1600),'#F4F5F2');d=ImageDraw.Draw(canvas)
d.text((90,55),'A QUARTER TURN',font=p.font(25,True),fill='#657A77')
d.text((90,103),'The little man now faces the other way',font=p.font(58,True),fill='#263C39')
d.text((90,187),'Same camera. Same handle clip. Figure turned 90 degrees.',font=p.font(30),fill='#586965')
for x,name,title in [(50,'Previous_Same_View.png','Previous orientation'),(1250,'Perpendicular_Same_View.png','Turned 90 degrees')]:
    d.text((x+55,280),title,font=p.font(39,True),fill='#263C39')
    canvas.paste(Image.open(ROOT/'images'/name),(x,355))
d.line([(1200,280),(1200,1465)],fill='#D8DFDA',width=2)
canvas.save(ROOT/'images/Orientation_Comparison.png')
