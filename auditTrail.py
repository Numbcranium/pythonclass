#an application where user can manage their bank account and it is saved in an audit trail file. The user can deposit, withdraw, and check their balance. The audit trail will keep track of all transactions made by the user.

def deposit(balance, amount):
    if amount <= 0:
        print("Amount must be greater than 0")
        return balance
    balance += amount
    with open("auditTrail.txt", "a") as file:
        file.write(f"User deposited: #{amount}\nBalance: #{balance}\n")
    return balance

def withdraw(balance,amount):
    if amount > balance:
        print("Insufficient funds")
        return balance
    balance -= amount
    with open("auditTrail.txt", "a") as file:
        file.write(f"User withdrew: #{amount}\nBalance: #{balance}\n")
    return balance

def check_balance(balance):
    with open("auditTrail.txt", "r") as file:
        transactions = file.readlines()
    print(transactions[-1])
    return balance
