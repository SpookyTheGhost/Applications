class BankAccount:
  balance = 0
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return ("Account holder %s, Balance: %.2f" % (self.name, self.balance) )
  
  def showBalance(self):
    print("%.2f" % self.balance)
    
  def deposit(self, amount):
    if (amount < 0):
      print("error")
      return
    else:
      print("Depositing %.2f into account" % amount)
      self.balance += amount
      self.showBalance()

  def withdraw(self, amount):
    if (amount < 0 or amount > self.balance):
      print("Invalid request!")
      return
    else:
      print("withdrawing %.2f from account" % amount)
      self.balance -= amount
      self.showBalance()
		
myAccount = BankAccount("k")
print(myAccount)
myAccount.showBalance()
myAccount.deposit(2000)
myAccount.withdraw(1000)
print(myAccount)
