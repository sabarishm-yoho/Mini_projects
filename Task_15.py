import pandas as pd
import matplotlib.pyplot as plt

employees = pd.read_csv("employees.csv")
print("Employee Data:",employees)
print("Average Salary:", employees["Salary"].mean())
print("Maximum Salary:", employees["Salary"].max())
print("Minimum Salary:", employees["Salary"].min())

plt.bar(employees["Name"], employees["Salary"])

plt.title("Employee Salary")
plt.xlabel("Employee Name")
plt.ylabel("Salary")

plt.show()