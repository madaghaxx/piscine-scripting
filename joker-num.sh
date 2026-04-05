#!/bin/bash

if [[ $# -ne 1 || ! "$1" =~ ^[0-9]+$ || "$1" -lt 1 || "$1" -gt 100 ]]; then
    echo "Error: wrong argument"
    exit 1
fi

secret="$1"

for ((move=1; move<=5; )); do
    tries_left=$((6 - move))
    echo "Enter your guess ($tries_left tries left):"
    read -r guess

    if [[ ! "$guess" =~ ^[0-9]+$ || "$guess" -lt 1 || "$guess" -gt 100 ]]; then
        continue
    fi

    if (( guess > secret )); then
        echo "Go down"
        ((move++))
    elif (( guess < secret )); then
        echo "Go up"
        ((move++))
    else
        echo "Congratulations, you found the number in $move moves!"
        exit 0
    fi
done

echo "You lost, the number was $secret"