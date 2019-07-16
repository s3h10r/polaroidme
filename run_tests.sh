#!/bin/bash
rm ./input/DSCF2330.polaroid.png
rm ./input/DSCF2313.polaroid.png
rm ./input/DSCF4700.polaroid.png

# the output of the following should be exactly the same (because we feed a perfect sqare in)
./polaroidme --crop ./input/DSCF4700.jpg 800 --alignment center --title "--crop option (square in)" -o ./input/DSCF4700.polaroid.jpg
./polaroidme --nocrop ./input/DSCF4700.jpg 800 --alignment center --title "--nocrop option (square in)" -o ./input/DSCF4700.polaroid.nocrop.jpg
feh ./input/DSCF4700.polaroid.png
feh ./input/DSCF4700.polaroid.nocrop.png

# --#

#./polaroidme --crop ./input/DSCF2330.jpg 800 center "--crop option center (landscape)"
#./polaroidme --crop ./input/DSCF2313.jpg 800 center "--crop option center (portrait)"
#./polaroidme --nocrop ./input/DSCF2330.jpg 800 center "--nocrop option (landscape in)"
#./polaroidme --nocrop ./input/DSCF2313.jpg 800 center "--nocrop option (portrait in)"

#feh ./input/DSCF2330.polaroid.png
#feh ./input/DSCF2313.polaroid.png

#mv ./input/DSCF2330.polaroid.png ./examples/DSCF2330.polaroid.nocrop.png
#mv ./input/DSCF2313.polaroid.png ./examples/DSCF2313.polaroid.nocrop.png
#mv ./input/DSCF4700.polaroid.png ./examples/DSCF4700.polaroid.png
#mv ./input/DSCF2330.polaroid.png ./examples/
#mv ./input/DSCF2313.polaroid.png ./examples/

#feh ./input/DSCF2330.polaroid.png
#feh ./input/DSCF2313.polaroid.png
