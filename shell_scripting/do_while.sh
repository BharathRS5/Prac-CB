# while [ condition ]
# do
#     statement1
#     statement2
# done

#!/bin/bash
 
count=0
num=10
 
while [ $count -lt 10 ]
do
  echo "$num to stop this process $1"
  sleep 1
  echo
  num=`expr $num - 1`
  count=`expr $count + 1`
done
sleep 5
echo "$1 is stopped"
echo