#!/usr/bin/env bash

error() {
    printf '%s\n' "$1" >&2
    exit 1
}

[ "$#" -eq 1 ] || error "Error: expect 1 argument only!"

students=$1
names=()
grades=()

for ((i = 1; i <= students; i++)); do
    read -r -p "Student Name #$i: " name
    read -r -p "Student Grade #$i: " grade

    [[ $grade =~ ^[0-9]+$ ]] && [ "$grade" -le 100 ] \
        || error "Error: The grade '$grade' is not a valid input. Only numerical grades between 0 and 100 are accepted."

    names+=("$name")
    grades+=("$grade")
done

for ((i = 0; i < students; i++)); do
    name=${names[i]}
    grade=${grades[i]}

    if [ "$grade" -ge 90 ]; then
        echo "$name: You did an excellent job!"
    elif [ "$grade" -ge 70 ]; then
        echo "$name: You did a good job!"
    elif [ "$grade" -ge 50 ]; then
        echo "$name: You need a bit more effort!"
    else
        echo "$name: You had a poor performance!"
    fi
done
