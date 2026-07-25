from tools.utility import *

while True:
    try:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Even check")
        print("3. Odd check")
        print("4. Minimum")
        print("5. Maximum")
        print("6. Average")
        print("7. Reverse string")
        print("8. Count vowels")
        print("9. Celsius to Fahrenheit")
        print("10. Fahrenheit to Celsius")
        print("11. Pounds to Kg")
        print("12. Kg to Pounds")
        print("13. Palindrome check")

        choice = input("Enter your choice (1-13): ")

        if choice in ["1","2","3","4","5","6","9","10","11","12"]:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

        if choice in ["7","8","13"]:
            text = input("Enter a word/text: ")

        if choice == "1":
            print("Addition:", add(a, b))
        elif choice == "2":
            print("Even:", is_even(a))
        elif choice == "3":
            print("Odd:", is_odd(b))
        elif choice == "4":
            print("Min:", find_min(a, b))
        elif choice == "5":
            print("Max:", find_max(a, b))
        elif choice == "6":
            print("Average:", average(a, b))
        elif choice == "7":
            print("Reverse:", reverse_string(text))
        elif choice == "8":
            print("Vowels:", count_vowels(text))
        elif choice == "9":
            print("Celsius to Fahrenheit:", celsius_to_fahrenheit(a))
        elif choice == "10":
            print("Fahrenheit to Celsius:", fahrenheit_to_celsius(b))
        elif choice == "11":
            print("Pounds to Kg:", pounds_to_kg(a))
        elif choice == "12":
            print("Kg to Pounds:", kg_to_pounds(b))
        elif choice == "13":
            print("Palindrome:", palindrome(text))
        else:
            print("Invalid choice! Please enter a number between 1 and 13.")

    except Exception as e:
        print("An error occurred:", e)

    again = input("Do you want to run again? (yes/no): ").lower()
    if again != "yes":
        break
