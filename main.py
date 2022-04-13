import gc

print(gc.isenabled())
gc.disable()
print(gc.isenabled())

class Person:
    def __init__(self):
        self.name = name
        self.dob = self.DOB()

    def display(self):
        print("Name is : ",self.name)
        self.dob.display()

    class DOB:
        def __init__(self):
            self.dd = date
            self.mm = month
            self.yyyy = year

        def display(self):
            print("Date of birth is {}-{}-{}".format(date,month,year))

name = input("Enter the name : ")
date = int(input("Enter the date : "))
month = int(input("Enter the month : "))
year = int(input("Enter the year : "))

p = Person()

p.display()


