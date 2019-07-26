#!/bin/bash -vx
GENS=('cowsay' 'psychedelic' 'squares+circles' 'sprites')

FONT=$(realpath ./polaroidme/fonts/contrast.ttf)
CONFIG=$(realpath ./polaroidme/polaroidme.conf)
TPL=$(realpath ./polaroidme/templates/random)
MAX_SIZE=600
FOUT="/tmp/test_generators.jpg"

pom --version 

for gen in "${GENS[@]}"
do
  echo "testing generator $gen..."
  pom --generator $gen -o $FOUT --title "--generator=${gen}" --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE|| exit 1
  feh $FOUT
done 

exit 0 

for gen in "${GENS[@]}"
do
  echo "testing generator $gen..."
  pom --generator $gen -o $FOUT --title "--generator=${gen}" --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE|| exit 1
  feh $FOUT
  pom --generator $gen -o $FOUT --title "--generator=${gen} + --filter=pixelsort,oil" --filter pixelsort,oil --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  pom --generator $gen -o $FOUT --title "--generator=${gen} + --filter=mosaic" --filter mosaic --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  pom --generator $gen -o $FOUT --title "--generator=${gen} + --filter=mosaic,oil" --filter mosaic,oil2 --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  pom --generator $gen -o $FOUT --title "--generator=${gen} + --filter=mosaic,oil2" --filter mosaic,oil2 --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  pom --generator $gen -o $FOUT --title "--generator=${gen} + --filter=pixelsort" --filter pixelsort --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  pom --generator $gen -o $FOUT --title "--generator=${gen} + --filter=pixelsort,oil2" --filter pixelsort,oil2 --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  pom --generator $gen -o $FOUT --title "--generator=${gen} + --filter=pixelsort,ascii,mosaic" --filter pixelsort,ascii,mosaic --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  pom --generator $gen -o $FOUT --title "--generator=${gen} + --filter=ascii" --filter ascii --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT
  pom --generator $gen -o $FOUT --title "--generator=${gen} + --filter=ascii,oil2" --filter ascii,oil2 --template $TPL -c $CONFIG -f $FONT -m $MAX_SIZE || exit 1
  feh $FOUT

done
