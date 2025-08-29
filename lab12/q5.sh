#!/bin/bash

divide() {
    
    num1=$1
    num2=$2

    # Check for division by zero
    if [ $num2 -eq 0 ]; then
        echo "Error: Division by zero is not allowed"
        return 1
    fi

    # Calculate quotient and remainder
     quotient=$(echo "scale=2; $num1 / $num2" | bc -l)
     remainder=$(echo "$num1 % $num2" | bc -l)
     
     echo "Quotient: $quotient"
     echo "Remainder: $remainder"
}

divide "$1" "$2"
