#!/bin/bash

#if directory exists
echo "Input directory_name"
read directory_name 

if [ -d "$directory_name" ] ;then
	echo "Directory exists '$directory_name' " 
	ls -l "$directory_name"
else
	echo "Making new directory"
	mkdir -p "$directory_name"
fi

