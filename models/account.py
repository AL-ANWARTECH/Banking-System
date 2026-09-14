class BankAccount:
    def __init__(self, account_number, account_type, balance):
        self.account_number= account_number
        self.account_type = account_type
        self.balance = balance
        self.is_active = True


    def display_account(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        print(f"Active: {self.is_active}")

    def deposit(self, amount):
        if not self.is_active:
            print("Transaction rejected. Account is inactive")
            return
        
        self.amount = amount
        if amount > 0:
            self.balance += amount
            print(f"New Balance:  ₦{self.balance}")
        else:
            print("Is not allow to deposit negative or zero.")


    def withdraw(self, amount):
        if not self.is_active:
            print("Transaction is rejected. Account is inactive")
            return
        
        if amount <= 0:
            print("Withdrawal Amount Must be Greater Than 0.")
            return
        if amount > self.balance:
            print("Insufficient Balance.")
            return
        self.balance -= amount
        print("Withdrawal Successful.")
        print(f"New Balance:  ₦{self.balance}")


    def deactivated_account(self):
        self.is_active = False
        print(f"Active: {self.is_active}")


    def activated_account(self):
        self.is_active = True
        print(f"Active: {self.is_active}")

    def transfer(self, destination, amount):
        if not self.is_active:
            print("Transaction rejected. Sender account is inactive.")
            return

        if not destination.is_active:
            print("Transaction rejected. Recipient account is inactive.")
            return

        if amount <= 0:
            print("Transfer Amount Must Be Greater Than 0.")
            return
        if amount > self.balance:
            print("Insufficient Balance.")
            return

        self.balance -= amount
        destination.balance += amount

        print("Transfer Successful.")
        print(f"Sender New Balance: ₦{self.balance}")
        print(f"Recipient New Balance: ₦{destination.balance}")


account1 = BankAccount(
    1001,
    "savings",
    5000,
)

account2 = BankAccount(
    1002,
    "savings",
    7000,
)
account1.display_account()
account1.deposit(3000)
account1.deposit(-348)
account1.withdraw(300)
account1.withdraw(50000)
account1.withdraw(-345)
account1.display_account()
account1.deactivated_account()
account1.display_account()
account1.activated_account()
account1.display_account()

account1.deposit(5000)
account1.deactivated_account()
account1.deposit(2000)
account1.withdraw(1000)
account1.activated_account()

account2.display_account()
account2.deposit(40000)
account2.activated_account()
account2.transfer(account1, 3000)