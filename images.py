#!/usr/bin/env python3

import sys
from PIL import Image, ImageDraw, ImageFont

SIZE = (100, 100)
MAX_FONT_SIZE = 100
MARGIN = 10
FONT = './OpenSans-Bold.ttf'

with open(sys.argv[1]) as f:
  for i in range(1, 7):
    name = '{}.png'.format(i)
    text = f.readline().strip()
    print(name)

    im = Image.new('L', SIZE, color=0)
    d = ImageDraw.Draw(im)

    font = ImageFont.truetype(FONT)

    d.text((0, 0), text, font=font, fill=256, anchor='mm')
    im.save(name)
