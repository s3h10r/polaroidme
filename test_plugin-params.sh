#!/bin/bash -vx
GENS=('psychedelic' 'squares+circles' 'sprites' 'cowsay')

FONT=$(realpath ./polaroidme/fonts/contrast.ttf)
CONFIG=$(realpath ./polaroidme/polaroidme.conf)
TPL=$(realpath ./polaroidme/templates/random)
MAX_SIZE=600
FOUT="/tmp/test_generators.jpg"

pom --version

pom --generator squares+circles --params-generator='{"shape" : 0}' -o /tmp/test.jpg --filter quads --params-filter='{"mode" : 1, "iterations" : 128}' --config ./polaroidme/polaroidme.conf --template /home/s3h10r/development/polaroidme/polaroidme/templates/random  --max-size 800 || exit 1
feh /tmp/test.jpg
pom --generator squares+circles --params-generator='{"shape" : 0}' -o /tmp/test.jpg --filter quads --params-filter='{"mode" : 2, "iterations" : 128}' --config ./polaroidme/polaroidme.conf --template /home/s3h10r/development/polaroidme/polaroidme/templates/random  --max-size 800 || exit 1
feh /tmp/test.jpg
pom --generator squares+circles --params-generator='{"shape" : 0}' -o /tmp/test.jpg --filter quads --params-filter='{"mode" : 3, "iterations" : 128}' --config ./polaroidme/polaroidme.conf --template /home/s3h10r/development/polaroidme/polaroidme/templates/random  --max-size 800 || exit 1
feh /tmp/test.jpg

pom ./input/DSCF6061.jpg -o /tmp/test.jpg --filter quads --params-filter='{"mode" : 3, "iterations" : 128}' --config ./polaroidme/polaroidme.conf --template /home/s3h10r/development/polaroidme/polaroidme/templates/random  --title-meta --max-size 800 || exit 1
feh /tmp/test.jpg
pom ./input/DSCF6061.jpg -o /tmp/test.jpg --filter quads --params-filter='{"mode" : 2, "iterations" : 512}' --config ./polaroidme/polaroidme.conf --template /home/s3h10r/development/polaroidme/polaroidme/templates/random  --title-meta --max-size 800 || exit 1
feh /tmp/test.jpg
pom ./input/DSCF6061.jpg -o /tmp/test.jpg --filter quads --params-filter='{"mode" : 1, "iterations" : 1024}' --config ./polaroidme/polaroidme.conf --template /home/s3h10r/development/polaroidme/polaroidme/templates/random  --title-meta --max-size 800 || exit 1
feh /tmp/test.jpg
