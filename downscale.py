"""Downscale a 2048x2048 render to the 1024x1024 entry image (PIL Lanczos).

Usage: python3 downscale.py render-2048.png entry.png
Also verifies the result is 1024x1024 and at most 1 MiB, and exits non-zero
when it is not, so a bad render fails loudly instead of shipping silently.
"""
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src)
assert im.size == (2048, 2048), f"expected 2048x2048, got {im.size}"
im = im.resize((1024, 1024), Image.LANCZOS)
im.save(dst, "PNG", optimize=True)
import os
size = os.path.getsize(dst)
print(f"wrote {dst}: {im.size} {size} bytes")
assert size <= 1048576, f"entry.png is {size} bytes, over the 1 MiB cap"
