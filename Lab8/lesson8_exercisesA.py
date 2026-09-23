
# ==========================================================
# Part A - Mutable default arguments
# ==========================================================

# 1. Create a BadTeam class with name and a default parameter members=[]. 
# Add an add_member() method.
class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)


# 2. Create two BadTeam objects without providing a members list. Add a member
# to only one team and print both lists. Explain in a comment what happened.
bad_team_1 = BadTeam("Falcons")
bad_team_2 = BadTeam("Wolves")

bad_team_1.add_member("Alice")

print(bad_team_1.name, bad_team_1.members)
print(bad_team_2.name, bad_team_2.members)
print("bad_team_1.members is bad_team_2.members:", bad_team_1.members is bad_team_2.members)

# What happened: members=[] is evaluated exactly once, when the class body
# runs and __init__ is defined - not once per call. Every BadTeam created
# without its own members argument ends up sharing that same single list
# object. Adding "Alice" to bad_team_1 therefore also shows up in bad_team_2,
# even though bad_team_2 was never touched directly - the `is` check above
# confirms it's genuinely the same list, not two equal-looking ones.


# 3. Create a corrected Team class using None as the default value and create
# a new list inside __init__.
class Team:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members if members is not None else []

    def add_member(self, member):
        self.members.append(member)


# 4. Repeat the test with two Team objects and show that each object
# now has its own list.
team_1 = Team("Falcons")
team_2 = Team("Wolves")

team_1.add_member("Alice")

print(team_1.name, team_1.members)
print(team_2.name, team_2.members)
print("team_1.members is team_2.members:", team_1.members is team_2.members)


# ==========================================================
# Part B - Dictionary or class?
# ==========================================================

# 1. Represent a movie using a dictionary with title, director and rating.
movie_dict = {"title": "Inception", "director": "Christopher Nolan", "rating": 8.8}
print(movie_dict["title"], "-", movie_dict["director"], "-", movie_dict["rating"])


# 2. Represent the same information using a Movie class.
# 3. Add a method to Movie that returns whether the movie is highly rated.
class Movie:
    HIGH_RATING_THRESHOLD = 8.0  # ratings are on a 0-10 scale here

    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        return self.rating >= Movie.HIGH_RATING_THRESHOLD


movie_1 = Movie("Inception", "Christopher Nolan", 8.8)
movie_2 = Movie("Cats", "Tom Hooper", 2.8)

for movie in (movie_1, movie_2):
    print(movie.title, "-", movie.director, "-", movie.rating, "- highly rated:", movie.is_highly_rated())


# 4. Briefly explain one situation where you would choose a dictionary and
# one where you would choose a class.
#
# Dictionary: good for a one-off piece of data being passed around or 
#   looked up by key, with no behaviour attached - e.g. a single record just
#   read from a JSON API response, or a small ad-hoc lookup table. No class
#   definition is needed for that.
#
# Class: good once the data has behaviour that belongs with it (like
#   is_highly_rated() here), or once many instances need to share the same
#   guaranteed structure. A dict can have any keys or be missing one silently;
#   a class's __init__ makes the required attributes explicit, and a typo in
#   an attribute name (movie.rtaing) fails immediately and clearly, whereas a
#   typo in a dict key (movie_dict["rtaing"]) only surfaces as a KeyError
#   wherever that key happens to get used.


# ==========================================================
# Part C - Inheritance fundamentals
# ==========================================================

# 1. Create a base class Account with owner and balance.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


# 2. Create SavingsAccount(Account) with an additional interest_rate attribute.
# 3. Use super() so SavingsAccount reuses the initialization from Account.
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


# 4. Create at least two objects and print their attributes.
account_1 = Account("Anna Andersson", 500)
savings_1 = SavingsAccount("David Kim", 1000, 0.03)
savings_2 = SavingsAccount("Sara Nilsson", 2500, 0.025)

print(account_1.owner, "-", account_1.balance)
print(savings_1.owner, "-", savings_1.balance, "-", savings_1.interest_rate)
print(savings_2.owner, "-", savings_2.balance, "-", savings_2.interest_rate)


# 5. Write the "is-a" statement that explains why this inheritance relationship makes sense.
#
# A SavingsAccount IS AN Account: it has everything a regular Account has
# (an owner and a balance) plus its own interest_rate on top. The isinstance()
# checks below confirm it - every SavingsAccount object is also considered an
# Account. The reverse doesn't hold: a plain Account has no interest_rate, so 
# it is not a SavingsAccount. Inheriting from Account means that shared
# owner/balance behaviour only needs to be written once, in Account, rather
# than duplicated inside SavingsAccount.
print("savings_1 is an Account:", isinstance(savings_1, Account))
print("savings_1 is a SavingsAccount:", isinstance(savings_1, SavingsAccount))
print("account_1 is a SavingsAccount:", isinstance(account_1, SavingsAccount))


# ==========================================================
# Part D - Inherited and subclass-specific behaviour
# ==========================================================

# 1. Create a base class Employee with name and a method get_information().
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        emp_cls = type(self).__name__
        type_string = f" of {emp_cls} class" if emp_cls != "Employee" else ""
        return f"{self.name} is an employee{type_string}."


# 2. Create Developer(Employee) and add a method that only Developer has.
class Developer(Employee):
    def write_code(self):
        return f"{self.name} is writing code."


# 3. Create another Employee subclass of your choice and give it its own subclass-specific method.
class Designer(Employee):
    def design_mockup(self):
        return f"{self.name} is designing a mockup."


# 4. Demonstrate that both subclasses can use inherited behaviour from Employee.
developer_1 = Developer("Alice")
designer_1 = Designer("Bob")
print(developer_1.get_information())
print(designer_1.get_information())

# Subclass-specific behaviour, for context.
print(developer_1.write_code())
print(designer_1.design_mockup())


# 5. Demonstrate that an Employee object cannot automatically use a method
# that only exists in one of its subclasses.
employee_1 = Employee("Charlie")
print(employee_1.get_information())

try:
    employee_1.write_code()
except AttributeError as error:
    print(f"employee_1.write_code() failed as expected: {error}")

# Inheritance only flows one way: a subclass gets everything the base class
# defines, but the base class knows nothing about what its subclasses later
# add. write_code() only exists on Developer, so a plain Employee object
# has no such method at all.
