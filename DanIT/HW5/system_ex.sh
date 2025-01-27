#!/bin/bash
#
MONITOR_DIR="/home/bob/watch"
test="$(ls -l)"

while true; do
    for file in "$MONITOR_DIR"/*; do
	    if [ -f "$file" ] && [[ "$(basename "$file")" != *.back ]]; then
	base=${file%.*}
	echo "$base"
	cat "$file"
            mv "$file" "$base.back"
            echo "Renamed: $file -> $base.back"
        fi
    done
    sleep 2 # Check every 2 seconds
done





