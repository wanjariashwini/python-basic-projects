import sys

class Customer:

    Bank_name = 'SBI'
    Branch_name = 'Indora'

    def __init__(self,name,bal_amount):
       self.name = name
       self.bal_amount = bal_amount

    def deposit(self,amt):
       self.bal_amount = self.bal_amount + amt
       return self.bal_amount

    def withdrawl(self,amt):
       if amt > self.bal_amount:
          print("Insufficient fund")

          choice =input("Do you want to deposit : (yes/no) ? ")

          if choice.lower() == 'yes':
              amt = float(input("Enter the amount to be deposit: "))
              print("Now the available balance is : {}".format(c.deposit(amt)))
          else:
              sys.exit()
       else:
          self.bal_amount = self.bal_amount - amt
          print("Now the available balance is  : ",self.bal_amount)

print("welcome to th bank (branch- {}) : {}".format(Customer.Branch_name, Customer.Bank_name))

name = input("Enter the customer name : ")
bal_amount = float(input("Enter the account balance : "))

c = Customer(name,bal_amount)

while(True):

    option =input("Choose the correct option from following : \n 'd' - Deposit\n 'w' - Withdrawl\n 'e' - Exit :\n ")

    if option.lower() == 'd':
         amt = float(input("Enter the amount to be deposit: "))
         print("Now the available balance is : {}".format(c.deposit(amt)))

    elif option.lower() == 'w':
         amt = float(input("Enter the amount to be withdrawl: "))
         c.withdrawl(amt)

    elif option.lower() == 'e':
        print("Thank you for visiting")
        sys.exit()

    print("Thanku for choosing SBI")

else:
    print("Invalid Option please choose correct one")




