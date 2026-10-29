"""Validate, render and package the actual exported Bin Buddies meshes.

No generated concept art: previews draw the triangles in the printable STL.
Uses the previous project's verified P1S PETG settings as a starting point.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib, json, struct, zipfile
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
NAMES = [('Happy_Helper', 'Happy Helper'), ('Overall_Buddy', 'Overall Buddy')]

def mesh(path):
    b = Path(path).read_bytes()
    count = struct.unpack_from('<I', b, 80)[0]
    d = np.frombuffer(b, dtype=np.dtype([('normal','<f4',3), ('v','<f4',(3,3)), ('a','<u2')]), count=count, offset=84)
    return d['v'].astype(float)

def analyze(v):
    vertices, inv = np.unique(v.reshape(-1,3), axis=0, return_inverse=True)
    faces = inv.reshape(-1,3)
    edges = Counter(tuple(sorted(e)) for f in faces for e in [(f[0],f[1]),(f[1],f[2]),(f[2],f[0])])
    parents = list(range(len(vertices)))
    def find(i):
        while parents[i] != i:
            parents[i] = parents[parents[i]]; i = parents[i]
        return i
    for a,b in edges:
        a,b = find(a),find(b)
        if a != b: parents[a]=b
    cross = np.cross(v[:,1]-v[:,0],v[:,2]-v[:,0])
    volume_parts = np.einsum('ij,ij->i',v[:,0],np.cross(v[:,1],v[:,2]))/6
    vol = volume_parts.sum()
    com = (volume_parts[:,None]*v.sum(axis=1)/4).sum(axis=0)/vol
    r = dict(vertices=len(vertices),triangles=len(faces), bounds_mm=[v.min(axis=(0,1)).tolist(),v.max(axis=(0,1)).tolist()],
             dimensions_mm=np.ptp(v.reshape(-1,3),axis=0).round(4).tolist(),
             boundary_edges=sum(n==1 for n in edges.values()),nonmanifold_edges=sum(n!=2 for n in edges.values()),
             degenerate_faces=int((np.linalg.norm(cross,axis=1)<1e-8).sum()),
             connected_components=len({find(i) for i in range(len(vertices))}),
             volume_mm3=round(float(vol),3),center_of_mass_mm=com.round(4).tolist())
    assert r['boundary_edges']==r['nonmanifold_edges']==r['degenerate_faces']==0, r
    assert r['connected_components']==1 and vol>0, r
    return r

def render(v, target, size=(1300,1250), crop=False):
    # World axes: left/right, depth, up. Rotate into an orthographic camera.
    w = np.stack([17.5-v[:,:,2],v[:,:,0]-24,v[:,:,1]],axis=-1)
    view = np.array([-.38,-1,.33]); view /= np.linalg.norm(view)
    right = np.cross(view,[0,0,1]);right /= np.linalg.norm(right)
    up = np.cross(right,view)
    if crop:
        # Include the character and its immediate join only.
        w = w[np.max(v[:,:,1],axis=1)>-9]
    # The world coordinate mapping includes a reflection, reversing winding.
    normal = -np.cross(w[:,1]-w[:,0],w[:,2]-w[:,0]);normal /= np.maximum(np.linalg.norm(normal,axis=1)[:,None],1e-9)
    # Light from the upper front left.
    light=np.array([-.4,-.65,1]);light/=np.linalg.norm(light)
    diffuse=np.clip(normal@light,0,1)
    shade=.61+.36*diffuse
    # A small amount of orientation shading gives recessed details depth.
    front = np.abs(normal[:,1])>.96
    source_x=w[:,:,1].mean(axis=1)+24
    recessed=(np.isclose(source_x,23.45,atol=.015)|np.isclose(source_x,26.95,atol=.015))&front
    shade[recessed] *= .60
    projected=np.stack([w@right,w@up],axis=-1)
    lo=projected.min(axis=(0,1));hi=projected.max(axis=(0,1))
    S=2; width,height=size
    scale=min((width-100)/(hi[0]-lo[0]),(height-90)/(hi[1]-lo[1]))*S
    xy=(projected-(lo+hi)/2)*scale
    xy[:,:,0]+=width*S/2;xy[:,:,1]=height*S/2-xy[:,:,1]
    canvas=Image.new('RGB',(width*S,height*S),'#F4F5F2')
    draw=ImageDraw.Draw(canvas)
    order=np.argsort((w@view).mean(axis=1))
    order=order[(normal@view)[order]>0.00001]
    base=np.array([168,180,179])
    for i in order:
        color=tuple(np.clip(base*shade[i]+6,0,255).astype(int))
        draw.polygon([tuple(p) for p in xy[i]],fill=color)
    canvas=canvas.resize(size,Image.Resampling.LANCZOS)
    canvas.save(target)

def font(size,bold=False):
    p='/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf'
    return ImageFont.truetype(p,size)

def comparison():
    canvas=Image.new('RGB',(2000,1620),'#F4F5F2');d=ImageDraw.Draw(canvas)
    d.text((85,50),'A LITTLE MORE PERSONALITY',font=font(24,True),fill='#657A77')
    d.text((85,91),'Two new bin buddies',font=font(58,True),fill='#263C39')
    d.text((85,169),'Bigger cheeks. Shorter legs. A proper little wave.',font=font(29),fill='#586965')
    for i,(name,title) in enumerate(NAMES):
        x=55+i*1000
        pic=Image.open(ROOT/'images'/f'{name}_Character.png').resize((910,1010),Image.Resampling.LANCZOS)
        canvas.paste(pic,(x+20,275))
        d.text((x+50,235),title,font=font(40,True),fill='#263C39')
        desc='Chunky hard hat + heart badge' if i==0 else 'Tilted cap + heart-pocket overalls'
        d.text((x+50,1305),desc,font=font(26),fill='#586965')
    d.line([(1000,255),(1000,1365)],fill='#D8DFDA',width=2)
    d.rounded_rectangle((85,1430,1915,1545),radius=22,fill='#E6EBE5')
    d.text((120,1465),'Actual printable CAD  /  Same handle collar  /  Physical flip test still needed',font=font(29),fill='#425A52')
    canvas.save(ROOT/'images/Bin_Buddies_Comparison.png')

def package(v,name,title):
    with zipfile.ZipFile(ROOT/'source/P1S_PETG_Template.3mf') as z:
        files={n:z.read(n) for n in z.namelist()}
    NS='http://schemas.microsoft.com/3dmanufacturing/core/2015/02'
    ET.register_namespace('',NS)
    model=ET.fromstring(files['3D/3dmodel.model'])
    def tag(s):return '{'+NS+'}'+s
    for m in model.findall(tag('metadata')):
        if m.attrib['name']=='Title':m.text=title
        if m.attrib['name']=='Description':m.text='Rounder original character; unchanged original collar and lid-contact arm.'
    obj=model.find('.//'+tag('object'));obj.set('name',title)
    oldmesh=obj.find(tag('mesh'));obj.remove(oldmesh)
    newmesh=ET.SubElement(obj,tag('mesh'));vertices=ET.SubElement(newmesh,tag('vertices'));triangles=ET.SubElement(newmesh,tag('triangles'))
    unique,inv=np.unique(v.reshape(-1,3),axis=0,return_inverse=True)
    for p in unique:ET.SubElement(vertices,tag('vertex'),dict(zip(['x','y','z'],[f'{n:.6f}' for n in p])))
    for a,b,c in inv.reshape(-1,3):ET.SubElement(triangles,tag('triangle'),{'v1':str(a),'v2':str(b),'v3':str(c)})
    # Center the supplied print orientation, keeping its minimum Z on the plate.
    lo=v.min(axis=(0,1));hi=v.max(axis=(0,1));center=(lo+hi)/2
    item=model.find('.//'+tag('item'));item.set('transform',f'1 0 0 0 1 0 0 0 1 {128-center[0]:.5f} {128-center[1]:.5f} {-lo[2]:.5f}')
    files['3D/3dmodel.model']=ET.tostring(model,encoding='utf-8',xml_declaration=True)
    conf=ET.fromstring(files['Metadata/model_settings.config'])
    for m in conf.iter('metadata'):
        if m.get('key') in ['name','plater_name']:m.set('value',title)
        if 'face_count' in m.attrib:m.set('face_count',str(len(v)))
    for m in conf.iter('mesh_stat'):m.set('face_count',str(len(v)))
    files['Metadata/model_settings.config']=ET.tostring(conf,encoding='utf-8',xml_declaration=True)
    settings=json.loads(files['Metadata/project_settings.config'])
    settings['print_settings_id']=title+' 0.20mm PETG P1S'
    files['Metadata/project_settings.config']=json.dumps(settings,indent=2).encode()
    out=ROOT/f'{name}_P1S_PETG_Prepared.3mf'
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for n,data in files.items():z.writestr(n,data)
    with zipfile.ZipFile(out) as z:assert z.testzip() is None

def main():
    results={}
    original=analyze(mesh(ROOT/'source/Bindicator_Original_Geometry.stl'))
    pivot=np.array([35.224,-26.827])
    old_a=np.arctan2(*(np.array(original['center_of_mass_mm'][:2])-pivot)[::-1])
    for name,title in NAMES:
        v=mesh(ROOT/f'{name}.stl')
        r=analyze(v)
        assert r['bounds_mm'][0][2] >= -0.001, 'Printed orientation must rest flat on the original collar.'
        angle=np.arctan2(*(np.array(r['center_of_mass_mm'][:2])-pivot)[::-1])
        r['static_balance_direction_change_deg']=round(float(np.degrees(angle-old_a)),2)
        r['physical_flip_tested']=False
        r['sha256']=hashlib.sha256((ROOT/f'{name}.stl').read_bytes()).hexdigest()
        results[name]=r
        print(name,json.dumps(r),flush=True)
        render(v,ROOT/'images'/f'{name}_Preview.png')
        render(v,ROOT/'images'/f'{name}_Character.png',size=(1000,1100),crop=True)
        package(v,name,title)
    (ROOT/'validation/mesh-validation.json').write_text(json.dumps(results,indent=2)+'\n')
    comparison()

if __name__=='__main__':main()
