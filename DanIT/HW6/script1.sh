#!/bin/bash
#
gennum=$(( 1 + RANDOM % 100 ))
echo "($gennum)"
echo "pls write the random number"
for i in $(seq 1 5);
do 
	read readnum
	if (( $readnum == $gennum ));
	then echo "gc! you win"
		exit 0
	elif [[ $readnum > $gennum ]];
	then echo "too hight"
	else echo "too low"
fi
done

echo "sorry tryes is over, the number $gennum"
