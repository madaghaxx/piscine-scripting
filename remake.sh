#!/bin/bash
# I used ai in this one so I don't repeat 
if [ $# -ne 1 ]; then
    echo "Error"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error"
    exit 1
fi

YEAR=$(date +%Y)

cd "$1" || exit 1

touch ciao
chmod 442 ciao
touch -t "${YEAR}01010001" ciao

mkdir -p mamma
chmod 777 mamma
touch -t "${YEAR}01020001" mamma

touch guarda
chmod 400 guarda
touch -t "${YEAR}01030001" guarda

touch come
chmod 642 come
touch -t "${YEAR}01040001" come

mkdir -p mi
chmod 452 mi
touch -t "${YEAR}01050001" mi

touch diverto
chmod 421 diverto
touch -t "${YEAR}01060001" diverto