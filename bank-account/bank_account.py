import time
import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.active = False
        self._lock = threading.Lock()

    def get_balance(self):
        if not self.active:
            raise ValueError('Account closed')
        return self.balance

    def open(self):
        if self.active:
            raise ValueError('Account already opened')
        self.active = True

    def deposit(self, amount):
        if not self.active:
            raise ValueError('Account is still closed')
        if amount < 0:
            raise ValueError('Cannot deposit negative value')
        with self._lock:
            self.balance += amount

    def withdraw(self, amount):
        if amount < 0 or amount > self.balance:
            raise ValueError('Withdrawal amount is exceeding savings')
        with self._lock:
            self.balance -= amount

    def close(self):
        if not self.active:
            raise ValueError('Account already closed')
        self.active = False
        self.balance = 0