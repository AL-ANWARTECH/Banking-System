from models.account import BankAccount
from models.customer import Customer


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []

    def add_account(self, account):
        self.accounts.append(account)


    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    
    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return

    def display_accounts(self):
        for account in self.accounts:
            account.display_account()


    def add_customer(self, customer):
        self.customers.append(customer)


    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None


    def remove_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                self.customers.remove(customer)
                return

    def display_customers(self):
        for customer in self.customers:
            customer.display_info()

    def open_account(self, customer, account):
        if self.find_account(account.account_number):
            print("Account already exists.")
            return
        
        self.accounts.append(account)
        customer.add_account(account)
        print("Account opened successfully.")

bank = Bank()
account1 = BankAccount(1001, "savings", 7000)
account2 = BankAccount(1002, "savings", 9000)
account3 = BankAccount(1003, "savings", 5000)
bank.add_account(account1)
bank.add_account(account2)
bank.add_account(account3)
print(bank.accounts)
account = bank.find_account(1002)
print(account)
bank.remove_account(1003)
print(bank.accounts)

bank.display_accounts()
print(bank.customers)

customer1 = Customer(1, "Anwar", "anwarsagirmustapha1@gmail.com", "09067508735")
customer2 = Customer(2, "Salma", "salman@gmail.com", "08099992410")
account4 = BankAccount(1004, "savings", 12000)
bank.customers
bank.add_customer(customer1)
print(bank.customers)
customer = bank.find_customer(1)
print(customer)

bank.remove_customer(1)
print(bank.customers)
bank.add_customer(customer1)
bank.add_customer(customer2)
bank.display_customers()

bank.open_account(customer1, account1)
print(bank.accounts)
print(customer1.accounts)
bank.open_account(customer1, account4)
print(bank.accounts)
print(customer1.accounts)