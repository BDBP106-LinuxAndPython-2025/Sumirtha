#!/bin/bash
#-e checks if  the file exists
#-s checks if the file has a size greater than zero
#-f checks if the file is a regular file.

#checking for -e
echo "Input filename"
read filename 

if [ -e "$filename" ];then
	echo 'The file '$filename' exists'
else 
	echo 'The file '$filename' does not exists'
fi

#checking for -f
echo "Input filename"
read filename

if [ -f "$filename" ];then
	echo 'The file '$filename' is a regular file'
else 
	echo 'The file '$filename' is not a regular file'
fi

#checking for -s
echo "Input filename"
read filename

if [ -s "$filename" ];then
	echo 'The size of the file '$filename' is greater than zero'
else 
	echo 'The size of the file '$filename' is not greater than zero'
fi

