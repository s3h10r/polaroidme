#!/bin/bash -vx
GENS=('psychedelic' 'sprites')

FONT=$(realpath ./polaroidme/fonts/contrast.ttf)
CONFIG=$(realpath ./polaroidme/polaroidme.conf)
TPL=$(realpath ./polaroidme/templates/random)
MAX_SIZE=600
FOUT="/tmp/test_generators.png"
for gen in "${GENS[@]}"
do
  echo "testing generator $gen..."
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic" --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE|| exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic + --filter=pixelsort,oil" --filter pixelsort,oil --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic + --filter=mosaic" --filter mosaic --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic + --filter=mosaic,oil" --filter mosaic,oil2 --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic + --filter=mosaic,oil2" --filter mosaic,oil2 --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic + --filter=pixelsort" --filter pixelsort --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic + --filter=pixelsort,oil2" --filter pixelsort,oil2 --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic + --filter=pixelsort,ascii,mosaic" --filter pixelsort,ascii,mosaic --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic + --filter=ascii" --filter ascii --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "--generator=psychedelic + --filter=ascii,oil2" --filter ascii,oil2 --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT

done
