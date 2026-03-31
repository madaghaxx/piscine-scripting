#!/bin/bash

ls -laSo --block-size=1K "$@" | awk '{$1=""; sub(/^ /, ""); print}'