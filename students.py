
students = {}
file = open("student.txt","r")
for line in file:
    try:
        data = line.split(",")
        name = data[0]
        marks = int(data[1])
        students[name] = marks
    except Valueerror:
        print("invalid record ignored")
        
file.close()
def find_topper():
    topper = max(students, key=students.get)
    print("topper:", topper)
    print("marks:", students[topper])

print("student dictionary:")
print(students)
find_topper()
        



