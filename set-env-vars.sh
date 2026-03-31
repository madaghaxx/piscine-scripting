#!/bin/bash

MY_MESSAGE="Hello World"
MY_NUM=100
MY_PI=3.142

export MY_MESSAGE
export MY_NUM
export MY_PI

printenv | grep "MY_NUM"
printenv | grep "MY_PI"
printenv | grep "MY_MESSAGE"