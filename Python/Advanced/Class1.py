class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector(self.x + other.x , self.y+ other.y)

    def __repr__(self):
        return f"X is : {self.x} and Y is : {self.y}"

# it is just like a toString func in java
# The __repr__ method in Python is a special method used to represent a class's objects as a string. It's called
# when you use the repr() function or when an object is printed or displayed using print(). Its purpose is to
# return a string that, when passed to the eval() function, should return a result equivalent to the original object.

    def __call__(self):
        print("I was called by ojbect")


v1 = vector(20,40)
v2 = vector(30,80)
print(v1.x)
v3 = v1 + v2
print("The x is :", v3.x, " and y is: ", v3.y)

print(v3)

v3() # fro that call method called

# The __call__ method in Python allows an object to be called as if it were a function. When you define __call__ within
# a class, you're essentially enabling instances of that class to be callable.

