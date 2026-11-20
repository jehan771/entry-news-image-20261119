#!/bin/sh
# Render frontpage-template.html to entry.png (1024x1024, <=1 MiB).
# 1) 2x copy with CSS zoom:2  2) screenshot at 2048  3) PIL Lanczos to 1024.
set -e
cd "$(dirname "$0")"
python3 make2x.py frontpage-template.html frontpage-2x.html
node "$HOME/workspace/makefun/shot-tools/shot.mjs" "file://$PWD/frontpage-2x.html" render-2048.png 2048 2048
python3 downscale.py render-2048.png entry.png
ls -la entry.png
python3 -c "from PIL import Image; im=Image.open('entry.png'); print(im.size, im.format)"
