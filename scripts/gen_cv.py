import json,sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from xml.sax.saxutils import escape as e
d=json.load(open(sys.argv[1],encoding='utf-8'));C=HexColor('#1F3A5F')
S=lambda n,**k:ParagraphStyle(n,fontName=k.pop('f','Helvetica'),fontSize=k.pop('s',9.5),leading=k.pop('l',12.5),**k)
H=S('h',f='Helvetica-Bold',s=18,l=22,textColor=C);T=S('t',s=10.5,l=14,textColor=C);N=S('n',s=9);B=S('b')
SEC=S('s',f='Helvetica-Bold',s=10.5,l=14,textColor=C,spaceBefore=7);P=S('p',f='Helvetica-Bold',spaceBefore=4)
L=S('l',leftIndent=10,bulletIndent=2)
f=[Paragraph(e(d['name']),H),Paragraph(e(d['headline']),T)]+[Paragraph(e(x),N) for x in d['contact']]
def sec(t):f.extend([Paragraph(e(t.upper()),SEC),HRFlowable(width='100%',thickness=.6,color=C,spaceAfter=3)])
sec(d['labels']['summary']);f.append(Paragraph(e(d['summary']),B))
sec(d['labels']['projects'])
for p in d['projects']:
    f.append(Paragraph(e(p['title']),P))
    if p.get('links'):f.append(Paragraph(e(p['links']),N))
    f+=[Paragraph(e(b),L,bulletText='•') for b in p['bullets']]
sec(d['labels']['skills']);f+=[Paragraph('<b>%s:</b> %s'%(e(k),e(v)),B) for k,v in d['skills']]
sec(d['labels']['education']);f+=[Paragraph(e(x),B) for x in d['education']]
if d.get('extra'):sec(d['labels']['extra']);f+=[Paragraph(e(x),B) for x in d['extra']]
SimpleDocTemplate(sys.argv[2],pagesize=A4,leftMargin=40,rightMargin=40,topMargin=34,bottomMargin=34,title=d['name']+' - CV').build(f)
