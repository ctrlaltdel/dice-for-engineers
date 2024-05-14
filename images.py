#!/usr/bin/env python3

import sys
from subprocess import run

SIZE = (100, 100)
MAX_FONT_SIZE = 100
MARGIN = 10
FONT = './OpenSans-Bold.ttf'

with open(sys.argv[1]) as f:
  for i in range(1, 7):
    name = '{}.png'.format(i)
    text = f.readline().strip()

    run(("convert", "-gravity", "center", "-background", "black", "-fill", "white", "-size", "100x100", "-font", FONT, "caption:" + text, name))
