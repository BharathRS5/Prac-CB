#!/bin/bash
for i in 1 2 3 4 5
do
echo "Welcome $i time"
done

#!/bin/bash
for i in eat run jump play
do
echo "See RSB $i"
done

#!/bin/bash
for i in {1..5}
do
  touch $i
  echo "File created with name $i"
done

#!/bin/bash
for i in {1..5}
do
  rm $i
  echo "File with name $i removed"
done


#!/bin/bash
i=1
for day in mon tue wed thu fri
do
 echo "The weekday is $((i++)): $day"
done

