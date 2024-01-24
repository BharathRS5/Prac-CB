#Function is a piece of code which as some logic to do a task and can re use.
'''
a = 2
b = 3

add = a+b
print(add)

sub = a-b
print(sub)

mul = a*b
print(mul)

Above we see a simple code without functional approach but if code is big it will be difficult to find and rectify the problem in the code. If a code is doing different functionalities like above we are doing add, sub and mul then use functions instead of writhing line by line. With the help of functions we are having some advantages
Adv of function: 1) Reusability 2) Readability 3) Debugging 
'''

'''
num1 = 5
num2 = 10

#Syntax of function
def addition():
    add = num1+num2
    print(add)

def substraction():
    sub = num1-num2
    print(sub)

def multiplication():
    mul = num1*num2
    print(mul)
#we need to explicitly call the function to execute the function code.
addition()
substraction()
multiplication()'''

# Functions primary responsibility is takes input, perform the required logic and returns the output.

def addition(num1, num2):
    add = num1+num2
    return add

def substraction(num1, num2):
    sub = num1-num2
    return sub

def multiplication(num1, num2):
    mul = num1*num2
    print(mul)

print(addition(5, 10))
print(substraction(10, 5))
multiplication(2, 7)

