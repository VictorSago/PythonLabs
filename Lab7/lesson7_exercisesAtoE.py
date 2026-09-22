
# ==========================================================
# Lab 7
# ==========================================================

# Helper functions to examine objects
# vars(obj) returns a dictionary of the object's attributes.
def get_attributes(obj):
    return vars(obj).copy()


def print_object(obj):
    attributes = get_attributes(obj)

    print(type(obj).__name__)

    for name, value in attributes.items():
        print(f'  "{name}": {repr(value)}')


# --- Part A - Classes and objects
# --------------------------------

# 1. Create a Book class with title, author and pages. 
# Create at least four Book objects and print their attributes.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def is_long(self):
        return self.pages > 300


book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 190)
book2 = Book("1984", "George Orwell", 320)
book3 = Book("Solaris", "Stanislaw Lem", 200)
book4 = Book("The Left Hand of Darkness", "Ursula K. Le Guin", 350)

books = [book1, book2, book3, book4]

for book in books:
    print_object(book)
    print()


# 2. Create a Laptop class with brand, model, ram_gb and price.
# Create three separate objects and change the price of one object.
class Laptop:
    def __init__(self, brand, model, ram_gb, price=999):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price


laptop1 = Laptop("Dell", "XPS 13", 16, 1200)
laptop2 = Laptop("Apple", "MacBook Air", 8, 999)
laptop3 = Laptop("Lenovo", "ThinkPad X1", 16, 1400)

laptop2.price = 899

laptops = [laptop1, laptop2, laptop3]
for laptop in laptops:
    print_object(laptop)
    print()


# 3. Create two objects with the same attribute values
laptop4 = Laptop("HP", "Pavilion", 8, 700)
laptop5 = Laptop("HP", "Pavilion", 8, 700)

# `is` checks whether they are the exact same object in memory
print(laptop4 is laptop5)  # False


# 4. Add a default value to at least one __init__ parameter.
laptop6 = Laptop("Acer", "Aspire", 8)
laptops.extend([laptop4, laptop6])
print_object(laptop6)   # "price": 999


# 5. Create an object using keyword arguments
laptop7 = Laptop(
    brand="Microsoft",
    model="Surface Laptop",
    ram_gb=16,
    price=1300
)
laptops.append(laptop7)
print_object(laptop7)


# --- Part B - Methods and state
# ------------------------------

# 1. Extend your Book class with an is_long() method
# See Part A, Ex1
print("Book1 is long:", book1.is_long())  # False
print("Book2 is long:", book2.is_long())  # True


# 2. Create a BankAccount class with owner and balance. Add a deposit() method
# that changes the balance.
# 3. Add a withdraw() method. Prevent withdrawals that would make the balance
# negative by raising a ValueError.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Withdrawal would make the balance negative")
        self.balance -= amount


account = BankAccount("Ada", 100)

account.deposit(50)
print("Account 1 balance:", account.balance)  # 150

account.withdraw(75)
print("Account 1 balance:", account.balance)  # 75

# This will raise a ValueError exception
# account.withdraw(100)


# 4. Create a Task class with title and completed=False. 
# Add complete() and reopen() methods.
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

task1 = Task("Complete the Python labs")

print(task1.completed)  # False

task1.complete()
print(task1.completed)  # True

task1.reopen()
print(task1.completed)  # False


# 5. Create at least two objects from one of your classes and show that
# changing the state of one object does not change the other.
task2 = Task("Write the report")
task3 = Task("Review the report")

task2.complete()

print(task2.completed)  # True
print(task3.completed)  # False


# --- Part C - Instance and class attributes
# ------------------------------------------

# 1. Create a Product class with name and price as instance attributes.
# 2. Add a class attribute tax_rate shared by all Product objects.
# 3. Add a price_with_tax() method that returns the price including tax.
class Product:
    # Class attribute shared by all Product objects
    tax_rate = 0.20
    def __init__(self, name, price):
        # Instance attributes
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)


# 4. Create at least three Product objects and print their prices with tax.
product1 = Product("Keyboard", 50)
product2 = Product("Mouse", 25)
product3 = Product("Monitor", 200)

for product in [product1, product2, product3]:
    print(product.name, round(product.price_with_tax(), 2))


# 5. Change Product.tax_rate and show how it affects the Product objects.
Product.tax_rate = 0.25

print("\nAfter changing Product.tax_rate:")

for product in [product1, product2, product3]:
    print(product.name, round(product.price_with_tax(), 2))


# 6. Give one Product object its own tax_rate. Print the tax rate from that
# object, another Product object and the Product class.
product1.tax_rate = 0.10

print("\nTax rates:")
print("product1:", round(product1.tax_rate, 2))
print("product2:", round(product2.tax_rate, 2))
print("Product class:", round(Product.tax_rate, 2))

print("\nPrices after giving product1 its own tax rate:")

for product in [product1, product2, product3]:
    print(product.name, round(product.price_with_tax(), 2))
