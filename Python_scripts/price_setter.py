from abc import ABC, abstractmethod


# 1. ABSTRACTION: Abstract base class representing a generic store product
class Product(ABC):

  def __init__(self, name, price):
    self.name = name
    self.__price = price  # 3. ENCAPSULATION: Private attribute hidden from direct access

  # Controlled access (Getter/Setter) for the private price
  def get_price(self):
    return self.__price

  def set_price(self, new_price):
    if new_price > 0:
      self.__price = new_price
    else:
      print("Error: Price must be greater than zero.")

  @abstractmethod
  def calculate_final_price(self):
    """Every product type must implement its own pricing/tax logic."""
    pass


# 2. INHERITANCE: Electronics inherits from Product
class Electronics(Product):

  # 4. POLYMORPHISM: Specific tax calculation for electronics
  def calculate_final_price(self):
    # Electronics have a 10% luxury tax added
    return self.get_price() * 1.10


# 2. INHERITANCE: Grocery inherits from Product
class Grocery(Product):

  # 4. POLYMORPHISM: Specific tax calculation for groceries
  def calculate_final_price(self):
    # Groceries are tax-free (no extra charge)
    return self.get_price()


# --- Demonstration ---
if __name__ == "__main__":
  # Create shopping cart items (Inheritance)
  cart = [
      Electronics("Smartphone", 500),
      Grocery("Organic Milk", 4),
  ]

  print("--- Cart Checkout (Polymorphism in Action) ---")
  # We loop through items and call the same method, 
  # but each product calculates its final price differently.
  for item in cart:
    final_price = item.calculate_final_price()
    print(f"- {item.name}: Final Price = ${final_price:.2f}")

  print("\n--- Encapsulation & Data Protection ---")
  phone = cart[0]
  # phone.__price = 100  # This would fail or create a separate variable because it's private
  
  # Safe update using the setter method with validation
  phone.set_price(450)
  print(f"Updated Smartphone Price: ${phone.get_price()}")