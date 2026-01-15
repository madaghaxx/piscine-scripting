#!/bin/bash

do_add() {
    echo $(($1 + $2))
}

do_sub() {
    echo $(($1 - $2))
}

do_mult() {
    echo $(($1 * $2))
}

do_divide() {
    echo $(($1 / $2))
}

if [ $# -ne 3 ]; then
    exit 1
fi

num1=$1
operator=$2
num2=$3

case "$operator" in
    "+")
        do_add $num1 $num2
        ;;
    "-")
        do_sub $num1 $num2
        ;;
    "*")
        do_mult $num1 $num2
        ;;
    "/")
        do_divide $num1 $num2
        ;;
    *)
        exit 1
        ;;
esac