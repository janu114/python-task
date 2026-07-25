# E-commerce checkout system

# Dictionary mapping items to their prices
store_items = {
    "Laptop": 50000,
    "Smartphone": 20000,
    "Headphones": 2000,
    "Keyboard": 1500,
    "Mouse": 800
}

# Cart to track user selections
cart = {}

print("Welcome to the E-Commerce Store!")

while True:
    print("\nAvailable items:")
    for item, price in store_items.items():
        print(f"{item} - Rs.{price}")

    print("\nMenu:")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Remove item from cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        item = input("Enter item name to add: ")
        if item in store_items:
            qty = int(input("Enter quantity: "))
            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty
            print(f"{qty} {item}(s) added to cart.")
        else:
            print("Item not found.")

    elif choice == "2":
        if not cart:
            print("Cart is empty.")
        else:
            print("\nItems in cart:")
            for item, qty in cart.items():
                print(f"{item} x {qty} - Rs.{store_items[item] * qty}")

    elif choice == "3":
        item = input("Enter item name to remove: ")
        if item in cart:
            qty = int(input("Enter quantity to remove: "))
            if qty >= cart[item]:
                del cart[item]
                print(f"{item} removed from cart.")
            else:
                cart[item] -= qty
                print(f"{qty} {item}(s) removed from cart.")
        else:
            print("Item not in cart.")

    elif choice == "4":
        if not cart:
            print("Cart is empty. Nothing to checkout.")
        else:
            total = sum(store_items[item] * qty for item, qty in cart.items())
            print("\nCheckout Summary:")
            for item, qty in cart.items():
                print(f"{item} x {qty} - Rs.{store_items[item] * qty}")
            print(f"Total Bill: Rs.{total}")
            print("Thank you for shopping!")
            break

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
