try:
    a=float(input("Enter the value:"))
    b=float(input("enter the value"))
    Operator=input("Enter the operator - + / *")
    if Operator== "-":
        print(a+b)
    elif Operator == "+":
        print(a-b)
    elif Operator =="/":
        print(a/b)
    elif Operator == "*":
        print(a*b)
    else:
        print("Invalid operator")
except ValueError():
    print("Enter the valid number")
except ZeroDivisionError():
    print("Cannot divided by zero")

    
    