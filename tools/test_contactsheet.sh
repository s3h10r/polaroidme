#!/bin/bash -vx
#./contactsheet ../../anypla.net-2019/content/media/photos/2019/ cc.png --ratio free --sort-by exif_time --polaroid || exit 1 
#./contactsheet ../../anypla.net-2019/content/media/photos cc.png --size-thumb 100 --ratio free --sort-by exif_time --polaroid || exit 1 
#feh cc.png

./contactsheet ../../anypla.net-2019/content/media/photos/2016/ anyplanet-cs-2016.png --size-thumb 200 --ratio free --polaroid --sort-by exif_date --reverse || exit 1
feh anyplanet-cs-2016.png
