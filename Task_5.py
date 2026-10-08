Students=[
 {'id': 1, 'name': 'Sabarish', 'age': 21, 'marks': 85},
 {'id': 2, 'name': 'Arun', 'age': 20, 'marks': 78},
 {'id': 3, 'name': 'Kumar', 'age': 21, 'marks': 92}
]
index=len(Students)+1
for i in range(1):
    print("\nEnter details for Student", i + 1)
    student_id = index
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    marks = int(input("Enter Student Marks: "))
    student={
            "id":student_id,
            "name":name,
            "age": age,
            "marks": marks       
        }
    Students.append(student)
id=int(input("Enter the student id:"))

for i in Students:
    if i["id"]==id:
        print(i)
        found=True
        break
if found==False:
    print("student is not found")