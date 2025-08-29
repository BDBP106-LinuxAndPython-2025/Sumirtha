#!/bin/bash

#multiplication table until 15 using until loop
echo "Input number"
read number
{
i=1
until [ $i -gt 15 ]; do
	result=$(($number*$i))
	echo "'$number'*'$i'=:"$result
	i=$((i+1))
done
}
