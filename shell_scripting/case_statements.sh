#!/bin/bash

echo "Plese choose the option to execute"
echo
echo "a = Display date and time"
echo
echo "b = Your present working directory is"
echo 
echo "c = List of files in this directory are"

read choices
case $choices in

a) date;;
b) pwd;;
c) ls;;
*) echo "Plese choose the correction option"

esac