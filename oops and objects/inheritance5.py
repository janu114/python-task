class customer:
    def __init__(self, name, mobilenumber):
        self.name = name
        self.mobilenumber = mobilenumber
        
    def display_customer(self):
        print("Name:",self.name)
        print("Mobile Number:",self.mobilenumber)
        
class ordered(customer):
    def __init__(self, name, mobilenumber, product_name, quantity, price):
        super().__init__(name, mobilenumber)
        self.product_name = product_name
        self.quantity = quantity
        self.price = price 
    
    def display_ordered(self):
        print("product Name:",self.product_name)
        print("Quantity:",self.quantity)
        print("price:",self.price)
        
class calculate(ordered):
    def __init__(self, name, mobilenumber, product_name, quantity, price):
        super().__init__(name, mobilenumber, product_name, quantity, price)
    def total_price(self):
        return self.quantity * self.price
        
class payment(calculate):
    def __init__(self, name, mobilenumber, product_name, quantity, price):
        super().__init__(name, mobilenumber, product_name, quantity, price)
    def display_payment(self):
        print("payment details")
class make(payment):
    def __init__(self, name, mobilenumber, product_name, quantity, price):
        super().__init__(name, mobilenumber, product_name, quantity, price)
    def make_payment(self):
        total = self.total_price()
        if total > 0:
            print("payment sucessful")
        else:
            print("invalid order")
            
name = input("Enter Name:")
mobilenumber = input("Enter Mobilenumber:")
quantity = int(input("enter quantity:"))
price = int(input("enter price:"))
product_name = input("enter product name:")

print("\nCustomer Details")
c = customer(name, mobilenumber)
c.display_customer()

print("\nOredered Details")
o = ordered(name, mobilenumber, product_name, quantity, price)
o.display_ordered()

print("\nTotal Price")
t = calculate(name, mobilenumber, product_name, quantity, price)
t.total_price()

print("\npayment details")
p = payment(name, mobilenumber, product_name, quantity, price)
p.display_payment()

print("\nmake payment")
m = make(name, mobilenumber, product_name, quantity, price)
m.make_payment()

