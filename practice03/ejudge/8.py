class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance

# Чтение входных данных
balance, withdrawal = map(int, input().split())

# Создаём аккаунт (имя можно любое, например "User")
acc = Account("User", balance)

# Пробуем снять деньги и выводим результат
print(acc.withdraw(withdrawal))
