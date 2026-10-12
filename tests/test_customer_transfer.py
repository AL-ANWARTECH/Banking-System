
import unittest

from models.customer import Customer
from models.account import BankAccount


class TestCustomerTransfer(unittest.TestCase):

    def setUp(self):
        """Create fresh accounts before every test."""

        self.customer = Customer(
            1,
            "Test Customer",
            "test@example.com",
            "08012345678"
        )

        self.sender = BankAccount(
            5001,
            "savings",
            2000
        )

        self.recipient = BankAccount(
            6001,
            "savings",
            3000
        )

        self.customer.add_account(self.sender)

    def test_successful_transfer(self):
        self.customer.transfer_to_account(
            5001,
            self.recipient,
            500
        )

        self.assertEqual(self.sender.balance, 1500)
        self.assertEqual(self.recipient.balance, 3500)

    def test_insufficient_balance(self):
        self.customer.transfer_to_account(
            5001,
            self.recipient,
            2500
        )

        self.assertEqual(self.sender.balance, 2000)
        self.assertEqual(self.recipient.balance, 3000)

    def test_transfer_from_inactive_sender(self):
        self.sender.is_active = False

        self.customer.transfer_to_account(
            5001,
            self.recipient,
            500
        )

        self.assertEqual(self.sender.balance, 2000)
        self.assertEqual(self.recipient.balance, 3000)

    def test_transfer_to_inactive_recipient(self):
        self.recipient.is_active = False

        self.customer.transfer_to_account(
            5001,
            self.recipient,
            500
        )

        self.assertEqual(self.sender.balance, 2000)
        self.assertEqual(self.recipient.balance, 3000)

    def test_zero_amount_transfer(self):
        self.customer.transfer_to_account(
            5001,
            self.recipient,
            0
        )

        self.assertEqual(self.sender.balance, 2000)
        self.assertEqual(self.recipient.balance, 3000)

    def test_negative_amount_transfer(self):
        self.customer.transfer_to_account(
            5001,
            self.recipient,
            -500
        )

        self.assertEqual(self.sender.balance, 2000)
        self.assertEqual(self.recipient.balance, 3000)

    def test_transfer_to_same_account(self):
        self.customer.transfer_to_account(
            5001,
            self.sender,
            500
        )

        self.assertEqual(self.sender.balance, 2000)

    def test_nonexistent_sender_account(self):
        self.customer.transfer_to_account(
            9999,
            self.recipient,
            500
        )

        self.assertEqual(self.recipient.balance, 3000)


if __name__ == "__main__":
    unittest.main()
