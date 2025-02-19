import uuid
import json
class Account:
    def __init__(self,  account_number, name, balance):
        self.account_number =account_number
        self.name = name
        self.balance = balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_deposit):
        if initial_deposit>0:
            account_number = str(uuid.uuid4())[:8]
            account = Account(account_number, name, initial_deposit)
            self.accounts[account_number] = {'name': name, 'balance': initial_deposit}
            print(f"Account created successfully, your account number: {account_number}")
            return account_number
        print('Cannot create an account with negative deposit')
    
    def view_account(self, account_number):
        if self.accounts.get(account_number):
            name = self.accounts[account_number]['name']
            balance = self.accounts[account_number]['balance']
            print(f'{name=}\n{balance=}')
        else:  
            print("There is not an account with this account number")
    
    def deposit(self, account_number, amount):
        if amount>0:
            self.accounts[account_number]['balance'] += amount
        else:
            print('Cannot deposit negative amount')

    def withdraw(self, account_number, amount):
        if amount <= self.accounts[account_number]['balance']:
            self.accounts[account_number]['balance'] -= amount
        else:
            print('Not enough money in your balance')
        
    def save_to_file(self):
        with open('bankAccounts.txt', 'w') as f:
            for k, v in self.accounts.items():
                f.write(k+', ')
                for key, value in v.items():
                    f.write(str(value)+', ')
                f.write('\n')
            

    def load_from_file(self):
        try:
            with open('bankAccounts.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = [p.strip() for p in line.strip().split(',') if p.strip()]
                    self.accounts[parts[0]] = {'name': parts[1], 'balance': float(parts[2])}
                     
        except FileNotFoundError:
            print("File could not be found")

bankManager = Bank()

