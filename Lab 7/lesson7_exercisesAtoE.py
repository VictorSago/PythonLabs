
# ==========================================================
# Part A - Classes and objects
# ==========================================================

# Helper functions to examine objects
def get_attributes(obj):
    return vars(obj).copy()


def print_object(obj):
    attributes = get_attributes(obj)

    print(type(obj).__name__)

    for name, value in attributes.items():
        print(f'  "{name}": {repr(value)}')


# 1. Create a Book class with title, author and pages. 
# Create at least four Book objects and print their attributes.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 200)
book2 = Book("1984", "George Orwell", 320)
book3 = Book("Solaris", "Stanislaw Lem", 200)
book4 = Book("The Left Hand of Darkness", "Ursula K. Le Guin", 300)

books = [book1, book2, book3, book4]

# for book in books:
#     print("Title:", book.title)
#     print("Author", book.author)
#     print("Number of pages:", book.pages)
#     print()

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

# print(laptop1)
# print(laptop2)
# print(laptop3)


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
