class Movie:
    def __init__(self,  name, ticket_price, num_tickets):
        self.name = name
        self.ticket_price = ticket_price
        self.num_tickets = num_tickets

    def calculate_bill(self):
        return self.ticket_price * self.num_tickets

    def save_booking(self):
        try:
            with open("movie.txt", "a") as f:
                f.write(f"{self.name},{self.ticket_price},{self.num_tickets},{self.calculate_bill()}\n")
            print(" Booking saved successfully!")
        except FileNotFoundError:
            print(" Error: movie.txt file not found!")

    @staticmethod
    def display_bookings():
        try:
            with open("movie.txt", "r") as f:
                print("\n--- All Bookings ---")
                for line in f:
                    movie_id, name, price, tickets, bill = line.strip().split(",")
                    print(f"Movie ID: {movie_id}, Name: {name}, Price: {price}, Tickets: {tickets}, Bill: {bill}")
        except FileNotFoundError:
            print(" Error: movie.txt file not found!")


# Menu-driven program
while True:
    print("\n Movie Ticket Booking System")
    print("1. Book Tickets")
    print("2. View Bookings")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter Movie Name: ")
        try:
            ticket_price = int(input("Enter Ticket Price: "))
            num_tickets = int(input("Enter Number of Tickets: "))
        except ValueError:
            print(" Please enter valid numbers for price and tickets!")
            continue

        movie = Movie( name, ticket_price, num_tickets)
        print(f"Total Bill: Rs.{movie.calculate_bill()}")
        movie.save_booking()

    elif choice == "2":
        Movie.display_bookings()

    elif choice == "3":
        print(" Exiting Thank you!")
        break

    else:
        print("Invalid choice, please try again.")
