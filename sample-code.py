# def calculate_total(prices, order):
#     cost_order = prices * order
#     return cost_order



# student1_name = "Sarah Conor"
# order = 2

# prices = [3.50, 4.00, 4.50, 2.50, 1.00, 6.87, 0]

# sizes = ("Small", "Medium", "Large")
# add_ons = ["oat-milk", "extra shot", "whipped cream"]

# go_cup = student1_name[0:6]
# print(go_cup)
# choosen_size = sizes[1:]
# print(choosen_size)

# print(calculate_total(prices[1], order))

# print(sorted(prices))

# def cal_area(length, width):
#     area = length * width
#     return area

# area =cal_area(5,10)

# print("Area of rectangle is: ", area)

# class students:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name: ", self.name)
#         print("Marks: ", self.marks)

#     def is_pass(self):
#         if self.marks >= 40:
#             return True
#         else:
#             return False

# student1 = students("Sarah Conor", 75)
# student2 = students("John Doe", 35)

# student1.display()
# student1.is_pass()

# student2.display()
# student2.is_pass()

# class names:

#     def __init__(self,first_name):
#         self.first_name = first_name

#     def greeting(self):
#         print("Hello, Welcome to the class " + self.first_name + "!")

# student1 = names("Komal")

# student1.greeting()


# my_list = [1, 2, 3, 4, 5]

# try:
#     element = my_list[8]
#     print(element)
# except IndexError:
#     print("Index out of range")


# try:
#     result = 10 / (int(input("Enter a number: ")))
#     print("Result: ", result)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

class Vehicles:
    def __init__(self, brand):
        self.brand = brand

    def engine_type(self):
        print("Engine type: Petrol")

class properties(Vehicles):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)
        self.battery_capacity = battery_capacity

my_car = properties("TATA", 100)
print(my_car.engine_type())


class carA:
    def model(self):
        return "TATA"

class carB:
    def model(self):
        return "Maruthi"

def indian_cars(cars):
    print(cars.model())

indian_cars(carA())
indian_cars(carB())


class bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

account = bankaccount("John Doe", 1000)
# print(account.get_balance())
account.deposit(500)
print(account.get_balance())




   