#defining the class for account creation
class BankAccunt:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

#adding a deposit method
def deposit(self, amount):
    self.amount_balance += amount

#Adding the withdrawal method
def withdraw(self, amount):
    if amount <= self.account_balance:
        self.account_balance -= amount
        return True
    else:
        return False
    
#Adding a display method
def display_balance(self):
    print(f"Current balance: ${self.account_balance}")    