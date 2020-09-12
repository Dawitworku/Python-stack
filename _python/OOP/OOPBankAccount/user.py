from bankaccount import BankAccount

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        #self.account = BankAccount()
        self.accounts = {
            # Dictionary to store the type of account as a key/value pairs
        }
    def create_Account(self, name):
        self.accounts[name] = BankAccount()
        return self
        
    def make_deposit(self,  amount, account_name):
        self.accounts[account_name].deposit(amount)  
        return self

    def make_withdrawal(self, amount, account_name):
        self.accounts[account_name].withdraw(amount)
        return self

    def display_user_balance(self, account_name):
        print(f"User: {self.name} - {account_name} Balance: ${self.accounts[account_name].balance}")
        return self

    def transfer_money(self,user,amount, account_from, account_to):
        self.accounts[account_from].withdraw(amount)
        user.accounts[account_to].deposit(amount)
        #user.make_deposit(amount)
        return self

#Using Method Chaining
Dave =User("Dave","dwc@yahoo.com") ## Creating/ Instantiating an object
Dave.create_Account('Savings')
Dave.create_Account('Checking')
Dave.make_deposit(5000, 'Savings').make_deposit(2000, 'Checking').make_deposit(1000,'Checking').make_withdrawal(1000, 'Checking').display_user_balance('Checking').display_user_balance('Savings')

Izzy = User("Izzy", "Izzy@yahoo.com") ## Creating/ Instantiating an object
Izzy.create_Account('Savings')
Izzy.make_deposit(1500, 'Savings').make_deposit(1500, 'Savings').make_withdrawal(500, 'Savings').make_withdrawal(500, 'Savings').display_user_balance('Savings')

Ghost = User("Ghost", "Ghost@yahoo.com")    ## Creating/ Instantiating an object
Ghost.create_Account('Savings')
Ghost.create_Account('Checking')
Ghost.make_deposit(10000, 'Checking').make_withdrawal(5000, 'Checking').make_withdrawal(500, 'Checking').make_withdrawal(500, 'Checking').display_user_balance('Checking')

Dave.transfer_money(Ghost, 500, 'Checking', 'Savings').display_user_balance('Checking')  # transfer from dave to ghost
Izzy.transfer_money(Dave, 1500, 'Savings', 'Checking').display_user_balance('Savings')  # transfer izzy to dave

Ghost.display_user_balance('Savings')
Ghost.display_user_balance('Checking')
Dave.display_user_balance('Checking')


