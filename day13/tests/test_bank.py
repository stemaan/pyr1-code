from unittest import TestCase

from bank import Account
from client import Client


class AccountTestCase(TestCase):
    def setUp(self):
        # wywolywana przed kazdym testem
        self.client1 = Client("Jan", "Kowalski", 123456789)
        self.client2 = Client("Anna", "Nowak", 987654321)
        self.account1 = Account(self.client1, 1500)
        self.account2 = Account(self.client2, 500)

    def test_deposit_ok(self):
        balance_before = self.account1.balance
        to_deposit = 100

        self.account1.deposit(to_deposit)

        expected = balance_before + to_deposit
        self.assertEqual(expected, self.account1.balance)

    def test_withdraw_ok(self):
        balance_before = self.account1.balance
        to_withdraw = 500

        self.account1.withdraw(to_withdraw)

        expected = balance_before - to_withdraw
        self.assertEqual(expected, self.account1.balance)