#!/bin/bash

echo "write filename for check :"
read File
if [ -e $File ]; 
	then echo "$File in this dir"
	else echo "Sorry file does not find"
fi
