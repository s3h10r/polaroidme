#!/bin/bash -vx
DIR_IN='./input/'
FQFN_CONF=$(realpath ./polaroidme/polaroidme.conf)
#FONT=$(realpath ./polaroidme/fonts/MiasScribblings~.ttf)
FQFN_FONT=$(realpath ./polaroidme/fonts/contrast.ttf)

#./pom ./input/spritething-13x13-10-2000.jpg -o ./examples/spritething-13x13-10-2000.polaroid.png -f fonts/asciid.fontvir.us.ttf  --template ./polaroidme/templates/fzm-Polaroid.Frame-10.jpg --title "space invaders" && feh ./examples/spritething-13x13-10-2000.polaroid.png
./pom ${DIR_IN}spritething-13x13-10-2000.jpg -o spritething-13x13-10-2000.polaroid-01.png -f fonts/asciid.fontvir.us.ttf  --template ./polaroidme/templates/fzm-Polaroid.Frame-10.jpg --title "space invaders" && feh spritething-13x13-10-2000.polaroid-01.png
./pom ${DIR_IN}spritething-13x13-10-2000.jpg -o spritething-13x13-10-2000.polaroid-01.small.png -f fonts/asciid.fontvir.us.ttf  --template ./polaroidme/templates/fzm-Polaroid.Frame-10.jpg --title "space invaders" -m 800 && feh spritething-13x13-10-2000.polaroid-01.small.png

#./pom ${DIR_IN}spritething-13x13-10-2000.jpg -o spritething-13x13-10-2000.polaroid-02.png -f fonts/asciid.fontvir.us.ttf  --template ./polaroidme/templates/fzm-Polaroid.Frame-10.jpg --title "UTF-8 vir.us f(r)ont :)" && feh spritething-13x13-10-2000.polaroid-02.png
# weiste bescheid ;)
echo "...weiste bescheid ;) #hierso #generativeart #bananencode #100bugs101bug101bugs110bugs111bugs aber mir gefällt das so #rem!xkultur #minimalsim #contextswitch Heil #digitslisi. Heftig inspired by -> https://medium.freecodecamp.org/how-to-create-generative-art-in-less-than-100-lines-of-code-d37f379859f
 "
exit 1

./pom ./input/IMG_20190720_122246.jpg -o ./examples/smartphone-endofgreenshirt.png  --title "Shirt" --title-meta --m 600 --template polaroidme/templates/fzm-Polaroid.Frame-04.jpg

./pom ./input/IMG_20190720_135807-01.jpeg -o ./examples/smartphone-john.png --title "yu-huh" --title-meta -m 600 --template polaroidme/templates/fzm-Polaroid.Frame-04.jpg

pom ${DIR_IN}DSCF4700.jpg -o test-00.png --title "test-00. --title" --max-size 400 || exit 1
pom ${DIR_IN}octocat.png -o test-01.png --title "test-01B --edit 2ascii" --edit 2ascii || exit 1
pom ${DIR_IN}reny_DSCF3307.jpg -o test-01C.png --title "--edit 2ascii" --edit 2ascii --title-meta --template ./templates/trimmed-fzm-Polaroid.Frame-01.jpg --config ${FQFN_CONF}|| exit 1
pom ${DIR_IN}reny_DSCF3307.jpg -o test-01D.png --title "--edit pixelsort" -m 600 --edit pixelsort --title-meta --template ./templates/trimmed-fzm-Polaroid.Frame-01.jpg --config ${FQFN_CONF}|| exit 1
pom ${DIR_IN}DSCF4700.jpg -o test-04.png --title "0.9.3 issue#4. EXIF." --title-meta --max-size 400 -f ${FQFN_FONT} --template ./templates/trimmed-fzm-Polaroid.Frame-01.jpg --config ${FQFN_CONF} || exit 1
pom ${DIR_IN}DSCF4700.jpg -o test-03.png --template ./templates/trimmed-fzm-Polaroid.Frame-03.jpg --title "0.9.3 issue#3. high-res tpl support" --max-size 4000 || exit 1
pom ${DIR_IN}DSCF4700.jpg -o test-04A.png --template ./templates/trimmed-fzm-Polaroid.Frame-01.jpg --config ${FQFN_CONF} --title "0.9.3 issue#3 & --max-size" --max-size 400 || exit 1
pom ${DIR_IN}DSCF6061.jpg -o test-04B.png --template ./templates/trimmed-fzm-Polaroid.Frame-03.jpg --config ${FQFN_CONF} --title "0.9.3 issue#3 & --max-size" --max-size 400 || exit 1
pom ${DIR_IN}DSCF6105.jpg -o test-04C.png --nocrop --template ./templates/trimmed-fzm-Polaroid.Frame-02.jpg --config ${FQFN_CONF} --title "0.9.3 issue#3 & --max-size" --max-size 600 || exit 1
pom ${DIR_IN}DSCF6105.jpg -o test-04D.png --crop --align center --template ./templates/trimmed-fzm-Polaroid.Frame-02.jpg -c ${FQFN_CONF} --title-meta --max-size 400 || exit 1
pom ${DIR_IN}DSCF6105.jpg -o test-04D2.png --crop --align left --template ./templates/trimmed-fzm-Polaroid.Frame-02.jpg --config ${FQFN_CONF} --title "--crop" --max-size 400 || exit 1

feh test-00.png
file test-00.png
feh test-01.png
file test-01.png
feh test-01B.png
file test-01B.png
feh test-01C.png
file test-01C.png
feh test-01D.png
file test-01D.png
feh test-04.png
file test-04.png
feh test-03.png
file test-03.png
feh test-04A.png
file test-04A.png
feh test-04B.png
file test-04B.png
feh test-04C.png
file test-04C.png
feh test-04D.png
file test-04D.png
feh test-04D2.png
file test-04D2.png


rm -i ./test*png
