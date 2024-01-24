for i in range(10):
    print("rsb")
    print(i)

colors = ["green", "yellow", "blue"]
for a in colors:
    print(a)

count = 0
while count < 5:
    print(count)
    count += 1 

numbers = [1,2,3,4,5]
for no in numbers:
    if no == 3:
        break
    print(no)

numbers = [1,2,3,4,5]
for no in numbers:
    if no == 3:
        continue
    print(no)
