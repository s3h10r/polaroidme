#!/bin/bash

./contactsheet ./examples/ out.png && feh out.png
./contactsheet ./examples/ out.png --ratio free --polaroid --font=/home/s3h10r/development/polaroidme/polaroidme/fonts/contrast.ttf && feh out.png
./contactsheet ./examples/ out.png --ratio square --polaroid --size=400 && feh out.png
