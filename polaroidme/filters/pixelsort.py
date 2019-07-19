#!/usr/bin/env python3
"""
pixelsort - rearranges the pixels of an input image via sorting them by color
latest source: https://github.com/s3h10r/pixelsort
"""
import logging
import math
import sys
import colorsys
from PIL import Image

# --- configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler() # console-handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
# ---


__version__ = "0.2.0"

def lum (r,g,b):
    """
    sorting directly for the perceived luminosity of a colour
    """
    return math.sqrt( .241 * r + .691 * g + .068 * b )

def do_pixelsort(image, algo=10):
    img_in = image
    if not isinstance(image, Image.Image):
        img_in = Image.open(image)
    # get the image as pixelmap (PixelAcces instance)
    # this allows accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img_in_pixels = img_in.load()
    [xs, ys] = img_in.size
    colors_rgb = []
    # Examine each pixel in the image file
    for x in range(0, xs):
      for y in range(0, ys):
        # ( )  Get the RGB color of the pixel
        [r, g, b] = img_in_pixels[x, y]
        colors_rgb.append([r,g,b])

    # sort the colors by choosen algo
    colors_s = colors_rgb
    sort_algo = algo
    if sort_algo == 0: # selftest 1:1 samme picture out as in
        colors_s = colors_rgb
    elif sort_algo == 1:
        colors_s.sort() # stupido
    elif sort_algo == 10:
        colors_s.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb) )
    elif sort_algo == 20:
        colors_s.sort(key=lambda rgb: lum(*rgb) )

    # create the suiting output image
    img_out = Image.new('RGB', (xs, ys), 'white')
    img_out_pixels = img_out.load()
    # iterate over every pixel of the image and set it to the value
    # corresponding the now ordered colors  ...
    for x in range(0, xs):
      for y in range(0, ys):
          idx = x * ys + y
          img_out_pixels[x,y] = tuple(colors_s[idx])
    return img_out
