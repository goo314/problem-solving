#!/usr/bin/env bash
readarray -t my_array </dev/stdin

echo "${my_array[@]: -3}"

# Test
# my_array=("element1" "element2" "element3" "element4" "element5")
# echo "${my_array[@]: -3}"
