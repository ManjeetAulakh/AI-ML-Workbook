# decorators add more functionailty to methods

def MyDecorator(function):

    def wrapper(*args, **kwargs):
         function(*args, **kwargs) # you can change squence of excuting
         print("Hello i have decoerating the function")
    return wrapper

# these args are use when function have arguments but when no then it will simply excuted

def Hello():
    print("Hello World")

Newfunc = MyDecorator(Hello)   # or directly MyDecoator(Hello)()
Newfunc()

# also no need to write above simple add like it and call orginal function

@MyDecorator
def World():
    print("In the World")

World()

# if we try to pass argument in World2 then wrapper func not tking argument is will give error

@MyDecorator
def World2(Country):
    print(f"Country in World is: {Country}")

World2("Punjab")
