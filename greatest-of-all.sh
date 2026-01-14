#!/bin/bash

max=-1
count=0

while [ $count -lt 10 ]; do
    read -p "Enter a number: " num
    
    if ! [[ "$num" =~ ^[0-9]+$ ]]; then
        echo "ERROR: Invalid input only positive numerical characters are allowed"
        exit 1
    fi
    
    if [ "$num" -gt 10000 ]; then
        echo "ERROR: The number entered is too large"
        exit 1
    fi
    
    if [ "$num" -gt "$max" ]; then
        max=$num
    fi
    
    count=$((count + 1))
done

echo "The largest number is: $max"