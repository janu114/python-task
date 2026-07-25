class BankAccount:
    def __init__(self):
        self.__balance = 0  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

account = BankAccount()

while True:
    print("\nBank Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        try:
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "2":
        try:
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "3":
        print("Current Balance:", account.get_balance())

    elif choice == "4":
        print("Thank you for using the Bank System!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
