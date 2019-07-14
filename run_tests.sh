#!/bin/bash
rm ./input/DSCF2330.polaroid.png
rm ./input/DSCF2313.polaroid.png
./polaroidme --nocrop ./input/DSCF2330.jpg 800 center "--nocrop option (landscape)"
./polaroidme --nocrop ./input/DSCF2313.jpg 800 center "--nocrop option (portrait)"
feh ./input/DSCF2330.polaroid.png
feh ./input/DSCF2313.polaroid.png
mv ./input/DSCF2330.polaroid.png ./examples/DSCF2330.polaroid.nocrop.png
mv ./input/DSCF2313.polaroid.png ./examples/DSCF2313.polaroid.nocrop.png
./polaroidme --crop ./input/DSCF2330.jpg 800 center "--crop option center (landscape)"
./polaroidme --crop ./input/DSCF2313.jpg 800 center "--crop option center (portrait)"
feh ./input/DSCF2330.polaroid.png
feh ./input/DSCF2313.polaroid.png
mv ./input/DSCF2330.polaroid.png ./examples/
mv ./input/DSCF2313.polaroid.png ./examples/

