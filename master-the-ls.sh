#!/bin/bash

ls -t -p -1 | grep -v '^\.' | paste -sd ',' -