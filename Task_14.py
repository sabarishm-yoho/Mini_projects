import matplotlib.pyplot as plt
products = input("Enter product names: ").split()
sales = list(map(int, input("Enter sales values: ").split()))
plt.bar(products, sales)
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()