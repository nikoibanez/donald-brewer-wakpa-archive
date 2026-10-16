from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote
import re
root=Path('.')
files=[Path('index.html'),Path('research/index.html'),*sorted(Path('paintings').glob('*.html'))]
class Audit(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.alts=[];self.headings=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('a','img','link'):
   u=a.get('href' if tag!='img' else 'src','')
   if u:self.refs.append((tag,u))
  if tag=='img':self.alts.append(a.get('alt',''))
  if tag=='h1':self.headings.append(tag)
bad=[]
for file in files:
 p=Audit();p.feed(file.read_text(encoding='utf-8'))
 if len(p.headings)!=1:bad.append((str(file),'H1 count '+str(len(p.headings))))
 for tag,u in p.refs:
  if u.startswith(('http:','https:','mailto:','tel:','#','data:')):continue
  rel=unquote(u.split('#')[0].split('?')[0])
  if not rel:continue
  f=(file.parent/rel).resolve()
  if not f.is_file():bad.append((str(file),rel))
 if any(not alt.strip() for alt in p.alts):bad.append((str(file),'empty image alt'))
print('AUDITED',len(files),'HTML pages; errors=',len(bad))
for err in bad[:40]:print('ERROR',err)
home=(root/'index.html').read_text(encoding='utf-8')
print('Home images',home.count('<img'),'home titles',home.count('class="painting"'))
print('Hero uses real painting:', 'artwork/dakota-thunder.jpg' in home)
print('Home has metadata artifact:', any(s in home for s in ('01 / THE ARTIST','EVIDENCE-LED','EDITORIAL PLACEHOLDER','DATE BASIS','<table>')))
if bad:raise SystemExit(1)
