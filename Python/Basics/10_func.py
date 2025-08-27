def maxi(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if (num2 > num3):
            return num2
        else:
            return num3


a = 35
b = 45
c = 50
largest = maxi(a, b, c)
print("The largest is: " + str(largest))


# factorail of fact(n)  = n * fact(n-1)
# sum of sum(n) = n + sum(n-1)



def sumfirstnatural(num):
    if (num <= 0):
        return 0
    else:
        return num + sumfirstnatural(num - 1)


x = 3
sums = sumfirstnatural(x)
print(sums)
