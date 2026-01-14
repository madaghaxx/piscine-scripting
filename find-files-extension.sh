#!/bin/bash
find . -type f -name "*.txt" -printf "%f\n" | cut -d "." -f 1
#                                   /\
#                                 / | \
#                               /  |   \
#                             /   |     \
#                     this part here gets the file name