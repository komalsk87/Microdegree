# # # n = 10
# # # try:
# # #     result = n/0
# # #     print("Result:", result)
# # # except ZeroDivisionError:
# # #     print("Error: Division by zero is not allowed.")

# # # a = ["10", "twenty", 30]
# # # try:
# # #     total =int(a[0]) + int(a[1]) + int(a[2])

# # # except ValueError:
# # #     print("Error: Invalid value encountered during conversion.")

# # # class Animal:
# # #     def eat(self):
# # #         print("Animal is eating grass.")

# # #     def sleeps(self):
# # #         print("Animal is sleeping.")

# # # class dog(Animal):
# # #     def bark(self):
# # #         print("Dog is barking.")

# # # dog1 = dog()

# # # dog1.eat()
# # # dog1.sleeps()
# # # dog1.bark()

# # # class A:
# # #     def root(self):
# # #         print("This is class A")

# # # class B(A):
# # #     def root(self):
# # #         print("This is class B")


# # # b = B()
# # # b.root()

# # class selling:
# #     def __init__(self):
# #         self.__original_price = 5000

# #     def sell(self):
# #         print("Selling price:", self.__original_price)

# #     def set_price(self, price):
# #         self.__original_price = price

# # s = selling()
# # # s.sell()

# # s.set_price(6000)
# # s.sell()

# class PasswordManager:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password  # Private attribute

#     def change_password(self, old_password, new_password):
#         if self.__password == old_password:
#             self.__password = new_password
#             print("Password changed successfully!")
#         else:
#             print("Incorrect old password!")

#     def check_password(self, password):
#         if self.__password == password:
#             print("Login successful!")
#         else:
#             print("Invalid password!")


# # Create an object
# user = PasswordManager("Komal", "Secure@123")

# # Check the password
# user.check_password("Secure@123")

# # Change the password
# user.change_password("Secure@123", "NewPass@456")

# # Try logging in with the new password
# user.check_password("NewPass@456")

# Try accessing the private attribute
# print(user.__password)  # Raises AttributeError

a = ["10", "twenty", 30]
try:
    total =int(a[0]) + int(a[1]) + int(a[2])

except ValueError as e:
    print("Error: Invalid value encountered during conversion.")