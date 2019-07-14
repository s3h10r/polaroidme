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
COLOR_CAPTION = (58, 68, 163)
# Font for the caption text
FONT_CAPTION = None

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
        FONT_CAPTION = ImageFont.truetype(f_font, RESOURCE_FONT_SIZE)
    except:
        show_error("Could not load resource '%s'." % fontName)
