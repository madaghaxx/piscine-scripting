#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error: No file provided"
    exit 1
fi

file="$1"

if [ -e "$file" ]; then
    echo "File exists"
else
    echo "File does not exist"
    exit 0
fi

if [ -r "$file" ]; then
    echo "File is readable"
else
    echo "File is not readable"
fi

if [ -w "$file" ]; then
    echo "File is writable"
else
    echo "File is not writable"
fi

if [ -x "$file" ]; then
    echo "File is executable"
else
    echo "File is not executable"
fi