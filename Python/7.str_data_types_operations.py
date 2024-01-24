name = "Cloud Builders"  #--> by seeing this string we will treat as one element but it stores each characters like list internally so we can do index on this string.
print(name[3])

a = "123456789"
print(a[5])

print(len(name))

print(name.upper())
print(name.lower())

# Strip function only removes spaces beginning and ending of the string not in the middle.
print(len(name.strip()))

c = " bharath@mail.com "
print(len(c))
print(len(c.strip()))

a = "i am learning pyhon language"
print(a)
print(a.capitalize()) # --> Capitalize function makes capital of first character of the string.
print(a.title()) # ---> Title function capitalize first character of each word in the string.

#Substring
print(a.split(" ")) # --> With the help of split function we can divide string of our requirement, here I have divided the string using spcaes and it converts string into list.
a = "arn:aws:region:account_id:service/resource_id"
print(a.split(":"))
print(a.split(":")[2])
print(a.split("/")[1])
print(a.split("_"))

print(a[8:14]) # it prints from 8th index positin to 13th index position
print(a[15:25])
print(a[:10])# it prints from 0th index position to 9th position
print(a[10:])# it prints from 10th index position to last
print(a[-1])
print(a[-2])
print(a[-1:])
print(a[-5:])
print(a[:-5])
#print(a[-1:10])
print(a[2:-2])

#Formating function
a = "python"
b = "training"

print("we are in {} {} program".format("1", "2"))
print("we are in {} {} program".format(a, b))
print("we are in {} {} {} program".format("1", "2", "3"))
print("we are in {} {} {} program".format(a, b, "c"))
#print("we are in {} {} {} program".format(a, b, f))
print("we are in {} {} program".format(a, b, "c"))

print(f"we are in {a} {b} program")
print(f"we are in {"Cloud"} {"Builders"} program")

#Join function ---> we can join only strings and lists 
a = "this is bharath"
b = a.split(" ")
print(b)
print(":".join(b))

print("/".join("rsb"))
print("/".join("r"))
print("/".join("1"))
#print("/".join(1))