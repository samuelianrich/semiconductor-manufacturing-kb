#!/usr/bin/env python3
"""Original editable SVG schematics; geometry is conceptual, not a vendor design."""
from pathlib import Path
from html import escape
import textwrap
ROOT=Path(__file__).resolve().parents[1]
INK='#17334a'; TEAL='#007c83'; SI='#d0e6ec'; GATE='#3c66a0'; OX='#f2b562'; RED='#ba4661'; LIGHT='#f3f7fa'
class SVG:
 def __init__(self,title,desc,sources):
  self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="{INK}"/></marker></defs><rect width="1200" height="720" fill="white"/>']
  self.text(40,55,title,32,bold=True);self.text(40,90,'Conceptual schematic • not to scale • original illustration',18,color='#506575')
  self.text(40,675,'Source basis: '+sources,16,color='#506575');self.text(40,703,'Semiconductor Manufacturing Knowledge Base • CC BY 4.0',15,color='#506575')
 def text(self,x,y,t,size=22,bold=False,color=INK,anchor='start'):
  self.parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}" text-anchor="{anchor}">{escape(t)}</text>')
 def paragraph(self,x,y,t,width=34,size=20,color=INK):
  for j,line in enumerate(textwrap.wrap(t,width=width)):self.text(x,y+j*(size+7),line,size,color=color)
 def rect(self,x,y,w,h,fill=LIGHT,stroke=INK,r=8):self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
 def line(self,x1,y1,x2,y2,color=INK,width=3,arrow=False,dash=False):self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="8 6"' if dash else '')+'/>')
 def circle(self,x,y,r=10,fill=TEAL):self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')
 def ellipse(self,x,y,rx,ry,fill=SI,stroke=INK):self.parts.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
 def box(self,x,y,w,h,title,subtitle='',fill=LIGHT):
  self.rect(x,y,w,h,fill);self.paragraph(x+16,y+32,title,max(12,int(w/12)),22)
  if subtitle:self.paragraph(x+16,y+h-50,subtitle,max(12,int(w/11)),18,color='#506575')
 def save(self,path):
  p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('\n'.join(self.parts)+'</svg>\n')

s=SVG('Silica to silicon: furnace functions','Quartz and carbon enter a furnace. Electrodes deliver energy. Hot reaction regions produce tapped silicon and an off-gas stream.','NTNU-SMELTING-001')
s.rect(300,220,490,345,fill='#eee8e1');s.rect(330,370,430,160,fill='#efb46a');s.text(362,460,'Hot reacting charge',26,bold=True)
for x in [400,525,650]:s.rect(x,165,28,230,fill='#566372',r=0)
s.text(385,135,'Electrical input / electrodes',22);s.line(555,145,555,165,arrow=True)
s.box(35,195,205,115,'Quartz + carbon','Prepared charge');s.line(240,260,315,305,arrow=True)
s.line(790,470,1010,470,arrow=True);s.text(825,440,'Tap liquid silicon',22);s.text(825,505,'Cool and handle product',19)
s.line(755,240,980,200,arrow=True);s.text(870,160,'Off-gas handling',22);s.text(830,235,'Reaction products and entrained material',17)
s.text(330,595,'Lining and reaction-zone geometry vary by furnace',20)
s.save('assets/equipment/silicon_furnace.svg')

s=SVG('Purify a silicon compound, then recover silicon','Silicon feed undergoes chemical conversion, distillation and deposition. The product is polysilicon; a separate alternative reactor route uses silane and granules.','WACKER-POLY-001; HSC-POLY-001; REC-FBR-001')
items=[('Metallurgical Si','Starting solid'),('Chemical conversion','Crude chlorosilanes'),('Distillation','Purified precursor'),('Deposition','Polysilicon product')]
for j,(t,b) in enumerate(items):
 x=30+j*295;s.box(x,210,245,160,t,b,SI if j in (0,3) else LIGHT)
 if j<3:s.line(x+245,285,x+280,285,arrow=True)
s.text(345,415,'Desired species separate from impurity-bearing streams',22)
s.box(850,510,300,105,'Alternative deposition','Silane → growing granules')
s.line(875,465,440,465,arrow=True,dash=True);s.text(485,505,'Conditioned recovery/recycle streams',20)
s.paragraph(45,510,'Functional map only: real plants contain additional reactions, separations, cleaning and packaging.',50,21)
s.save('assets/process_flows/purification.svg')

s=SVG('Single-crystal growth: CZ and float-zone','CZ draws a seed-oriented crystal from a crucible melt. Float-zone growth passes a localized melt through a feed rod without a crucible contacting the melt.','PVA-CZ-001; SUMCO-WAFER-001; SILTRONIC-FZ-001')
s.text(80,150,'Czochralski (CZ)',27,bold=True);s.text(675,150,'Float zone (FZ)',27,bold=True);s.line(600,130,600,630,color='#c2d2da',width=2)
s.rect(100,360,340,195,fill='#ede5da');s.rect(120,395,300,135,fill='#f4c77d');s.text(145,480,'Silicon melt',22)
s.rect(245,230,65,185,fill=SI);s.rect(263,185,29,45,fill=SI);s.line(279,178,279,150,arrow=True)
s.line(320,285,510,285);s.text(343,270,'Growing crystal',20);s.text(86,588,'Crucible + surrounding hot zone',21)
s.text(55,330,'Seed',19);s.line(105,325,263,205,width=2)
s.rect(835,200,95,145,fill='#c6ccd4');s.ellipse(882,367,60,27,fill='#f4c77d');s.rect(845,392,75,165,fill=SI)
s.rect(790,352,185,14,fill=GATE,r=2);s.rect(790,383,185,14,fill=GATE,r=2)
s.text(960,245,'Feed rod',21);s.line(928,255,950,255,width=2)
s.text(680,325,'Induction coil',20);s.line(800,330,808,352,width=2)
s.text(960,435,'Crystal',20);s.line(925,440,950,440,width=2)
s.text(687,591,'Localized melt; no contacting crucible',20)
s.save('assets/equipment/crystal_growth.svg')

s=SVG('Wafer preparation: geometry, surface and acceptance','Ingot shaping and orientation precede slicing, edge preparation, face finishing, cleaning and inspection; measured acceptance determines disposition.','SUMCO-WAFER-001; SILTRONIC-WAFER-001')
for j,(t,b) in enumerate([('Shape and orient','Select usable ingot'),('Slice','Allow for kerf'),('Prepare edge','Control edge profile'),('Prepare faces','Lap / etch / polish')]):
 x=30+j*295;s.box(x,190,250,130,t,b)
 if j<3:s.line(x+250,255,x+280,255,arrow=True)
s.line(1050,330,1050,405,arrow=True);s.box(930,420,230,125,'Clean + inspect','Measure required properties')
s.line(925,485,815,485,arrow=True);s.box(570,420,235,125,'Disposition','Accept / segregate / reject',SI)
s.line(565,485,455,485,arrow=True);s.text(460,465,'Accept only',16);s.box(40,420,400,125,'Accepted starting wafer','Specification + identity + clean handling',SI)
s.paragraph(55,602,'Specialized epitaxial and SOI wafers have additional routes. This flow does not impose every listed tool on every wafer.',105,20)
s.save('assets/process_flows/wafer_finishing.svg')

s=SVG('Energy bands: allowed states and mobile carriers','Energy is vertical. A conduction electron and a valence-band hole are shown as an excitation across the band gap; the gap is not physical empty space.','HU-PHYSICS-001; MIT-CARRIERS-001')
s.line(130,580,130,175,arrow=True);s.text(55,150,'Energy',23,bold=True)
s.rect(235,180,640,140,fill=SI,stroke=SI);s.rect(235,445,640,130,fill='#c4d6ee',stroke='#c4d6ee')
s.line(235,320,875,320,width=3);s.line(235,445,875,445,width=3)
s.text(910,326,'Ec',24);s.text(910,451,'Ev',24);s.text(285,220,'Conduction band',26,bold=True);s.text(285,545,'Valence band',26,bold=True)
s.line(560,475,560,278,arrow=True);s.circle(560,266,12);s.ellipse(560,484,12,12,fill='white',stroke=RED)
s.text(595,275,'Electron',22);s.text(595,490,'Hole',22);s.text(285,390,'Band gap Eg = Ec − Ev',23)
s.paragraph(60,625,'The vertical axis is energy. This is not a drawing of physical layers or a crack in the wafer.',100,20)
s.save('assets/cross_sections/energy_bands.svg')

s=SVG('PN junction: fixed charge creates an internal field','P region left and N region right. Negative ionized acceptors sit on the p-side depletion region; positive donors on the n side. The electric field points right to left.','HU-PN-001; MIT-JUNCTION-001')
s.rect(95,240,500,240,fill='#f4dce1');s.rect(595,240,500,240,fill='#d6e6f4');s.rect(460,240,270,240,fill='#fff4dc')
s.text(210,210,'p-type region',27,bold=True);s.text(805,210,'n-type region',27,bold=True)
for x,sign,col in [(500,'−',RED),(550,'−',RED),(635,'+',GATE),(685,'+',GATE)]:
 for y in [290,355,420]:s.text(x,y,sign,30,bold=True,color=col,anchor='middle')
s.line(460,500,730,500,width=2);s.line(460,490,460,510,width=2);s.line(730,490,730,510,width=2);s.text(460,545,'Depletion region',25,bold=True)
s.line(715,165,475,165,arrow=True);s.text(515,140,'Electric field',22)
s.paragraph(60,580,'Fixed acceptor ions: negative. Fixed donor ions: positive. At equilibrium, drift and diffusion currents balance.',105,22)
s.save('assets/cross_sections/pn_junction.svg')

s=SVG('MOS gate control and an n-channel transistor','A p-body MOS capacitor moves through accumulation, depletion and inversion; a longitudinal nMOS section adds n+ source and drain and an induced electron channel.','HU-MOS-001; MIT-MOS-001; MIT-MOSFET-001')
for j,(t,bias,charges) in enumerate([('Accumulation','Relative gate bias: negative','+  +  +  +'),('Depletion','More positive gate bias','−  −  −  −'),('Inversion','Sufficient positive bias','electrons at surface')]):
 x=40+j*395;s.text(x,140,t,25,bold=True);s.rect(x,170,330,35,fill=GATE);s.rect(x,205,330,12,fill=OX,r=0);s.rect(x,217,330,90,fill=SI,r=0);s.text(x+35,255,charges,23);s.text(x+35,287,['Mobile holes','Fixed acceptor ions','Mobile electrons'][j],17);s.text(x,335,bias,18)
s.text(45,400,'Longitudinal nMOS cross section',24,bold=True);s.rect(170,490,740,130,fill=SI)
s.rect(345,430,385,43,fill=GATE);s.rect(345,473,385,17,fill=OX,r=0);s.rect(195,490,150,60,fill='#aac7e5',r=0);s.rect(730,490,150,60,fill='#aac7e5',r=0)
s.text(228,525,'n+ source',19);s.text(758,525,'n+ drain',19);s.text(450,584,'p-type body',22)
s.line(347,500,727,500,color=TEAL,width=6);s.text(425,535,'Induced electron channel',19)
s.text(785,442,'Gate conductor',19);s.line(730,450,780,450,width=2);s.text(952,488,'Dielectric',18);s.line(731,479,945,479,width=2)
s.save('assets/cross_sections/mos_device.svg')

s=SVG('CMOS inverter: complementary pull-up and pull-down','Input drives pMOS and nMOS gates. pMOS connects output toward VDD; nMOS toward ground. An output capacitance is shown at the shared node.','MIT-CMOS-001; MIT-POWER-001')
s.text(490,145,'VDD',25,bold=True);s.line(515,155,515,210)
s.box(420,210,190,100,'pMOS','Pull-up',SI);s.box(420,450,190,100,'nMOS','Pull-down',SI)
s.line(515,310,515,450);s.circle(515,380,6,INK);s.line(515,550,515,602);s.line(475,602,555,602);s.line(490,615,540,615);s.line(502,628,528,628)
s.text(55,388,'Input',26,bold=True);s.line(150,380,290,380);s.line(290,260,290,500);s.line(290,260,420,260);s.line(290,500,420,500)
s.line(515,380,1020,380,arrow=True);s.text(970,355,'Output',25,bold=True);s.line(825,380,825,475);s.line(780,475,870,475);s.line(780,491,870,491);s.line(825,491,825,588);s.line(792,588,858,588);s.text(893,490,'CL',24)
s.text(40,190,'Input low → output high',21);s.text(40,220,'Input high → output low',21)
s.save('assets/diagrams/cmos_inverter.svg')

s=SVG('Transistor cross sections: how the gate reaches the channel','Cross sections normal to current compare a surface gate, a gate around three exposed fin faces, and a surrounding gate around stacked nanosheet channels.','HU-SCALING-001; IBM-NANOSHEET-001')
for x,t in [(40,'Planar'),(435,'FinFET'),(830,'Nanosheet GAA')]:s.text(x+15,150,t,27,bold=True)
# Planar: substrate beneath a top dielectric/conductor.
s.rect(65,360,290,200,fill=SI,r=0);s.rect(95,335,230,25,fill=OX,r=0);s.rect(95,280,230,55,fill=GATE,r=0);s.text(120,425,'Silicon body',22)
# Fin, dielectric around top and sides, then U-shaped gate.
s.rect(455,505,310,55,fill=SI,r=0);s.rect(535,275,150,230,fill=GATE,r=0);s.rect(558,298,104,207,fill=OX,r=0);s.rect(575,315,70,190,fill=SI,r=0);s.rect(455,505,120,18,fill=OX,r=0);s.rect(645,505,120,18,fill=OX,r=0)
# GAA: blue block with dielectric rings and silicon cores.
s.rect(890,230,240,325,fill=GATE,r=8)
for y in [280,365,450]:s.rect(916,y,188,55,fill=OX,r=12);s.rect(932,y+12,156,31,fill=SI,r=8)
s.text(45,595,'Current: into / out of page',23);s.text(45,630,'Conductor',19,color=GATE);s.rect(157,613,30,20,fill=GATE,r=0);s.text(220,630,'Dielectric',19,color='#a36314');s.rect(323,613,30,20,fill=OX,r=0);s.text(390,630,'Silicon',19);s.rect(465,613,30,20,fill=SI,r=0)
s.save('assets/cross_sections/transistor_geometries.svg')
print('Wrote 9 original SVG figures.')
