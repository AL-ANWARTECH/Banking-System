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
