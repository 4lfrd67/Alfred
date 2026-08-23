class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.owner = owner
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount

    def __str__(self):
        return f"{self.owner}: {self._balance:.2f}"


# Alfred's Bank Account
account = BankAccount("Alfred", 1500)
print(account)
  
