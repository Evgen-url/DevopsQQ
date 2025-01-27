#!/bin/bash

echo "write name of file: "
read file
if [ -f $file ]; then 
	cat < $file
	else echo "File does not find"
fi 
