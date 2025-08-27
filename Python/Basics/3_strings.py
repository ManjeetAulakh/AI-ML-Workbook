a = "helloworld"
print(a[6])
# a[4]= "f" not allowed
print(a[0:4])  # yani 0 se 3 tak print and third value is skip value and piche se -1 shuru
c= (a[-1:5:-1])
print(c)


# start = -1: This means the slicing starts at the last character of the string ('d' in "helloworld").
# stop = 5: This means the slicing will stop just before index 5 (the character at index 5 is 'w' in "helloworld").
# step = -1: This means we are stepping backwards through the string.


# strings functions

str = "manjeet m singh aulakh  amanpal jatinder karan"
print(len(str))
print(str.endswith("hello"))   # return true or false
print(str.count("a"))
print(str.capitalize())  # capitalixe first word in string
print(str.find("m"))  # retur first occuerne index
print(str.replace("karan","armaan"))    # jitni baar hi aya sab ko hi kr deta hai
