#!/bin/bash

echo "Starting the program at $(date)" # Date will be susbtituted
echo "Running program $0 with $# arguments with pid $$"

for file in "$@"; do
	grep foobar "$file" > /dev/null 2> /dev/null
	# When frep is not found, grep has exit status
	# We redirect STDOUT and STDERR to a null register about them
	if [["$?" -ne 0]]; then
		echo "File $file does not have any foobar, adding the "
		echo "# foobaar" >> "$file"
	fi
done
