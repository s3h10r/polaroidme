#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
import datetime as dt
import json
import os
import site
import sys
import logging
from docopt import docopt
import exifread
from PIL import Image, ImageDraw, ImageFont, ExifTags

from polaroidme.filters.filters import convert_ascii_to_image, convert_image_to_ascii
from polaroidme.helpers.helpers import get_exif, get_resource_file, show_error
from polaroidme.helpers.gfx import crop_image_to_square
from polaroidme.helpers.gfx import scale_image_to_square, scale_image, scale_square_image



# --- configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler() # console-handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
# ---

# Image size constraints
IMAGE_SIZE   = 800                      # the thumbnail size (= the inner picture)
IMAGE_TOP    = int(IMAGE_SIZE / 16)     # added space on top
IMAGE_BOTTOM = int(IMAGE_SIZE / 5.333)  # added space on bottom
IMAGE_LEFT   = int(IMAGE_SIZE / 16)     # ...
IMAGE_RIGHT  = int(IMAGE_SIZE / 16)     # ...
BORDER_SIZE  = 3
# Colors
COLOR_FRAME   = (237, 243, 214)
COLOR_BORDER  = (0, 0, 0)
COLOR_TEXT_TITLE = (58, 68, 163)
COLOR_TEXT_DESCR = COLOR_TEXT_TITLE
COLOR_BG_INNER = (0,0,0)                # usefull if --nocrop
# Font for the caption text
RESOURCE_FONT      = "fonts/default.ttf"
RESOURCE_FONT_SIZE = int(IMAGE_BOTTOM - (IMAGE_BOTTOM * 0.9))
RESOURCE_CONFIG_FILE="polaroidme.conf"

TEMPLATE_BOXES = {} # if --template is used we need a dict with templatename and box-definition for the image

__version__ = (0,9,33)

# ---

def setup_globals(size, configfile=None, template = None, show = True):
    global IMAGE_SIZE
    global IMAGE_TOP
    global IMAGE_BOTTOM
    global IMAGE_LEFT
    global IMAGE_RIGHT
    global BORDER_SIZE
    global RESOURCE_FONT_SIZE
    global TEMPLATE_BOXES

    if configfile:
        if not (os.path.isfile(configfile)):
            log.warning("configfile {} not found... please always give absolute paths to config-file to avoid confusions :D".format(configfile))
            sys.exit(1)
        # --- load config file (if any)
        with open(configfile) as f:
            log.info("reading config...")
            code = compile(f.read(), configfile, 'exec')
            global_vars ={}
            local_vars = {}
            exec(code,global_vars, local_vars)
            TEMPLATE_BOXES=local_vars['TEMPLATE_BOXES']
    else:
        if template:
            log.critical("to use --template you need to define a config-file")
            sys.exit(1)

    if not template:
        IMAGE_SIZE   = size
        IMAGE_TOP    = int(IMAGE_SIZE / 16)
        IMAGE_BOTTOM = int(IMAGE_SIZE / 5.333)
        IMAGE_LEFT   = int(IMAGE_SIZE / 16)
        IMAGE_RIGHT  = int(IMAGE_SIZE / 16)
        BORDER_SIZE  = 3
        RESOURCE_FONT_SIZE = int(IMAGE_BOTTOM - (IMAGE_BOTTOM * 0.2))
    else:
        # calculate the values based on the properties of the template image
        # --- setup templates
        for k in TEMPLATE_BOXES:
            TEMPLATE_BOXES[k] = [int(round(f)) for f in TEMPLATE_BOXES[k]]
        # ---

        box = TEMPLATE_BOXES[os.path.basename(template)]
        w = box[2] - box[0]
        h = box[3] - box[1]
        if w != h:
            log.warning("boxdefinition for template {} is not a square. w,h {},{}".format(k,w,h))
            log.warning("auto-fixing => making it square...")
            if w > h: #AUTO_FIX
                box[3] += (w - h)
            else:
                box[2] += (h - w)
            TEMPLATE_BOXES[os.path.basename(template)] = [box[0], box[1], box[2], box[3]]
            box = TEMPLATE_BOXES[os.path.basename(template)]
            w = box[2] - box[0]
            h = box[3] - box[1]
            log.warning("boxdefinition for template {} auto-adjusted to: w,h {},{}".format(k,w,h))
            assert(w == h)
        size = w
        assert((size == w) and (size== h))
        IMAGE_SIZE = size
        # overwrite the above calculated  _TOP,_BOTTOM, ... values
        # by the one our template "dictates"
        try:
            tpl = Image.open(template)
        except:
            tpl = Image.open(get_resource_file(template))

        tpl_x, tpl_y = tpl.size
        tpl.close()
        IMAGE_TOP = box[1]
        IMAGE_BOTTOM = tpl_y - (IMAGE_TOP + IMAGE_SIZE)
        IMAGE_LEFT = box[0]
        IMAGE_RIGHT = tpl_x - (IMAGE_LEFT + w)
        BORDER_SIZE  = 3
        RESOURCE_FONT_SIZE = int(IMAGE_BOTTOM - (IMAGE_BOTTOM * 0.2))

    # --- show
    if show:
        SETTINGS = {
        'IMAGE_SIZE' : IMAGE_SIZE,
        'IMAGE_TOP' : IMAGE_TOP,
        'IMAGE_BOTTOM' : IMAGE_BOTTOM,
        'IMAGE_LEFT' : IMAGE_LEFT,
        'IMAGE_RIGHT' : IMAGE_RIGHT,
        'BORDER_SIZE' : BORDER_SIZE,
        'RESOURCE_FONT_SIZE' : RESOURCE_FONT_SIZE,
        'TEMPLATE_KEY' : template,
        'TEMPLATE_VALUE': None,# we fill this if template ist != None
        }
        if template:
            SETTINGS['TEMPLATE_KEY'] = os.path.basename(template),
            SETTINGS['TEMPLATE_VALUE'] = TEMPLATE_BOXES[os.path.basename(template)],
        print(json.dumps(SETTINGS,indent=4,sort_keys=True))


def make_polaroid(source, size, options, align, title, f_font = None, font_size = None, template = None, bg_color_inner=(255,255,255),filter_func=None):
    """
    Converts an image into polaroid-style. This is the main-function of the module
    and it is exposed. It can be imported and used by any Python-Script.

    returns
        PIL image instance
    """
    caption = title
    img_in = None
    if isinstance(source,Image.Image):
        img_in = source
    else:
        img_in = Image.open(source)
    img_in.load()
    img = rotate_image(img_in, options['rotate'])
    [w, h] = img.size
    # Determine ratio of image length to width to
    # determine oriantation (portrait, landscape or square)
    image_ratio = float(float(h)/float(w))
    log.debug("image_ratio: %f size_w: %i size_h: %i" % (image_ratio, w, h))
    if round(image_ratio, 1) >= 1.3: # is_portrait
        log.info("source image ratio is %f (%s)" % (image_ratio, 'is_portrait'))
    elif round(image_ratio, 1) == 1.0: # is_square
        log.info("source image ratio is %f (%s)" % (image_ratio, 'is_square'))
    elif round(image_ratio, 1) <= 0.8: # is_landscape
        log.info("source image ratio is %f (%s)" % (image_ratio, 'is_landscape'))
    if options['crop']:
        img = crop_image_to_square(img, align)
    else:
        img = scale_image_to_square(img, bg_color=bg_color_inner)
    img = scale_square_image(img, size)
    if filter_func:
        img = filter_func(img)
    if template:
        log.warning("--template is experimental!")
        img = _paste_into_template(image=img, template=template)
        description = None
        img = add_text(img, caption, description, f_font = f_font, font_size = font_size)
    else:
        img = add_frame(img)
        description = None
        img = add_text(img, caption, description, f_font = f_font, font_size = font_size)
    return img


def _paste_into_template(image = None, template = './templates/fzm-Polaroid.Frame-01.jpg', box=None):
    """
    """
    if not box:
        box = TEMPLATE_BOXES[os.path.basename(template)]
    try:
        img_tpl = Image.open(template)
    except:
        img_tpl = Image.open(get_resource_file(template))

    w = int(box[2] - box[0])
    h = int(box[3] - box[1])
    log.debug("box-size the picture will be pasted into is (w,h) {} {}".format(w,h))
    region2copy = image.crop((0,0,image.size[0],image.size[1]))
    if region2copy.size[0] > w:
        # Downsample
        log.info("downsampling... (good)")
        region2copy = region2copy.resize((w,h),Image.ANTIALIAS)
    else:
        log.info("upscaling... (not so good ;)")
        region2copy = region2copy.resize((w,h), Image.BICUBIC)
    assert(region2copy.size == (w,h))
    #print(region2copy.size, (w,h))
    #print(region2copy.size, box)
    img_tpl.paste(region2copy,box)
    return img_tpl


def rotate_image(image, rotation):
    """
    rotates the image appropriately
    """
    if rotation == "clockwise":
        image = image.rotate(-90)
    elif rotation == "anticlockwise":
        image = image.rotate(90)
    return image

def add_frame(image, border_size = 3, color_frame = COLOR_FRAME, color_border = COLOR_BORDER):
    """
    adds the frame around the image
    """
    frame = Image.new("RGB", (IMAGE_SIZE + IMAGE_LEFT + IMAGE_RIGHT, IMAGE_SIZE + IMAGE_TOP + IMAGE_BOTTOM), COLOR_BORDER)
    # Create outer and inner borders
    draw = ImageDraw.Draw(frame)
    draw.rectangle((BORDER_SIZE, BORDER_SIZE, frame.size[0] - BORDER_SIZE, frame.size[1] - BORDER_SIZE), fill = COLOR_FRAME)
    draw.rectangle((IMAGE_LEFT - BORDER_SIZE, IMAGE_TOP - BORDER_SIZE, IMAGE_LEFT + IMAGE_SIZE + BORDER_SIZE, IMAGE_TOP + IMAGE_SIZE + BORDER_SIZE), fill = COLOR_BORDER)
    # Add the source image
    frame.paste(image, (IMAGE_LEFT, IMAGE_TOP))
    return frame

def add_text(image, title = None, description = None, f_font = RESOURCE_FONT, font_size = RESOURCE_FONT_SIZE):
    """
    adds a title (string) to the image
    description is unused at the moment

    returns
        PIL Image instance
    """
    if (title is None) or (len(title)==0):
        return image
    size = font_size
    f_font = get_resource_file(f_font)
    try:
        font_title = ImageFont.truetype(f_font, font_size)
    except:
        show_error("Could not load resource '%s'." % f_font)
    width, height = font_title.getsize(title)
    while ((width > IMAGE_SIZE) or (height > IMAGE_BOTTOM)) and (size > 0):
        size = size - 2
        try:
            font_title = ImageFont.truetype(f_font, font_size)
        except:
            show_error("Could not load resource '%s'." % f_font)
        font_title = ImageFont.truetype(get_resource_file(f_font), size)
        width, height = font_title.getsize(title)
        log.debug("searching suiting font_size... trying {}".format(size))
    if (size <= 0):
        showError("Text is too large")
    draw = ImageDraw.Draw(image)
    pos_x = (IMAGE_SIZE + IMAGE_LEFT + IMAGE_RIGHT - width) / 2
    pos_y = IMAGE_SIZE + IMAGE_TOP + ((IMAGE_BOTTOM - height)) / 2
    log.info("title fontsize {} pos_x, pos_y {},{}".format(size, pos_x, pos_y))
    draw.text(
        (pos_x, pos_y),
        title, font = font_title, fill = COLOR_TEXT_TITLE,
    )
    return image


#if __name__ == '__main__':
def main(args):
    options = { 'rotate': None, 'crop' : True } # defaults
    source = None
    size = IMAGE_SIZE # inner size, only the picture without surrounding frame
    target = None
    align = "center"
    title = ""
    f_font = None
    template = None
    configfile = get_resource_file(RESOURCE_CONFIG_FILE)
    max_size = None # max size (width) of the contactsheet
    add_exif_to_title = None

    bg_color_inner = COLOR_BG_INNER
    # process options
    source = args['<source-image>']
    if source.lower() in('-', 'stdin'):
        raise Exception("hey, great idea! :) reading from STDIN isn't supported yet but it's on the TODO-list.")
    if args['--clockwise']:
        option['rotate'] = 'clockwise'
    elif args['--anticlock']:
        option['rotate'] = 'anticlockwise'
    if args['--crop']:
        options['crop'] = True
    elif args['--nocrop']:
        options['crop'] = False
    if args['--size-inner']:
        size = int(args['--size-inner'])
    if args['--alignment']: # only used if --crop
        align = args['--alignment']
    if args['--title']:
        title = args['--title']
    if args['--title-meta']:
        add_exif_to_title = True
    if args['--font']:
        f_font = args['--font']
    else:
        f_font = RESOURCE_FONT
    if args['--output']:
        target = args['--output']
    if args['--template']:
        template = args['--template']
    if args['--config']:
        configfile = args['--config']
    filter_2ascii = False
    if args['--filter-2ascii']:
        filter_2ascii = True
    # ---
    if template:
        size = None # needs to be calculated
    setup_globals(size, configfile, template)
    size = IMAGE_SIZE
    if args['--max-size']:
        max_size = int(args['--max-size'])
    # heree we go...
    if add_exif_to_title:
        exif_data = get_exif(source)
        if ('EXIF DateTimeOriginal') in exif_data:
            v = exif_data['EXIF DateTimeOriginal']
            timestamp = dt.datetime.strptime(str(v), '%Y:%m:%d %H:%M:%S')
            meta = timestamp
            if len(title) > 0:
                title += " "
            title += "%s" % (timestamp)
        else:
            log.warning("--title-meta set but exif_data about DateTime unavailable for the input-image. :-/ : {}; ;".format(fn))
    name, ext = os.path.splitext(source)
    if not os.path.isfile(source):
        show_error("Source file '%s' does not exist." % source)
    if not target:
        target = name + ".polaroid.png"
    if not align in ("left", "right", "top", "bottom", "center"):
        show_error("Unknown alignment %s." % align)
    # Prepare our resources
    f_font = get_resource_file(f_font)
    font_size = IMAGE_BOTTOM
    if filter_2ascii:
        img = Image.open(source)
        img_as_ascii = convert_image_to_ascii(img)
        img = convert_ascii_to_image(img_as_ascii)
        source = img
    # finally create the polaroid.
    img = make_polaroid(
        source = source, size = size, options = options, align =align,
        title = title, f_font = f_font, font_size = font_size,
        template = template,
        bg_color_inner = bg_color_inner)
    log.debug("size: %i %i" % (img.size[0], img.size[1]))
    # ---  if --max-size is given: check if currently bigger and downscale if necessary...
    if max_size:
        xs, ys = img.size
        if (xs > max_size) or (ys > max_size):
            log.info('scaling result down to --max_size %i' % max_size)
            factor = 1
            if xs >= ys:
                factor = max_size / xs
            else:
                factor = max_size / ys
            x_new = int(img.width * factor)
            y_new = int(img.height * factor)
            img = img.resize((x_new,y_new),Image.ANTIALIAS)
    # yai, finally ... :)
    img.save(target)
    print(target)
