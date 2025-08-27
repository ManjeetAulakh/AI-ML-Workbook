# all methods with self are non static method
# but there are also staic methods without self

# for static method we have to use decorator

class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hey World")

s1 = Student("Manjeet",[10,20,30])
s1.hello()


class Bank:
    def __init__(self,acc,password):
        self.accountNumber = acc
        # to make paasword private use __
        self.__password = password

    def resetPass(self):
        print(self.__password)

b1 = Bank("1234","abcd")
print(b1.accountNumber)
# print(b1.__password error ad password i private
b1.resetPass()