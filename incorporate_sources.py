from pathlib import Path
from html import escape
import re, json

ROOT=Path('.')
HEARD='https://5019.sydneyplus.com/Heard_Museum_ArgusNET_Final/Portal/Portal.aspx?component=AAAM&record=23fce813-e019-424e-8b6a-0fd6617537f3&lang=en-US'
CLARKSON='https://sites.clarkson.edu/gallery/browse-the-artists/don-brewer-wakpa/'
WINTER='https://wintercount.com/Don%20Brewer/wakpa.html'
NEWS='https://antiquesandthearts.com/command-performance-by-native-american-works-multiples/'
WA='https://westernartandarchitecture.com/departments/auction-block/auction-block-higher-and-higher'
MUTUAL='https://www.mutualart.com/Artist/Donald-Brewer/C1CE6065523DDFE2'
YOUTUBE='https://www.youtube.com/watch?v=pdnsb7LVxRg'
SANTAFE='https://www.santafeartauction.com/auction-lot/donald-brewer-wakpa-untitled-morning-clouds_7e44198a4e'
ARTSY='https://www.artsy.net/artwork/donald-brewer-wakpa-seven-night-riders'
GOOGLE='https://www.google.com/search?q=donald+brewer+native+sioux+mural'
WORTH1='https://www.worthpoint.com/worthopedia/native-american-don-brewer-wakpa-160229706'
WORTH2='https://www.worthpoint.com/worthopedia/don-brewer-wakpa-original-painting-4639262330'
FB1='https://www.facebook.com/groups/209071863318/posts/10153804155998319/'
FB2='https://www.facebook.com/groups/1565615467041339/posts/4480557592213764/'
exhibitions=[
{'year':'1992','title':'United Tribes Indian Art Expo','venue':'Bismarck, North Dakota','dates':'September 11–13, 1992','type':'Exhibition / art expo','source':HEARD},
{'year':'1990','title':'Come Dance With Us','venue':'Heritage Center, Red Cloud Indian School, Pine Ridge, South Dakota','dates':'1990; exact dates unknown','type':'Touring exhibition; additional venues unknown','source':HEARD},
{'year':'1990','title':'Northern Plains Tribal Arts','venue':'Sioux Falls, South Dakota','dates':'September 1990','type':'Exhibition','source':HEARD},
{'year':'1989','title':'Red Cloud Indian School Art Show','venue':'Red Cloud Indian School, Pine Ridge, South Dakota','dates':'June–August 1989','type':'Art exhibition','source':HEARD},
{'year':'1988','title':'Northern Plains Tribal Arts','venue':'Sioux Falls, South Dakota','dates':'October 1988','type':'Exhibition','source':HEARD},
]
markets=[
{'year':'2010','title':'Heard Museum Guild Indian Fair & Market','venue':'Heard Museum, Phoenix, Arizona','dates':'March 6–7, 2010','type':'Juried-market participation not confirmed; event listing','source':HEARD},
{'year':'2007','title':'Heard Museum Guild Indian Fair & Market','venue':'Heard Museum, Phoenix, Arizona','dates':'March 3–4, 2007','type':'Artist market appearance','source':HEARD}
]
awards=[
{'year':'1990','title':'First Place, painting, Division I (oil and acrylic)','venue':'Northern Plains Tribal Arts, Sioux Falls, South Dakota','dates':'September 1990','source':HEARD},
{'year':'1989','title':'Aplan Award','venue':'Red Cloud Indian School Art Show, Pine Ridge, South Dakota','dates':'June 1989','source':HEARD}
]
art_older=[
{'title':'Waiting for the Scout','date':'Unknown','where':'Wintercount greeting-card and matted-print listing','url':WINTER},
{'title':'Good Dancer','date':'Unknown','where':'Wintercount greeting-card and matted-print listing','url':WINTER},
{'title':'Fancy Dancer','date':'Unknown','where':'Wintercount greeting-card and matted-print listing','url':WINTER},
{'title':'Many Coup','date':'Unknown','where':'Wintercount greeting-card and matted-print listing','url':WINTER}
]
sources=[
{'title':'Clarkson University Art Gallery artist biography','type':'Institutional biography and reported collections','date':'Unknown','status':'Read and verified','url':CLARKSON},
{'title':'Heard Museum Native American Artists Resource Collection','type':'Artist archive: 5 exhibitions, 2 market appearances, 2 awards, publications','date':'1988–2010 records','status':'Read and verified','url':HEARD},
{'title':'MutualArt Donald Brewer database','type':'Secondary-market index; 13 artworks and 12 auction-result listings','date':'Ongoing','status':'Read and verified; not exhibition proof','url':MUTUAL},
{'title':'Antiques and the Arts Weekly: Command Performance','type':'Published auction review and artist coverage','date':'April 26, 2022','status':'Read and verified','url':NEWS},
{'title':'NPIAM artist profile video','type':'Video artist profile published by sintegleskautube','date':'June 3, 2022','status':'Title, date and publisher verified','url':YOUTUBE},
{'title':'Wintercount Don Brewer prints','type':'Four titled reproductions offered as prints and cards','date':'Unknown','status':'Read and verified','url':WINTER},
{'title':'Santa Fe Art Auction: Untitled (Morning Clouds)','type':'Original auction lot 145; acrylic on canvas','date':'April 16, 2022','status':'Read and verified','url':SANTAFE},
{'title':'WorthPoint listing 160229706','type':'Potential artwork-sales listing','date':'Unknown','status':'Page access restricted; details unverified','url':WORTH1},
{'title':'WorthPoint listing 4639262330','type':'Potential artwork-sales listing','date':'Unknown','status':'Page access restricted; details unverified','url':WORTH2},
{'title':'Facebook group post 10153804155998319','type':'Potential historical artist reference','date':'Unknown','status':'Post content inaccessible; attribution unverified','url':FB1},
{'title':'Facebook group post 4480557592213764','type':'Potential historical artist reference','date':'Unknown','status':'Post content inaccessible; attribution unverified','url':FB2},
{'title':'Google search for Don Brewer murals','type':'Discovery query, not an independent documentary source','date':'Current search','status':'Discovery only','url':GOOGLE},
]
(ROOT/'research'/'sources_catalog.json').write_text(json.dumps({'exhibitions':exhibitions,'markets':markets,'awards':awards,'older_artworks':art_older,'user_links':sources},indent=2,ensure_ascii=False),encoding='utf-8')
def ext(text,url):
 return '<a href="'+escape(url,quote=True)+'" rel="noopener noreferrer" target="_blank">'+escape(text)+'</a>'
def event_row(e):
 return '<tr><td>'+escape(e['dates'])+'</td><td><strong>'+escape(e['title'])+'</strong><div class="source-subline">'+escape(e['type'])+'</div></td><td>'+escape(e['venue'])+'</td><td>'+ext('Heard Museum record',e['source'])+'</td></tr>'
def page(title,heading,content):
 nav=nav_markup('../')
 footer=footer_markup('../')
 return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="Documented paintings, exhibitions, awards and publications of Donald Brewer (Wakpa)."><title>'+escape(title)+' · Donald Brewer (Wakpa)</title><link rel="stylesheet" href="../style.css"></head><body>'+nav+'<main class="research wrap"><h1>'+escape(heading)+'</h1>'+content+'</main>'+footer+'</body></html>'
def nav_markup(base):
 return '<header class="site-header"><a href="'+base+'index.html" class="brand">Donald Brewer<small>Wakpa</small></a><nav aria-label="Main navigation" class="nav"><a href="'+base+'index.html#paintings">Paintings</a><a href="'+base+'index.html#about">About Don</a><a href="'+base+'index.html#public-art">Public Art</a><a href="'+base+'exhibitions/index.html">Exhibitions</a><a href="'+base+'publications/index.html">Publications</a><a href="'+base+'research/index.html">Research</a><a href="'+base+'index.html#commissions">Commissions</a></nav></header>'
def footer_markup(base):
 return '<footer class="site-footer"><div>© Donald Brewer (Wakpa). Artwork reproduced with permission.</div><div><a href="'+base+'research/index.html">Research and documentation</a> &nbsp; <a href="mailto:supereukarya@gmail.com?subject=Donald%20Brewer%20portfolio%20inquiry">Contact</a></div></footer>'
exh_body='<p class="research-lede">Exhibitions, artist-market appearances, and awards documented in the Heard Museum’s Native American Artists Resource Collection. The dates below are those recorded by the museum; they are not inferred from subsequent auction sales.</p>'
exh_body+='<h2>Exhibitions</h2><div class="table-wrap"><table class="timeline-table"><thead><tr><th>Dates</th><th>Event</th><th>Venue</th><th>Source</th></tr></thead><tbody>'+''.join(event_row(x) for x in exhibitions)+'</tbody></table></div>'
exh_body+='<h2>Art markets</h2><p>The museum lists two Heard Museum Guild Indian Fair &amp; Market appearances. An artist-market entry should not be described as a museum gallery exhibition or an award without further evidence.</p><div class="table-wrap"><table class="timeline-table"><thead><tr><th>Dates</th><th>Market</th><th>Location</th><th>Source</th></tr></thead><tbody>'+''.join(event_row(x) for x in markets)+'</tbody></table></div>'
exh_body+='<h2>Awards</h2><div class="awards-records">'+''.join('<div class="award-record"><strong>'+escape(x['year'])+'</strong><div><h3>'+escape(x['title'])+'</h3><p>'+escape(x['venue'])+' · '+escape(x['dates'])+'</p></div><div>'+ext('Museum archive',x['source'])+'</div></div>' for x in awards)+'</div>'
exh_body+='<h2>Collections and archives</h2><p>'+ext('Clarkson University Art Gallery',CLARKSON)+' lists Don’s work in the Akta Lakota Museum, Red Cloud Indian School, Crazy Horse Museum, United Tribes Technical College Collection and Chicago’s former Sears Tower (now Willis Tower). The particular paintings, accession numbers and current display status have not been verified from each institution.</p>'
exh_body+='<p>The '+ext('Heard Museum artist archive',HEARD)+' also confirms an artist file in the Billie Jane Baguley Library and Archives and a record in the Native American Artists Collection (RC62). This refers to archival materials, not proof of ownership of a painting in the museum’s object collection.</p>'
exh_body+='<p class="important-note"><strong>For grant applications:</strong> These records document professional exhibitions from 1988–1992 and recorded market appearances in 2007 and 2010. They do not establish ten qualifying exhibitions during the past ten years. Recent exhibitions, if any, still need to be documented separately.</p>'
(ROOT/'exhibitions').mkdir(exist_ok=True)
(ROOT/'exhibitions'/'index.html').write_text(page('Exhibitions and awards','Exhibitions and awards',exh_body),encoding='utf-8')
pubs=[
('1995','Biographical directory','The Biographical Directory of Native American Painters','Patrick D. Lester, SIR Publications, Tulsa; Don is listed on page 82 in the Heard Museum archive.',HEARD),
('2001','Record-cover artwork','Prayer for Peace','Silver Wave Records, Boulder, Colorado. The Heard Museum lists a 2001 cover-art credit.',HEARD),
('2022','Video profile','NPIAM Artist Profile: Donald Brewer','Artist-profile video uploaded June 3, 2022 by the sintegleskautube YouTube channel.',YOUTUBE),
('April 2022','Press coverage','Command Performance By Native American Works & Multiples','Antiques and the Arts Weekly covered Donald Brewer’s April 2022 Santa Fe Art Auction sale; includes artwork discussion and a photograph of Untitled (Night Clouds).',NEWS),
('2022','Auction coverage','Auction Block: Higher and Higher','Western Art & Architecture covered the Santa Fe sale and illustrated Untitled (Night Clouds).',WA),
('Unknown','University artist profile','Don Brewer Wakpa','Clarkson University Art Gallery published an artist biography and lists collection references; the page does not give a dated exhibition opening.',CLARKSON),
('Unknown','Book artwork reference','Luther Standing Bear (University of Nebraska Press)','The Clarkson biography states Don’s imagery was used for a University of Nebraska Press book associated with Luther Standing Bear. The precise title, edition and artwork reproduction have not been independently established.',CLARKSON),
('Unknown','Licensed reproductions','Wintercount Don Brewer prints and greeting cards','Four titled illustrations are offered as greeting cards or matted prints. The original creation dates and media are unknown.',WINTER),
('2022–2023','Auction catalogs','Santa Fe Art Auction and estate works','Multiple original paintings are listed in the April 2022 sale and later sessions. These document market activity, not participation in a curated exhibition.',SANTAFE),
('Ongoing','Auction market index','Donald Brewer on MutualArt','The database lists 13 artworks and 12 auction results as of the October 2026 check. Auction prices may differ depending on buyer’s-premium inclusion.',MUTUAL),
]
pub_body='<p class="research-lede">Published references to Don’s paintings and artistic career, including book and record artwork, press coverage, a video artist profile, and auction publications. Dates are publication or event dates unless otherwise indicated.</p>'
pub_body+='<div class="publication-ledger">'+''.join('<article class="publication-entry"><div class="publication-date">'+escape(y)+'</div><div><h2>'+escape(title)+'</h2><p class="source-subline">'+escape(kind)+'</p><p>'+escape(desc)+'</p>'+ext('View source',url)+'</div></article>' for y,kind,title,desc,url in pubs)+'</div>'
pub_body+='<h2>Further artwork references</h2><p>'+ext('Wintercount',WINTER)+' publishes four additional titled images. The cards and prints are documented, but the source does not state when the original paintings were created.</p><ul>'+''.join('<li>'+escape(x['title'])+' — creation date unknown; '+ext('Wintercount listing',x['url'])+'</li>' for x in art_older)+'</ul>'
pub_body+='<h2>What counts as an exhibition?</h2><p>Press, museum artist files, historical advertisements, card reproductions and auction listings demonstrate professional circulation of artwork. They do not count as exhibitions merely by being published. For a grant requiring a recent exhibition history, document the dates, venue, title, curatorial or selection details, and at least one invitation, program, catalog or venue confirmation.</p>'
(ROOT/'publications').mkdir(exist_ok=True)
(ROOT/'publications'/'index.html').write_text(page('Publications and media','Publications and media',pub_body),encoding='utf-8')
# Update navigation throughout the artist site, including all individual paintings.
htmlfiles=[ROOT/'index.html',ROOT/'research'/'index.html',*sorted((ROOT/'paintings').glob('*.html'))]
for file in htmlfiles:
 content=file.read_text(encoding='utf-8')
 base='' if file==ROOT/'index.html' else '../'
 original=re.search(r'<header class="site-header">.*?</header>',content,re.S)
 if not original:raise ValueError('Header missing '+str(file))
 content=content.replace(original.group(0),nav_markup(base))
 file.write_text(content,encoding='utf-8')
home=ROOT/'index.html'
content=home.read_text(encoding='utf-8')
spot='<section id="public-art"'
if spot not in content:raise ValueError('Home Public Art insertion point missing')
feature='<section id="exhibitions-preview" class="context-band"><div class="wrap context-band-inner"><div><h2>Exhibitions and awards</h2><p>Don’s work has appeared at Northern Plains Tribal Arts, Red Cloud Indian School and the United Tribes Indian Art Expo. The Heard Museum archive also records two juried-market-era appearances and awards from 1989 and 1990.</p></div><div><p><strong>1990</strong> First Place, Northern Plains Tribal Arts</p><p><strong>1989</strong> Aplan Award, Red Cloud Indian School Art Show</p><a class="text-link" href="exhibitions/index.html">View exhibition and award history</a></div></div></section>'
content=content.replace(spot,feature+spot)
comm='<section id="commissions"'
if comm not in content:raise ValueError('Home commissions insertion point missing')
press_feature='<section class="context-band context-band-light"><div class="wrap context-band-inner"><div><h2>Publications and media</h2><p>Don’s work has circulated in print, music packaging, artist references and independent reporting. His April 2022 auction results were covered in two arts publications.</p></div><div><p><strong>2022</strong> Artist-profile video and published auction coverage</p><p><strong>1995–2001</strong> Directory entry and record-cover artwork</p><a class="text-link" href="publications/index.html">View publications and media</a></div></div></section>'
content=content.replace(comm,press_feature+comm)
home.write_text(content,encoding='utf-8')
# Enrich original research page with two new links and source audit, maintaining provenance.
researchfile=ROOT/'research'/'index.html'
content=researchfile.read_text(encoding='utf-8')
content=content.replace('These 11 listings are documented outside', 'These 12 listings are documented outside')
source_rows=''.join('<tr><td>'+ext(x['title'],x['url'])+'</td><td>'+escape(x['type'])+'</td><td>'+escape(x['date'])+'</td><td>'+escape(x['status'])+'</td></tr>' for x in sources)
newsection='<h2>Exhibitions and publications</h2><p>See the '+ext('Heard Museum exhibition and award record','../exhibitions/index.html')+' and '+ext('documented publications and media','../publications/index.html')+'. Historical appearance dates are not recent exhibition counts.</p>'
newsection+='<h2>Additional source links</h2><p>All user-supplied links are recorded here, including sources we could not authenticate. Search results and restricted social posts are leads, not verified proof.</p><div class="table-wrap"><table><thead><tr><th>Reference</th><th>Category</th><th>Date</th><th>Verification</th></tr></thead><tbody>'+source_rows+'</tbody></table></div>'
anchor='<h2>How this catalogue is maintained</h2>'
if anchor not in content:raise ValueError('Research insertion point missing')
content=content.replace(anchor,newsection+anchor)
researchfile.write_text(content,encoding='utf-8')
stylefile=ROOT/'style.css'
styles=stylefile.read_text(encoding='utf-8')
if '.context-band-inner{' not in styles:
 styles+="""
.context-band{padding:82px 0;background:#f0f1ec;border-top:1px solid var(--line)}
.context-band-light{background:var(--paper)}
.context-band-inner{display:grid;grid-template-columns:1.2fr 1fr;gap:min(12vw,150px);align-items:start}
.context-band-inner h2{font-size:clamp(2rem,3.6vw,3.5rem);margin-bottom:25px}
.context-band-inner p{line-height:1.78;color:#414a43;font-size:1.05rem}
.context-band-inner a{display:inline-block;margin-top:15px}
.timeline-table td,.timeline-table th{padding:19px 16px 19px 0;vertical-align:top}
.timeline-table td:first-child,.timeline-table th:first-child{width:165px}
.source-subline{font-size:.89rem;color:var(--muted);margin:8px 0 0}
.award-record{display:grid;grid-template-columns:75px 1fr auto;gap:32px;border-top:1px solid var(--line);padding:28px 0}
.award-record h3{margin-bottom:7px}.award-record p{margin:0;color:var(--muted)}
.award-record a{font-size:.9rem}
.important-note{background:#ecefe8;padding:25px 30px;border-left:3px solid #8b493a;margin-top:48px;max-width:none}
.publication-entry{display:grid;grid-template-columns:138px 1fr;border-top:1px solid var(--line);gap:38px;padding:32px 0}
.publication-entry h2{font-size:clamp(1.6rem,2.5vw,2.2rem);margin:0 0 8px}
.publication-entry p{font-size:.96rem;color:#3f4740;margin-top:12px}
.publication-entry .source-subline{font-size:.82rem;color:var(--muted)}
.publication-date{font-weight:600;color:var(--muted)}
.research .publication-ledger{margin-top:46px}
@media(max-width:850px){.context-band-inner{grid-template-columns:1fr;gap:20px}.award-record{grid-template-columns:75px 1fr}.award-record>div:last-child{grid-column:2}}
@media(max-width:560px){.context-band{padding:65px 0}.publication-entry{grid-template-columns:1fr;gap:10px}.award-record{gap:15px}.timeline-table{font-size:.84rem}}
"""
 stylefile.write_text(styles,encoding='utf-8')
print('Enriched',len(htmlfiles)+2,'pages; 5 exhibitions, 2 market appearances, 2 awards, 10 publications/media references,',len(sources),'user source links')

# Additional paintings documented in older gallery, print and auction references.
other_rows=[]
records=json.loads((ROOT/'catalog.original.json').read_text(encoding='utf-8'))
for item in [x for x in records if not x.get('image')]:
    creation=item.get('year','unknown')
    shown=item.get('shown','unknown')
    other_rows.append('<tr><td><strong>'+escape(item['title'])+'</strong></td><td>'+escape(str(creation))+'</td><td>'+escape(str(shown))+'</td><td>'+ext('View original listing',item['url'])+'</td></tr>')
extra_rows=''.join('<tr><td><strong>'+escape(x['title'])+'</strong></td><td>Unknown</td><td>Unknown</td><td>'+ext('Wintercount prints',x['url'])+'</td></tr>' for x in art_older)
extra_body='<p class="research-lede">Paintings and titled artwork reproductions found outside Don’s present Fine Art America portfolio. Auction dates and print-listing dates do not identify when a painting was made, and some independently listed records may refer to the same physical work.</p>'
extra_body+='<h2>Gallery and auction records</h2><div class="table-wrap"><table><thead><tr><th>Artwork</th><th>Creation year</th><th>Published or auctioned</th><th>Link</th></tr></thead><tbody>'+''.join(other_rows)+'</tbody></table></div>'
extra_body+='<h2>Wintercount editions</h2><p>'+ext('Wintercount',WINTER)+' offers images titled Waiting for the Scout, Good Dancer, Fancy Dancer and Many Coup on greeting cards and matted prints. The source does not identify original painting dates, media, or ownership. These titles are not assumed to be the same works as similarly named paintings in the current gallery.</p><div class="table-wrap"><table><thead><tr><th>Artwork title</th><th>Creation</th><th>Publication</th><th>Source</th></tr></thead><tbody>'+extra_rows+'</tbody></table></div>'
(ROOT/'paintings'/'other-works.html').write_text(page('Other documented artworks','Other documented works',extra_body),encoding='utf-8')
hp=ROOT/'index.html'
h=hp.read_text(encoding='utf-8')
pattern=r'(<div class="gallery">.*?</div>)(</section>)'
count=re.findall(pattern,h,re.S)
if len(count)!=1:raise ValueError('Expected one gallery for other-works link, got '+str(len(count)))
h=re.sub(pattern,lambda m:m.group(1)+'<p class="other-works-link"><a href="paintings/other-works.html">See more paintings documented in galleries, auction catalogs and print archives</a></p>'+m.group(2),h,count=1,flags=re.S)
h=h.replace('two juried-market-era appearances','two Heard Museum artist-market appearances')
hp.write_text(h,encoding='utf-8')
pubp=ROOT/'publications'/'index.html'
pubtxt=pubp.read_text(encoding='utf-8')
video='<div class="video-embed"><iframe src="https://www.youtube-nocookie.com/embed/pdnsb7LVxRg" title="NPIAM Artist Profile: Donald Brewer, published June 3, 2022" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'
pubtxt=pubtxt.replace('<div class="publication-ledger">',video+'<div class="publication-ledger">')
pubp.write_text(pubtxt,encoding='utf-8')
sty=ROOT/'style.css'
txt=sty.read_text(encoding='utf-8')
if '.video-embed{' not in txt:
 txt+='\n.video-embed{aspect-ratio:16/9;width:min(100%,880px);background:#202321;margin:45px 0 60px}.video-embed iframe{width:100%;height:100%;border:0}.other-works-link{margin-top:55px;max-width:42em}.other-works-link a{font-weight:600;text-underline-offset:6px}\n'
sty.write_text(txt,encoding='utf-8')
print('Added additional artwork page, videos, links and refinements.')
