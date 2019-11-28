#!/usr/bin/env python3

import sys
from PIL import Image, ImageDraw, ImageFont

SIZE = (100, 100)
MAX_FONT_SIZE = 100
MARGIN = 10
FONT = '/usr/share/fonts/truetype/open-sans/OpenSans-Bold.ttf'

def maximize_text_size(d, text):
  for size in range(MAX_FONT_SIZE, 1, -1):
    font = ImageFont.truetype(FONT, size)
    x, y = d.textsize(text, font=font)

    # https://stackoverflow.com/questions/59008322/pillow-imagedraw-text-coordinates-to-center/59008967#59008967
    offset_x, offset_y = font.getoffset(text)
    x += offset_x
    y += offset_y

    if x < SIZE[0] - 2 * MARGIN and y < SIZE[1] - 2 * MARGIN:
      print("Font size: {}".format(size), (x,y))
      return font, x, y

  raise Exception()
 
with open(sys.argv[1]) as f:
  for i in range(1, 7):
    name = '{}.png'.format(i)
    text = f.readline().strip()
    print(name)

    im = Image.new('L', SIZE, color=0)
    d = ImageDraw.Draw(im)

    font, x, y = maximize_text_size(d, text)

    position = ((SIZE[0] - x) / 2, (SIZE[1] - y) / 2)
    print(position)

    d.text(position, text, font=font, fill=256)
    im.save(name)
