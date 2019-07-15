#!/bin/bash
./build.sh
rm -Rf ./venv_polaroidme
rm -Rf ./tmp/
mkdir -p ./tmp/tests/
python3 -m venv ./tmp/venv_polaroidme
source ./tmp/venv_polaroidme/bin/activate
#pip3 install ./dist/* 
pip3 install ./dist/*
find ./tmp/venv_polaroidme/ -name "*ttf"
cp ./examples/example.ps-10.png ./tmp/tests/
polaroidme ./tmp/tests/example.ps-10.png 800 center "testbuild script"
feh ./tmp/tests/example.ps-10.polaroid.png
rm -Rf ./tmp/
