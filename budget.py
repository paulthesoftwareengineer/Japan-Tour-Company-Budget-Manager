available = 10000
budgets = {}
expenditure = {}

def add_budget(name, amount):
    global available
    if name in budgets:
        raise ValueError ("Budget exists")
    if amount > available:
        raise ValueError ("Insufficient funds")
    if name not in expenditure:
        raise ValueError ("No such budget")
    budgets[name] = amount
    available -= amount
    expenditure[name] = 0
    return available
  
