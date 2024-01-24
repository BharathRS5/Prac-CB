'''
1) Simple Data Types: a. String(str)  b. Number/Integer(int)  c. Floating numbers(float) 
2) Collection Data Types: 
    a. List(list): Group of elements are calld as lists. We can also called as array(in other languages). ex: [1, 2, 3] ["a", "b", "c"].It can contain mutiple data types like ex: [1, "a", 2.3, "b", "c", 5, "d"] but other languages doesn't support other data types in list.

    b. Set(set): Set is also same like list but removes duplicate values(repeated values) in the set. ex: {1, 2, 2, 3, 4, 5, 5, "a", "bc", "a"}  ---> in the set it may have duplicates but while printing it will not print duplictes.

    c. Tuple(tuple): Same like set and list but in tuple we can not modify the elements in the list it maintains same elements across the program with out modification.
    ex: a = ("Monday", "Tuesday", "Wednesday)

    d. Dictionary(dict): It contains group of key value pairs. This is similar to JSON format.
    ex: a = {"name": "rsb", "dept": "DevOps"}

3) Boolean Data Type(bool): It contains True and False. Mostly these are used in conditions, if these conditions are "True" execute this or "False" execute false conditions.
'''
# With the help of type() function we can identify the data type of the input we have given.

#Simple Data Types
a = 1+4
print(a)
print(type(a))

a = "Hi this is Bharath"
print(a)
print(type(a))

print(type(5.0))

#Collection Data Types
#-->a. Lists(list)

a = [1, 2, 3]
print(type(a))

a = ["a", "b", "c", "d"]
print(type(a))

a = [1, 2.3, "abc", 5, "b", 3.2, "c"]
print(type(a))
print(a)
print(a[2])
print(type(a[1]))

# --->b. Set(set)
a = [1, 2, 5, 5, 6, 14, 14, "ab", "ab", "bc", "b"]
print(a)

b = {1, 2, 5, 5, 6, 14, 14, "ab", "ab", "bc", "b"}
print(type(b))
print(b)

#--->c. Tuple(tuple)
a = ("a", "b", "c")
print(type(a))

#--->d. Dictionary(dict)
a = {"name": "rsb", "dept": "DevOps"}
print(type(a))


#Boolean Data Type (bool)
a = True
print(type(a))

b = False
print(type(b))