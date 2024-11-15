class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def add(self):
        add= int(input("Введите сумму которую хотите добавить на баланс:"))
        self.balance += add
        print(f"На ваш баланс зачисленна сумма: {add}") 
        print(f"теперь на вашем счену находится:{self.balance}")
    def withdraw(self):
        minus = int(input("введите сумму которую хотите снять: "))
        if minus < self.balance:
            self.balance -= minus
            print(f"С вашего баланса снята сумма: {minus}")
            print(f"Теперь на вашем балансе: {self.balance}")
        else:
            print("На балансе недостаточно средств")

maks = BankAccount(4444444444444444, 15000)
maks.add()
maks.withdraw()

