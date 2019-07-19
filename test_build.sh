#!/bin/bash -vx
#IMAGE="./tmp/tests/example.ps-10"
IMAGE="./tmp/tests/DSCF4700"
IMAGE_EXT=".jpg"
IMAGE_FQFN="${IMAGE}${IMAGE_EXT}"
IMAGE_FN="$(basename ${IMAGE_FQFN})"
#FONT=$(realpath ./polaroidme/fonts/MiasScribblings~.ttf)
FONT=$(realpath ./polaroidme/fonts/contrast.ttf)

./build.sh
rm -Rf ./venv_polaroidme
rm -Rf ./tmp/
mkdir -p ./tmp/tests/
python3 -m venv ./tmp/venv_polaroidme
source ./tmp/venv_polaroidme/bin/activate
#pip3 install ./dist/*
pip3 install ./dist/*
find ./tmp/venv_polaroidme/ -name "*ttf"
cp ./examples/${IMAGE_FN} ./tmp/tests/
VERSION=$(polaroidme --version)
echo $VERSION

pom $IMAGE_FQFN --size 400 --alignment center --title "testbuild ${VERSION} script" --font $FONT
feh ./tmp/tests/${IMAGE_FN%.jpg}.polaroid.png # ${VAR%pattern} - removes file extension
pom $IMAGE_FQFN --size 400 --alignment center --title "testbuild ${VERSION} script" || exit 1
if [ $? -eq 0 ]
then
  feh ./tmp/tests/${IMAGE_FN%.jpg}.polaroid.png # ${VAR%pattern} - removes file extension
  cp ./tmp/tests/${IMAGE_FN%.jpg}.polaroid.png /tmp/
fi

./test_polaroidme.sh

rm -Rfi ./tmp/
