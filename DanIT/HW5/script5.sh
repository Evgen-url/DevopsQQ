#!/bin/bash

echo "Write a file would you want to remove : "
read name
if [ -f $name ]; then 
	echo "Youre file is here" 
	echo "Write path where u want move this file"
	read path
	if [ -d $path ]; then
	mv "$name" "$path"
	echo " File move to $path ";
	 else
	echo "Youre path not correct "
	fi 
	else echo "Youre file not found"
fi




