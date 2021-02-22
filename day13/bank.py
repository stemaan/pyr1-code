from client import Client


class NotEnoughFundsError(Exception):
    pass


class WithdrawalLimitExceeded(Exception):
    pass


class Account:
    accounts_quantity = 0

    def __init__(self, client, initial_balance, monthly_withdrawal_limit=1000):
        Account.accounts_quantity += 1
        self.id = Account.accounts_quantity
        self.client = client
        self.balance = initial_balance
        self.monthly_withdrawal_limit = monthly_withdrawal_limit
        self.remaining_withdrawal_limit = self.monthly_withdrawal_limit

    def deposit(self, amount):
        self.balance += amount
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
        else:
            raise NotEnoughFundsError("Not enough funds to withdraw")
        return self.balance

    def transfer(self, to, amount):
        self.withdraw(amount)
        to.deposit(amount)


if __name__ == '__main__':
    kowalski = Client("Jan", "Kowalski", 123456789)
    nowak = Client("Jan", "nowak", 123123)
    bank_account = Account(kowalski, 1500)
    bank_account2 = Account(nowak, 500)
    print(bank_account.balance)
    print(bank_account2.balance)
    bank_account.transfer(bank_account2, 300)
    print(bank_account.balance)
    print(bank_account2.balance)

