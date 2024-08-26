class ATM:
    def __init__(self, balance=0.0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited to your account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn from your account.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def exit(self):
        print("Thank you for using the ATM. Goodbye!")
        return False

    def menu(self):
        print("Welcome to ATM Machine!")
        while True:
            print("\nPlease select an option:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                if not self.exit():
                    break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    atm = ATM(balance=1000.0)  # Initial balance set here
    atm.menu()
