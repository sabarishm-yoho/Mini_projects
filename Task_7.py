class Bank_account:
    def __init__(self,Balance):
        self.Balance = Balance
    def Deposit(self,deposit):
        self.deposit=deposit
        self.Balance+=self.deposit
        print(f"Account balance:{self.Balance}")
    def Withdraw(self,amount):
        self.amount=amount
        if self.amount<self.Balance:
            self.Balance-=self.amount
            print(f"Withdrawal the amount successfully\nAccount Balance:{self.Balance}")
        else:
            print("Insufficient Balance")
b=Bank_account(10000)
while True:
    print("1. Deposit amount")
    print("2. Withdrawal amount")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            b.Deposit(int(input("Enter the deposit amount:")))

        elif choice == 2:
            b.Withdraw(int(input("Enter the withdrawal amount")))
        else:
            print("Invalid choice")
    except ValueError():
        print("Enter only number")
            




