from models import  Expense
from datetime import datetime

def get_user_expenses():
    expenses = []

    while True:
        try:
            amount = float(input("Lütfen harcama miktarini giriniz: "))
            if amount == 0:
                break

            if amount < 0:
                print("Negatif deger girilmez")
                continue
            category = input("Kategori: ").strip()

            if category == "":
                print("Kategori bos birakilamaz.")
                continue
            expense = Expense(amount, category)
            expenses.append(expense)
        except ValueError:
            print("Gecersiz giris. Sayi giriniz")
    return expenses