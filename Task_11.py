import json
Employee =[
    {
        "id": 1,
        "name": "peter",
        "department": "Developer"
    },
    {
        "id": 2,
        "name": "John",
        "department": "IT"
    },
    {
        "id": 3,
        "name": "Joe",
        "department": "Data analyst"
    }
]
with open("Employee.txt","w")as files:
 json.dump(Employee,files,sort_keys=True)
with open("Employee.txt","r") as files:
 Employee = json.load(files)
print(Employee)