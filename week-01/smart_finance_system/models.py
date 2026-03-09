from datetime import datetime

class Expense():
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category
        self.date = datetime.now()

    def __str__(self):
        return self.amount

class Budget():
    def __init__(self, limit):
        self.limit = limit
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

    def average_expense(self):
        if len(self.expenses) == 0:
            return 0
        return self.total_expense() / len(self.expenses)

    def is_limit_exceeded(self):
        return self.total_expense() > self.limit


