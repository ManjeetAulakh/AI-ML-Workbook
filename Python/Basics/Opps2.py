class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("Hello ",self.name," your avg marks are ",sum/3);

s1 = Student("Manjeet",[10,20,30])
s1.avg()

# i can also change oject attribites
s1.name = "Singh"
s1.avg()