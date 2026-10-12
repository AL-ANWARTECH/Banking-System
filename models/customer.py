import re
from models import account
from models.account import BankAccount

class Customer:
    def __init__(self, customer_id, name, email, phone):
        if not isinstance(customer_id, int) or isinstance(customer_id, bool):
            raise TypeError("Customer ID must be an integer.")

        if customer_id <= 0:
            raise ValueError("Customer ID must be greater than 0.")

        if not isinstance(name, str):
            raise TypeError("Customer name must be a string.")

        if not name.strip():
            raise ValueError("Customer name cannot be empty.")

        if not isinstance(email, str):
            raise TypeError("Customer email must be a string.")

        if not email.strip():
            raise ValueError("Customer email cannot be empty.")

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            raise ValueError("Please enter a valid email address.")

        if not isinstance(phone, str):
            raise TypeError("Customer phone number must be a string.")

        if not phone.strip():
            raise ValueError("Customer phone number cannot be empty.")

        if not re.fullmatch(r"0\d{10}", phone):
            raise ValueError("Phone number must contain 11 digits and start with 0.")
        
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
        for existing_account in self.accounts:
            if existing_account.account_number == account.account_number:
                print("This account is already linked to the customer.")
                return

        self.accounts.append(account)
        print("Account added successfully.")



    def find_account(self, account_number):
        for account in self.accounts:
            if  account.account_number == account_number:
                return account
        return None

    def display_accounts(self):
        if not self.accounts:
            print("This customer has no accounts.")
            return

        for account in self.accounts:
            account.display_account()
            print("_" * 30)

    def display_account_balance(self, account_number):
        account = self.find_account(account_number)

        if account is None:
            print("Account not found.")
            return

        print(f"Account {account_number} Balance:  ₦{account.balance}")

    def remove_account(self, account_number):
        account = self.find_account(account_number)

        if account is None:
            print("Account not found.")
            return

        if account.is_active:
            print("Cannot remove an active account.")
            return

        self.accounts.remove(account)
        print(f"Account {account_number} removed successfully.")

    def get_account_count(self):
        return len(self.accounts)

    def display_account_count(self):
        count = self.get_account_count()

        if count == 1:
            print(f"Customer {self.name} has 1 account.")
        else:
            print(f"Customer {self.name} has {count} accounts.")


    def get_total_balance(self):
        total = 0

        for account in self.accounts:
            total += account.balance

        return total

    def display_total_balance(self):
        print(f"Customer {self.name} has a total balance of {self.get_total_balance()}.")


    def deposit_to_account(self, account_number, amount):
        account = self.find_account(account_number)


        if account is None:
            print("Account not found.")
            return

        if not account.is_active:
            print("Cannot deposit to an inactive account.")
            return
        
        account.deposit(amount)

    def withdraw_from_account(self, account_number, amount):
        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
            return

        if not account.is_active:
            print("Cannot withdraw from an inactive account.")
            return

        account.withdraw(amount)


    def transfer_to_account(self, account_number, destination_account, amount):
        my_account = self.find_account(account_number)

        if my_account is None:
            print("Account not found.")
            return

        if not my_account.is_active:
            print("Cannot transfer from an inactive account.")
            return

        if not destination_account.is_active:
            print("Cannot transfer to an inactive account.")
            return

        if my_account is destination_account:
            print("Cannot transfer to the same account.")
            return

        if amount <= 0:
            print("Transfer amount must be greater than zero.")
            return

        if amount > my_account.balance:
            print("Insufficient balance.")
            return

        my_account.transfer(destination_account, amount)


    def deactivate_account(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.deactivated_account()
            print(f"Account {account_number} deactivated successfully.")
        else:
            print("Account not found.")


    def activate_account(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.activated_account()
            print(f"Account {account_number} activated successfuly")
        else:
            print("Account not found.")

if __name__ == "__main__":


   
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
    customer1.deposit_to_account(1002, 2000)
    customer1.withdraw_from_account(1002, 2000)
    customer1.transfer_to_account(1002, account2, 2000)
    customer1.remove_account(1002)
    customer1.remove_account(1001)
    account.deactivated_account()
    account.activated_account()
    customer1.remove_account(1001)
    customer1.deactivate_account(1001)
    customer1.activate_account(1001)
    customer1.deactivate_account(1001)

    customer1.deposit_to_account(1001, 5000)


    customer1.withdraw_from_account(1001, 2000)
    account1.activated_account()
    destination_account.activated_account()
    destination_account.deactivated_account()
    customer1.transfer_to_account(1001, destination_account, 1000)
    customer1.transfer_to_account(1001, account1, 1000)
    account1.activated_account()
    destination_account.activated_account()
    customer1.transfer_to_account(1001, destination_account, -1000)
    customer1.transfer_to_account(1001, destination_account, 0)
    customer1.transfer_to_account(1001, destination_account, 10000)
    customer1.transfer_to_account(1001, destination_account, 1000)
    customer1.transfer_to_account(1001, destination_account, 1000)
    print("Sender balance after transfer:", account1.balance)
    print("Recipient balance after transfer:", destination_account.balance)
    customer1.display_account_balance(1001)
    customer1.display_account_balance(9999)
    customer1.display_accounts()
    Customer(3, "Test User", "test@example.com", "08099992410").display_accounts()
    print("Customer account count: ", customer1.get_account_count())

    empty_customer = Customer(
        3,
        "Test User",
        "test@example.com",
        "08099992410"
    )
    print("Empty customer account count: ", empty_customer.get_account_count())
    customer1.display_account_count()
    empty_customer.display_account_count()

    found_account = customer1.find_account(1001)

    if found_account is not None:
        print(f"Account found:", found_account.account_number)
    else:
        print("Account not found.")

    missing_account = customer1.find_account(9999)

    if missing_account is not None:
        print("Account found:", missing_account.account_number)
    else:
        print("Account not found.")

    customer1.deactivate_account(1001)
    customer1.remove_account(1001)

    print("Accounts after removal:", customer1.get_account_count())


    test_customer = Customer(
        4,
        "Test Customer",
        "customer@example.com",
        "08012345678"
    )

    test_account = BankAccount(4001, "savings", 5000)
    test_customer.add_account(test_account)

    test_customer.remove_account(4001)

    print(
        "Account count after attempted removal:",
        test_customer.get_account_count()
    )


    test_customer.deactivate_account(4001)
    test_customer.remove_account(4001)

    print(
        "Account count after deactivation and removal:",
        test_customer.get_account_count()
    )
    customer1.deposit_to_account(9999, 1000)
    customer1.withdraw_from_account(9999, 1000)

    test_customer2 = Customer(
        5,
        "Deposit Test Customer",
        "deposit@example.com",
        "08011111111"
    )

    test_account2 = BankAccount(5001, "savings", 5000)
    test_customer2.add_account(test_account2)

    test_customer2.deactivate_account(5001)
    test_customer2.deposit_to_account(5001, 1000)

    test_customer2.withdraw_from_account(5001, 1000)

    destination_test_account = BankAccount(5002, "savings", 3000)
    destination_test_account.activated_account()

    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        1000
    )


    test_customer2.activate_account(5001)
    destination_test_account.deactivated_account()

    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        1000
    )

    print(
        "Sender balance after rejected transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected transfer:",
        destination_test_account.balance
    )




    destination_test_account.activated_account()

    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        1000
    )

    print(
        "Sender balance after successful transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after successful transfer:",
        destination_test_account.balance
    )

    print( "Customer total balance after transfer:", test_customer2.get_total_balance() )



    test_customer2.deposit_to_account(5001, 2000)

    print(
        "Customer total balance after deposit:",
        test_customer2.get_total_balance()
    )


    test_customer2.withdraw_from_account(5001, 1500)

    print(
        "Customer total balance after withdrawal:",
        test_customer2.get_total_balance()
    )



    test_customer2.withdraw_from_account(5001, 10000)

    print(
        "Balance after rejected withdrawal:",
        test_customer2.find_account(5001).balance
    )




    test_customer2.deposit_to_account(5001, -2000)

    print(
        "Balance after rejected negative deposit:",
        test_customer2.find_account(5001).balance
    )




    test_customer2.deposit_to_account(5001, 0)

    print(
        "Balance after rejected zero deposit:",
        test_customer2.find_account(5001).balance
    )



    test_customer2.withdraw_from_account(5001, -1000)

    print(
        "Balance after rejected negative withdrawal:",
        test_customer2.find_account(5001).balance
    )


    test_customer2.withdraw_from_account(5001, 0)

    print(
        "Balance after rejected zero withdrawal:",
        test_customer2.find_account(5001).balance
    )


    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        0
    )

    print(
        "Sender balance after rejected zero transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected zero transfer:",
        destination_test_account.balance
    )


    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        -1000
    )

    print(
        "Sender balance after rejected negative transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected negative transfer:",
        destination_test_account.balance
    )



    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        10000
    )

    print(
        "Sender balance after rejected excessive transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected excessive transfer:",
        destination_test_account.balance
    )



    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        4500
    )

    print(
        "Sender balance after full-balance transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after full-balance transfer:",
        destination_test_account.balance
    )


    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        1000
    )

    print(
        "Sender balance after rejected transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected transfer:",
        destination_test_account.balance
    )



    test_customer2.deposit_to_account(5001, 2000)

    print(
        "Sender balance after deposit:",
        test_customer2.find_account(5001).balance
    )

    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        1000
    )

    print(
        "Sender balance after new transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after new transfer:",
        destination_test_account.balance
    )



    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        1000
    )

    print(
        "Sender balance after final transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after final transfer:",
        destination_test_account.balance
    )




    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        1
    )

    print(
        "Sender balance after rejected transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected transfer:",
        destination_test_account.balance
    )


    test_customer2.transfer_to_account(
        9999,
        destination_test_account,
        1000
    )

    print(
        "Recipient balance after rejected transfer:",
        destination_test_account.balance
    )

    destination_test_account.deactivated_account()

    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        500
    )

    print(
        "Sender balance after rejected transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected transfer:",
        destination_test_account.balance
    )


    destination_test_account.deactivated_account()

    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        500
    )

    print(
        "Sender balance after rejected transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected transfer:",
        destination_test_account.balance
    )


    destination_test_account.activated_account()

    test_customer2.deposit_to_account(5001, 1000)

    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        500
    )

    print(
        "Sender balance after successful transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after successful transfer:",
        destination_test_account.balance
    )




    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        501
    )

    print(
        "Sender balance after rejected transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected transfer:",
        destination_test_account.balance
    )


    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        500
    )

    print(
        "Sender balance after exact-balance transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after exact-balance transfer:",
        destination_test_account.balance
    )

    test_customer2.deposit_to_account(5001, 2000)

    print(
        "Sender balance after new deposit:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after sender deposit:",
        destination_test_account.balance
    )


    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        1500
    )

    print(
        "Sender balance after transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after transfer:",
        destination_test_account.balance
    )


    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        501
    )

    print(
        "Sender balance after rejected transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected transfer:",
        destination_test_account.balance
    )

    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        500
    )

    print(
        "Sender balance after exact-balance transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after exact-balance transfer:",
        destination_test_account.balance
    )


    test_customer2.transfer_to_account(
        5001,
        destination_test_account,
        1
    )

    print(
        "Sender balance after rejected transfer:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after rejected transfer:",
        destination_test_account.balance
    )


    test_customer2.deposit_to_account(5001, 1000)

    print(
        "Sender balance after new deposit:",
        test_customer2.find_account(5001).balance
    )

    print(
        "Recipient balance after sender deposit:",
        destination_test_account.balance
    )

    customer1 = Customer(1, "Anwar", "anwar@example.com", "08012345678")
    print("Valid customer ID:", customer1.customer_id)

    # customer2 = Customer(0, "Anwar", "anwar@example.com", "08012345678")
    # customer3 = Customer(3, "", "anwar@example.com", "08012345678")

    # customer4 = Customer(4, "Anwar", "", "08012345678")

    # customer5 = Customer(5, "Anwar", "anwar.com", "08012345678")
    # customer6 = Customer(6, "Anwar", "anwar@example.com", "")
    # customer7 = Customer(7, "Anwar", "anwar@example.com", "12345")
    # customer8 = Customer(8, "Anwar", "anwar@example.com", "08012345678")
    # print("Valid customer phone:", customer8.phone)
    # customer9 = Customer(9, "Anwar", "anwar@gmail.com", 8012345678)
    customer10 = Customer(10, "Anwar", "anwar@example.com", "08012345678")
    print("Customer created successfully:", customer10.name)

    # Step 25: Test adding an account to a customer

    customer11 = Customer(
        11,
        "Test Customer",
        "test@example.com",
        "08012345678"
    )

    account11 = BankAccount(1011, "savings", 5000)

    customer11.add_account(account11)

    print("Customer accounts:", len(customer11.accounts))
    print("Account number:", customer11.accounts[0].account_number)

    account11 = BankAccount(1011, "savings", 5000)


    customer11.add_account(account11)
    customer11.add_account(account11)

    print(
        "Customer accounts after duplicate test:",
        len(customer11.accounts)
    )


    # Part 54: Test insufficient transfer balance

    print("\n--- Part 54: Insufficient Transfer Balance ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 499

        print("Sender balance before transfer:", sender_account.balance)
        print("Recipient balance before transfer:", destination_test_account.balance)

        test_customer2.transfer_to_account(
            5001,
            destination_test_account,
            500
        )

        print("Sender balance after transfer:", sender_account.balance)
        print("Recipient balance after transfer:", destination_test_account.balance)


    # Part 55: Test transfer to a nonexistent account

    print("\n--- Part 55: Nonexistent Recipient Account ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 1000

        recipient_before = destination_test_account.balance

        test_customer2.transfer_to_account(
            9999,
            destination_test_account,
            500
        )

        print("Sender balance after rejected transfer:", sender_account.balance)
        print("Recipient balance after rejected transfer:", destination_test_account.balance)

    # Part 56: Test successful customer transfer

    print("\n--- Part 56: Successful Customer Transfer ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 2000

        sender_before = sender_account.balance
        recipient_before = destination_test_account.balance

        test_customer2.transfer_to_account(
            5001,
            destination_test_account,
            500
        )

        print("Sender balance before:", sender_before)
        print("Sender balance after:", sender_account.balance)
        print("Recipient balance before:", recipient_before)
        print("Recipient balance after:", destination_test_account.balance)


    # Part 57: Verify total balance before and after transfer

    print("\n--- Part 57: Total Balance Verification ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 2000
        destination_test_account.balance = 3000

        total_before = (
            sender_account.balance
            + destination_test_account.balance
        )

        test_customer2.transfer_to_account(
            5001,
            destination_test_account,
            500
        )

        total_after = (
            sender_account.balance
            + destination_test_account.balance
        )

        print("Total before transfer:", total_before)
        print("Total after transfer:", total_after)
        print("Total preserved:", total_before == total_after)


    # Part 58: Reject transfer to the same account

    print("\n--- Part 58: Transfer to Same Account ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 2000

        balance_before = sender_account.balance

        test_customer2.transfer_to_account(
            5001,
            sender_account,
            500
        )

        print("Balance before transfer:", balance_before)
        print("Balance after transfer:", sender_account.balance)
        print("Balance unchanged:", balance_before == sender_account.balance)


    # Part 59: Reject transfer from an inactive sender account

    print("\n--- Part 59: Transfer from Inactive Sender ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 2000
        sender_account.is_active = False
        destination_test_account.balance = 3000

        sender_balance_before = sender_account.balance
        recipient_balance_before = destination_test_account.balance

        test_customer2.transfer_to_account(
            5001,
            destination_test_account,
            500
        )

        print("Sender balance before:", sender_balance_before)
        print("Sender balance after:", sender_account.balance)
        print("Recipient balance before:", recipient_balance_before)
        print("Recipient balance after:", destination_test_account.balance)

        # Restore the sender account for future tests
        sender_account.is_active = True


    # Part 60: Reject transfer to an inactive recipient

    print("\n--- Part 60: Transfer to Inactive Recipient ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 2000
        sender_account.is_active = True

        destination_test_account.balance = 3000
        destination_test_account.is_active = False

        sender_balance_before = sender_account.balance
        recipient_balance_before = destination_test_account.balance

        test_customer2.transfer_to_account(
            5001,
            destination_test_account,
            500
        )

        print("Sender balance before:", sender_balance_before)
        print("Sender balance after:", sender_account.balance)
        print("Recipient balance before:", recipient_balance_before)
        print("Recipient balance after:", destination_test_account.balance)

        # Restore the recipient account for future tests
        destination_test_account.is_active = True


    # Part 61: Reject a zero-amount transfer

    print("\n--- Part 61: Zero-Amount Transfer ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 2000
        sender_account.is_active = True

        destination_test_account.balance = 3000
        destination_test_account.is_active = True

        sender_balance_before = sender_account.balance
        recipient_balance_before = destination_test_account.balance

        test_customer2.transfer_to_account(
            5001,
            destination_test_account,
            0
        )

        print("Sender balance before:", sender_balance_before)
        print("Sender balance after:", sender_account.balance)
        print("Recipient balance before:", recipient_balance_before)
        print("Recipient balance after:", destination_test_account.balance)

    # Part 62: Reject a negative transfer amount

    print("\n--- Part 62: Negative-Amount Transfer ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 2000
        sender_account.is_active = True

        destination_test_account.balance = 3000
        destination_test_account.is_active = True

        sender_balance_before = sender_account.balance
        recipient_balance_before = destination_test_account.balance

        test_customer2.transfer_to_account(
            5001,
            destination_test_account,
            -500
        )

        print("Sender balance before:", sender_balance_before)
        print("Sender balance after:", sender_account.balance)
        print("Recipient balance before:", recipient_balance_before)
        print("Recipient balance after:", destination_test_account.balance)


    # Part 63: Reject a transfer exceeding the balance

    print("\n--- Part 63: Excessive Transfer Amount ---")

    sender_account = test_customer2.find_account(5001)

    if sender_account is not None:
        sender_account.balance = 2000
        sender_account.is_active = True

        destination_test_account.balance = 3000
        destination_test_account.is_active = True

        sender_balance_before = sender_account.balance
        recipient_balance_before = destination_test_account.balance

        test_customer2.transfer_to_account(
            5001,
            destination_test_account,
            2500
        )

        print("Sender balance before:", sender_balance_before)
        print("Sender balance after:", sender_account.balance)
        print("Recipient balance before:", recipient_balance_before)
        print("Recipient balance after:", destination_test_account.balance)
