def MyDecorator(function):

    def wrapper(*args, **kwargs):
         function(*args, **kwargs) # you can change squence of excuting
         print("Hello i have decoerating the function")
    return wrapper

# these args are use when function have arguments but when no then it will simply excuted


# if we try to pass argument in World2 then wrapper func not tking argument is will give error

@MyDecorator
def World(Country):
    print(f"Country in World is: {Country}")
World("Punjab")
