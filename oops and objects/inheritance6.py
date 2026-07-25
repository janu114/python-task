class Login:
    def login(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == "customer" and password == "food123":
            print("Login Successful")
            return True
        else:
            print("Invalid Login")
            return False

class FoodOrder:
    def place_order(self):
        self.items = {
            "pizza": 150,
            "burger": 100,
            "sandwich": 80
        }

        self.food = input("Enter Food Name: ").lower()
        self.qty = int(input("Enter Quantity: "))

        if self.food in self.items:
            self.total = self.items[self.food] * self.qty
            print("Order Placed Successfully")
            return True
        else:
            print("Food Item is Not Available")
            return False

class FoodDelivery(Login, FoodOrder):
    def generate_bill(self):
        print("\nBILL")
        print("Food Name :", self.food)
        print("Quantity  :", self.qty)
        print("Total Bill:", self.total)
        
product = FoodDelivery()

if product.login():
    if product.place_order():
        product.generate_bill()