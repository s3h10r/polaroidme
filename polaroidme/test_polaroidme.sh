#!/bin/bash -vx
./polaroidme ../examples/DSCF4700.jpg -o test.png --title "usual stuff" || exit 1
feh test.png
file test.png

./polaroidme ../examples/DSCF4700.jpg -o test.png --template ./templates/trimmed-fzm-Polaroid.Frame-04.jpg  --config ./polaroidme.conf --title "0.9.3 provides --template support & --max-size etc." --max-size 400 || exit 1
feh test.png
file test.png

./polaroidme ../examples/DSCF4700.jpg -o test.png --template ./templates/trimmed-fzm-Polaroid.Frame-01.jpg --config ./polaroidme.conf --title "0.9.3 provides --template support" --max-size 800 || exit 1
feh test.png
file test.png
