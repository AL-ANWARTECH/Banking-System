
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


    def test_transfer_preserves_total_balance(self):
        total_before = (
            self.sender.balance + self.recipient.balance
        )

        self.customer.transfer_to_account(
            5001,
            self.recipient,
            500
        )

        total_after = (
            self.sender.balance + self.recipient.balance
        )

        self.assertEqual(total_before, total_after)


    def test_invalid_recipient_object(self):
        sender_balance_before = self.sender.balance
        recipient_balance_before = self.recipient.balance

        with self.assertRaises(TypeError):
            self.customer.transfer_to_account(
                5001,
                "not a bank account",
                500
            )

        self.assertEqual(
            self.sender.balance,
            sender_balance_before
        )

        self.assertEqual(
            self.recipient.balance,
            recipient_balance_before
        )



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


    def test_string_transfer_amount(self):
        sender_balance_before = self.sender.balance
        recipient_balance_before = self.recipient.balance

        with self.assertRaises(TypeError):
            self.customer.transfer_to_account(
                5001,
                self.recipient,
                "500"
            )

        self.assertEqual(
            self.sender.balance,
            sender_balance_before
        )
        self.assertEqual(
            self.recipient.balance,
            recipient_balance_before
        )

    def test_boolean_transfer_amount(self):
        sender_balance_before = self.sender.balance
        recipient_balance_before = self.recipient.balance

        with self.assertRaises(TypeError):
            self.customer.transfer_to_account(
                5001,
                self.recipient,
                True
            )

        self.assertEqual(
            self.sender.balance,
            sender_balance_before
        )
        self.assertEqual(
            self.recipient.balance,
            recipient_balance_before
        )


if __name__ == "__main__":
    unittest.main()
