class laptop:
    def __init__(self,brand,ram):
        self.brand = brand 
        self.ram = ram 
    def display(self):
        print("brand",self.brand)
        print("ram",self.ram)
L1 = laptop("dell",500)
L1.display()
L2 = laptop("hp",600)
L2.display()