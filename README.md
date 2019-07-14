polaroidme
==========

I guess everyone and his/her grandmother already wrote a script to
convert an image into a "Polaroid-style". Nevertheless i couldn't
find one which fulfills my needs yet.

Example output:

<img src="/examples/example.ps-10.polaroid.jpg" width="48%"></img>
<img src="/examples/example2.ps-10.polaroid.jpg" width="48%"></img>
<img src="/examples/example.corkboard.jpg" width="48%"></img>
<img src="/examples/DSCF6061.polaroid.jpg" width="48%"></img>
<img src="/examples/DSCF2330.polaroid.nocrop.png" width="48%"></img>
<img src="./examples/DSCF2313.polaroid.nocrop.png" width="48%"></img>

```
polaroidme.py

Usage:

  polaroidme.py [options] source-image [size] [alignment] [title]

Where:

  source-image  name of the image file to transform. If no extension is
                specified .jpg is assumed.
  size          size of the picture part of the polaroid (default=800)
  alignment     one of 'top', 'left', 'bottom', 'right' or 'center'. This
                specifies the portion (crop) of the image to include in the final
                output. 'top' and 'left' are synonomous as are 'bottom' and
                'right'. (default="center")
  title         If specified defines the caption to be displayed at the
                bottom of the image. (default=None)

Available options are:

  --nocrop        Recale the image to fit fullframe in the final output
                  (default="--crop"). btw. alignment is ignored if option is set.
  --clockwise     Rotate the image clockwise before processing
  --anticlockwise Rotate the image anti-clockwise before processing
```

example:

```console
foo@bar:~$ ./polaroidme.py --crop ./example/example.png .jpg 800 center "--crop option center"
foo@bar:~$ feh ./example/example.polaroid.png
foo@bar:~$ ./polaroidme.py --nocrop ./example/example.png .jpg 800 center "--nocrop option"
foo@bar:~$ feh ./example/example.polaroid.png
```

<!--
literature
----------
- https://craiget.com/python/python-pil-pretty-polaroids
-->

TODO
----
 - optional text: title + description (auto-scaled to the dimensions of the image)
 - eye-candy like distortion filters
 - implement some tests
 - rewrite corkboard (https://github.com/thegaragelab/pythonutils/tree/master/polaroid)

 changelog
 ---------

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
