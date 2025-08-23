#!/bin/bash
#string comparsion with case sensitivity

val1=Testing
val2=testing
if [ $val1\>$val2 ]; then
	echo "$val1 is greater than $val2"
else
	echo "$val1 is lesser than $val2"
fi

echo val1>teststringfile
echo val2>>teststringfile

sort teststringfile

