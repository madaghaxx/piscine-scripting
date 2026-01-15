#!/bin/bash

echo $PWD
printenv | grep H | cut -d= -f1
