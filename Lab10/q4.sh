#!/bin/bash
#checking if a file exists
#
filename=$1
if [ -f "$filename" ];then
	echo 'The file '$filename' exists!'
	exit 200
else
	echo 'The file '$filename' does not exists.'
	exit 201
fi

#checking if file is executable
#
filename=$1
if [ -x "$filename" ];then
	echo 'The file '$filename' is executable'
else 
	echo 'The file '$filename' is not executable'
fi


#4_i_echo $? to check exit code generated.
#4_ii_output is obtained only when echo $? is after 'fi'. This variable contains the exit status and delivers  the existence status.
#4_iii_No, the output is not obtained as echo $? ensures the exit status
