#!/bin/bash -vx
FILTERS=('2ascii' 'pixelsort' 'diffuse' 'emboss' 'find_edge' 'glowing_edge' 'ice' 'molten' 'mosaic')
FONT=$(realpath ./polaroidme/fonts/contrast.ttf)
FIN="./input/octocat.png"
FOUT="/tmp/test_filter.png"

for filter in "${FILTERS[@]}"
do
  echo "testing filter $filter..."
#./pom $FIN -o $FOUT --template /home/s3h10r/development/polaroidme/polaroidme/templates/random --config polaroidme/polaroidme.conf --crop --alignment center --title "--filter $filter" --filter $filter --font $FONT -m 600 || exit 1
./pom $FIN -o $FOUT --template /home/s3h10r/development/polaroidme/polaroidme/templates/random --config polaroidme/polaroidme.conf --nocrop --title "--filter $filter" --filter $filter --font $FONT -m 600 || exit 1
feh $FOUT
done 



