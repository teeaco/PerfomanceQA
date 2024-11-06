def get_balance(name, transactions):
    balance = 0
    for transaction in transactions:
        if transaction["name"] == name:
            balance += transaction["amount"]
    return balance

def count_debts(names, amount, transactions):
    debts = {}
    for name in names:
        balance = get_balance(name, transactions)
        debt = amount - balance if balance < amount else 0
        debts[name] = debt
    return debts


transactions = [
    {"name": "Василий", "amount": 500},
    {"name": "Петя", "amount": 100},
    {"name": "Василий", "amount": -300},
]


