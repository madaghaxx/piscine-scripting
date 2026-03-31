#!/bin/bash

truncate -s 1000 file1.txt
chmod 600 file1.txt
touch -t 202201010000 file1.txt