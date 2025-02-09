#!/bin/bash
#
input=${1}
echo "$input"
if [ "$input" == start ]; then
       if [ -n "$(ps aux | grep ww.sh | grep -v grep | awk '{ print $2 }')" ]; then 
       echo "script already started"
	exit 0
else
       	
	cd /home/bob/DevopsQQ/DanIT/workplace/ 
	./ww.sh &
	echo "script started"
#	exit 0
       fi
	elif
	       [ "$input" == stop ]; then
	       	kill -9 $(ps aux | grep ww.sh | grep -v grep | awk '{ print $2 }')
 	echo "script stop"
elif
		[ "$input" == restart ]; then
		kill -9 $(ps aux | grep ww.sh | grep -v grep | awk '{ print $2 }')
		sleep 1
	cd /home/bob/DevopsQQ/DanIT/workplace/ 
		./ww.sh &
	echo "script restarted"
fi
