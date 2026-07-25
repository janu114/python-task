class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, user, pwd):
        if user == self.username and pwd == self.password:
            print("Login successful ")
            return True
        else:
            print("Invalid username or password ")
            return False


class OTPVerification:
    def __init__(self):
        self.current_otp = "1234"  
    
    def verify_otp(self, otp):
        if otp == self.current_otp:
            print("OTP verified successfully ")
            return True
        else:
            print("Invalid OTP ")
            return False


class SecureBank(Login, OTPVerification):
    def __init__(self, username, password, balance):
        Login.__init__(self, username, password)
        OTPVerification.__init__(self)
        self.balance = balance
        self.mini_statement = []
    
    def dashboard(self):
        print("\nSecure Bank Dashboard ")
        print(f"Balance: ₹{self.balance}")
        print("Mini Statement:")
        if self.mini_statement:
            for txn in self.mini_statement:
                print("-", txn)
        else:
            print("No transactions yet:")
            
bank = SecureBank("user1", "pass123", 5000)

if bank.login("user1", "pass123"):
    if bank.verify_otp("1234"):
        bank.mini_statement.append("Deposited ₹2000")
        bank.mini_statement.append("Withdrawn ₹1000")
        bank.dashboard()
      