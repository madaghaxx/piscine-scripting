#!/bin/bash

if [ -f "$1" ] && [ -x "$1" ]; then
    echo "File is executable"
else
    echo "File is not an executable or does not exist"
fi
