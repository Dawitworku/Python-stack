class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self,amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self,user,amount):
        self.account_balance -= amount
        user.account_balance += amount
        #user.make_deposit(amount)


Dave = User("Dave","dwc@yahoo.com") ## Creating/ Instantiating an object
Dave.make_deposit(500)
Dave.make_deposit(500)
Dave.make_deposit(500)
Dave.make_withdrawal(1000)
Dave.display_user_balance()

Izzy = User("Izzy", "Izzy@yahoo.com") ## Creating/ Instantiating an object
Izzy.make_deposit(1500)
Izzy.make_deposit(2500)
Izzy.make_withdrawal(500)
Izzy.make_withdrawal(500)
Izzy.display_user_balance()

Ghost = User("Ghost", "Ghost@yahoo.com")    ## Creating/ Instantiating an object
Ghost.make_deposit(10000)
Ghost.make_withdrawal(5000)
Ghost.make_withdrawal(500)
Ghost.make_withdrawal(500)
Ghost.display_user_balance()


Dave.transfer_money(Ghost, 400)
Izzy.transfer_money(Dave, 2000)
Dave.display_user_balance()
Ghost.display_user_balance()
Izzy.display_user_balance()