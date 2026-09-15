from models.account import BankAccount


class Bank:
    def __init__(self):
        self.accounts = []

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