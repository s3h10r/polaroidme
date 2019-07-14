#!/usr/bin/env python3
"""
polaroidme.py

Usage:

  polaroidme.py [options] source-image alignment [caption]

Where:

  source-image  name of the image file to transform. If no extension is
                specified .jpg is assumed.
  alignment     one of 'top', 'left', 'bottom', 'right' or 'center'. This
                specifies the portion of the image to include in the final
                output. 'top' and 'left' are synonomous as are 'bottom' and
                'right'.
  caption       If specified defines the caption to be displayed at the
                bottom of the image.

Available options are:

  --nocrop        # TODOP2
  --clockwise     Rotate the image clockwise before processing
  --anticlockwise Rotate the image anti-clockwise before processing
"""
import os
import sys
import logging
from PIL import Image, ImageDraw, ImageFont

# --- configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler() # console-handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
# ---

RESOURCE_FONT      = "caption.ttf"
RESOURCE_FONT_SIZE = 142

# Image size constraints
IMAGE_SIZE   = 800
IMAGE_TOP    = IMAGE_SIZE / 16 # 50
IMAGE_BOTTOM = IMAGE_SIZE / 5.333
IMAGE_LEFT   = IMAGE_SIZE / 16
IMAGE_RIGHT  = IMAGE_SIZE / 16

BORDER_SIZE  = 3
# Colors
COLOR_FRAME   = (237, 243, 214)
COLOR_BORDER  = (0, 0, 0)
COLOR_TEXT_TITLE = (58, 68, 163)
COLOR_TEXT_DESCR = COLOR_TEXT_TITLE
# Font for the caption text
FONT_TITLE = None

__author__ = 'Sven Hessenmüller (sven.hessenmueller@gmail.com)'
__date__ = '2019'
__version__ = (0,1,0)
__license__ = "MIT"

# --- argparsing helpers etc
def get_resource_file(basefile):
    """
    Get the fully qualified name of a resource file
    """
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), basefile)

def get_option(args):
    """
    Check the argument list for an option (starting with '--').

    Returns the adjusted argument list and the option found.
    """
    if len(args) == 0:
        return None, args
    if args[0][:2] == "--":
        return args[0][2:], args[1:]
    return None, args

def get_argument(args):
    """
    Get the next argument from the command line parameters

    Returns the adjusted argument list and the value of the argument.
    """
    if len(args) == 0:
        return None, args
    return args[0], args[1:]

def show_error(msg):
    """
    Show an error message and exit
    """
    log.critical("Error: %s" % msg)
    sys.exit(1)
# ---

def rotate_image(image, rotation):
    """
    rotates the image appropriately
    """
    if rotation == "clockwise":
        image = image.rotate(-90)
    elif rotation == "anticlockwise":
        image = image.rotate(90)
    return image

def crop_image_to_square(image, align):
    """
    crops the image into square-format

    returns cropped Image
    """
    # Do the cropping needed
    if image.size[0] > image.size[1]:
        if align in ("left", "top"):
            box = (0, 0, image.size[1], image.size[1])
        elif align in ("right", "bottom"):
            delta = image.size[0] - image.size[1]
            box = (delta, 0, image.size[0], image.size[1])
        elif align == "center":
            delta = (image.size[0] - image.size[1]) / 2
            box = (delta, 0, image.size[0] - delta, image.size[1])
        image = image.crop(box)
        image.load()
    elif image.size[1] > image.size[0]:
        if align in ("left", "top"):
            box = (0, 0, image.size[0], image.size[0])
        elif align in ("right", "bottom"):
            delta = image.size[1] - image.size[0]
            box = (0, delta, image.size[0], image.size[1])
        elif align == "center":
            delta = (image.size[1] - image.size[0]) / 2
            box = (0, delta, image.size[0], image.size[1] - delta)
        image = image.crop(box)
        image.load()
    # make sure we have a perfect square
    log.debug("cropped to size: %i %i" % (image.size[0], image.size[1]))
    if image.size[0] != image.size[1]:
        if image.size[0] > image.size[1]:
            box = (0, 0, image.size[1], image.size[1])
        else:
            box = (0, 0, image.size[0], image.size[0])
        image = image.crop(box)
        image.load()
        log.debug("re-cropped to size: %i %i" % (image.size[0], image.size[1]))
    return image

def scale_image(image, size):
    """
    scales the image to size (up-/downsampling)

    returns scaled image
    """
    if image.size[0] != image.size[1]:
        raise Exception("ouch - no square image.")
    if image.size[0] > size:
        # Downsample
        image = image.resize((size, size), Image.ANTIALIAS)
    else:
        image = image.resize((size, size), Image.BICUBIC)
    log.debug("scaled to size: %i %i" % (image.size[0], image.size[1]))
    return image

def add_frame(image_in, border_size = 3, color_frame = COLOR_FRAME, color_border = COLOR_BORDER):
    pass

def add_text(image_in, title = None, desription = None, ):
    pass

if __name__ == '__main__':
    options = { 'rotate': None }
    source = None
    target = None
    align = None
    caption = None
    # process options
    option, args = get_option(sys.argv[1:])
    while option is not None:
        if option in ("clockwise", "anticlockwise"):
            options['rotate'] = option
        else:
            show_error("Unrecognised option --%s" % option)
        option, args = get_option(args)
    # process arguments
    source, args = get_argument(args)
    if source is None:
        print(__doc__)
        sys.exit()
    align, args = get_argument(args)
    if align is None:
        print(__doc__)
        sys.exit()
    caption, args = get_argument(args)
    if len(args) != 0:
        print(__doc__)
        sys.exit()

    log.debug("here we go...")
    name, ext = os.path.splitext(source)
    if not os.path.isfile(source):
        show_error("Source file '%s' does not exist." % source)
    target = name + ".polaroid.png"
    if not align in ("left", "right", "top", "bottom", "center"):
        show_error("Unknown alignment '%s'." % align)
    # Prepare our resources
    f_font = get_resource_file(RESOURCE_FONT)
    try:
        FONT_TITLE = ImageFont.truetype(f_font, RESOURCE_FONT_SIZE)
    except:
        show_error("Could not load resource '%s'." % fontName)

    img_in = Image.open(source)
    [w, h] = img_in.size
    img_in.load()
    img_in = rotate_image(img_in, options['rotate'])
    # Determine ratio of image length to width to
    # determine oriantation (portrait, landscape or square)
    image_ratio = float(float(h)/float(w))
    log.debug("image_ratio: %f size_w: %i size_h: %i" % (image_ratio, w, h))
    if round(image_ratio, 1) >= 1.3: # is_portrait
        print("source image ratio is %f (%s)" % (image_ratio, 'is_portrait'))
    elif round(image_ratio, 1) == 1.0: # is_square
        print("source image ratio is %f (%s)" % (image_ratio, 'is_square'))
    elif round(image_ratio, 1) <= 0.8: # is_landscape
        print("source image ratio is %f (%s)" % (image_ratio, 'is_landscape'))
    img_in = crop_image_to_square(img_in, align)
    img_in = scale_image(img_in, IMAGE_SIZE)
    img_in = add_frame(img_in)
    description = None
    img_in = add_text(img_in, caption, description)
