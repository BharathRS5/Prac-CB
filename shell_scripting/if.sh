#!/bin/bash

a="CloudBuilders"

if[ $a="CloudBuilders" ]
then 
    echo "The name is correct"
else 
    echo "Please give the correct name"
fi


#!/bin/bash

echo "Please enter your name"
read name

if [ $name = "CloudBuilders" ]
then
    echo "The name is correct"
else
    echo "Please give the correct name"
fi



#!/bin/bash

NUMBER=100

if [ $NUMBER -gt 10 ]

then
    echo "NUMBER is greater than 10"
elif [ $NUMBER = 10 ]
    echo "gjg"
else
    echo "NUMBER is not greater than 10"
fi


#!/bin/bash

#echo "Please enter your name"
#read name
name=CloudBuilders
if [ $name = "CloudBuilders" ]
then
    echo "The name is correct"
else
    echo "Please give the correct name"
fi



#!/bin/bash

if [ -e /home/ec2-user/ifff.sh ]
then
  echo "the file exits"
else
  echo "Please chek the file"
fi
