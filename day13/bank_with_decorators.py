import functools
from datetime import datetime
from pprint import pprint

from client import Client


class NotEnoughFundsError(Exception):
    pass


class WithdrawalLimitExceeded(Exception):
    pass


class InvalidTransactionType(Exception):
    pass


class Transaction:
    WITHDRAWAL = 0
    DEPOSIT = 1
    INBOUND_TRANSFER = 2
    OUTBOUND_TRANSFER = 3
    TRANSACTION_TYPES = (WITHDRAWAL, DEPOSIT, INBOUND_TRANSFER, OUTBOUND_TRANSFER)

    def __init__(self, sender, amount, recipient=None, timestamp=None, transaction_type=WITHDRAWAL):
        if timestamp is None:
            self.created = datetime.now()
        else:
            self.created = timestamp
        self.amount = amount
        self.from_account = sender
        self.to = recipient
        self.type = transaction_type

    def __str__(self):
        return f'[{self.type}] {self.created} {self.amount} {self.from_account} {self.to}'

    def __repr__(self):
        return f'[{self.type}] {self.created} {self.amount} {self.from_account} {self.to}'


def log_transactions(transaction_type=None):
    def log_transaction(func):
        """Sleep 1 second before calling the function"""

        @functools.wraps(func)
        def wrapper_log_transaction(*args, **kwargs):
            args[0].transactions_history.append(
                Transaction(*args, transaction_type=transaction_type, **kwargs)
            )
            return func(*args, **kwargs)

        return wrapper_log_transaction

    return log_transaction


class Account:
    accounts_quantity = 0

    def __init__(self, client, initial_balance, monthly_withdrawal_limit=1000):
        Account.accounts_quantity += 1
        self.id = Account.accounts_quantity
        self.client = client
        self.balance = initial_balance
        self.monthly_withdrawal_limit = monthly_withdrawal_limit
        self.remaining_withdrawal_limit = self.monthly_withdrawal_limit
        self.transactions_history = []

    @log_transactions(transaction_type=Transaction.DEPOSIT)
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def __validate_withdrawal_limit(self, amount):
        remaining_limit = self.remaining_withdrawal_limit - amount
        if remaining_limit >= 0:
            return remaining_limit
        raise WithdrawalLimitExceeded("Monthly withdrawal limit has got exceeded!")

    @log_transactions(transaction_type=Transaction.WITHDRAWAL)
    def withdraw(self, amount):
        remaining_limit = self.__validate_withdrawal_limit(amount)
        if remaining_limit >= 0 and amount <= self.balance:
            self.balance -= amount
            self.remaining_withdrawal_limit = remaining_limit
        else:
            raise NotEnoughFundsError("Not enough funds to withdraw")
        return self.balance

    @log_transactions(transaction_type=Transaction.OUTBOUND_TRANSFER)
    def transfer(self, to, amount):
        self.withdraw(amount)
        to.deposit(amount)

    def increase_withdrawal_limit(self, new_limit):
        # 2000 limitu, remaining_withdrawal_limit = 2000?
        self.monthly_withdrawal_limit = new_limit
        self.remaining_withdrawal_limit = self.monthly_withdrawal_limit

    def __str__(self):
        return f'{self.client.client_id} {self.client.firstname} {self.client.lastname}'


if __name__ == '__main__':
    kowalski = Client("Jan", "Kowalski", 123456789)
    nowak = Client("Jan", "nowak", 123123)
    bank_account = Account(kowalski, 1500)
    bank_account2 = Account(nowak, 500)
    # print(bank_account.balance)
    # print(bank_account2.balance)
    bank_account.transfer(bank_account2, 300)
    bank_account2.transfer(bank_account, 100)
    # print(bank_account.balance)
    # print(bank_account2.balance)
    pprint(bank_account.transactions_history)
    pprint(bank_account2.transactions_history)
