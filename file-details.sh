#!/bin/bash

ls -l --time-style="+%F %R" hard-perm | awk 'NR>1 {print $1, $6, $7, $8}'