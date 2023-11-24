import datetime
class Account:
    def __init__(self, account_number, account_name, initial_balance=0, status="Active"):
        self.account_number = account_number
        self.account_name = account_name
        self.balance_amount = initial_balance
        self.status = status
        self.transaction_history = []

    def display_details(self):
        print("Account Number:", self.account_number)
        print("Account Name:", self.account_name)
        print("Balance Amount:", self.balance_amount)
        print("Account Status:", self.status)

    def deposit(self, amount):
        if amount > 0:
            self.balance_amount += amount
            self._add_transaction("Deposit", amount)
            print(f"Deposit successful. New balance: {self.balance_amount}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance_amount:
            self.balance_amount -= amount
            self._add_transaction("Withdrawal", amount)
            print(f"Withdrawal successful. New balance: {self.balance_amount}")
        else:
            print("Invalid withdrawal amount. Please check your balance and try again.")

    def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def _add_transaction(self, transaction_type, amount):
        # Use a simple timestamp string
        timestamp = self._get_timestamp()
        transaction_details = {
            "Type": transaction_type,
            "Amount": amount,
            "Date": timestamp
        }
        self.transaction_history.append(transaction_details)
        if len(self.transaction_history) > 5:
            self.transaction_history.pop(0)

    def _get_timestamp(self):
        # A simple timestamp string (you can customize this based on your needs)
        return "YYYY-MM-DD HH:MM:SS"



        

class Account:
    def __init__(self, account_number, account_name, initial_balance=0, status="Active"):
        self.account_number = account_number
        self.account_name = account_name
        self.balance_amount = initial_balance
        self.status = status
        self.transaction_history = []

    def display_details(self):
        print("Account Number:", self.account_number)
        print("Account Name:", self.account_name)
        print("Balance Amount:", self.balance_amount)
        print("Account Status:", self.status)

    def deposit(self, amount):
        if amount > 0:
            self.balance_amount += amount
            self._add_transaction("Deposit", amount)
            print(f"Deposit successful. New balance: {self.balance_amount}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance_amount:
            self.balance_amount -= amount
            self._add_transaction("Withdrawal", amount)
            print(f"Withdrawal successful. New balance: {self.balance_amount}")
        else:
            print("Invalid withdrawal amount. Please check your balance and try again.")

    def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def _add_transaction(self, transaction_type, amount):
        # Use a simple timestamp string
        timestamp = self._get_timestamp()
        transaction_details = {
            "Type": transaction_type,
            "Amount": amount,
            "Date": timestamp
        }
        self.transaction_history.append(transaction_details)
        if len(self.transaction_history) > 5:
            self.transaction_history.pop(0)

    def _get_timestamp(self):
    # Get the current date and time
        now = datetime.datetime.now()
        # Format the date and time
        return now.strftime("%Y-%m-%d %H:%M:%S")    
    


def main():
    # Create an account
    account_number = input("Enter Account Number: ")
    account_name = input("Enter Account Name: ")
    initial_balance = float(input("Enter Initial Balance: "))
    account = Account(account_number, account_name, initial_balance)

    # Display account details
    print("\nAccount Details:")
    account.display_details()

    # Deposit an amount
    deposit_amount = float(input("\nEnter the deposit amount: "))
    account.deposit(deposit_amount)

    # Withdraw an amount
    withdrawal_amount = float(input("\nEnter the withdrawal amount: "))
    account.withdraw(withdrawal_amount)

    # Display transaction history
    account.display_transaction_history()

if __name__ == "__main__":
    main()











