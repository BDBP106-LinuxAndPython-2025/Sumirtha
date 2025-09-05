#!/bin/bash

if [ $# -eq 4 ]; then
	echo "The given arguments are: $@"
	exit 777
else
	echo "Input four arguments"
	exit 888
fi

