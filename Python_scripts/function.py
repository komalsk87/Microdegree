# def far_to_cel(far):
#     return (far - 32) * 5 / 9

# temperature = 100

# print(far_to_cel(temperature))
# print(far_to_cel(32))

# def print_statment(str):
#     print(str)
#     return;

# print_statment("Hello World!, this is my first function in python.")
# print_statment("I am learning python programming language.")

# def test_list(cat):
#     print("This is inside a function")
#     print ("Age list:", cat)


# var = [10, 20, 30, 40, 50]
# cat = "This is a string variable"
# print("This is outside a function")
# test_list(cat)
# print("This is nest:", var)

# def people(*name):
#     print("The youngest child is " + name[2])

# people("Emil", "Tobias", "Linus")

# def my_func(*args):
#     print("Name:", args[0])
#     print("all names:", args)

# my_func("Emil", "Tobias", "Linus")


# class Bike:
#     name = ""
#     gear = 0

# Bike1 = Bike()
# Bike1.name = "Mountain Bike"
# Bike1.gear = 5

# print(Bike1.name)
# print(Bike1.gear)

# class Employee:
#     employee_id = 0

# Employee1 = Employee()
# Employee2 = Employee()

# Employee.employee_id = 1001
# print(Employee1.employee_id)

# class Room:
#     length = 0
#     breadth = 0

#     def calculate_area(self):
#         print("Area of the room is:", self.length * self.breadth)

# study_room = Room()

# study_room.length = 10
# study_room.breadth = 12

# study_room.calculate_area()

class Human:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am", self.name)


person = Human("Komal")

person.speak()
