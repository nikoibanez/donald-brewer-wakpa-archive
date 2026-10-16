from pathlib import Path
import json, re, html

root = Path('.')
records = json.loads((root / 'catalog.original.json').read_text(encoding='utf-8'))
featured = [x for x in records if x.get('image')]
external = [x for x in records if not x.get('image')]
by_title = {x['title']:x for x in featured}
def clean(s):
    return html.escape(str(s or ''), quote=True)
def slug(s):
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s.lower())).strip('-')
def url(x):
    return 'paintings/' + slug(x['title']) + '.html'
def date_fmt(d):
    if not d or d == 'unknown': return 'Unknown'
    from datetime import datetime
    try: return datetime.strptime(d, '%Y-%m-%d').strftime('%B %-d, %Y')
    except: return d

descriptions = {
'Blu Fancy': 'A dancer in feathered regalia stands in a burst of electric blue, indigo and violet. Bright turquoise strokes and fine red accents cross the face and clothing.',
'Buffalo moon': 'Four pale bison rise from a bank of luminous blue clouds above a broad prairie. A tiny group of horseback riders crosses the dark horizon below.',
'Dakota Thunder': 'Four horseback riders carrying upright staffs appear in silhouette against a glowing red-orange sky. The foreground fades into dark blue and violet.',
'Eagles woman': 'A woman’s face emerges from a great blue cloud over an open prairie. Small riders move along the distant horizon under the towering sky.',
'Fancy Dance': 'A dancer wearing large blue-and-black feathered regalia is pictured in profile. Orange and red streamers sweep across a pale gold background.',
'Fancy Shawl Dancer': 'A dancer extends a red shawl across a field of violet and blue, with one leg raised mid-step. Fine bright specks scatter around the figure.',
'Feather Medicine': 'A bowed figure is built from expressive strokes of red, turquoise, blue and pale pink. Geometric star-like forms appear across the figure and background.',
'Four Winds': 'Four dark mounted figures form a line beneath a hot red sky. Small electric-blue highlights cut through their shadowed silhouettes.',
'Gamer': 'A faintly outlined figure is partially obscured by pink, mauve and blue paint. A feather-like shape rises near the upper edge of the portrait.',
'Horse play': 'Two pale horses appear to run out of a glowing cloud above a blue prairie. Far below, four tiny horseback riders gather along the horizon.',
'Horse Thief': 'Layers of blue storm clouds stretch over a grassy plain, with dark hills in the distance. A few small figures are visible near the low horizon.',
'King': 'A frontal portrait in red and blue is bordered by king-of-hearts playing-card symbols. A dark feathered headdress frames the figure’s closed eyes.',
'Lakota fire': 'Four dark riders move forward through a blaze of orange and red, their outlines dissolving into the color. Deep purple shadows gather along the bottom.',
'Meadowlark Morning': 'Four riders face forward on horseback along a low grassy ridge. The background is a wide, pale apricot sky that leaves the figures sharply defined.',
'Misty Morning': 'A distant group of riders crosses a green-blue prairie beneath a pink and lilac sky. The pale suggestion of a bison appears within the mist above them.',
'North Dakota': 'Five riders move together across an open grassland. An enormous pink-and-blue sky fills most of the horizontal composition.',
'Prairie song': 'A small group of riders crosses a dark-green ridge beneath bands of violet, coral and pink clouds. The broad sky takes up most of the painting.',
'Spade': 'A blue-toned frontal portrait is overlaid with king-of-spades playing-card symbols. Pale blue, black and red strokes surround the figure and feathered adornment.',
'Star quilt': 'A frontal figure in pink and magenta stands before a large pointed star shape. Turquoise and orange outlines trace the face and shoulders.',
'Sweat Lodge': 'A nearly abstract composition shifts from deep rose at the top to pale turquoise below. Vertical drips and a faint cross-in-circle motif emerge through the color.',
'Tatonka': 'A single bison stands in profile against a vivid red and magenta ground. Golden yellow and dark brown paint model its heavy shoulders and head.',
'Transition': 'A figure bends forward amid a sweep of blue feathers and turquoise paint. Small star-like marks and red accents punctuate the composition.',
'Untitled': 'Five horseback riders form a dark silhouette against deep teal and midnight blue, with the figures partly absorbed by the surrounding haze.',
"Wacipi Wast'e": 'A dancer in feathered regalia turns amid blue, white and turquoise strokes. The circular ornaments and streaming feathers give the composition a strong sense of motion.',
'When The Drums Stop': 'A dancer bows their head, with tall feathers and pale strands of regalia moving across a blue-violet background. Fine speckles of paint surround the figure.',
'Wind Song Sister': 'Pale blue ridges and a low dark mountain range sit beneath a massive rolling cloud formation. A few tiny figures appear on the distant plain.'
}
missing=[x['title'] for x in featured if x['title'] not in descriptions]
if missing: raise ValueError('Missing descriptions: '+str(missing))
for x in featured:
    x['description']=descriptions[x['title']]
    x['alt']=descriptions[x['title']]
    x['slug']=slug(x['title'])

order=['Dakota Thunder','Meadowlark Morning',"Wacipi Wast'e",'Buffalo moon','Fancy Dance','Tatonka','Misty Morning','When The Drums Stop','Lakota fire','Horse play','Eagles woman','Blu Fancy','North Dakota','Feather Medicine','King','Horse Thief','Fancy Shawl Dancer','Four Winds','Wind Song Sister','Star quilt','Spade','Prairie song','Transition','Gamer','Sweat Lodge','Untitled']
arr=[by_title[name] for name in order]
assert len(arr)==26

styles = """
:root{color-scheme:light;--ink:#252723;--muted:#59615a;--line:#deded8;--red:#963d2d;--paper:#fbfbf8;--soft:#f0f0eb}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:system-ui,-apple-system,'Segoe UI',Arial,sans-serif;font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit}a:focus-visible,button:focus-visible{outline:3px solid #a9573b;outline-offset:4px}a:hover{color:#8a382c}
button{font:inherit}img{max-width:100%;height:auto}h1,h2,h3,p{margin-top:0}h1,h2,h3{font-weight:570;line-height:1.1;letter-spacing:-.042em}h1{font-size:clamp(3.5rem,6.5vw,6.9rem)}h2{font-size:clamp(2.1rem,4vw,4rem)}h3{font-size:clamp(1.3rem,2vw,1.85rem)}p{max-width:66ch}
.site-header{height:84px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);padding:0 max(5vw,24px);gap:18px}
.brand{font-size:1.1rem;font-weight:700;letter-spacing:-.025em;text-decoration:none;line-height:1.15}.brand small{display:block;font-size:.72rem;font-weight:450;letter-spacing:0;color:var(--muted);margin-top:4px}.nav{display:flex;align-items:center;gap:clamp(14px,2vw,32px);flex-wrap:wrap}.nav a{text-decoration:none;font-size:.9rem}.nav a:hover{text-decoration:underline;text-underline-offset:6px}
.wrap{width:min(1420px,90%);margin:0 auto}.hero{min-height:min(740px,78vh);display:grid;grid-template-columns:minmax(310px,40%) minmax(0,60%);align-items:stretch}.hero-copy{padding:clamp(52px,6vw,100px) 8% clamp(50px,5vw,95px) max(5vw,28px);display:flex;flex-direction:column;align-items:flex-start;justify-content:center}.hero h1{margin-bottom:20px}.artist-alias{font-size:1.2rem;font-weight:550;margin-bottom:28px}.hero-intro{font-size:clamp(1.08rem,1.5vw,1.35rem);line-height:1.55;max-width:21em;margin-bottom:35px}.text-link{font-weight:580;text-underline-offset:6px;text-decoration-thickness:1px}.hero-image{display:flex;align-items:center;justify-content:center;padding:32px 5vw 40px 0;background:var(--soft)}.hero-image img{display:block;max-height:640px;width:100%;height:auto;object-fit:contain;filter:drop-shadow(0 9px 16px rgba(18,18,18,.09))}.hero-image:hover img{filter:drop-shadow(0 9px 16px rgba(18,18,18,.13))}
main section{scroll-margin-top:25px}.section{padding:115px 0}.section-heading{margin-bottom:46px}.section-heading p{color:var(--muted);margin-top:14px;font-size:1.08rem}
.gallery{columns:3 290px;column-gap:clamp(24px,4vw,64px)}.painting{break-inside:avoid;margin:0 0 clamp(48px,6vw,92px)}.painting a{display:block;text-decoration:none}.painting img{display:block;width:100%;height:auto;background:#eeede9;transition:transform .27s ease}.painting a:hover img{transform:translateY(-3px)}.painting figcaption{margin-top:17px;font-weight:550;font-size:1.02rem}.painting figcaption span{display:none}
.about{background:var(--soft);padding:115px 0}.about-grid{display:grid;grid-template-columns:1fr 1.25fr;gap:min(12vw,170px)}.about-text p{color:#414a43;font-size:1.06rem;margin-bottom:22px}.about-text a{font-weight:600;text-underline-offset:4px}
.work-section{padding:115px 0}.project-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:60px}.project{border-top:1px solid #bbbdb5;padding-top:23px}.project h3{margin-bottom:16px}.project p{font-size:.98rem;color:var(--muted)}
.commission{background:#26352d;color:white;padding:115px 0}.commission .flex{display:grid;grid-template-columns:1.4fr 1fr;align-items:end;gap:75px}.commission p{color:#e6e6dc;line-height:1.75;font-size:1.1rem}.commission a{display:inline-block;color:white;text-underline-offset:7px;font-size:1.08rem;font-weight:650}.site-footer{display:flex;gap:30px;align-items:center;justify-content:space-between;padding:38px max(5vw,24px);border-top:1px solid var(--line);font-size:.85rem;color:var(--muted)}.site-footer a{text-decoration:none}.site-footer a:hover{text-decoration:underline}
.breadcrumb{margin:44px 0 40px;font-size:.93rem}.breadcrumb a{text-underline-offset:4px}.detail{padding:0 0 125px}.detail-grid{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(300px,.7fr);gap:min(7vw,95px);align-items:start}.detail-art{background:#eee;display:flex;align-items:center;justify-content:center}.detail-art img{display:block;width:100%;height:auto;object-fit:contain;max-height:760px}.detail-body{padding-top:16px}.detail-body h1{font-size:clamp(2.6rem,4vw,4.7rem);margin-bottom:33px}.detail-body>p{font-size:1.16rem;line-height:1.76;color:#3f4740}.detail-actions{margin-top:50px;display:flex;gap:22px;flex-wrap:wrap;align-items:center}.detail-actions a{font-size:.93rem;text-underline-offset:5px}.source-note{margin-top:75px;border-top:1px solid var(--line);padding:22px 0;font-size:.92rem;color:var(--muted)}.source-note summary{cursor:pointer;color:var(--ink);font-weight:600}.source-note p{margin-top:17px;max-width:55ch}.detail-pagination{border-top:1px solid var(--line);margin-top:96px;padding-top:30px;display:flex;justify-content:space-between;gap:20px}.detail-pagination a{font-size:.93rem}
.research{max-width:1100px;padding:90px 0 115px}.research h1{font-size:clamp(2.7rem,5vw,5rem);margin-bottom:20px}.research-lede{font-size:1.14rem;color:var(--muted)}.research h2{font-size:2.1rem;margin:78px 0 23px}.research a{text-underline-offset:4px}.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:.92rem}th{text-align:left;font-weight:650;color:#475047;border-bottom:2px solid var(--line);padding:16px 12px 16px 0}td{vertical-align:top;padding:15px 12px 15px 0;border-bottom:1px solid var(--line)}td:nth-child(2){white-space:nowrap}.research p{line-height:1.8}.research li{padding:6px 0}.research ul{padding-left:1.2rem}
@media(max-width:850px){.hero{grid-template-columns:1fr;min-height:auto}.hero-copy{padding:70px 5vw 40px}.hero-image{padding:32px 5vw;min-height:340px}.hero-image img{max-height:480px}.about-grid,.commission .flex,.detail-grid{grid-template-columns:1fr;gap:30px}.project-grid{grid-template-columns:1fr 1fr;gap:45px}.detail-grid{gap:45px}.detail-body{padding-top:0}}
@media(max-width:560px){.site-header{height:auto;min-height:88px;padding:18px 5vw;align-items:flex-start;flex-direction:column}.nav{gap:16px}.nav a{font-size:.84rem}.hero h1{font-size:3.7rem}.section,.about,.work-section,.commission{padding:75px 0}.section-heading{margin-bottom:33px}.gallery{columns:1}.painting{margin-bottom:55px}.project-grid{grid-template-columns:1fr;gap:34px}.site-footer{align-items:flex-start;flex-direction:column}.detail{padding-bottom:65px}.detail-pagination{margin-top:60px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.painting img{transition:none}}
"""
(root/'style.css').write_text(styles.strip()+'\n',encoding='utf-8')

def header(base='',section=None):
    def link(fragment, name):
        if section:
            return '<a href="'+base+'index.html#'+fragment+'">'+name+'</a>'
        return '<a href="#'+fragment+'">'+name+'</a>'
    return f'''<header class="site-header"><a href="{base}index.html" class="brand">Donald Brewer<small>Wakpa</small></a><nav aria-label="Main navigation" class="nav">{link('paintings','Paintings')}{link('about','About Don')}{link('public-art','Public Art')}<a href="{base}research/index.html">Research</a><a href="{base}index.html#commissions">Commissions</a></nav></header>'''

def footer(base=''):
    return f'<footer class="site-footer"><div>© Donald Brewer (Wakpa). Artwork reproduced with permission.</div><div><a href="{base}research/index.html">Research and documentation</a> &nbsp; <a href="mailto:supereukarya@gmail.com,dbrewer0708@gmail.com?subject=Donald%20Brewer%20portfolio%20inquiry">Contact</a></div></footer>'
def document(title,body, base=''):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#fbfbf8"><meta name="description" content="Paintings and projects by Donald Brewer (Wakpa)."><title>'+clean(title)+' · Donald Brewer (Wakpa)</title><link rel="stylesheet" href="'+base+'style.css"></head><body>'+body+'</body></html>'

tiles=[]
for w in arr:
    tiles.append(f'<figure class="painting"><a href="{url(w)}"><img loading="lazy" decoding="async" src="{clean(w["image"])}" alt="{clean(w["alt"])}"><figcaption>{clean(w["title"])}</figcaption></a></figure>')
hero=by_title['Dakota Thunder']
main= f'''{header()}<main><section class="hero"><div class="hero-copy"><h1>Donald Brewer</h1><div class="artist-alias">Wakpa</div><p class="hero-intro">Paintings and projects by Donald Brewer</p><a class="text-link" href="#paintings">View the paintings</a></div><a class="hero-image" href="{url(hero)}" aria-label="View Dakota Thunder"><img src="{hero['image']}" alt="{clean(hero['alt'])}" fetchpriority="high"></a></section>
<section id="paintings" class="section wrap"><div class="section-heading"><h2>Paintings</h2><p>Prairie landscapes, dancers, riders and portraits.</p></div><div class="gallery">{"".join(tiles)}</div></section>
<section id="about" class="about"><div class="wrap about-grid"><div><h2>About Don</h2></div><div class="about-text"><p>Donald Brewer, who paints under the name Wakpa, is an artist with Cheyenne River Sioux roots. Raised in Thornton, Colorado, he spent summers with family in South Dakota. His paintings return to the landscape of the Plains, the movement of horses and dancers, and the presence of people within vast open skies.</p><p>For years Don worked primarily in acrylic, developing layered color and precise transitions between figures, clouds and land. More recently, he has begun a new period of experimentation with oil paint and increasingly abstract compositions. He describes the switch in medium as a chance to learn all over again.</p><p>Don also makes traditional regalia and participates in powwow dancing. His experience in community art includes work with students and murals, alongside an extensive painting practice.</p><a href="research/index.html">Read the documented history</a></div></div></section>
<section id="public-art" class="work-section wrap"><div class="section-heading"><h2>Public Art</h2><p>Painting beyond the studio.</p></div><div class="project-grid"><div class="project"><h3>School murals</h3><p>Don recalls working with Denver-area middle-school students and teachers on collaborative murals for grades six through eight. The schools and project dates are being researched.</p></div><div class="project"><h3>Murals in Arizona</h3><p>He also recalls murals on buildings around Globe and San Carlos, Arizona, including a Geronimo-themed work that no longer survives. Archival photographs are being sought.</p></div><div class="project"><h3>New work in oils</h3><p>After decades of acrylic painting, Don is exploring a more abstract direction in oils while continuing his figurative work. New pieces will be added as they are documented.</p></div></div></section>
<section id="commissions" class="commission"><div class="wrap flex"><div><h2>Commissions and collaborations</h2><p>Interested in discussing an original painting, mural, public-art project or a workshop for young artists? For portfolio and project inquiries, email Don and Super Eukarya together.</p></div><div><a href="mailto:supereukarya@gmail.com,dbrewer0708@gmail.com?subject=Donald%20Brewer%20commission%20inquiry">Email Don and Super Eukarya</a></div></div></section></main>{footer()}'''
(root/'index.html').write_text(document('Paintings and projects',main),encoding='utf-8')

(root/'paintings').mkdir(exist_ok=True)
for i,w in enumerate(arr):
    previous=arr[i-1] if i>0 else None
    next_w=arr[i+1] if i+1<len(arr) else None
    prev_link = f'<a href="{slug(previous["title"])}.html">← {clean(previous["title"])}</a>' if previous else '<span></span>'
    next_link = f'<a href="{slug(next_w["title"])}.html">{clean(next_w["title"])} →</a>' if next_w else '<span></span>'
    published=w.get('shown','unknown')
    creation=w.get('year','unknown')
    notes=f'''<details class="source-note"><summary>Artwork record and source</summary><p>Artist: Donald Brewer (Wakpa). Creation date: {clean(creation)}. Online publication date: {clean(published)}. Medium: {clean(w.get('medium','unknown'))}. Current physical location: unknown.</p><p>Publication dates refer to online listings, not necessarily the date the painting was created. <a href="{clean(w['url'])}" target="_blank" rel="noopener noreferrer">View this artwork on Fine Art America</a>.</p></details>'''
    piece=f'''{header('../',True)}<main class="detail wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html#paintings">Paintings</a> <span aria-hidden="true">›</span> {clean(w['title'])}</nav><div class="detail-grid"><div class="detail-art"><img src="../{clean(w['image'])}" alt="{clean(w['alt'])}" fetchpriority="high"></div><div class="detail-body"><h1>{clean(w['title'])}</h1><p>{clean(w['description'])}</p><div class="detail-actions"><a href="{clean(w['url'])}" target="_blank" rel="noopener noreferrer">See the original listing ↗</a><a href="../index.html#paintings">All paintings</a></div>{notes}</div></div><div class="detail-pagination">{prev_link}{next_link}</div></main>{footer('../')}'''
    (root/'paintings'/(slug(w['title'])+'.html')).write_text(document(w['title'],piece,'../'),encoding='utf-8')

(root/'research').mkdir(exist_ok=True)
trs=[]
for x in arr:
    trs.append(f'<tr><td><a href="../{url(x)}">{clean(x["title"])}</a></td><td>{clean(x.get("shown","unknown"))}</td><td>Unknown</td><td><a href="{clean(x["url"])}" target="_blank" rel="noopener noreferrer">Artist listing</a></td></tr>')
other=[]
for x in external:
    other.append(f'<tr><td><a target="_blank" rel="noopener noreferrer" href="{clean(x["url"])}">{clean(x["title"])}</a></td><td>{clean(x.get("year","unknown"))}</td><td>{clean(x.get("shown","unknown"))}</td><td>{clean(x.get("source","unknown"))}</td></tr>')
research=f'''{header('../',True)}<main class="research wrap"><h1>Research and documentation</h1><p class="research-lede">An independent working record of Don's paintings and earlier projects. This section preserves sources and unresolved information without putting archival labels into the gallery.</p>
<h2>Published paintings</h2><p>These 26 paintings appear in the artist's Fine Art America portfolio. Their upload dates can be verified on the individual pages. The date an image was uploaded is not a confirmed date of creation. Physical locations remain unknown unless otherwise established.</p><div class="table-wrap"><table><thead><tr><th>Painting</th><th>Online publication</th><th>Creation</th><th>Source</th></tr></thead><tbody>{"".join(trs)}</tbody></table></div>
<h2>Other catalog and auction records</h2><p>These 11 listings are documented outside the artist's Fine Art America portfolio. Some may represent the same physical painting as another record; no duplication is asserted without image comparison. A dated auction appearance is separate from a work's creation year.</p><div class="table-wrap"><table><thead><tr><th>Recorded title</th><th>Creation year</th><th>Listing or sale date</th><th>Reference</th></tr></thead><tbody>{"".join(other)}</tbody></table></div>
<h2>Biographical references</h2><p><a href="https://sites.clarkson.edu/gallery/browse-the-artists/don-brewer-wakpa/" target="_blank" rel="noopener noreferrer">Clarkson University Art Gallery</a> maintains an artist biography with reported collection associations, including the Willis Tower. Don has additionally described a Penn State painting acquired through an alumnus's collection donation. The specific works remain to be located and independently documented.</p>
<h2>Murals and community projects</h2><p>Don's oral history references Denver-area school murals with middle-school students, murals around Globe and San Carlos in Arizona, traditional regalia and dance, and future public-art interests. No photographs or specific project dates have yet been verified for those historical murals. Those details should not be treated as independently confirmed commissions.</p>
<h2>How this catalogue is maintained</h2><p>Artist-owned reproductions are shown with permission. Source links identify where each image or listing was found. Artwork descriptions document visible composition rather than claiming knowledge of the artist's intentions. This is a working portfolio, not a catalogue raisonné; additions and corrections are welcome.</p><p>For corrections or documentation, <a href="mailto:supereukarya@gmail.com,dbrewer0708@gmail.com?subject=Donald%20Brewer%20archive%20documentation">contact the portfolio coordinator</a>.</p></main>{footer('../')}'''
(root/'research'/'index.html').write_text(document('Research',research,'../'),encoding='utf-8')
(root/'catalog.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print('Generated',len(arr),'artist painting pages and',len(external),'additional research records')

# Responsive and editorial refinements
css_path = root / 'style.css'
css_path.write_text(css_path.read_text(encoding='utf-8') + """
.hero > * { min-width: 0 }
@media(max-width:560px){
.site-header{width:100%}
.nav{width:100%;display:grid;grid-template-columns:repeat(3,max-content);column-gap:18px;row-gap:10px}
.hero{display:block;width:100%;overflow:hidden}
.hero-copy{min-width:0}
.hero h1{font-size:clamp(2.85rem,12vw,3.25rem);overflow-wrap:break-word}
.hero h1 span{display:block}
.hero-image{max-width:100%;width:100%;min-width:0;overflow:hidden}
.hero-image img{max-width:100%;width:100%;height:auto}
}
""", encoding='utf-8')
home_path = root / 'index.html'
home_path.write_text(home_path.read_text(encoding='utf-8').replace('<h1>Donald Brewer</h1>','<h1>Donald <span>Brewer</span></h1>'), encoding='utf-8')
research_path = root / 'research' / 'index.html'
research_text = research_path.read_text(encoding='utf-8')
research_text=research_text.replace('reported collection associations, including the Willis Tower.', 'collection associations including Akta Lakota Museum, the Crazy Horse Memorial, Red Cloud Indian School, United Tribes Technical College and the Willis Tower. The original biography should be consulted for the wording of each claim.')
research_text=research_text.replace('Those details should not be treated as independently confirmed commissions.</p>', 'Those details should not be treated as independently confirmed commissions. Don has also described service in the U.S. Marine Corps and several years as a firefighter with San Carlos Apache; dates and independent records are still being sought.</p>')
research_path.write_text(research_text,encoding='utf-8')
