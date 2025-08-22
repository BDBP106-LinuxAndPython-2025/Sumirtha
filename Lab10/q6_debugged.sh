#!/bin/bash
echo "Input a number: "
read n
if [ "$n" -gt 100 ] ; then
echo "The number "$n" is greater than 100."
else
echo "The number "$n" is not greater than 100."
fi

#line4:The unwanted parenthesis were removed; ']' at the end was removed as well
#line5:Added "$n" in the echo statement
#line7:Added "$n" in the echo statement
#line 9,10,11 were removed

