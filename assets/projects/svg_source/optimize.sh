#!/bin/bash
# change to script dir
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to that directory
cd "$SCRIPT_DIR" || exit

for f in $(find . -maxdepth 1 -type f | grep ".*.svg"); do
  scour -i $f -o ../svg/$f --enable-viewboxing --enable-id-stripping --enable-comment-stripping --shorten-ids --indent=none --remove-display-none
done
