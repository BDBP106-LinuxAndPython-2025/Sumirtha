#!/bin/bash
#checking if a file exists
#
filename=$1
if [ -f "$filename" ];then
	echo 'The file '$filename' exists!'
else
	echo 'The file '$filename' does not exists.'
fi

#checking if file is executable
#
filename=$1
if [ -x "$filename" ];then
	echo 'The file '$filename' is executable'
else 
	echo 'The file '$filename' is not executable'
fi

