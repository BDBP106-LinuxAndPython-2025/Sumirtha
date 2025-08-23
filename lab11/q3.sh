#!/bin/bash
#checking if script is empty

echo 'Input String'
read $string

if [ -z "$string" ]; then
	echo 'The string '$string'is not empty'
else
	echo 'The string '$string'is empty'
fi
if [ -n "$string" ];then
	echo 'The string '$string'is empty'
else
	echo 'The string '$string'is not empty'
fi

