class student:
    # default
    # if i have college name same for all students so we donot create every time in oject
    # we create as class attribute
    collegeName = "LPU"  # class attribute
    def __init__(self):
        # self is parameter is refernce to the current instance (object) of the class
        print("Construtor called")

        # paraterized constructor
    def __init__(self,lastname):
        self.name = lastname     # obj attribute

    def __init__(self,lastname,marks=0):
        self.name = lastname
        self.marks = marks

    # However, in Python, you can't define multiple __init__ methods within the same class.
    # Only the last __init__ method defined will be considered.

    def welcome(self):
        print("hello stunet", self.name)

    def getMarks(self):
        return self.marks

# constrctor is defined by __init__ function
s1 = student("aulakh",50)
print(s1.name)

s2 = student("gill")
print(s2.name)

# both are write
print(s1.collegeName)
print(student.collegeName)

s1.welcome()
print(s1.getMarks())