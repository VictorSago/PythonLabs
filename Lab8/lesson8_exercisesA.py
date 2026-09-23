
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
