class car:
    def __init__(self,brand,color):
        self.brand = brand 
        self.color = color 
    def show(self):
        print("brand",self.brand)
        print("color",self.color)
S1 = car("suzuki","red")
S1.show()