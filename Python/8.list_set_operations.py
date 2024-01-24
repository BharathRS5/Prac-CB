a = [1, 2, 3, 4, 5]
print(len(a))

b = [1, 22, 22, 2, 3, 3, 4, 5, 55, 5, 5]
print(len(b))
print(min(a))
print(min(b))
print(max(a))
print(max(b))
print(sum(a))
print(sum(b))
print(a.count(3)) #this helps to know the element how many times in the list.
print(a.count(55))
print(b.count(3))
print(set(b))
print(b.index(22)) # this tells index position of element in the list.
print(b.index(4))

a.remove(4) # remove helps us to remove the element in the list
print(a)
b.remove(22)
print(b)
b.remove(22)
print(b)

del a[2] # delete removes the index position element mentioned in the list
print(a)

c = [98, 99]
c.extend(a) # it concatenates and store the values in c.
print(c)
print(a+c) # here only concatenation is done but values are not stored.

c.sort() # it will sort in ascending order
print(c)
c.sort(reverse=True) # along with reversing it will sort the elements. 
print(c)

f = [1, 44, 55, 66, 32, 55.5]
f.sort()
print(f)

f.reverse() # reverse function simply do rverse the order in the list but not sorts.
print(f)