#!/bin/bash 
#IMAGE="./tmp/tests/example.ps-10"
IMAGE="./tmp/tests/DSCF4700"
IMAGE_EXT=".jpg"
IMAGE_FQFN="${IMAGE}${IMAGE_EXT}"
IMAGE_FN="$(basename ${IMAGE_FQFN})"
#FONT=$(realpath ./polaroidme/fonts/MiasScribblings~.ttf)
FONT=$(realpath ./polaroidme/fonts/contrast.ttf)
VENV_INSTALL=$(realpath ./tmp/venv_polaroidme)

# --- build fresh package and install it in a venv for testing purpose 
./build.sh
rm -Rf $VENV_INSTALL #mrproper
rm -Rf ./tmp/
mkdir -p ./tmp/tests/
python3 -m venv $VENV_INSTALL || exit 1
source ${VENV_INSTALL}/bin/activate || exit 1
pip3 install ./dist/* || exit 1
find ./tmp/venv_polaroidme/ -name "*ttf"
cp ./examples/${IMAGE_FN} ./tmp/tests/
VERSION=$(polaroidme --version) || exit 1
echo $VERSION
echo "please activate venv to test. the command to do this is:"
SWITCH2VENV_TEST="source $VENV_INSTALL/bin/activate"
echo "$SWITCH2VENV_TEST" 

./test_generators.sh || exit 1
./test_filters.sh || exit 1

echo "please activate venv to test. the command to do this is:"
SWITCH2VENV_TEST="source $VENV_INSTALL/bin/activate"
echo "$SWITCH2VENV_TEST" 

exit 0

# --- some tests which needs interaction
pom $IMAGE_FQFN --size 400 --alignment center --title "testbuild ${VERSION} script" --font $FONT || exit 1
feh ./tmp/tests/${IMAGE_FN%.jpg}.polaroid.png # ${VAR%pattern} - removes file extension

#if [ $? -eq 0 ]
#then
#  feh ./tmp/tests/${IMAGE_FN%.jpg}.polaroid.png # ${VAR%pattern} - removes file extension
#  cp ./tmp/tests/${IMAGE_FN%.jpg}.polaroid.png /tmp/
#fi

./test_polaroidme.sh
#./test_generators.sh
#./test_filters.sh
rm -Rfi ./tmp/
