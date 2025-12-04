#Adding the Bank Acoount object for performing deposit, withdraw and show
import sys
from bank_account import BankAccunt

account = BankAccunt()

command = sys.argv[1]

if command in ["deposit", "withdraw"]:
    amount = float(sys.argv[2])

if command == "deposit":
    account.deposit(amount)
    account.displa_balance()

elif command == "withdraw":
    success = account.withdraw(amount)
    if success:
        print("Withdrawal successful")
    else:
        print("Insufficient funds")  
    account.display_balance()
elif command == "balance":
    account.display_balance()
else:
    print("Unknown command")