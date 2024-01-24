'''import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Hello I will create a t2.micro instance")
else:
    print("I have only access to create t2.micro")'''

'''import sys
type = sys.argv[1]

if type == "t2.micro":
    print("It will charage 2 dollars to create t2.micro")
else:
    print("It will charge 4 dollars to create t2.medium")'''

# in the above code for other than t2.medium if user gives other name also it will print 4 dollars, to overcome this we have elif

import sys
type = sys.argv[1]

if type == "t2.micro":
    print("It will charage 2 dollars to create t2.micro")
elif type == "t2.medium":
    print("It will charage 4 dollars to create t2.medium")
elif type == "m2.large":
    print("It will charage 10 dollars to create m2.large")
elif type == "m5.large":
    print("It will charage 15 dollars to create m5.large")
else:
    print("The instance type is not available")