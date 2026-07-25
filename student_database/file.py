file_path = "student_database/student.txt"

def write_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    dept = input("Dept: ")
    marks = input("Marks: ")
    with open(file_path, "w") as f:   
        f.write(f"{roll},{name},{dept},{marks}\n")
    print("Record written to student.txt")

def append_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    dept = input("Dept: ")
    marks = input("Marks: ")
    with open(file_path, "a") as f:  
        f.write(f"{roll},{name},{dept},{marks}\n")
    print("Record appended to student.txt")

def read_students():
    try:
        with open(file_path, "r") as f:  
            print("\nStudent Records ")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No records yet!")
while True:
    print("\nStudent Record System ")
    print("1. Write Student (overwrite)")
    print("2. Append Student")
    print("3. Read Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        write_student()
    elif choice == "2":
        append_student()
    elif choice == "3":
        read_students()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
