#!/bin/bash

fruits[0]=apple
fruits[1]=cherry
fruits[2]=orange
fruits[3]=pomegranate

echo ${fruits[0]}

echo ${fruits[*]}

for i in ${fruits[*]}

	do
	echo $i
	done
