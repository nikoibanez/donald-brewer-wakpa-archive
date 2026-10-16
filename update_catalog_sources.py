import json
from pathlib import Path
p=Path('catalog.original.json')
data=json.loads(p.read_text(encoding='utf-8'))
for row in data:
 if row['title']=='Untitled (Morning Clouds)':
  row['url']='https://www.santafeartauction.com/auction-lot/donald-brewer-wakpa-untitled-morning-clouds_7e44198a4e'
  row['source']='Santa Fe Art Auction, lot 145'
if not any(x['title']=='Untitled (Four Figures)' for x in data):
 data.append(dict(title='Untitled (Four Figures)',year='unknown',shown='2022-04-16',basis='Auction sale date only; creation date unknown',medium='Oil on canvas, 15 × 30 × 1⅝ in.',place='Santa Fe Art Auction, Sanchez estate (2022); current location unknown',desc='Painting cataloged as Four Figures; image and visual composition require separate review.',url='https://www.santafeartauction.com/auction-lot/donald-brewer-wakpa-untitled-four-figures_F4848FBA95',source='Santa Fe Art Auction, lot 144',group='Auction records'))
p.write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding='utf-8')
print('Catalog:',len(data),'records')