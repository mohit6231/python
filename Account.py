from abc import ABC, abstractmethod

# Abstract Base Class (Abstraction)


class Account(ABC):
    def __init__(self, owner, balance=0):
        self._owner = owner        # Encapsulation (private attribute)
        self._balance = balance    # Encapsulation (private attribute)

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __str__(self):
        return f"Account(owner={self._owner}, balance={self._balance})"

# Savings Account Class (Inheritance)


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        # Encapsulation (private attribute)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    def apply_interest(self):
        self._balance += self._balance * self._interest_rate

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid amount")

    def __str__(self):
        return f"SavingsAccount(owner={self._owner}, balance={self._balance}, interest_rate={self._interest_rate})"

# Checking Account Class (Inheritance)


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        # Encapsulation (private attribute)
        self._overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and self._balance - amount >= -self._overdraft_limit:
            self._balance -= amount
        else:
            raise ValueError("Overdraft limit exceeded or invalid amount")

    def __str__(self):
        return f"CheckingAccount(owner={self._owner}, balance={self._balance}, overdraft_limit={self._overdraft_limit})"

# Polymorphism: Function accepting any Account type


def print_account_details(account):
    print(account)


# Main Execution
if __name__ == "__main__":
    # Create accounts
    savings = SavingsAccount("Alice", 1000, 0.02)
    checking = CheckingAccount("Bob", 500)

    # Deposit
    savings.deposit(500)
    checking.deposit(200)

    # Withdraw
    savings.withdraw(300)
    checking.withdraw(600)

    # Apply interest (specific to SavingsAccount)
    savings.apply_interest()

    # Polymorphism in action
    print_account_details(savings)
    print_account_details(checking)
