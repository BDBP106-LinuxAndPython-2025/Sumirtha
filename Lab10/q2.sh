#!/bin/bash

#Script to check whether the user is an adult or not
echo "Input user age:"
read n

if [ "$n" -ge 18 ];then
	echo "You are an adult"
else 
	echo "You are a minor"
fi
