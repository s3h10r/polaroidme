#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime as dt
from collections import OrderedDict
import logging
from operator import itemgetter
import os
import json

import exifread
from PIL import Image

# --- configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
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

def sort_images_by_time(images, exclude_on_no_data = True, reverse= True, return_meta = False):
    return sort_images_by_original_ctime(images, exclude_on_no_data = exclude_on_no_data, reverse = reverse, return_meta = return_meta)

def sort_images_by_original_ctime(images, exclude_on_no_data = True, reverse = True, return_meta = True):
    """
    """
    DATA_UNAVAIL = []
    meta = { }

    for fn in images:
        exif_data = get_exif(fn)
        if ('EXIF DateTimeOriginal') in exif_data:
            log.debug("exif_data about DateTime: {}; {}; {}".format(fn, exif_data['Image DateTime'], exif_data['EXIF DateTimeOriginal']))
            v = exif_data['EXIF DateTimeOriginal']
            timestamp = dt.datetime.strptime(str(v), '%Y:%m:%d %H:%M:%S')
            meta[fn] = timestamp
        else:
            log.debug("exif_data about DateTime unavailable: {}; ;".format(fn))
            DATA_UNAVAIL.append(fn)
    log.info("exif_data about DateTime unavailable for {} images.".format(len(DATA_UNAVAIL)))
    # create sorted list
    for k,v in meta.items():
        if (k == None) or (v == None):
            log.critical("Oooouch. This should not happen... :-/ %s,%s" % (k,v))
    meta_sorted = OrderedDict(sorted(meta.items(), key = itemgetter(1), reverse = reverse))
    sorted_list = meta_sorted.keys()
    sorted_list = list(sorted_list)
    if not exclude_on_no_data:
        sorted_list.append(DATA_UNAVAIL)
        for fn in DATA_UNAVAIL:
            meta_sorted[fn] = None
        log.warning("exlude_on_no_data={} => added {} images without exif-data.".format(exclude_on_no_data, len(DATA_UNAVAIL)))
    else:
        log.warning("exlude_on_no_data={} => skipped {} images without exif-data.".format(exclude_on_no_data, len(DATA_UNAVAIL)))
    if return_meta:
        return sorted_list, meta_sorted, DATA_UNAVAIL
    return sorted_list


def filter_images_by_time(images, exclude_on_no_data = True):
    pass

def filter_images_by_size(images, min_size, max_size = None):
    """
    usefull to find only high-resolution photos and kicking out
    thumbnails and junk on the fly
    """
    pass


def paste_into_template(image = None, template = './templates/fzm-Polaroid.Frame-01.jpg', box=None):
    """
    """
    template_boxes = {
        # box = left, upper, right, lower
        'fzm-Polaroid.Frame-01.jpg' : [618.426369561389, 531.81956699281, 4257.608395919741, 4242.358103671913],
    }
    for k in template_boxes:
        template_boxes[k] = [round(f) for f in template_boxes[k]]
    print(json.dumps(template_boxes,indent=4,sort_keys=True))

    if not box:
        box = template_boxes[os.path.basename(template)]
    img_tpl = Image.open(template)

    w = box[2] - box[0]
    h = box[3] - box[1]
    log.debug("box-size the picture will be pasted into is (w,h) {} {}".format(w,h))
    region2copy = image.crop((0,0,image.size[0],image.size[1]))
    if region2copy.size[0] > w:
        # Downsample
        log.info("downsampling... (good)")
        region2copy = region2copy.resize((w,h),Image.ANTIALIAS) # FIXME verzerrung
    else:
        log.info("upscaling... (not so good ;)")
        region2copy = region2copy.resize((w,h), Image.BICUBIC) # FIXME verzerrung

    assert(region2copy.size == (w,h))
    print(region2copy.size, (w,h))
    print(region2copy.size, box)
    img_tpl.paste(region2copy,box)
    return img_tpl
