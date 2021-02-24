from client import Client
from datetime import datetime


class NotEnoughFundsError(Exception):
    pass


class WithdrawalLimitExceeded(Exception):
    pass


class Transaction:
    def __init__(self, amount, sender, recipient=None, timestamp=None, transaction_type=None):
        self.amount = amount
        if timestamp is None:
            self.created = datetime.now()
        else:
            self.created = timestamp
        self.type = transaction_type
        self.sender = sender
        self.recipient = recipient

    def __str__(self):
        return f'[{self.type}] {self.created} amount:{self.amount} from: {self.sender} to: {self.recipient}'

    def __repr__(self):
        # __str__() is used for creating output for end user while __repr__() is mainly used for debugging and development.
        # The default implementation is useless (it’s hard to think of one which wouldn’t be, but yeah)
        # __repr__ goal is to be unambiguous
        # __str__ goal is to be readable
        # Container’s (lists, tuples, dictionaries)  __str__ uses contained objects’ __repr__
        return f'[{self.type}] {self.created} amount:{self.amount} from: {self.sender} to: {self.recipient}'


class Account:
    accounts_quantity = 0

    def __init__(self, client, initial_balance, monthly_withdrawal_limit=1000):
        Account.accounts_quantity += 1
        self.id = Account.accounts_quantity
        self.client = client
        self.balance = initial_balance
        self.monthly_withdrawal_limit = monthly_withdrawal_limit
        self.remaining_withdrawal_limit = self.monthly_withdrawal_limit
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(
            Transaction(amount, sender=self, transaction_type='DEPOSIT')
        )
        return self.balance

    def __validate_withdrawal_limit(self, amount):
        remaining_limit = self.remaining_withdrawal_limit - amount
        if remaining_limit >= 0:
            return remaining_limit
        raise WithdrawalLimitExceeded("Monthly withdrawal limit has got exceeded!")

    def withdraw(self, amount):
        remaining_limit = self.__validate_withdrawal_limit(amount)
        if remaining_limit >= 0 and amount <= self.balance:
            self.balance -= amount
            self.remaining_withdrawal_limit = remaining_limit
            self.transaction_history.append(
                Transaction(amount, sender=self, transaction_type='WITHDRAWAL')
            )
        else:
            raise NotEnoughFundsError("Not enough funds to withdraw")
        return self.balance

    def transfer(self, to, amount):
        self.transaction_history.append(
            Transaction(amount, sender=self, recipient=to, transaction_type='OUTBOUND_TRANSFER')
        )
        self.withdraw(amount)
        to.transaction_history.append(
            Transaction(amount, sender=self, recipient=to, transaction_type='INBOUND_TRANSFER')
        )
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
    # print(bank_account.balance)
    # print(bank_account2.balance)
    bank_account.deposit(123)
    bank_account.withdraw(321)
    print(bank_account.transaction_history)
    print(bank_account2.transaction_history)
