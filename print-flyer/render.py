import sys
from playwright.sync_api import sync_playwright
src, png, pdf = sys.argv[1:4]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1056,'height':816}, device_scale_factor=2)
    pg.goto('file://' + src); pg.wait_for_timeout(500)
    # report any overflow inside a flyer
    print(pg.evaluate("""() => { const f=document.getElementById('flyer'); let tot=0; for (const c of f.children) tot+=c.getBoundingClientRect().height; return {available:f.clientHeight, used:Math.round(tot)} }"""))
    pg.screenshot(path=png)
    pg.pdf(path=pdf, width='11in', height='8.5in', print_background=True, prefer_css_page_size=True)
    b.close()
