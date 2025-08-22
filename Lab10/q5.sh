#!/bin/bash
#checking if the number is positive or negative or zero 
#
echo "Input a number: "
read n
if [ "$n" -ge 1 ]; then
	echo "The number '$n' is Positive"
elif [ "$n" -lt 0 ]; then
	echo "The number '$n' is Negative"
else 
	echo "The number '$n' is Zero"
fi
