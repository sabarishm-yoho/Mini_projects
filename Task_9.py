with open("student_data.txt","w") as file:
    file.write("Student name:"+input("Enter the student name:"))
    file.write(" Student mark:"+input("Enter the mark:"))
with open("Student_data.txt","r") as file:
    content=file.read()
    print(content)
