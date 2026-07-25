class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    
    def doctor_info(self):
        print("Department:", self.department)

class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease
    
    def patient_info(self):
        print("Disease:", self.disease)

class MedicalIntern(Person):
    def __init__(self, name, age, department, disease, intern_id):
        super().__init__(name, age)
        self.department = department
        self.disease = disease
        self.intern_id = intern_id
    
    def doctor_info(self):
        print("Department:", self.department)
    
    def patient_info(self):
        print("Disease:", self.disease)
    
    def intern_info(self):
        print("Intern ID:", self.intern_id)

print("\nEnter Person Details")
p_name = input("Enter name: ")
p_age = int(input("Enter age: "))
person = Person(p_name, p_age)

print("\nEnter Doctor Details")
d_name = input("Enter doctor name: ")
d_age = int(input("Enter doctor age: "))
d_dept = input("Enter department: ")
doctor = Doctor(d_name, d_age, d_dept)

print("\nEnter Patient Details")
pt_name = input("Enter patient name: ")
pt_age = int(input("Enter patient age: "))
pt_disease = input("Enter disease: ")
patient = Patient(pt_name, pt_age, pt_disease)

print("\nEnter Medical Intern Details")
i_name = input("Enter intern name: ")
i_age = int(input("Enter intern age: "))
i_dept = input("Enter intern department: ")
i_disease = input("Enter intern disease: ")
i_id = input("Enter intern ID: ")
intern = MedicalIntern(i_name, i_age, i_dept, i_disease, i_id)


print("\nPerson Details")
person.display_person()

print("\nDoctor Details")
doctor.display_person()
doctor.doctor_info()

print("\nPatient Details")
patient.display_person()
patient.patient_info()

print("\nMedical Intern Details")
intern.display_person()
intern.doctor_info()
intern.patient_info()
intern.intern_info()
