"""Make a 2x render copy of the front-page template.

Reads the 1024x1024 template and writes a copy with CSS zoom:2 on the body,
so a 2048x2048 screenshot captures the page at twice the resolution.
Usage: python3 make2x.py frontpage-template.html frontpage-2x.html
"""
import sys

src, dst = sys.argv[1], sys.argv[2]
html = open(src, encoding="utf-8").read()
marker = "<body>"
assert marker in html, "template has no <body> tag"
html = html.replace(marker, '<body style="zoom:2">', 1)
open(dst, "w", encoding="utf-8").write(html)
print(f"wrote {dst}")
