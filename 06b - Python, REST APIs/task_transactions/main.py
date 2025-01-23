import json
import os
from datetime import datetime

TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
  try:
    with open(TRANSACTIONS_FILE, "r") as f:
      return json.load(f)
  except FileNotFoundError:
    return []

def save_transactions(transactions):
  with open(TRANSACTIONS_FILE, "w") as f:
    json.dump(transactions, f, indent=2)

def add_transaction():
  try:
    type = input("Enter transaction type (income/expense): ").lower()
    if type not in ("income", "expense"):
      raise ValueError("Invalid transaction type.")

    amount = float(input("Enter transaction amount: "))
    if amount <= 0:
      raise ValueError("Amount must be positive.")

    category = input("Enter transaction category: ")

    date_str = input("Enter transaction date (YYYY-MM-DD): ")
    datetime.strptime(date_str, "%Y-%m-%d") # Validate date format

    transactions = load_transactions()
    transactions.append({
      "type": type,
      "amount": amount,
      "category": category,
      "date": date_str
    })
    save_transactions(transactions)
    print("Transaction added successfully.")

  except ValueError as e:
    print(f"Error: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def view_transactions():
  transactions = load_transactions()
  if not transactions:
    print("No transactions found.")
    return

  for i, transaction in enumerate(transactions):
    print(f"\nTransaction {i+1}:")
    for key, value in transaction.items():
      print(f"  {key.capitalize()}: {value}") # Indentation for key-value pairs

def generate_summary():
  transactions = load_transactions()
  if not transactions:
    print("No transactions found. Cannot generate summary.")
    return

  total_income = 0
  total_expenses = 0

  for transaction in transactions:
    if transaction["type"] == "income":
      total_income += transaction["amount"]
    elif transaction["type"] == "expense":
      total_expenses += transaction["amount"]

  balance = total_income - total_expenses

  print("\nFinancial Summary:")
  print(f"  Total Income: {total_income}") # Indentation for summary items
  print(f"  Total Expenses: {total_expenses}")
  print(f"  Balance: {balance}")

def main():
  while True:
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Generate Financial Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      add_transaction()
    elif choice == "2":
      view_transactions()
    elif choice == "3":
      generate_summary()
    elif choice == "4":
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()