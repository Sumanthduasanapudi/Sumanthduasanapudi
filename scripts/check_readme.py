"""Validate local README/demo assets and section links without network access."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import re, sys
ROOT=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        self.links.extend(v for k,v in attrs if k in {'src','srcset','href'} and v)
errors=[];checked=0
for path in [ROOT/'README.md',*(ROOT/'docs').rglob('*.md')]:
    text=path.read_text();parser=Links();parser.feed(text)
    headings=[];counts={}
    for heading in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        slug=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-');count=counts.get(slug,0);counts[slug]=count+1
        headings.append(slug+(f'-{count}' if count else ''))
    for link in parser.links+re.findall(r'!?\[[^\]]*\]\(([^\s)]+)',text):
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        checked+=1
        if not u.path:
            if u.fragment and unquote(u.fragment) not in headings:errors.append(f'{path.relative_to(ROOT)}: missing anchor {link}')
            continue
        target=(path.parent/unquote(u.path)).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():errors.append(f'{path.relative_to(ROOT)}: missing asset {link}')
    if text.count('<details')!=text.count('</details>'):errors.append(f'{path}: unbalanced project details')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {checked} local asset and section references across README and demo notes.')
