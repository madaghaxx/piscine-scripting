#!/bin/bash

pwd
printenv | grep H | cut -d= -f1
