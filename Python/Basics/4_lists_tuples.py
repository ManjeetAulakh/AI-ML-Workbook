# pyhton lists are datatypes to store set of values of any daat type
# lists are ordered yani jaise squenec me hai vese hi hai
# ["bdb", "bcd", 2, False]

a= ["majeet","amanpal", 2,4]
print(a)
a[1] = 5  # lists can be changed
print(a[2])
print(a)
print(a[0:2])  # slicing in lists         2 not included

# lists functions
l1 = [1,6,4,8,1,2,1,5,45]
l1.sort()
print(l1)
l1.reverse()   # reverse the list
l1.append(5)  # append at the last to list
l1.insert(5,100)  #  at 5 index value 100
print(l1)
l1.pop(2)  # pop at index 2 and return its value
l1.remove(1)  # remove 1 from list if more then 1 time then remove onpy 1 1 
print(l1)