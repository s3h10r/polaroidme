#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
polaroidme - converts an image into vintage polaroid style

Usage:
  polaroidme <source-image> [--output=<filename>]
  polaroidme <source-image> [-o=<filename>] [--title=<str>] [--title-meta] [--font=<f>] [--filter=<str>]
  polaroidme <source-image> [-o=<fn>] [--template=<str>] [--config=<str>] [--crop] [--alignment=<str>] [--filter=<str>] [--title=<str>]
  polaroidme <source-image> [-o=<fn>] [--nocrop|--crop] [--alignment=<str>] [--size-inner=<n>] [--max-size=<w>] [--template=<str>] [--config=<str>] [--title=<str>][--title-meta] [--filter=<str>]
  polaroidme <source-image> [-o=<fn>] [--template=<str>] [--config=<str>] [--title=<str>][--title-meta] [--font=<f>] [--size-inner=<n>] [--max-size=<w>] [--filter=<str>]
  polaroidme <source-image> [-o=<fn>] [--size-inner=<n>] [--alignment=<str>] [--title=<str>][--title-meta] [-f=<f>] [--template=<str>] [-c=<str>] [-m=<w>] [--filter=<str>]
  polaroidme <source-image> [--nocrop|--crop] [--alignment=<str>] [--title=<str>] [--title-meta] [-f=<str>] [-s=<n>] [-o=<filename>] [--template=<str>] [--config=<str>] [--max-size=<w>] [--filter=<str>]
  polaroidme <source-image> [--clockwise|--anticlock] [--nocrop|--crop] [--title=<str>] [--title-meta] [-f=<f>] [-s=<n>] [-o=<fn>] [--alignment=<str>] [--template=<str>] [-config=<str>] [-m=<w>] [--title-meta] [--filter=<str>]
  polaroidme [--generator=<str>] [-o=<fn>] [--template=<str>] [-config=<str>] [--filter=<str>] [--clockwise|--anticlock] [--title=<str>] [--title-meta] [-f=<f>] [-s=<n>] [-m=<w>]

Where:
  source-image    Name of the image file to convert.
Options:
  --alignment=<str> Used for cropping - specifies the portion of the image
                    to include in the final output.
                    One of 'top', 'left', 'bottom', 'right' or 'center'.
                    'top' and 'left' are synonomous as are 'bottom' and
                    'right'. (default="center").
                    Not of any use if --nocrop option is set.
  --anticlockwise   Rotate the image anti-clockwise before processing
  -c,--config=<py>  a config is only necessary if --template is used (see docs)
  --clockwise       Rotate the image clockwise before processing
  --crop            the images will be cropped to fit. see --alignment
  -f, --font=<f>    Specify (ttf-)font to use (full path!)
  --filter=<str>    One or more (seperated by comma) of
                    'ascii', 'ascii-color', 'pixelsort', 'diffuse', 'emboss',
                    'find_edge', 'glowing_edge', 'ice', 'molten', 'mosaic', ...
                    If more than one filter is used (filterchain) they will be applied in
                    the sequence given.
  --generator=<str> Get phonky & create some generative art instead of using an input-image.
  -s,--size-inner=<n> Size of the picture-part of the polaroid in pixels (default=800)
  -t,--title=<str>  Defines an optional caption to be displayed at the
                    bottom of the image. (default=None)
  --title-meta      Adds EXIF-data (date of capturing) to the title. If Input is
                    a generator this adds infos about the generator's params.
  -m,--max-size=<w> Sets maximum size (width) of the created polaroid.
                    (size-inner + frame <= max-size)
  --nocrop          Rescale the image to fit fullframe in the final output
                    (default="--crop"). btw. alignment is ignored if option is set.
  -o, --output=<s>  Defines the name of the outputfile. If omitted a filename
                    based on the original will be used - example:
                    'test.polaroid.png' will be used as filename if input-file is 'test.png'
  --template=<t>    Specify a template to use. A template can be a high-res
                    scan of a real Polaroid or something of its shape.
                    By using a template the visual output quality gains on
                    expression & authenticity.

  -h, --help        Print this.
      --version     Print version.

The `latest version is available on github: https://github.com/s3h10r/polaroidme>
"""
from docopt import docopt
from polaroidme.core import __version__, main, make_polaroid

if __name__ == '__main__':
    # --- process args & options
    args = docopt(__doc__, version=__version__)
    main(args)
