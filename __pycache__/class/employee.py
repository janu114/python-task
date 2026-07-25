class employee:
    def __init__(self,name,id,basicsalary):
        self.name=name
        self.id=id
        self.basicsalary=basicsalary
    def display(self):
        print("name:",self.name)
        print("id:",self.id)
        print("basicsalary:",self.basicsalary)
    def bonus(self):
        if self.basicsalary >= 50000:
            bonus =0.1*self.basicsalary
            print("bonus:",bonus)
        else:
            bonus =0.05*self.basicsalary
            print("bonus:",bonus)
e1 = employee("anu",14,4000)
e1.display()
e1.bonus()
e2 = employee("hasini",56,5678)
e2.display()
e2.bonus()
e3=employee("thanu",89,9090)
e3.display()
e3.bonus()