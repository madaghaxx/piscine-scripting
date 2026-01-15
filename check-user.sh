#!/bin/bash

flag="$1"
username="$2"

if [ "$flag" = "-e" ]; then
    if getent passwd "$username" > /dev/null 2>&1; then
        echo "yes"
    else
        echo "no"
    fi
elif [ "$flag" = "-i" ]; then
    getent passwd "$username"
fi