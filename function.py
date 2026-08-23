# 1. Define the function
def multiply(x, y):
    sum = x + y
    return sum

# 2. Call the function
result1 = multiply(5, 3)
result2 = multiply(10, 2)

print(result1) 
print(result2) # Output: Result 1: 8

#-----------------------------------------------#

# Function definition with a default parameter value
# def calculate_total(price, tax_rate=0.05):
#     """Calculates total cost including tax."""
#     total = price + (price * tax_rate)
#     return total

# # Function calls
# item_price = 100

# # Using default tax_rate
# cost_standard = calculate_total(item_price)
# print(f"Standard Total: ${cost_standard}")  # Output: $105.0

# # Specifying a custom tax_rate
# cost_custom = calculate_total(item_price, tax_rate=0.10)
# print(f"Custom Total: ${cost_custom}")      # Output: $110.0

# #-----------------------------------------------#

# def my_function():
#     secret_number = 42  # Local variable
#     print(secret_number)

# my_function()  # Output: 42

# Trying to access secret_number outside the function will cause an error:
# print(secret_number)  # NameError: name 'secret_number' is not defined