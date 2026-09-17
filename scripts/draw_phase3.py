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

s=SVG('Planar and fin devices: distinguish the section direction','Left: longitudinal planar section with source and drain separated by a gated channel. Right: transverse tri-gate fin section with dielectric separating the gate and silicon; current is normal to the page.','AGH-CMOS-001; INTEL-FLOW-001')
s.text(45,150,'Planar: along current path',26,bold=True);s.text(665,150,'Fin: across channel under gate',26,bold=True)
s.rect(60,380,485,185,SI,r=0);s.rect(60,380,65,150,OX,r=0);s.rect(480,380,65,150,OX,r=0)
s.rect(150,380,120,65,TEAL,r=0);s.rect(355,380,100,65,TEAL,r=0)
s.rect(270,362,85,18,OX,r=0);s.rect(270,265,85,97,GATE,r=0)
s.rect(245,320,25,60,LIGHT,r=0);s.rect(355,320,25,60,LIGHT,r=0)
s.text(155,470,'Source',20);s.text(372,470,'Drain',20);s.text(276,247,'Gate',21)
s.line(280,405,343,405,arrow=True);s.text(205,515,'Body / well',23)
s.text(56,605,'STI at sides; gate dielectric is gold',20)
s.rect(710,490,390,75,SI,r=0);s.rect(710,455,145,35,OX,r=0);s.rect(965,455,135,35,OX,r=0)
s.rect(820,245,180,210,GATE,r=0);s.rect(845,270,130,220,OX,r=0);s.rect(860,285,100,205,SI,r=0)
s.text(866,390,'Fin',24);s.circle(910,425,8,INK)
s.text(710,205,'Gate wraps top + both sides',22);s.text(710,610,'● Channel current normal to page',20)
s.save('assets/diagrams/planar_finfet_sections.svg')

s=SVG('Nanosheets: sacrificial layers become gate access','Three transverse channel sections show alternating retained silicon and sacrificial SiGe, released silicon sheets and an insulated surrounding gate. Source/drain anchors are outside this section.','IMEC-SHEETS-001; IBM-GAA-001')
for j,title in enumerate(['1. Patterned stack','2. Released sheets','3. Surrounding gate']):
 x=45+j*400;s.text(x,155,title,25,bold=True)
 if j==2:s.rect(x+10,245,285,265,GATE,r=0)
 for n in range(3):
  y=270+n*80
  if j==2:s.rect(x+45,y-12,215,59,OX,r=5)
  s.rect(x+60,y,185,35,SI,r=0)
  if j==0 and n<2:s.rect(x+60,y+35,185,45,RED,r=0)
 s.text(x+30,555,['Si / sacrificial SiGe','Si retained; SiGe removed','Dielectric separates Si / gate'][j],18)
 if j<2:s.line(x+310,375,x+375,375,arrow=True)
s.rect(80,595,22,20,SI,r=0);s.text(112,613,'Si',19);s.rect(205,595,22,20,RED,r=0);s.text(237,613,'Sacrificial SiGe',19);s.rect(475,595,22,20,OX,r=0);s.text(507,613,'Gate dielectric',19);s.rect(730,595,22,20,GATE,r=0);s.text(762,613,'Gate conductor',19)
s.text(48,205,'Across channel; source/drain anchors and inner spacers are out of plane',22)
s.save('assets/process_flows/nanosheet_release.svg')

s=SVG('MOL contacts: reach each terminal without crossing insulation','A longitudinal illustrative planar device shows separate source/drain and gate contact plugs through dielectric. Source/drain interface layers are distinct from the gate dielectric.','IMEC-CONTACT-001; AMAT-W-001')
s.rect(110,445,790,140,SI,r=0);s.rect(110,180,790,265,LIGHT,r=0)
s.rect(195,445,200,65,TEAL,r=0);s.rect(620,445,200,65,TEAL,r=0)
s.rect(415,425,180,20,OX,r=0);s.rect(415,335,180,90,GATE,r=0);s.rect(390,350,25,95,OX,r=0);s.rect(595,350,25,95,OX,r=0)
for x in [265,705]:s.rect(x,225,55,210,GATE,r=0);s.rect(x-8,435,71,10,RED,r=0)
s.rect(480,225,55,110,GATE,r=0)
s.text(225,155,'Source contact',22);s.text(450,155,'Gate contact',22);s.text(680,155,'Drain contact',22)
s.text(221,548,'Source region',22);s.text(651,548,'Drain region',22)
s.text(935,280,'Interlayer',22);s.text(935,310,'dielectric',22);s.line(920,325,855,340,arrow=True)
s.text(110,625,'Pink: prepared source/drain interface • Gold under gate: insulating gate dielectric',20)
s.save('assets/diagrams/mol_contacts.svg')

s=SVG('A wire is a distributed resistance and capacitance','Left: conductor length and cross-section define resistance. Right: series resistor segments and shunt capacitors represent a uniform RC wire; each segment has its own length.','HARRIS-RC-001')
s.text(50,160,'Geometry and units',26,bold=True)
s.rect(75,260,395,90,GATE,r=0);s.line(75,230,470,230);s.text(230,215,'L',23)
s.rect(150,435,155,90,GATE,r=0);s.text(199,564,'width w',22);s.text(325,490,'height h',22)
s.text(50,610,'R = ρL / (w h) • r = R/L in Ω/m',23)
s.text(615,160,'Small segments along the route',26,bold=True)
for j in range(3):
 x=630+j*175;s.line(x,280,x+30,280);s.rect(x+30,262,75,36,LIGHT,r=0);s.line(x+105,280,x+175,280)
 s.text(x+40,245,'r ΔL',20);s.circle(x+140,280,4,INK);s.line(x+140,280,x+140,365)
 s.line(x+112,365,x+168,365);s.line(x+112,379,x+168,379);s.line(x+140,379,x+140,435)
 s.line(x+112,435,x+168,435);s.line(x+120,445,x+160,445);s.line(x+128,455,x+152,455);s.text(x+102,495,'c ΔL',20)
s.text(605,555,'Grounded-capacitance approximation',21);s.text(605,595,'Coupling to switching neighbors needs more detail',19)
s.save('assets/diagrams/wire_rc.svg')

s=SVG('The conducting core and its surrounding interfaces','Left: a liner consumes some cross-sectional area while providing needed interface functions. Right: conceptual void, bridge and dielectric failure paths are distinct.','IBM-LINER-001; IBM-BEOL-001; STANFORD-EM-001')
s.text(45,160,'Integrated line cross-section',26,bold=True)
s.rect(80,230,400,330,LIGHT,r=0);s.rect(160,285,240,220,RED,r=0);s.rect(180,285,200,200,GATE,r=0)
s.text(218,413,'Core',24,color='white');s.text(60,610,'Liner/barrier functions use part of the opening',20)
s.text(650,160,'Different defect mechanisms',26,bold=True)
s.rect(675,250,420,60,GATE,r=0);s.ellipse(860,280,50,25,fill='white');s.text(715,350,'Void reduces current-carrying area',21)
s.rect(675,420,420,35,GATE,r=0);s.rect(675,535,420,35,GATE,r=0);s.rect(790,455,24,80,GATE,r=0)
s.line(970,460,970,527,color=RED,dash=True,arrow=True)
s.text(670,620,'Bridge (solid) ≠ dielectric leakage path (dashed)',20)
s.save('assets/diagrams/interconnect_reliability.svg')

s=SVG('Devices → contacts → multilevel wiring → terminal','A schematic four-level interconnect stack with selected vias above a device/contact boundary and a top terminal opening. No product-specific layer count or terminal design is implied.','HU-FAB-001; IBM-BEOL-001')
s.rect(90,210,720,380,LIGHT,r=0);s.rect(90,590,720,45,SI,r=0)
levels=[(520,[(140,250),(505,220)]),(420,[(225,465)]),(315,[(140,200),(455,280)]),(210,[(225,440)])]
for n,(y,segments) in enumerate(levels,1):
 for x,w in segments:s.rect(x,y,w,35,GATE,r=0)
 s.text(845,y+25,f'M{n}: wiring level',22)
for x,y,h in [(275,455,65),(550,455,65),(275,350,70),(525,350,70),(270,245,70),(505,245,70)]:s.rect(x,y,25,h,GATE,r=0)
for x in [195,610]:s.rect(x,555,28,35,TEAL,r=0);s.rect(x-25,590,80,20,TEAL,r=0)
s.rect(90,185,720,25,OX,r=0);s.rect(410,170,105,40,GATE,r=0)
s.text(90,145,'Terminal opening / top metallization',23);s.text(845,580,'MOL: terminal access',22);s.text(845,620,'FEOL: device regions',22)
s.text(90,665,'',16)
s.save('assets/diagrams/beol_stack.svg')

s=SVG('Dual damascene: pattern dielectric, fill, then planarize','Three section snapshots show a connected trench and via cavity landing on a lower conductor, lined and filled overburden, and the retained conductor after CMP.','IBM-BEOL-001; IBM-LINER-001; IBM-FILL-001; MACK-CMP-001')
for j,title in enumerate(['1. Trench + via cavity','2. Liner / seed + fill','3. CMP overburden']):
 x=35+j*400;s.text(x,155,title,24,bold=True);s.rect(x,265,330,290,LIGHT,r=0);s.rect(x+105,525,120,30,GATE,r=0)
 if j==0:
  s.rect(x+45,265,240,100,'white',stroke='white',r=0);s.rect(x+145,350,40,175,'white',stroke='white',r=0)
 else:
  s.rect(x+45,265,240,100,RED,r=0);s.rect(x+145,350,40,175,RED,r=0)
  s.rect(x+53,265,224,92,GATE,r=0);s.rect(x+153,350,24,167,GATE,r=0)
  if j==1:s.rect(x,225,330,40,GATE,r=0)
 if j<2:s.line(x+340,400,x+380,400,arrow=True)
 s.text(x+73,595,'Lower conductor',20)
s.text(45,205,'One illustrative added level; no fixed via-first / trench-first mask order',21)
s.save('assets/process_flows/dual_damascene.svg')
s=SVG('Nanosheet inner spacers: a section along the channels','Retained sheets join source and drain. Dielectric inner spacers separate gate material between sheets from the source/drain ends. Gate dielectric coats the channels in the gate region.','IMEC-SHEETS-001; IBM-GAA-001')
s.text(70,150,'Longitudinal conceptual section • channel current left ↔ right',24)
s.rect(180,255,150,280,TEAL,r=0);s.rect(870,255,150,280,TEAL,r=0)
s.rect(410,235,380,320,GATE,r=0)
for y in [285,370,455]:
 s.rect(410,y-10,380,50,OX,r=0);s.rect(330,y,540,30,SI,r=0)
for y in [315,400]:
 s.rect(330,y,80,55,RED,r=0);s.rect(790,y,80,55,RED,r=0)
s.text(190,215,'Source region',22);s.text(875,215,'Drain region',22);s.text(495,205,'Gate region',23)
s.text(445,595,'Pink: inner spacers between sheets',22)
s.line(430,580,370,355,arrow=True);s.line(800,580,830,435,arrow=True)
s.text(65,635,'Gate dielectric is gold; external spacers and other surrounding films are omitted.',20)
s.save('assets/diagrams/nanosheet_inner_spacers.svg')
