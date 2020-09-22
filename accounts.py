class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("*" * 80)
        print("Account created for {0} ".format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("*" * 80)
            #print("Amount {} deposited successfully, new balance is {}".format(amount, self.balance))
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("*" * 80)
            #print("Amount {} withdraw successfully, new balance is {}".format(amount, self.balance))
            self.show_balance()
        else:
            print("Amount must be less than or equal to your balance")
            print("*" * 80)
        self.show_balance()

    def show_balance(self):
        print("Balance is {0} ".format(self.balance))
        print("*" * 80)

if __name__ == '__main__':
    Ranjit=Account("Ranjit", 0)
    Ranjit.show_balance()
    Ranjit.deposit(1000)
    Ranjit.withdraw(500)
    Ranjit.show_balance()
