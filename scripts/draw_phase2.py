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

s=SVG('Fab processing: repeated interfaces, not one fixed recipe','Film formation, patterning, transfer and surface preparation repeat with measurement gates; deposition and implant are alternative functions.','HU-FAB-001; MACK-QUALITY-001; MACK-CMP-001')
for x,t,b in [(40,'Form a film','Add or grow material'),(345,'Pattern resist','Define protected regions'),(650,'Transfer pattern','Etch or implant'),(955,'Prepare surface','Strip / clean')]:
 s.box(x,180,210,170,t,b)
 if x<955:s.line(x+210,260,x+293,260,arrow=True)
s.line(1060,350,1060,435);s.line(1060,435,145,435);s.line(145,435,145,350,arrow=True)
s.text(310,420,'Repeat only as required by the integration flow',23)
s.box(290,495,620,120,'Measure, inspect and decide','Accept / investigate / qualified rework or disposition',SI)
s.line(600,435,600,490,color=TEAL,dash=True,arrow=True)
s.text(40,140,'Input: compatible wafer state → Output: qualified patterned state',23)
s.save('assets/process_flows/fab_loops.svg')

s=SVG('Positive-tone resist → etched oxide → strip','Three cross-sections show an opening in resist, oxide removal through that opening, and remaining patterned oxide after resist strip. Silicon is retained in this teaching example.','MACK-QUALITY-001; LAM-ETCH-001; UBC-CLEAN-001')
for j,title in enumerate(['1. Developed resist','2. Transfer into oxide','3. Strip resist']):
 x=45+395*j;s.text(x,170,title,24,bold=True);s.rect(x,380,320,110,SI,r=0)
 if j==0:s.rect(x,340,320,40,OX,r=0)
 else:
  s.rect(x,340,110,40,OX,r=0);s.rect(x+210,340,110,40,OX,r=0)
 if j<2:
  s.rect(x,280,110,60,RED,r=0);s.rect(x+210,280,110,60,RED,r=0)
 s.text(x+100,445,'Silicon',21)
 if j<2:s.line(x+330,380,x+375,380,arrow=True)
s.text(45,225,'Exposed positive resist removed',19);s.text(443,225,'Etch exposed oxide',19);s.text(840,225,'Oxide pattern remains',19)
for x in [580,605,630]:s.line(x,270,x,365,arrow=True,color=TEAL)
s.rect(50,550,28,22,RED,r=0);s.text(90,570,'Resist',21);s.rect(250,550,28,22,OX,r=0);s.text(290,570,'Oxide',21)
s.text(50,620,'Teaching route: selectivity and compatibility must preserve the intended remaining layers.',21)
s.save('assets/process_flows/lithography_transfer.svg')

s=SVG('Deposition: transport and reaction are different choices','Three panels show directional sputtered flux, precursor reaction at a heated surface, and alternating ALD exposure and purge steps.','LESKER-PVD-001; ASM-FURNACE-001; ASM-ALD-001')
for x,t in [(40,'Sputter PVD'),(440,'Thermal CVD'),(840,'ALD cycle')]:s.text(x,160,t,27,bold=True)
s.rect(60,205,280,30,GATE,r=0);s.text(115,195,'Target',21)
for x in [95,160,225,290]:s.line(x,250,x+25,365,arrow=True)
s.rect(65,400,275,40,SI,r=0);s.rect(65,388,275,12,OX,r=0)
s.text(60,475,'Ejected target atoms',21);s.paragraph(60,515,'Feature geometry can screen directional flux.',24,21)
s.rect(450,230,285,220,LIGHT);s.rect(475,395,235,35,SI,r=0)
for x in [495,550,605,660]:s.circle(x,290,9,TEAL);s.line(x,315,x,380,arrow=True)
s.text(470,485,'Gas → surface reaction',21);s.paragraph(450,525,'Temperature and transport affect the resulting film.',25,21)
for j,t in enumerate(['A exposure','Purge','B exposure','Purge']):
 s.box(850,210+j*85,280,65,t)
 if j<3:s.line(990,275+j*85,990,287+j*85,arrow=True)
s.text(850,605,'Repeat calibrated cycles',21)
s.save('assets/equipment/deposition_methods.svg')

s=SVG('Etch: mask budget, direction and the final profile','A mask protects the target film while ions and reactive species access an opening. A separate profile comparison distinguishes vertical removal from lateral undercut.','LAM-ETCH-001; TUWIEN-BOSCH-001')
s.text(55,155,'RIE functional cross-section',27,bold=True)
s.rect(70,480,455,75,SI,r=0);s.rect(70,340,160,140,OX,r=0);s.rect(365,340,160,140,OX,r=0)
s.rect(70,290,160,50,RED,r=0);s.rect(365,290,160,50,RED,r=0)
for x in [263,297,331]:s.line(x,185,x,460,arrow=True,color=TEAL)
s.text(65,600,'Mask (pink) • target (gold) • underlayer (blue)',20)
s.text(630,155,'Profile comparison',27,bold=True)
s.rect(650,260,480,120,OX,r=0);s.rect(800,245,150,140,'white',stroke='white',r=0)
s.text(670,420,'Directional removal: small lateral loss',22)
s.rect(650,475,480,105,OX,r=0);s.rect(765,465,220,120,'white',stroke='white',r=0)
s.rect(650,450,150,25,RED,r=0);s.rect(950,450,180,25,RED,r=0)
s.text(670,620,'Undercut: removal extends beneath mask',21)
s.save('assets/equipment/etch_profiles.svg')

s=SVG('Implantation: ion delivery followed by activation','Source, selection, acceleration and scan functions deliver ions to a masked wafer. A separate thermal step changes activation and repairs damage.','MIT-IMPLANT-001; HU-FAB-001; NPTEL-CHANNEL-001')
for j,(t,b) in enumerate([('Ion source','Generate ions'),('Select species','Mass / charge'),('Accelerate + scan','Energy / area'),('Masked wafer','Dose delivered')]):
 x=35+j*300;s.box(x,200,250,150,t,b)
 if j<3:s.line(x+250,275,x+287,275,arrow=True)
s.rect(140,475,375,90,SI,r=0);s.rect(140,440,100,35,RED,r=0);s.rect(420,440,95,35,RED,r=0)
for x in [275,315,355,395]:s.line(x,395,x,495,arrow=True,color=TEAL);s.circle(x,520+(x%3)*8,5,RED)
s.text(140,605,'Delivered atoms + lattice damage',21)
s.line(555,515,685,515,arrow=True);s.box(720,425,400,165,'Qualified thermal exposure','Activation / repair / redistribution',OX)
s.save('assets/equipment/implantation.svg')

s=SVG('Thermal oxidation consumes the silicon surface','A 100 nm illustrative oxide extends 55.9 nm above the old surface and consumes 44.1 nm of silicon below it, using a planar density-based mass balance.','UALBERTA-OXIDE-001; HU-FAB-001')
s.rect(120,350,400,220,SI,r=0);s.text(190,460,'Silicon before growth',25)
s.rect(680,405,400,165,SI,r=0);s.rect(680,280,400,125,OX,r=0)
s.line(80,350,1140,350,dash=True,width=2);s.text(135,320,'Original surface reference',22)
s.text(755,335,'Oxide',25,bold=True);s.text(775,495,'Silicon',25)
s.line(600,280,600,405,width=2);s.line(585,280,615,280);s.line(585,405,615,405)
s.text(555,240,'100 nm',23)
s.text(720,205,'55.9 nm above original surface',21);s.line(850,218,850,280,arrow=True)
s.text(710,625,'44.1 nm Si consumed below original surface',21);s.line(705,590,705,405,arrow=True)
s.save('assets/diagrams/oxidation_geometry.svg')

s=SVG('Cleaning qualifies a surface for its next operation','Contaminants enter through air, handling, chemicals and equipment. Cleaning is chosen for the incoming material stack and verified before downstream use.','STANFORD-CLEAN-001; UBC-CLEAN-001; UBC-RCA-001')
for j,t in enumerate(['Particles','Organic residue','Metals / history']):
 s.box(45,165+j*140,255,100,t);s.line(300,215+j*140,435,350,arrow=True)
s.box(455,265,300,175,'Compatible clean','Removal + rinse + dry',SI)
s.line(755,350,830,350,arrow=True);s.box(855,265,300,175,'Verify output','Residues / loss / damage',OX)
s.paragraph(65,600,'Air cleanliness does not establish chemical or tool compatibility.',49,21)
s.text(455,175,'Known incoming material stack',22);s.line(605,190,605,255,arrow=True)
s.text(845,510,'Next operation receives',21);s.text(845,540,'a qualified surface state',21)
s.save('assets/process_flows/cleaning_interfaces.svg')

s=SVG('CMP: coupled chemistry, contact and local geometry','A loaded wafer contacts a pad supplied with slurry. The right cross-section illustrates a recessed feature; text distinguishes this dishing from erosion of a patterned region.','AMAT-CMP-001; EBARA-CMP-001; MACK-CMP-001')
s.rect(120,345,475,45,GATE,r=0);s.rect(120,390,475,95,LIGHT,r=0);s.text(240,458,'Moving platen / pad',22)
s.rect(240,275,235,45,SI,r=0);s.rect(240,320,235,25,OX,r=0)
for x in [275,345,415]:s.line(x,190,x,268,arrow=True)
s.text(245,170,'Applied load',24)
s.line(60,285,200,345,arrow=True,color=TEAL);s.text(45,250,'Slurry',23)
s.line(155,520,550,520,arrow=True);s.text(200,560,'Relative sliding motion',22)
s.text(700,180,'Local geometry after polishing',24,bold=True)
s.rect(720,320,400,80,SI,r=0);s.rect(720,290,140,30,OX,r=0);s.rect(980,290,140,30,OX,r=0);s.rect(860,307,120,93,GATE,r=0)
s.text(790,450,'Dishing: feature recessed',21);s.line(920,420,920,310,arrow=True)
s.text(700,530,'Erosion: patterned region lowered',21);s.paragraph(700,570,'Measure local height as well as average remaining film.',35,20)
s.save('assets/equipment/cmp.svg')

s=SVG('Measurement → evidence → process decision','Measurement is interpreted with model and sampling context before comparing specifications and statistical baseline, investigating excursions and deciding disposition.','NIST-SPC-001; NIST-CAPABILITY-001; NIST-ELLIPSO-001')
for j,(t,b) in enumerate([('Define measurand','Property / units / sites'),('Measure + calibrate','Method / uncertainty'),('Interpret evidence','Model / sample limits'),('Decide disposition','Accept or investigate')]):
 x=30+j*300;s.box(x,180,255,170,t,b,SI if j<2 else LIGHT)
 if j<3:s.line(x+255,265,x+285,265,arrow=True)
s.box(85,450,465,150,'Product specification','Does measured output meet a requirement?',OX)
s.box(655,450,465,150,'Statistical control limits','Does behavior differ from the baseline?',SI)
s.text(280,410,'These are different questions; passing one does not imply the other.',21)
s.save('assets/process_flows/metrology_control.svg')
