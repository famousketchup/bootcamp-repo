class BankAccount:
  def __init__(self, account_number, initial_balance=0):
    self.account_number = account_number
    self.balance = initial_balance
    self.is_active = True

  def balance_check(self):
    if self.is_active:
      return self.balance
    else:
      return "Account is closed."

  def deposit(self, amount):
    if self.is_active:
      if amount > 0:
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
      else:
        return "Invalid deposit amount."
    else:
      return "Account is closed."

  def withdraw(self, amount):
    if self.is_active:
      if amount > 0 and amount <= self.balance:
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
      elif amount <= 0:
        return "Invalid withdrawal amount."
      else:
        return "Insufficient funds."
    else:
      return "Account is closed."

  def close_account(self):
    if self.is_active:
      self.is_active = False
      return "Account closed successfully."
    else:
      return "Account is already closed."


def main():
  account_number = input("Enter your account number: ")
  try:
    initial_balance = float(input("Enter initial balance (or 0): "))
  except ValueError:
    print("Invalid input. Setting initial balance to 0.")
    initial_balance = 0

  account = BankAccount(account_number, initial_balance)

  while True:
    print("\nChoose an action:")
    print("1. Balance check")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Close account")
    print("5. Exit")

    choice = input("> ")

    try:
      choice = int(choice)
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    if choice == 1:
      print(account.balance_check())
    elif choice == 2:
      try:
        amount = float(input("Enter deposit amount: "))
        print(account.deposit(amount))
      except ValueError:
        print("Invalid amount")
    elif choice == 3:
      try:
        amount = float(input("Enter withdrawal amount: "))
        print(account.withdraw(amount))
      except ValueError:
        print("Invalid Amount")
    elif choice == 4:
      print(account.close_account())
      if not account.is_active:
        break  # exit loop if account is closed
    elif choice == 5:
      break
    else:
      print("Invalid choice. Please try again.")

main()