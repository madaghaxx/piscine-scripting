#!/bin/bash

flag="$1"
username="$2"

case "$flag" in
    -e)
        if getent passwd "$username" > /dev/null 2>&1; then
            echo "yes"
        else
            echo "no"
        fi
        ;;
    -i)
        getent passwd "$username"
        ;;
esac