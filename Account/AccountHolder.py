from abc import ABC


class AccountHolder(ABC):
    def __init__(self, id: int, email: str):
        self._id = id
        self._email = email
        self._accounts = list([Account()])

    def add_account(self, account: Account):
        self._accounts.append(account)
