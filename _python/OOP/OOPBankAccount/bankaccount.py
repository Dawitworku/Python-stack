class BankAccount:   # super class
    def __init__(self, balance = 0, int_rate = 0.01): # overridding constructor/ default constructor
        self.int_rate = int_rate
        self.balance = balance
        #self.account_type = account_type

    def deposit(self, amount): # have if statment to determine whicch account we want to run
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient finds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            intreset = self.balance * self.int_rate
            self.balance = self.balance + intreset
        return self




# Account1 = BankAccount()    # default constructor b/c we don't have to use a parameter
# Account2 = BankAccount(2000)      # default constructor b/c we don't have to use a parameter

# Account1.display_account_info()  # Will desplay balance of 0 which is when we initially create an account.
# Account2.display_account_info()  # The default paramenter is being passed on here

# Account1.deposit(1000).deposit(1000).deposit(1000).withdraw(1500).yield_interest().display_account_info()

# Account2.deposit(8000).deposit(1000).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().display_account_info()
