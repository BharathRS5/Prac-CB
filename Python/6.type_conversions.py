a = 10
b = 10.5
print(a+b)   #--> Here we will get float values, but in some case we need only integers then we can convert which is shown below.
print(int(a+b))

# print(int("abc")) #here it will throw error as str can not be converted to integer to do so it shoud be in base 10 values which means number.
print(int("5"))  # --> Here we represent number like str but we can convert to int with conversion but str can not be converted to int.
print(int("1"+"2"))


a = input("enter the first number:")
b = input("enter the second number:")
print(type(a)) # --> Here we will give input as int but it will take as str in input function, so we should convert into int.
print(a+b) # Here it will do concatenation of str rather than addition.

a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
print(a + b)