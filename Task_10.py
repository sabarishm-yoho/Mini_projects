import pandas as pd
student=pd.read_csv("student_data (1).csv")
print("Average mark:", student["Marks"].mean())
print("Maximum marks:",student["Marks"].max())
print("Minimum marks:",student["Marks"].min())
print(student[student["Marks"]>80])




