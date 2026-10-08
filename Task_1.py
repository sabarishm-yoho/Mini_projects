Student = str(input("Enter the Student name:"))
Eng = int(input("Enter the mark:"))
Maths = int(input("Enter the mark:"))
Sci = int(input("Enter the mark:"))
Social = int(input("Enter the mark:"))
Tamil = int(input("Enter the mark:"))

Total_marks = Eng+Maths+Sci+Social+Tamil
Percentage = (Total_marks/500)*100
if Percentage>90:
    print(f"A grade with {Percentage}")
elif Percentage>80:
    print(f"B grade with {Percentage}")
elif Percentage>70:
    print(f"C grade with {Percentage}")
elif Percentage>60:
    print(f"E grade with {Percentage}")
else:
    print(f"F grade with {Percentage}")
