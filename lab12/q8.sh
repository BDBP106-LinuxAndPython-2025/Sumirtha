#!/bin/bash

#ls
#ls > listoffiles
#ls 1> listoffiles
#ls -1 . newdir
#ls -1 . newdir 1>presentfiles 2>filesnotpresent

#"ls: cannot access 'newdir': No such file or directory"is the output for the newdir example
#yes the successful part of the ls command went to presentfiles and  the error part went to filesnotpresent file was noticed

#ls -l . newdir >listoffiles:"ls: cannot access 'newdir': No such file or directory". command aims to list newdir in listoffiles while newdir does not exist. listoffiles has present true files in dir.

