#!/usr/bin/env python3
# coding: utf-8
"""
Copyright (c) 2018 Jianzhu Guo (MIT License)
original source of this [ImageToAscii](https://github.com/cleardusk/ImageToAscii/blob/master/img_to_ascii.py)
"""
import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
import argparse

PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255  # PIL color to use for "off"

large_font = 12  # get better resolution with larger size


def _convert_ascii_to_img(ascii_str, font_path='fonts/Menlo-Regular.ttf'):
    """Convert text file to a grayscale image with black characters on a white background.

    arguments:
    ascii_str - string of ascii format
    font_path - path to a font file (for example impact.ttf)
    """
    grayscale = 'L'
    ascii_str = ascii_str.replace('\r\n', '\n')  # for windows
    lines = ascii_str.rstrip().split('\n')

    # choose a font (you can see more detail in my library on github)
    # font_path = font_path or 'cour.ttf'  # Courier New. works in windows. linux may need more explicit path
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    # make the background image based on the combination of font and lines
    pt2px = lambda pt: int(round(pt * 96.0 / 72))  # _convert points to pixels
    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    # max height is adjusted down because it's too large visually for spacing
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    max_width = pt2px(font.getsize(max_width_line)[0])
    height = max_height * len(lines)  # perfect or a little oversized
    width = int(round(max_width + 40))  # a little oversized
    image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)

    # draw each line of text
    vertical_position = 5
    horizontal_position = 5
    line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
    for line in lines:
        draw.text((horizontal_position, vertical_position),
                  line, fill=PIXEL_ON, font=font)
        vertical_position += line_spacing

    # return image
    # crop the text
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image


def convert_ascii_to_img(image_as_ascii):
    ascii_str = image_as_ascii
    image = _convert_ascii_to_img(ascii_str)
    return image
