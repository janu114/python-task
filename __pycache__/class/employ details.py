class employee:
    def __init__(self,name,id,dept,salary):
        self.name = name
        self.id = id
        self.dept = dept
        self.salary = salary
    def display(self):
        print("name:",self.name)
        print("id:",self.id)
        print("dept:",self.dept)
        print("salary:",self.salary)
employees = []
n = int(input("enter number of employees:"))
for i in range(n):
    name = input("enter employee name:")
    id = int(input("enter employee id:"))
    dept = input("enter employee dept:")
    salary = float(input("enter employee salary:"))
    emp = employee(name,id,dept,salary)
    employees.append(emp)
print("employee details:")
for emp in employees:
    emp.display()
    
    