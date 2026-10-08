class employee:
    def __init__(self,employee_id,Name,Department,Salary):
        self.employee_id=employee_id
        self.Name=Name
        self.Department=Department
        self.Salary=Salary
    def Employee_details(self):
        print(f"Employee_name:{self.employee_id}\nEmployee_name:{self.Name}\nDepartment:{self.Department}\nEmployee_Salary:{self.Salary}")
e1=employee(1,"Sabarish","IT",50000)
e1.Employee_details()        