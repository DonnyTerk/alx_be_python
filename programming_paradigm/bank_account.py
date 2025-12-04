class BankAccount:
    """
    A class that represents a bank account.
    """
    
    def __init__(self, initial_balance = 0):
        """
        Initialize the bank account with a balance of 0.
        """
        self.balance = 0

    def deposit(self, amount):
        """
        Adds the amount to the balance.
        """
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """
        Subtracts the amount from the balance if funds are sufficient.
        """
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return True
            else:
                print("insufficient funds.")
                return False
                # Depending on requirements, you might need to print an error
                # or just do nothing if funds are insufficient.
        return False
              

    def display_balance(self):
        """
        Prints the current balance.
        """
        print(f"Current Balance: {self.balance:.2f}")