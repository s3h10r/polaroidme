#!/bin/bash -vx
GENS=('psychedelic' 'sprites')

FONT=$(realpath ./polaroidme/fonts/contrast.ttf)
CONFIG=$(realpath ./polaroidme/polaroidme.conf)
TPL=$(realpath ./polaroidme/templates/random)
FOUT="/tmp/test_generators.png"

for gen in "${GENS[@]}"
do
  echo "testing generator $gen..."
  ./pom --generator $gen -o $FOUT --title "generator=psychedelic" --template $TPL -c $CONFIG -f $FONT|| exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "generator=psychedelic + --filter pixelsort" --filter pixelsort --template $TPL -c $CONFIG -f $FONT|| exit 1
  feh $FOUT
  ./pom --generator $gen -o $FOUT --title "generator=psychedelic + --filter ascii" --filter ascii --template $TPL -c $CONFIG -f $FONT|| exit 1
  feh $FOUT
done
