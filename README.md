polaroidme
==========

I guess everyone and his/her grandmother already wrote a script to
convert an image into a "Polaroid-style". Nevertheless i couldn't
find one which fulfills my needs yet.

Current version is [based on this implementation](https://github.com/thegaragelab/pythonutils/tree/master/polaroid).

Example output:

<img src="/examples/example.ps-10.polaroid.jpg" width="48%"></img>
<img src="/examples/example2.ps-10.polaroid.jpg" width="48%"></img>
<img src="/examples/example.corkboard.jpg" width="48%"></img>
<img src="/examples/DSCF6061.polaroid.jpg" width="48%"></img>

usage:

```console
foo@bar:~$ #TODO
```

<!--
example:

```console
foo@bar:~$ ./polaroidme.py ... TODO && feh test.png
```
-->

<!--
literature
----------
- https://craiget.com/python/python-pil-pretty-polaroids
-->

TODO
----
 - support for high-res "Polaroid-styles" - not only thumbnail-stuff
   (example: huge prints with recursive polaroid framing ("polaroid in polaroid"))
 - cropping and scaling options
 - eye-candy like distortion filters
 - support for different fonts
 - optional text: title & description (auto-scaled to the dimensions of the image)


 changelog
 ---------

 **0.1.0**

 - initial commit based on https://github.com/thegaragelab/pythonutils/tree/master/polaroid
 - converts to python3
