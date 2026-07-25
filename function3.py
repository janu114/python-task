def sign_in():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = input("Enter your password: ")

    if first_name and last_name and password:
        print("Sign in successful!")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print("Password saved successfully!")
    else:
        print("Please fill in all fields.")
sign_in() 
