#!/bin/bash -vx
DIR_IN='./input/'
#FQFN_CONF='/home/s3h10r/development/pom/pom/pom.conf'
FQFN_CONF=$(realpath ./polaroidme/polaroidme.conf)
#FONT=$(realpath ./pom/fonts/MiasScribblings~.ttf)
FQFN_FONT=$(realpath ./polaroidme/fonts/contrast.ttf)


pom ${DIR_IN}DSCF4700.jpg -o test-00.png --title "test-00. --title" --max-size 400 || exit 1
pom ${DIR_IN}DSCF4700.jpg -o test-01.png --title "test-01 --filter-2ascii" --filter-2ascii || exit 1
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
feh test-04.png
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
