class bankaccount:
    def __init__(self,name,balance):
        self.name = name 
        self.balance = balance 
    def show(self):
        print("name",self.name)
        print("balance",self.balance)
S1 = bankaccount("janu",15000)
S1.show()
