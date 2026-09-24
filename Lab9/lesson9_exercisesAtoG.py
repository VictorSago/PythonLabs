
# ==========================================================
# Part A - Polymorphism
# ==========================================================

# 1. Create three classes: EmailNotification, SMSNotification and PushNotification.
# 2. Give all three classes a method called send(), but make each method return a different message.
class EmailNotification:
    def send(self):
        return "Sending an email notification."


class SMSNotification:
    def send(self):
        return "Sending an SMS notification."


class PushNotification:
    def send(self):
        return "Sending a push notification."


# 3. Create one object from each class and store them in the same list.
notifications = [EmailNotification(), SMSNotification(), PushNotification()]

# 4. Loop through the list and call send() on every object.
for notification in notifications:
    print(notification.send())

# 5. In a comment, explain why the loop does not need to know the exact class
# of each object.
#
# The loop only ever calls notification.send() - it never checks which specific
# class notification belongs to. All three classes happen to provide a send()
# method with that exact name, so the same line of code works uniformly across
# every object in the list. This is polymorphism: one piece of code, many
# possible object types, as long as each supports the method being called.


# ==========================================================
# Part B - Polymorphism with inheritance
# ==========================================================

# 1. Create a base class Document with a title attribute and a method describe().
class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "This is a general document."


# 2. Create PDFDocument(Document) and TextDocument(Document).
# 3. Override describe() in both subclasses so they return different descriptions.
class PDFDocument(Document):
    def describe(self):
        return f"'{self.title}' is a PDF document."


class TextDocument(Document):
    def describe(self):
        return f"'{self.title}' is a plain text document."


# 4. Create several PDFDocument and TextDocument objects and store them in one list.
documents = [
    PDFDocument("Annual Report"),
    TextDocument("Meeting Notes"),
    PDFDocument("Invoice 2026-04"),
    TextDocument("Todo List"),
]

# 5. Loop through the list and print each document's title and the result of describe().
for document in documents:
    print(document.title, "-", document.describe())


# ==========================================================
# Part C - Duck typing
# ==========================================================

# 1. Create two unrelated classes. Do not use inheritance between them.
# 2. Give both classes a method called display_status().
class Printer:
    def display_status(self):
        return "Printer is ready and has paper loaded."


class Screen:
    def display_status(self):
        return "Screen is on and displaying content."


# 3. Create objects from both classes and store them in the same list.
printer_1 = Printer()
screen_1 = Screen()
devices = [printer_1, screen_1]

# 4. Loop through the list and call display_status() on each object.
for device in devices:
    print(device.display_status())

# 5. In a comment, explain why this works even though the classes do
# not share a base class.
#
# Python does not check an object's class or inheritance chain before calling a
# method - it only checks, at the moment display_status() is called, whether that
# particular object happens to have a method by that name. Since Printer and 
# Screen both independently define display_status(), the loop works for either
# one. This is duck typing: "if it walks like a duck and quacks like a duck,
# treat it as a duck" - what an object CAN DO matters more than what it formally IS.


# ==========================================================
# Part D - isinstance()
# ==========================================================


# 1. Create a base class User and a subclass AdminUser(User).
class User:
    def __init__(self, username):
        self.username = username


class AdminUser(User):
    pass


# 2. Create an AdminUser object.
admin_1 = AdminUser("alice_admin")

# 3. Use isinstance() to check whether the object is an AdminUser, a User and a string.
is_admin_user = isinstance(admin_1, AdminUser)
is_user = isinstance(admin_1, User)
is_string = isinstance(admin_1, str)

# 4. Print all three results.
print("admin_1 is an AdminUser:", is_admin_user)
print("admin_1 is a User:", is_user)
print("admin_1 is a str:", is_string)

# 5. In a comment, explain why the AdminUser object is also considered
# an instance of User.
#
# AdminUser inherits from User, so every AdminUser object automatically has
# everything a User has - it "is a" User as well as being its own, more
# specific type. isinstance() checks an object's entire inheritance chain, not
# just its exact class, which is why it reports True for both AdminUser and
# User. It correctly reports False for str, since AdminUser's inheritance
# chain has nothing to do with str.

