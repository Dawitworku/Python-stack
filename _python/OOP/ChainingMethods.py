class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self,user,amount):
        self.account_balance -= amount
        user.account_balance += amount
        #user.make_deposit(amount)
        return self

## Using Method Chaining
Dave = User("Dave","dwc@yahoo.com") ## Creating/ Instantiating an object
Dave.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(1000).display_user_balance()

Izzy = User("Izzy", "Izzy@yahoo.com") ## Creating/ Instantiating an object
Izzy.make_deposit(1500).make_deposit(1500).make_withdrawal(500).make_withdrawal(500).display_user_balance()

Ghost = User("Ghost", "Ghost@yahoo.com")    ## Creating/ Instantiating an object
Ghost.make_deposit(10000).make_withdrawal(5000).make_withdrawal(500).make_withdrawal(500).display_user_balance()

Dave.transfer_money(Ghost, 400).display_user_balance()  # transfer from dave to ghost
Izzy.transfer_money(Dave, 1500).display_user_balance()  # transfer_money from izzy to dave
Ghost.display_user_balance()

