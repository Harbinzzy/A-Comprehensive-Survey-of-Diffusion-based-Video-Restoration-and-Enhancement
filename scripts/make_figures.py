"""Survey diagrams and attributed evidence figures.
Rebuild with Python and reportlab. Coordinates use final publication points.
"""
from pathlib import Path
from math import atan2, cos, sin
import random
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

OUT=Path(__file__).resolve().parents[1]/'figures'
OUT.mkdir(exist_ok=True)
INK='#20252C'; GRAY='#64717A'; LINE='#B3BDC5'
BLUE='#4776AD'; GREEN='#49856A'; ORANGE='#BD7545'; RED='#B65155'; PURPLE='#8468A3'
PB='#E4EDF7'; PG='#E6F0E7'; PO='#FAEBDD'; PP='#EEE8F4'

class F:
    def __init__(self,name,h):
        self.h=h;self.c=canvas.Canvas(str(OUT/(name+'.pdf')),pagesize=(516,h),pageCompression=1)
        self.c.setTitle(name.replace('_',' ').title());self.c.setAuthor('Survey authors')
    def text(self,x,y,s,size=9,col=INK,bold=False,center=False,italic=False):
        self.c.setFont('Times-Bold' if bold else 'Times-Italic' if italic else 'Times-Roman',size)
        self.c.setFillColor(HexColor(col))
        (self.c.drawCentredString if center else self.c.drawString)(x,self.h-y-size*.8,s)
    def lines(self,x,y,ss,size=9,col=INK,bold=False,leading=12,center=False):
        for i,s in enumerate(ss):self.text(x,y+i*leading,s,size,col,bold,center)
    def rect(self,x,y,w,h,fill='#FFFFFF',stroke=LINE,lw=.65):
        self.c.setFillColor(HexColor(fill));self.c.setStrokeColor(HexColor(stroke));self.c.setLineWidth(lw)
        self.c.rect(x,self.h-y-h,w,h,fill=1,stroke=1)
    def line(self,x,y,xx,yy,col=INK,lw=.7):
        self.c.setStrokeColor(HexColor(col));self.c.setLineWidth(lw);self.c.line(x,self.h-y,xx,self.h-yy)
    def path(self,pts,fill=None,col=INK,lw=.8,close=False):
        p=self.c.beginPath();p.moveTo(pts[0][0],self.h-pts[0][1])
        for x,y in pts[1:]:p.lineTo(x,self.h-y)
        if close:p.close()
        self.c.setStrokeColor(HexColor(col));self.c.setLineWidth(lw)
        if fill:self.c.setFillColor(HexColor(fill))
        self.c.drawPath(p,fill=bool(fill),stroke=1)
    def arrow(self,x,y,xx,yy,col=INK,lw=.8):
        self.line(x,y,xx,yy,col,lw);a=atan2(yy-y,xx-x)
        self.path([(xx-4*cos(a-.48),yy-4*sin(a-.48)),(xx,yy),(xx-4*cos(a+.48),yy-4*sin(a+.48))],col=col,lw=lw)
    def route(self,pts,col=INK,lw=.8):
        for a,b in zip(pts[:-2],pts[1:-1]):self.line(*a,*b,col,lw)
        self.arrow(*pts[-2],*pts[-1],col,lw)
    def circle(self,x,y,r,fill='#FFFFFF',col=INK):
        self.c.setFillColor(HexColor(fill));self.c.setStrokeColor(HexColor(col));self.c.setLineWidth(.65)
        self.c.circle(x,self.h-y,r,fill=1,stroke=1)
    def label(self,x,y,s,col=INK):self.text(x,y,s,10,col,True)
    def stack(self,x,y,w=28,h=20,fill=PB,label=None):
        for d in [6,3,0]:self.rect(x+d,y-d,w,h,fill,BLUE,.6)
        if label=='z0':
            self.text(x+w/2-3,y+h/2-4,'z',10,INK,False,False,True)
            self.text(x+w/2+1,y+h/2+1,'0',6)
        elif label:self.text(x+w/2,y+h/2-4,label,9,INK,False,True)
    def network(self,x,y,w=57,h=27,label='Denoiser',fill=PG):
        self.path([(x,y),(x+w*.38,y+5),(x+w*.62,y+5),(x+w,y),(x+w,y+h),(x+w*.62,y+h-5),(x+w*.38,y+h-5),(x,y+h)],fill,INK,.8,True)
        self.text(x+w/2,y+h/2-4,label,8.6,INK,False,True)
    def enc(self,x,y,w=26,h=30,decode=False):
        pts=[(x,y),(x+w,y+7),(x+w,y+h-7),(x,y+h)] if not decode else [(x,y+7),(x+w,y),(x+w,y+h),(x,y+h-7)]
        self.path(pts,PO,ORANGE,.8,True);self.text(x+w/2,y+h/2-4,'D' if decode else 'E',10,INK,True,True)
    def noise(self,x,y,w=26,h=23,seed=1,amount=1):
        r=random.Random(seed)
        for row in range(6):
            for col in range(7):
                g=int(245-r.random()*150*amount);c=f'#{g:02x}{g:02x}{g:02x}'
                self.rect(x+col*w/7,y+row*h/6,w/7,h/6,c,c,0)
    def scene(self,x,y,w=42,h=29,t=0,style='coherent',variant=0):
        self.rect(x,y,w,h,'#F5F8FC',LINE,.5);self.line(x+1,y+h-6,x+w-1,y+h-6,'#9CAAB2',.6)
        ox=x+5+t*(w-25)/3;oy=y+7
        if style=='smooth':self.rect(ox,oy,16,14,'#B7CFDB','#8FAEBF',.5)
        elif style=='degraded':
            self.rect(ox,oy,16,14,'#ADC1CA','#ADC1CA',0);self.rect(ox+3,oy+3,8,7,'#9EBBC9','#9EBBC9',0)
        else:
            self.rect(ox,oy,16,14,PB,BLUE,.55)
            if variant==1 or (style=='flicker' and t%2):
                for k in range(3):self.line(ox+1,oy+3+k*4,ox+15,oy+3+k*4,BLUE,1)
            else:
                for k in range(4):self.line(ox+2+k*4,oy+1,ox+2+k*4,oy+13,BLUE,1)
        self.circle(ox+3,oy+15,1.1,GRAY,GRAY);self.circle(ox+13,oy+15,1.1,GRAY,GRAY)
    def save(self):self.c.showPage();self.c.save()

def taxonomy():
    f=F('taxonomy',355)
    f.text(258,2,'Diffusion-based video restoration and enhancement',13,INK,True,True);f.line(0,21,516,21,INK,.85)
    rows=[
      ('Problem settings',PO,ORANGE,[('Tasks','Resolution / blur / noise / weather / missing content'),('Domains','Natural / HDR / underwater / infrared / faces / AIGC'),('Degradations','Single / composite / unknown / generative artifacts')]),
      ('Generative priors',PG,GREEN,[('Origin','Restoration training / pretrained image / pretrained video'),('Representation','Pixels / features / spatial or spatiotemporal latents'),('Dynamics','Diffusion / score-based models / flow matching')]),
      ('Conditioning',PB,BLUE,[('Observed content','Low-quality frames / aligned features / reference frames'),('Side information','Motion / text / events / physics / codec information')]),
      ('Temporal modeling',PP,PURPLE,[('Sample coupling','Shared or warped noise / latent initialization'),('Information exchange','Flow / temporal attention / memory / decoding')]),
      ('Learning strategies',PG,GREEN,[('Training','Paired supervision / self-supervision / distillation'),('Adaptation','Zero-shot transfer / internal learning / test-time updates')]),
      ('Efficient inference',PO,ORANGE,[('Computation','One-step / few-step / sparse attention / compact decoder'),('Context','Full clip / tiled or windowed / causal and streaming')]),
      ('System and evaluation',PB,BLUE,[('Organization','Single-task / multi-task / all-in-one / agentic restoration'),('Assessment','Fidelity / perception / temporal consistency / cost')])]
    y=30;cs=[]
    for title,pale,col,items in rows:
        h=len(items)*14+6;cy=y+h/2;cs.append(cy);f.rect(25,y,106,h,pale,col)
        f.text(78,cy-4,title,9.4,INK,True,True);f.line(131,cy,143,cy,col,1);f.line(143,y+8,143,y+h-8,col,1)
        for i,(sub,s) in enumerate(items):
            yy=y+4+i*14;f.line(143,yy+5,150,yy+5,col,.8);f.text(154,yy,sub,8.4,col,True);f.text(249,yy,s,8.5)
        y+=h+5
    f.line(12,cs[0],12,cs[-1],INK,1)
    for cy in cs:f.line(12,cy,25,cy);f.circle(12,cy,1.8,INK,INK)
    f.line(0,337,516,337,LINE,.6);f.text(258,343,'Complementary dimensions: a method combines choices across several branches.',9,GRAY,False,True,True);f.save()


def prior_routes():
    f=F('prior_routes',286);f.label(0,0,'(a) Learning an observation-conditioned generator')
    f.stack(8,45,31,22,label='Y');f.text(25,73,'LQ video',8.3,GRAY,False,True)
    f.arrow(47,55,66,55);f.enc(66,40,27,30);f.arrow(93,55,113,55)
    f.rect(113,43,66,24,PO,ORANGE);f.text(146,51,'Condition branch',8.5,INK,False,True)
    f.route([(179,55),(225,55),(225,34),(279,34),(279,47)],ORANGE);f.text(202,22,'features / references',8.5,ORANGE)
    f.noise(196,61,25,22);f.arrow(224,72,246,72);f.network(247,51,64,39,'Denoiser')
    f.text(279,93,'Image or video prior',8.2,GRAY,False,True);f.arrow(312,72,336,72);f.stack(338,62,24,21,PG,'z0')
    f.arrow(369,72,390,72);f.enc(391,56,27,31,True);f.arrow(419,72,440,72);f.stack(444,61,30,23,PG,'X')
    f.text(460,93,'Restored video',8.3,GRAY,False,True);f.line(0,109,516,109,LINE,.55)
    f.label(0,118,'(b) Constraining a pretrained prior during sampling')
    f.noise(15,153,27,23);f.text(29,180,'z(s)',8.5,GRAY,False,True);f.arrow(44,165,65,165)
    f.network(67,145,74,38,'Frozen prior',PB);f.arrow(143,165,163,165);f.stack(167,154,26,22,PG,'z0')
    f.arrow(199,165,219,165);f.enc(222,149,27,31,True);f.arrow(251,165,270,165)
    f.rect(273,149,80,31,PO,ORANGE);f.lines(313,154,['Observation model','and discrepancy'],8.4,INK,False,10,True)
    f.stack(391,150,28,21,label='Y');f.arrow(390,165,355,165,ORANGE)
    f.route([(313,181),(313,200),(5,200),(5,165),(13,165)],RED,.9);f.text(153,204,'Data-consistency gradient / projection',9,RED,False,True)
    f.lines(459,154,['Temporal','constraints'],8.5,PURPLE,False,11,True);f.route([(459,181),(459,200),(319,200)],PURPLE)
    f.line(0,220,516,220,LINE,.55);f.label(0,230,'(c) Distilling iterative restoration into a fast generator')
    for i in range(4):
        f.noise(15+31*i,250,23,20,i+2,1-i*.25)
        if i<3:f.arrow(39+31*i,260,45+31*i,260,GRAY,.6)
    f.text(75,277,'Multi-step teacher',8,GRAY,False,True);f.arrow(141,260,197,260,ORANGE,1);f.text(169,245,'distill',8.5,ORANGE,False,True)
    f.network(204,249,68,23,'Student',PO);f.arrow(275,260,308,260);f.stack(312,250,27,20,PG,'X')
    f.lines(367,249,['Reconstruction / distribution matching','Temporal / adversarial supervision'],8.5,INK,False,12);f.save()


def deployment():
    f=F('deployment',262);f.text(65,1,'Context pattern',10,INK,True,True);f.text(338,1,'Input frames and output availability',10,INK,True,True)
    for i in range(8):f.text(189+i*37,21,str(i+1),9,GRAY,False,True)
    for y,title,col,pale in [(40,'(a) Full clip',BLUE,PB),(113,'(b) Overlapping clips',ORANGE,PO),(186,'(c) Causal stream',GREEN,PG)]:
        f.label(0,y,title,col)
        for r in range(6):
            for c in range(6):f.rect(5+c*7,y+17+r*7,6.5,6.5,pale if (y==40 or (y==113 and abs(c-r)<=1) or (y==186 and c<=r)) else '#FFFFFF',LINE,.2)
        f.lines(64,y+23,['Rows: outputs','Cols: context'],8,GRAY,False,12)
        for i in range(8):f.rect(176+i*37,y+2,26,17,'#F6F7F8',LINE,.5);f.text(189+i*37,y+6,f'y{i+1}',8.5,GRAY,False,True)
        if y==40:
            f.line(177,y+26,461,y+26,col,2);f.arrow(461,y+26,461,y+40,col)
            for i in range(8):f.circle(189+i*37,y+47,3,col,col)
            f.line(189,y+47,448,y+47,col,.65);f.text(319,y+58,'All inputs precede full-clip restoration',8.5,col,False,True)
        elif y==113:
            for x,ww,dy in [(176,100,27),(250,100,36),(324,100,45),(398,63,54)]:f.line(x,y+dy,x+ww,y+dy,col,2.4);f.arrow(x+ww,y+dy,x+ww+8,y+dy,col)
            f.lines(481,y+27,['overlap','and','blend'],8,col,False,12,True)
        else:
            for i in range(8):
                x=189+i*37;f.arrow(x,y+21,x,y+36,col);f.circle(x,y+43,4,PG,col)
                if i<7:f.arrow(x+5,y+43,x+31,y+43,PURPLE)
            f.text(315,y+59,'Past state + current frame; reset at scene cuts',8.5,col,False,True)
    f.line(162,14,162,255,LINE,.6);f.save()


if __name__=='__main__':
    for fn in (taxonomy,prior_routes,deployment):fn()
    from make_evidence_figures import main
    main()
    print('Generated six survey figures.')
