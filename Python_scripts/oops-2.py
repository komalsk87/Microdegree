
from abc import ABC, abstractmethod

# 1. ABSTRACTION
class BankAccount(ABC):

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # ENCAPSULATION

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def withdraw(self, amount):
        pass


# 2. INHERITANCE
class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.get_balance():
            print("Savings account withdrawal successful:", amount)
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.get_balance() + 5000:
            print("Current account withdrawal successful:", amount)
        else:
            print("Withdrawal limit exceeded")


# 3. CREATING OBJECTS
account1 = SavingsAccount("Rahul", 10000)
account2 = CurrentAccount("Priya", 20000)


# 4. USING ENCAPSULATION
account1.deposit(2000)

print("Rahul's balance:", account1.get_balance())


# 5. USING POLYMORPHISM
accounts = [account1, account2]

for account in accounts:
    account.withdraw(12000)



#######################################################


from abc import ABC, abstractmethod

# 1. ABSTRACTION
class Vehicle(ABC):

    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed  # 2. ENCAPSULATION

    def get_speed(self):
        return self.__speed

    def display_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.__speed, "km/hr")

    @abstractmethod
    def start(self):
        pass


# 3. INHERITANCE
class Car(Vehicle):

    def start(self):
        print(self.brand, "car starts with a key")


class Bike(Vehicle):

    def start(self):
        print(self.brand, "bike starts with a button")


# Creating objects
car1 = Car("Toyota", 120)
bike1 = Bike("Honda", 90)


# Display vehicle information
car1.display_info()
bike1.display_info()


# 4. POLYMORPHISM
vehicles = [car1, bike1]

for vehicle in vehicles:
    vehicle.start()
