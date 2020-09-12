Users with Bank Accounts


Objectives:
Practice writing classes with associations
Update your existing User class to have an association with the BankAccount class. You should not have to change anything in the BankAccount class. The method signatures of the User class (the first line of the method with the def keyword) should also remain the same.

For example, our User class currently has a method like this:

class User:
    # other methods
    def make_deposit(self, amount):
    	self.account_balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore
But our User class no longer has a self.account_balance attribute. Instead, we have replaced this with an instance of a BankAccount by the name of self.account. That means our make_deposit (and other methods referencing self.account_balance) need to be updated! That's the goal of this assignment.

Remember in our User methods, we can now access the BankAccount class through our self.account attribute, like so:

class User:
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    	print(self.account.balance)		# or access its attributes