import unittest

from models.account import BankAccount


class TestBankAccountDeposit(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(9001, "savings", 1000)

    def test_successful_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_zero_deposit_does_not_change_balance(self):
        self.account.deposit(0)
        self.assertEqual(self.account.balance, 1000)

    def test_negative_deposit_does_not_change_balance(self):
        self.account.deposit(-200)
        self.assertEqual(self.account.balance, 1000)

    def test_string_deposit_is_rejected(self):
        with self.assertRaises(TypeError):
            self.account.deposit("hello")

        self.assertEqual(self.account.balance, 1000)

    def test_boolean_deposit_is_rejected(self):
        with self.assertRaises(TypeError):
            self.account.deposit(True)

        self.assertEqual(self.account.balance, 1000)

    def test_nan_deposit_is_rejected(self):
        with self.assertRaises(ValueError):
            self.account.deposit(float("nan"))

        self.assertEqual(self.account.balance, 1000)

    def test_infinite_deposit_is_rejected(self):
        with self.assertRaises(ValueError):
            self.account.deposit(float("inf"))

        self.assertEqual(self.account.balance, 1000)


if __name__ == "__main__":
    unittest.main()
