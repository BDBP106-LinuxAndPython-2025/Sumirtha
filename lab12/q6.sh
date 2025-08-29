#!/bin/bash

#maximum numbers

var=$1
var=$2
{
if [ $1 -gt $2 ]; then
	echo "Maximum number is:"$1
elif [ $2 -gt $1 ];then
	echo "Maximum number is:"$2
fi
}
