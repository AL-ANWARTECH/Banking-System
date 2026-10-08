from models import account
from models.account import BankAccount

class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = []

    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")

    def add_account(self, account):
        self.accounts.append(account)


    def find_account(self, account_number):
        for account in self.accounts:
            if  account.account_number == account_number:
                return account
        return None

    def display_accounts(self):
        for account in self.accounts:
            account.display_account()

    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return

        print("Account not found.")

    def get_account_count(self):
        return len(self.accounts)

    def display_account_count(self):
        print(f"Customer {self.name} has {self.get_account_count()} accounts.")

    def get_total_balance(self):
        total = 0

        for account in self.accounts:
            total += account.balance

        return total

    def display_total_balance(self):
        print(f"Customer {self.name} has a total balance of {self.get_total_balance()}.")


    def deposit_to_account(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_from_account(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")


    def transfer_to_account(self, account_number, destination_account, amount):
        my_account = self.find_account(account_number)
        if my_account:
            my_account.transfer(destination_account, amount)
        else:
            print("Account not found.")

customer1 = Customer(
    1,
    "Anwar sagir",
    "anwarsagir@gmail.com",
    "09067508735"
)

customer1.display_info()

print(customer1.accounts)

account1 = BankAccount(1001, "savings", 5000)

customer1.add_account(account1)
print(customer1.accounts)

customer1.find_account(1001)
customer1.display_accounts()
customer1.remove_account(1001)
customer1.display_accounts()
customer1.remove_account(1001)

customer = Customer(1, "Anwar sagir", "anwarsagir@gmail.com", "09067508735")

account = BankAccount(1001, "savings", 5000)

customer.add_account(account)

print(customer.accounts)
print(customer.get_total_balance())
customer.display_total_balance()
customer.deposit_to_account(1001, 2000)
print(customer.get_total_balance())

customer.withdraw_from_account(1001, 2000)

account2 = BankAccount(1002, "savings", 9000)
destination_account = account2
customer.transfer_to_account(1001, destination_account, 1000)
