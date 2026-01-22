class Bank:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Transaction failed.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display(self):
        print("\n--- Account Details ---")
        print("Customer Name :", self.name)
        print("Account Number:", self.acc_no)
        print("Balance       : ₹", self.balance)


# Main Program
if __name__ == "__main__":
    name = input("Enter Customer Name: ")
    acc_no = input("Enter Account Number: ")
    initial_balance = float(input("Enter Initial Balance: "))

    customer = Bank(name, acc_no, initial_balance)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Display Account\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            customer.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            customer.withdraw(amount)

        elif choice == "3":
            customer.display()

        elif choice == "4":
            print("Thank you for using the Bank Management System!")
            break

        else:
            print("Invalid choice. Try again.")