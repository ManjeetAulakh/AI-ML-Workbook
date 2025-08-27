i = 0
while i < 10:
    print(i)
    i = i + 1

fruits = ['banana','mango','apple']
for i in fruits:
    print(i)
for i in range(2,9,2): # range(start, stop, step_size)
    print(i)
print("break ke baad nhi hota print")
for i in range(8):
    print(i)
    if(i==5):
        break
print("continue yani is ko shod do aur continue karo")
for i in range(8):
    if(i==5):
        continue
    print(i)
# agar kahli cohdna hai to use pass
