#!/bin/bash

nohup sh -c 'cat facts | grep "moon" && echo "The moon fact was found!" >> output.txt' &