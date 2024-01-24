#!/bin/bash

echo "Hi my name is Bharath"
echo "-----------"
echo "What is your name?"
read a #in linux "read" helps us to give prompt to the user on terminal while runnig this script and it stores in the variable we define after read, here it is 'a'.
echo "Hello $a welcome to the CloudBuilders"
echo 

#How to run a linux command and store in variable.
b=`hostname`
c=$(pwd)

echo "My server name is $b"
echo 
echo "We are presently located at $c"