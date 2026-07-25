def authenticate(username, password):
    valid_username = "student"
    valid_password = "python123"
    return username == valid_username and password == valid_password

def login_system():
    username = input("Username: ")
    password = input("Password: ")

    if authenticate(username, password):
        print("Login successful")
    else:
        print("Login failed")
login_system()


