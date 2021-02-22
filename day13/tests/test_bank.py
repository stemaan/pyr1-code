from unittest import TestCase

from bank import Account, NotEnoughFundsError, WithdrawalLimitExceeded
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

    def test_withdraw_raises_not_enough_funds_error(self):
        to_withdraw = 600
        self.assertRaises(NotEnoughFundsError, self.account2.withdraw, to_withdraw)

    def test_withdraw_raises_withdrawal_limit_exceeded_error(self):
        to_withdraw = 1100
        self.assertRaises(WithdrawalLimitExceeded, self.account1.withdraw, to_withdraw)

    def test_transfer_ok(self):
        to_transfer = 900
        account1_balance_before = self.account1.balance
        account2_balance_before = self.account2.balance

        self.account1.transfer(self.account2, to_transfer)

        expected_acctount1_balance = account1_balance_before - to_transfer
        self.assertEqual(self.account1.balance, expected_acctount1_balance)

        expected_acctount2_balance = account2_balance_before + to_transfer
        self.assertEqual(self.account2.balance, expected_acctount2_balance)

    def test_transfer_raises_not_enough_funds_error(self):
        to_transfer = 600
        self.assertRaises(NotEnoughFundsError, self.account2.transfer, self.account1, to_transfer)

    def test_increase_withdrawal_limit_ok(self):
        previous_limit = self.account1.monthly_withdrawal_limit
        new_limit = 2000
        self.account1.increase_withdrawal_limit(new_limit)
        self.assertNotEqual(previous_limit, self.account1.monthly_withdrawal_limit)
        self.assertEqual(self.account1.monthly_withdrawal_limit, new_limit)

    def test_increase_withdrawal_limit_bug_on_production(self):
        to_withdraw = 500
        balance_before_withdraw = self.account1.balance
        self.account1.withdraw(to_withdraw)

        expected = balance_before_withdraw - to_withdraw
        self.assertEqual(expected, self.account1.balance)

        self.account1.increase_withdrawal_limit(2000)
        # FIXME: remaining_withdrawal_limit nie resetuje sie po zmianie limitu!
        to_withdraw = 600
        balance_before_withdraw = self.account1.balance
        self.account1.withdraw(to_withdraw)

        expected = balance_before_withdraw - to_withdraw
        self.assertEqual(expected, self.account1.balance)

