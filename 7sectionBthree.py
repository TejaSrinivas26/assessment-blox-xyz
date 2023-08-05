import requests

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsError

    def transfer(self, to_account, amount):
        try:
            with Transaction(self, to_account):
                self.withdraw(amount)
                to_account.deposit(amount)
        except InsufficientFundsError as e:
            print("Transaction failed: Insufficient funds.")
        except Exception as e:
            print("Transaction failed:", str(e))

class Transaction:
    def __init__(self, from_account, to_account):
        self.from_account = from_account
        self.to_account = to_account

    def __enter__(self):
        # Start transaction
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            # Rollback transaction on exception
            self.from_account.rollback()
            self.to_account.rollback()
        else:
            # Commit transaction on success
            self.from_account.commit()
            self.to_account.commit()

class InsufficientFundsError(Exception):
    pass

if __name__ == "__main__":
    # Create two bank accounts
    account_a = BankAccount("123456789", 10000)
    account_b = BankAccount("987654321", 0)

    # Transfer 5000 from account A to account B
    account_a.transfer(account_b, 5000)

    print("Account A balance:", account_a.balance)
    print("Account B balance:", account_b.balance)

    # Additional transactions
    # Deposit 3000 to account A
    account_a.deposit(3000)
    # Withdraw 1000 from account B
    account_b.withdraw(1000)

    print("Account A balance:", account_a.balance)
    print("Account B balance:", account_b.balance)
    
"""In this modified code, we've added a Transaction class that acts as a context manager (with statement). 
The __enter__ method is empty, and the __exit__ method handles the transaction behavior. If any exception 
occurs during the transaction, it will be caught in the __exit__ method, and a rollback will be performed 
by calling rollback() on each account involved in the transaction. Otherwise, if the transaction is successful,
it will be committed by calling commit() on each account. The rollback() and commit() methods are not defined 
in the code provided, but you can implement them in the BankAccount class as per your specific requirements."""




# import requests

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             raise InsufficientFundsError

#     def transfer(self, to_account, amount):
#         self.withdraw(amount)
#         to_account.deposit(amount)

# class InsufficientFundsError(Exception):
#     pass

# if __name__ == "__main__":
#     # Create two bank accounts
#     account_a = BankAccount("123456789", 10000)
#     account_b = BankAccount("987654321", 0)

#     # Transfer 5000 from account A to account B
#     account_a.transfer(account_b, 5000)

#     print("Account A balance:", account_a.balance)
#     print("Account B balance:", account_b.balance)
#     #Account A balance: 5000
#     #Account B balance: 5000

#     # Additional transactions
#     # Deposit 3000 to account A
#     account_a.deposit(3000)
#     # Withdraw 1000 from account B
#     account_b.withdraw(1000)

#     print("Account A balance:", account_a.balance)
#     print("Account B balance:", account_b.balance)
#     #Account A balance: 8000
#     #Account B balance: 4000

"""The provided code defines a simple BankAccount class with three main methods: deposit, withdraw, 
    and transfer. Below is a short explanation of each method:

    deposit(amount): This method is used to deposit a given amount into the bank account. It increases 
    the account balance by the specified amount.

    withdraw(amount): This method is used to withdraw a given amount from the bank account. It checks if 
    the account has sufficient funds (balance greater than or equal to the withdrawal amount) and deducts 
    the amount from the account balance. If there are insufficient funds, it raises an InsufficientFundsError exception.

    transfer(to_account, amount): This method facilitates transferring a given amount from the current 
    account to another bank account (to_account). It uses the withdraw method to reduce the balance of 
    the current account and the deposit method of the target account (to_account) to increase its balance."""


"""Banking works by transferring money from account A to account B. Most of the time
account A is in one bank while account B is another bank. Implement the code to
transfer money. Remember, payee's code runs on a different computer than that of
the receiver's code.
1. What are the issues in such a system?
    Security: The system must be secure to prevent unauthorized access to or modification of financial data.
    Accuracy: The system must be accurate to ensure that the correct amount of money is transferred to the correct account.
    Availability: The system must be available to users at all times, or at least within a reasonable timeframe.
    Scalability: The system must be able to handle a large volume of transactions without performance degradation.

2. What can we do to mitigate some of the issues ?

    Use strong encryption to protect financial data.
    Implement a robust authentication and authorization system to prevent unauthorized access.
    Use checksums or other data validation techniques to ensure the accuracy of transactions.
    Implement a load balancing system to distribute traffic across multiple servers.
    Use a distributed database to store financial data.

3. Write the fixing yourself to demonstrate the mitigations
This code fixes the 'BankAccount' object has no attribute 'transfer' error by defining a 
function called transfer that takes three arguments: the sender's BankAccount object, the 
recipient's BankAccount object, and the amount to transfer. The function first checks if the 
sender has enough money in their account to make the transfer. If they do, the function then 
hashes the transfer request and sends it to the server. If the server returns a successful response, 
the function then updates the balances of the two accounts. Otherwise, the function raises an exception."""


#method2
"""import hashlib
import json
import requests

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        # Check if the sender has enough money in their account.
        balance = get_balance(self.account_number)
        if balance < amount:
            raise InsufficientFundsError

        # Hash the transfer request.
        transfer_request = {
            "account_a_number": self.account_number,
            "account_b_number": account_b.account_number,
            "amount": amount
        }
        transfer_request_hash = hashlib.sha256(json.dumps(transfer_request).encode()).hexdigest()

        # Send the transfer request.
        response = requests.post("https://api.bank.com/transfer", data={
            "transfer_request_hash": transfer_request_hash,
            "transfer_request": json.dumps(transfer_request)
        })

        # Check the response.
        if response.status_code == 200:
            self.balance -= amount
            account_b.balance += amount
        else:
            raise TransferError

class InsufficientFundsError(Exception):
    pass

class TransferError(Exception):
    pass

def transfer(account_a, account_b, amount):
    # Check if the sender has enough money in their account.
    balance = get_balance(account_a.account_number)
    if balance < amount:
        raise InsufficientFundsError

    # Hash the transfer request.
    transfer_request = {
        "account_a_number": account_a.account_number,
        "account_b_number": account_b.account_number,
        "amount": amount
    }
    transfer_request_hash = hashlib.sha256(json.dumps(transfer_request).encode()).hexdigest()

    # Send the transfer request.
    response = requests.post("https://api.bank.com/transfer", data={
        "transfer_request_hash": transfer_request_hash,
        "transfer_request": json.dumps(transfer_request)
    })

    # Check the response.
    if response.status_code == 200:
        account_a.balance -= amount
        account_b.balance += amount
    else:
        raise TransferError

if name == "__main__":
    # Create two bank accounts
    account_a = BankAccount("123456789", 10000)
    account_b = BankAccount("987654321", 0)

    # Transfer 5000 from account A to account B
    try:
        transfer(account_a, account_b, 5000)
    except InsufficientFundsError:
        print("Insufficient funds in account A")
    except TransferError:
        print("Transfer failed")
    else:
        print("Transfer successful")

    print("Account A balance:", account_a.balance)
    print("Account B balance:", account_b.balance)"""
