a={1,3,5,5,6,5,88,84}  #repetative items no print
print(a)
# this sytax create a empty dict not a empty set
a={}
# the empty set can be created by
b=set()
b.add(5)
b.add(6)
b.add(1)
b.add(2)
b.add(4)
# b.add([1,2,3]) as list and dict can be chnaged but tuple can be added to
b.add((1,5))
print(b)


# sets are unorderd yani set ka yeh elemet de do vo de not posible and set items are not changed and
# not contain duplicate values

print(len(b))
b.remove(5)
print(b)
b.pop() # remove any rondom varible from set
print(b)
# b.clear()  empty the set
print(b)
