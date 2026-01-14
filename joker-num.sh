#!/bin/bash
count=5
while [[ $count -gt 0 ]]; do
    echo "Enter your guess ($count tries left)"
    read guess
    if [[ $guess -gt $1 ]]; then
        echo "Go down"
    elif [[ $guess -lt $1 ]]; then
        echo "Go up"
    else
        echo "Congratulations, you found the number in $((6-count)) moves!"
        break
    fi
    count=$(($count-1))
done