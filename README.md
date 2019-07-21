polaroidme - converts an image into vintage polaroid style
==========================================================

polaroidme is a command-line-tool for placing an image into a
Polaroid-like frame and optionally put a title / description or meta infos
out of EXIF-data on the bottom.
The default font mimics scribbled handwriting but any (ttf-)font
which suits your taste is supported. The tool offers basic features
like auto-scaling up-/downwards and/or cropping, using any (ttf-)font,
supports high-res output and gets it's job done well.

<img src="examples/spritething-13x13-10-2000.polaroid-01.small.png" width="90%" title="weiste bescheid... ;)"></img>

polaroidme was intitiated by the need for a script which creates some high-resolution contact sheets
of an archive of photographs and its output shouldn't make the beholder's eyes bleed.

Since Version 0.9.4 it polaroidme is also used for publishing minimalistic
generative art projects. This functionality is inspiring + phonky but in a very early state yet.

polaroidme is simple to use:

```console
foo@bar:~$ polaroidme ./example/example.png .jpg --title "thatseasyhu?" -o /tmp/mypolaroid.png
```

To get an appealing rugged analogue style you can [use high-resolution scans of
polaroid Frames - the ones i use at the moment can be downloaded here for free](http://www.fuzzimo.com/free-hi-res-blank-polaroid-frames/).

Example output:

<img src="/examples/test-04.png" width="48%"></img>
<img src="/examples/test-04B.png" width="48%"></img>

If you need more control over the output polaroidme offers you plenty of options.
The `--nocrop` Flag is an example of an option which is handy if your input images
are not in square-format and you don't want to get parts cropped (default).   

Though polaroidme is intended and commonly used as a command-line-tool it is also
a regular python-module (since version 0.9.2). Using it in other software is
therefore as simple as:

```
#!/usr/bin/env python3

from polaroidme import make_polaroid

[...]
```

polaroidme is actively maintained & developed (2019). To see if it fits
your needs take a look at the project's github-repo and check out the
[examples](https://github.com/s3h10r/polaroidme/blob/master/README.md)

Contributions are welcome, and they are greatly appreciated!

<img src="/examples/test_generator-psychedelic.filter-mosaic,oil2.png" width="48%" title="Psychedelisches Öl2"></img>
<img src="/examples/test_generator-psychedelic.filter-pixelsort,oil.png" width="48%" title="Psychedelisches sortiert"></img>

installation
------------

To install polaroidme, run this command in your terminal:

```console
    $ pip install polaroidme
```

This is the preferred method to install the software, as it will always install
the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide
you through the process.

usage
-----

example usage:

```console
foo@bar:~$ polaroidme ./example/example.png -o /tmp/mypolaroid.png
```

If the `-o, --output` argument is omitted the resulting filename will be the input-filename
extended by the string '.polaroid.' For example:

```console
foo@bar:~$ polaroidme ./example/example.png --size 400 --nocrop --title "--nocrop option"
```

will create the file `./example/example.polaroid.png`.

To display the creation date of the Photo (EXIF-data) as title the
option `-title-meta` can be used:

```console
foo@bar:~$ polaroidme ./example/example.png -o ./example/example.polaroid.png --size 400 --title-meta
```

To view the picture from the console you can use [feh](https://feh.finalrewind.org)
or any image viewer of your choice:

```console
foo@bar:~$ feh ./example/example.polaroid.png
```

Use `polaroidme --help` to get a description of all available options:

```console
foo@bar:~$ polaroidme --help

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
```

installation from sources
-------------------------

The sources for polaroidme can be downloaded from the [Github repo](https://github.com/s3h10r/polaroidme).

You can clone the public repository:

```console
    $ git clone https://github.com/s3h10r/polaroidme
```

Once you have a copy of the source, you can install it with:

```
    $ python setup.py install
```


<!--
Instead of installing the software system-wide it's usally best practice to install
it in a python-virtualenv:

```console
foo@bar:~$ python3 -m venv vent_polaroidme
foo@bar:~$ source venv_polaroidme/bin/activate
(venv_polaroidme) foo@bar:~$ pip install polaroidme
[...]
Installing collected packages: polaroidme
  Running setup.py install for polaroidme ... done
Successfully installed polaroidme-0.8.6
(venv_polaroidme) foo@bar:~$ polaroidme
(venv_polaroidme) foo@bar:~$ ...
(venv_polaroidme) foo@bar:~$ deactivate
foo@bar:~$
```
-->

Credits
-------

The ASCII-art filter relies on codesnippets from the following Open Source projects:

 - [asciify](https://github.com/RameshAditya/asciify)
 - [ImageToAscii](https://github.com/cleardusk/ImageToAscii/blob/master/img_to_ascii.py)
   Copyright (c) 2018 Jianzhu Guo, MIT License

The generator 'sprites' is made with [code by Eric Davidson](https://medium.freecodecamp.org/how-to-create-generative-art-in-less-than-100-lines-of-code-d37f379859f).

The generator 'psychedelic' is the wonderfull code of ["Random (Psychedelic) Art, and a Pinch of Python" by Jeremy Kun](http://jeremykun.com/2012/01/01/random-psychedelic-art/).

The generator 'circles' is heavily [inspired by Kevin Howbrook's Squares|https://medium.com/@kevinhowbrook/learning-python-and-being-creative-making-art-with-code-da02880e3738]

Some filters are taken from:

 - [https://github.com/Tinker-S/SomeImageFilterWithPython](https://github.com/Tinker-S/SomeImageFilterWithPython)

**Thank you guys for sharing your ideas for free and supporting the remix culture - and also for making IT fun again!** Live long and prosper! :)
All the crap in the code is by me of course. Please feel free to refacture, fix, tinker, ...

TODO
----
 - minimalistic & fun to use plugins (edit/filter/generate): asciiart, pixelsort, texture-blending, ... #generativeart
 - support more shapes than square (means: much more template usecases :))
 - custom colors (arg, means, ...)
 - finish contactsheet (feature)
 - template auto-preps
 - automated testing
 - option to put a description-text / link / Copyleft below title / watermark
 - rewrite corkboard (lab-branch) and add it to master
 - basic stats & picture analysis
 - include some templates(-configuration) for easypeasy usage

 changelog
 ---------

 **0.9.33** (work in progress)
 - restructuring the messy parts a bit ([packages](https://docs.python.org/3.6/tutorial/modules.html#packages)
 - adds minimalistic filter-funcs for fun (asciiart, pixelsorting, ...)
 - includes serious filters from https://github.com/Tinker-S/SomeImageFilterWithPython
 - enables filter-chaining possibility
 - support random-template choice (`--template <fqdir>/random`, `--template <fqdir>/rand`)
 - adds `--generator` option as an alternative to source-image and getting phonky instead :D
 - contactsheet supports filtering by time-window (PLANNED)
 - improved template support
 - bugfixes & new bugs :)

 **0.9.32**
 - option to use high-res scanned blank Polaroid frames as template
   (NEW args `--template` & `--config`). visual output quality
   gains expression by this. :)
 - inits tools for template-preparation (trim_, setup_)
 - option to use EXIF-data (DateTimeOriginal) as title or append it to the title
   (NEW arg `--title-meta`).
 - new args `--size-inner` & `--max-size``
 - several minor bugfixes   
 - contactsheet: sorting options based on EXIF-data

 **0.9.2**
 - converts into a "real" python-module which exports its core-functionality (`make_polaroid()`-function)
 - adds contactsheet-script (thumbnails can be polaroids with filename as caption)
 - convinient argparsing (via docopt)
 - testbuild-script
 - updates docs

 **0.9.1**
 - argument alignment omitted if `--nocrop option` is set
 - updates packaging meta-data & docs
 - adds more free fonts. changes default font to [Jakes Handwriting](https://www.dafont.com/jakeshandwriting.font)

 **0.9.0**
 - packaging (pypi)

 **0.8.4**
 - updates usage-string
 - adds correct file encoding (`pydoc3 ./polaroidme`)

 **0.8.2**
 - adds free example fonts (source: https://www.dafont.com/ttf.d592)
 - support for different fonts via argument

 **0.8.0**
 - supports for high-res output (argument size, default=800)
 - adds `--nocrop` option
 - refactoring

 **0.1.0**

 - initial commit based on https://github.com/thegaragelab/pythonutils/tree/master/polaroid
 - converts to python3


 older example output
 --------------------

 <img src="/examples/test-04D.png" width="48%"></img>
 <img src="/examples/example.corkboard.jpg" width="48%"></img>
 <!--
 <img src="/examples/example2.ps-10.polaroid.jpg" width="48%"></img>
 -->
 <!-- TODO: add contactsheet example -->

 <img src="/examples/DSCF2330.polaroid.nocrop.png" width="48%"></img>
 <img src="/examples/DSCF2313.polaroid.nocrop.png" width="48%"></img>
