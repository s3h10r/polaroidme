#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import json
from PIL import Image
import exifread

# --- configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)
handler = logging.StreamHandler() # console-handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
# ---

def get_exif(source):
    """
    """
    if isinstance(source, Image.Image):
        if hasattr(source, filename):
            source = source.filename
        else:
            raise Exception("Sorry, source is an Image-instance and i could not determine the filename. Please geve me a FQFN instead.")
    elif not isinstance(source, str):
        raise Exception("Ouch. Sorry, source must be a valid filename.")
    with open(source, 'rb') as f:
        exif_data = exifread.process_file(f, details=True)
    for tag in exif_data:
        log.debug("exif_data has key: %s" % (tag))
        if tag in ('Image DateTime', 'EXIF DateTimeOriginal'):
            log.debug("EXIF data of %s for key %s is %s" % (source, tag, exif_data[tag]))
    return exif_data

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

def sort_images_by_name(images):
    pass

def sort_images_by_time(images, exclude_on_no_data = True):
    pass

def filter_images_by_time(images, exclude_on_no_data = True):
    pass

def filter_images_by_size(images, min_size, max_size = None):
    """
    usefull to find only high-resolution photos and kicking out
    thumbnails and junk on the fly
    """
    pass
