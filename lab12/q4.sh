#!/bin/bash

#creating num.text
echo "1 2 3 4" > nums.txt
#read numbers as array
read -ra numbers < nums.txt
#print array
echo "Original numbers in array:"
for num in "${numbers[@]}"; 
do 
	echo "$num"
done

#doubling
echo "Doubled numbers:"
for num in "${numbers[@]}";
do
	doubled=$(($num*2))
	echo "$num doubled is: $doubled"
done
