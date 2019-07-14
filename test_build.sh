#!/bin/bash
./build.sh
rm -Rf ./venv_polaroidme
rm -Rf ./tmp/
mkdir -p ./tmp/tests/
python3 -m venv ./tmp/venv_polaroidme
source ./tmp/venv_polaroidme/bin/activate
pip3 install ./dist/polaroidme-0.8.6-py3-none-any.whl
#pip3 install ./dist/polaroidme-0.8.6.tar.bz2
find ./tmp/venv_polaroidme/ -name "*ttf"
cp ./examples/example.ps-10.png ./tmp/tests/
polaroidme ./tmp/tests/example.ps-10.png 800 center "installed via pip"
feh ./tmp/tests/example.ps-10.polaroid.png
rm -Rf ./tmp/
#deactivate
