#!/usr/bin/env python3
"""
contactsheet - create a contact sheet for all images in the specified directory

usage:

  contactsheet [image_directory] [aspect_ratio_cs] [size_of_thumbnails]

where

  image_directory    the directory in which the images reside

  aspect_ratio_cs    the aspect ratio of the contact sheet. one of
                     'square' (1:1), 'classic' (2:3) or 'digital' (3:4).
                     the value 'free' means "auto-optimize". (default="digital")

  size_of_thumbnail  width of thumbnail in pixels (default=200)

Latest version

  The `latest version is available on github <https://github.com/s3h10r/polaroidme>`_

Current Version
"""
"""
TODO
====
[ ] option: filename as caption on bottom/top/left/right of thumbnail
[ ] color
0.2.0
[X] "self-optimizing" grid layout (no empty slots) -> aspect_ratio_cs='free'
"""
import os
import sys
import logging
from PIL import Image, ImageDraw, ImageFont

# --- configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler() # console-handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
# ---

THUMBNAIL_SIZE=200 #defaukt

__version__ = (0,1,2)
__license__ = "MIT"


def make_contact_sheet(fnames = None, ncols = 4,nrows = 4, photow = 360,photoh = 400,
                       marl = 0, mart = 0, marr = 0, marb = 0,
                       padding = 0):
    """
    Make a contact sheet from a list of filenames:

    fnames       A list of names of the image files

    ncols        Number of columns in the contact sheet
    nrows        Number of rows in the contact sheet
    photow       The width of the photo thumbs in pixels
    photoh       The height of the photo thumbs in pixels

    marl         The left margin in pixels
    mart         The top margin in pixels
    marr         The right margin in pixels
    marb         The bottom margin in pixels

    padding      The padding between images in pixels

    returns a PIL image object.
    """

    # Calculate the size of the output image, based on the
    #  photo thumb sizes, margins, and padding
    marw = marl+marr
    marh = mart+ marb
    padw = (ncols-1)*padding
    padh = (nrows-1)*padding
    isize = (ncols*photow+marw+padw,nrows*photoh+marh+padh)

    # Create the new image. The background doesn't have to be white
    white = (255,255,255)
    inew = Image.new('RGB',isize,white)

    count = 0
    # Insert each thumb:
    for irow in range(nrows):
        for icol in range(ncols):
            left = marl + icol*(photow+padding)
            right = left + photow
            upper = mart + irow*(photoh+padding)
            lower = upper + photoh
            bbox = (left,upper,right,lower)
            try:
                # Read in an image and resize appropriately
                #img = Image.open(fnames[count]).resize((photow,photoh))

                # --- scales the image proportionally to fit the thumbnail box...
                img = Image.open(fnames[count])
                img_bbox = img.getbbox()
                width = img_bbox[2] - img_bbox[0]
                height = img_bbox[3] - img_bbox[1]
                # calculate a scaling factor depending on fitting the larger dimension into the thumbnail
                ratio = max(height/float(photoh), width/float(photow))
                newWidth = int(width/ratio)
                newHeight = int(height/ratio)
                newSize = (newWidth, newHeight)
                img = img.resize(newSize)
            except:
                break

            new_left = left
            new_upper = upper
            if ( newWidth < photow):
                new_left = int(left + ((photow - newWidth)/2))
            if ( newHeight < photoh):
                new_upper = int(upper + ((photoh - newHeight)/2))
            inew.paste(img, (new_left, new_upper))
            count += 1

    return inew

def get_images_in_dir(directory=None, suffix=('jpg','jpeg','png','gif', 'bmp', 'tif','tiff'),traversal=True):
    res = []
    if traversal:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(suffix):
                    fqfn = os.path.join(root, file)
                    res.append(fqfn)
                    log.debug("file match: {}".format(fqfn))
    else:
        for file in os.listdir(directory):
            if file.endswith(suffix):
                fqfn = os.path.join(directory, file)
                res.append(fqfn)
    return res

def euclid (a,b): #ggt
    if (b == 0) :
        return a
    else :
        return Euclid (b, (a % b))

def get_factors(x):
    """
    find the factors of a number x

    returns list of factors of x
    """
    res = [] # teh factors of x are ...
    for i in range(1, x + 1):
        if x % i == 0:
            res.append(i)
    return res

def get_optimized_grid(n_elements):
    """
    returns a grid-size where no slot is free
    (excluded are 0 and primes -> (1,n_elements))
    """
    facts = get_factors(n_elements)
    log.debug("the factors of {} are {}".format(n_elements, facts))
    if n_elements in (0,1):
        return None
    if len(facts) == 2:
        log.info("oh! seems we've got a prime ({})? very cool but not usable for the purpose of an optimal grid.".format(n_elements)) # not usable
        return None
    else:
        facts = facts[1:-1] # kick 1 and number itself
        middle_idx = (len(facts) - 1)//2
        fact = facts[middle_idx]
        res = (fact, int(n_elements / fact))
        assert(res[0]*res[1] == n_elements)
        return res


if __name__ == '__main__':
    # define possible aspect ratios of contact sheet
    aspect_ratio = {
        'square'  : (1,1),
        'classic' : (2,3), # kleinbidkamera
        'digital' : (3,4), # apsc
        'free'    : None   # auto-optimized
    }
    ar_name = 'square' # default
    dir = None
    if len(sys.argv) < 2:
        print(__doc__)
        print("  v" + '.'.join([str(el) for el in __version__]))
        sys.exit(0)
    elif len(sys.argv) >= 3:
        ar_name = sys.argv[2]
        dir = sys.argv[1]
    elif len(sys.argv) >= 2:
        dir = sys.argv[1]

    fqfn_images = get_images_in_dir(dir, traversal=True)
    nr_images = len(fqfn_images)
    ncols = None
    nrows = None

    # ---
    # calculate grid-dimensions based on the wanted aspect ratio
    # of the contact sheet (h:w)
    if ar_name not in aspect_ratio:
        ar_name = 'digital' # default
    if ar_name == 'free':
        aspect_ratio['free'] = aspect_ratio['square']
    ar_cs = aspect_ratio[ar_name]
    log.info("aspect ratio of Contact Sheet set to {}:{} # ar_w {} / ar_h {} = {}".format(ar_cs[0], ar_cs[1], ar_cs[1], ar_cs[0], ar_cs[1] / ar_cs[0]))
    for i in range(1,nr_images):
        if nr_images <= ( (i * ar_cs[0]) * (i * ar_cs[1]) ):
            ncols = i * ar_cs[1]
            nrows = i * ar_cs[0]
            break
    # ---
    log.info("{} images found. Contact Sheet grid is set to (ncolsXnrows): {}x{} (aspect ratio of sheet is set to {}:{})".format(nr_images, ncols,nrows,nrows,ncols) )

    if (ar_cs[1] / ar_cs[0]) != (ncols / nrows): #plausi check
        raise Exception("Ouch. aspect ratio of contact sheet is not okay. :-/")

    # --- calculate space usage
    free_slots = ncols * nrows - nr_images
    if free_slots > ncols:
        log.warning("there's free space for {} items. Suggestion: add {} images, try aspect ratio 'free' or just don't care ;)".format(free_slots, free_slots))
    log.warning("{} empty rows. {} empty slot in last row which contains an image.".format(free_slots // ncols, free_slots % ncols))
    # --- optimize - try to find a grid where no slots are free (example 8 => (2, 4))
    if free_slots > 0 and ar_name == 'free':
        res = get_optimized_grid(nr_images) # experimental ;)
        if res:
            ar_cs = res
            aspect_ratio[ar_name] = ar_cs
            ncols = ar_cs[1]
            nrows = ar_cs[0]
            log.info("Contact Sheet ratio 'free' => grid optimized to (ncolsXnrows): {}x{} (aspect ratio of sheet is set to {}:{})".format(ncols,nrows,nrows,ncols) )
        else:
            log.info("Contact Sheet ratio 'free' => no optimzed alternative found.".format() )
    # ---

    # set size of thumbnails
    photow = THUMBNAIL_SIZE; photoh = photow
    if len(sys.argv) >= 4:
        photow = int(sys.argv[3])
        photoh = photow
    log.info("photow {} / photoh {} = {} || ar_w {} / ar_h {} = {}".format(photow, photoh, photow / photoh, ar_cs[1], ar_cs[0], ar_cs[1] / ar_cs[0]))
    padding = int(photow / 8)
    mar = int(padding / 2)
    marl = mar; mart = mar; marr = mar; marb = mar
    # --- precalc image size
    marw = marl+marr
    marh = mart+ marb
    padw = (ncols-1)*padding
    padh = (nrows-1)*padding
    isize = (ncols*photow+marw+padw,nrows*photoh+marh+padh)
    # ---
    log.info("Contact Sheet size: {}".format(isize))
#    img = make_contact_sheet(fqfn_images, ncols = 1, nrows = 7,
    img = make_contact_sheet(fqfn_images, ncols = ncols, nrows = nrows,
        photow = photow, photoh = photoh, padding=padding,
        marl=mar, mart=mar, marr=mar, marb = mar)

    img.save("contactsheet.png")
