#!/bin/bash

printenv | grep H | cut -d= -f1
