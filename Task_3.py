def bill(Price,Quantity):
    return Price*Quantity
def calculate(Total,Product):
    if Total>500:
        Discount=Total*0.10
        Final = Total-Discount
        print(f"Product:{Product}\nSub_total:{Total}\nDiscount :{Discount}\nTotal:{Final}")
    else:
        print(f"Product:{Product}\nSub_total:{Total}\nDiscount :0%\nTotal:{Total}")
Product = str(input("Enter the Product name:"))
Price = int(input("Enter the Price:"))
Quantity = int(input("Enter the Quantity:"))
Total=bill(Price,Quantity)
calculate(Total,Product)
