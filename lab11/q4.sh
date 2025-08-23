#!/bin/bash
#string comparsion

val1=Jayashree
val2=Nagesh
if [ $val1\>$val2 ]; then
	echo "$val1 is greater than $val2"
else
	echo "$val1 is lesser than $val2"
fi

#Script has compared the given string, as we have used \>. Using only '>' will only create a new file.No extra file created but only the strings being compared.
