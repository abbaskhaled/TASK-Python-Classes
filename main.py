class Wallet:
    def __init__(self, money):
        self.money = money 
        
        

    def credit(self , amount): #deposit
        self.money = amount + self.money
        print(f"you have {self.money}")
        

    def debit(self , amount):# withdrawl
        self.money = self.money - amount 
        print(f"you have {self.money}")
        


wallet = Wallet(6)
# wallet = Wallet()  # This should default money inside the wallet to 0
print(wallet.money)
print(wallet.credit(4))


class Person:
    # Implement the code here
    def __init__(self,name,location,money):
        self.name = name 
        self.location = location
        self.wallet = Wallet(money)




name_one = Person("abbas",10,200)
print(name_one.wallet.money)


person = Person("Moh", 5, 50)


# class Vendor:
#     # implement Vendor!
#     pass


# vendor = Vendor("Abdallah", 3, 6)


# class Customer:
#     # implement Customer!
#     pass


# customer = Customer("Abdallah", 3, 6)
