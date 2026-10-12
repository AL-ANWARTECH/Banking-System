import unittest

from models.account import BankAccount


class TestBankAccountWithdraw(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(9012, "savings", 1000)

    def test_successful_withdrawal(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)

    def test_zero_withdrawal_does_not_change_balance(self):
        self.account.withdraw(0)
        self.assertEqual(self.account.balance, 1000)

    def test_negative_withdrawal_does_not_change_balance(self):
        self.account.withdraw(-200)
        self.assertEqual(self.account.balance, 1000)

    def test_insufficient_balance(self):
        self.account.withdraw(1500)
        self.assertEqual(self.account.balance, 1000)

    def test_string_withdrawal_is_rejected(self):
        with self.assertRaises(TypeError):
            self.account.withdraw("hello")

        self.assertEqual(self.account.balance, 1000)

    def test_boolean_withdrawal_is_rejected(self):
        with self.assertRaises(TypeError):
            self.account.withdraw(True)

        self.assertEqual(self.account.balance, 1000)

    def test_nan_withdrawal_is_rejected(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(float("nan"))

        self.assertEqual(self.account.balance, 1000)

    def test_infinite_withdrawal_is_rejected(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(float("inf"))

        self.assertEqual(self.account.balance, 1000)

    def test_inactive_account_withdrawal_is_rejected(self):
        self.account.deactivated_account()
        self.account.withdraw(300)

        self.assertEqual(self.account.balance, 1000)


if __name__ == "__main__":
    unittest.main()