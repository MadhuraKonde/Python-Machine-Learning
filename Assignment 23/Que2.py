class BankAccount:
    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount
    
    def Display(self):
        print("Account holder name :",self.Name)
        print("Current balance :",self.Amount)
    
    def Deposit(self):
        deposit = int(input("Enter the amount to deposit : "))
        self.Amount += deposit
    
    def Withdraw(self):
        withdraw = int(input("Enter the amount to withdraw : "))

        if(withdraw > self.Amount):
            print("Insufficient Balance !")
        
        else:
            self.Amount -= withdraw
    
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

name = input("Enter Account Holder Name : ")
balance = int(input("Enter Account Balance : "))

obj1 = BankAccount(name,balance)
print()
obj1.Display()
print()
obj1.Deposit()
obj1.Display()
print()
obj1.Withdraw()
obj1.Display()
print()
print("Interest :",obj1.CalculateInterest())

print()
name = input("Enter Account Holder Name : ")
balance = int(input("Enter Account Balance : "))

obj1 = BankAccount(name,balance)
print()
obj1.Display()
print()
obj1.Deposit()
obj1.Display()
print()
obj1.Withdraw()
obj1.Display()
print()
print("Interest :",obj1.CalculateInterest())