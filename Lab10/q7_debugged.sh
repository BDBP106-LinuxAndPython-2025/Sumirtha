#!/bin/bash
# Getting the username of the logged-in user
logged_in_user="$(whoami)"
# Checking if the user is logged in
if [ -n "$logged_in_user" ];then
	echo "The logged_in_user is:"$logged_in_user
else
	echo "User is not logged in"
fi

#changes made on to be debugged
#line3:"$(whoami)"
#line5:loged to logged;')' replaced by ']';
#line6:underscore corrections made; 'then' is moved to line 5;intended with tab
#line8:intended with tab
