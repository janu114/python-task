class student:
    def __init__(self,name,rollno,marks):
        self.name = name 
        self.rollno = rollno 
        self.marks = marks 
    def display(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("marks:",self.marks)
    def result(self):
        if self.marks >= 50:
            print("pass")
        else:
            print("fail")
S1 = student("janu",25,90)
S1.display()
S1.result()
S2 = student("anu",12,10)
S2.display()
S2.result()