class User:
    def __init__(self, email, name):
        self.email = email
        self.name = name

    def display_user(self):
        print("User Details:")
        print("Name:", self.name)
        print("Email:", self.email)


class Student(User):
    def __init__(self, email, name, course_name=""):
        super().__init__(email, name)
        self.course_name = course_name

    def enroll_course(self):
        if self.course_name.strip() != "":
            print("Enrollment Successful in course:", self.course_name)
        else:
            print("Please enter a course name")


class Instructor(User):
    def __init__(self, email, name, course_name=""):
        super().__init__(email, name)
        self.course_name = course_name

    def create_course(self):
        if self.course_name.strip() != "":
            print("Course created successfully:", self.course_name)
        else:
            print("Course name cannot be empty")

student1 = Student("student@example.com", "Alice", "Python Programming")
student1.display_user()
student1.enroll_course()

print("\n")

instructor1 = Instructor("instructor@example.com", "Bob", "Data Science")
instructor1.display_user()
instructor1.create_course()
