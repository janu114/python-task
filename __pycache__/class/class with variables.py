class student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def show(self):
        name = input("enter student name:")
        age = input("enter student age:")
S1 = student("name","age")
S1.show()