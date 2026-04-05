#!/usr/bin/env bash

error() {
    >&2 echo "$1"
    exit "$2"
}

[ "$#" -eq 3 ] || error "Error: expect 3 arguments" 1

num1=$1
operator=$2
num2=$3

[[ $num1 =~ ^-?[0-9]+$ && $num2 =~ ^-?[0-9]+$ ]] || error "Error: invalid number" 4

case "$operator" in
    "+") echo $((num1 + num2)) ;;
    "-") echo $((num1 - num2)) ;;
    "*") echo $((num1 * num2)) ;;
    "/")
        [ "$num2" -ne 0 ] || error "Error: division by 0" 2
        echo $((num1 / num2))
        ;;
    *)
        error "Error: invalid operator" 3
        ;;
esac
