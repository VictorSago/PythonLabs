
# ==========================================================
# Part H - Applied challenge: User accounts
# ==========================================================

# 1. Build a small user account system using inheritance.

# 2. Create a base class User with at least username and email.
# 3. Add a useful method to User that all user types should inherit.
# 6. Add one method to User and override it differently in AdminUser and PremiumUser.
# 9. Add at least one sensible validation using ValueError.
class User:
    def __init__(self, username, email):
        if "@" not in email:
            raise ValueError("email must contain '@'")
        self.username = username
        self.email = email

    def get_display_name(self):
        return f"@{self.username}"

    def get_role_description(self):
        return f"{self.username} is a standard user."


# 4. Create AdminUser(User) and PremiumUser(User). Give each subclass
# at least one additional attribute and one subclass-specific method.
# 5. Use super() in both subclasses instead of duplicating User's initialization.
# 7. In one overridden method, use super() to reuse the base implementation and extend it.
class AdminUser(User):
    def __init__(self, username, email, access_level):
        super().__init__(username, email)
        self.access_level = access_level

    def revoke_access(self, target_username):
        return f"{self.username} revoked access for {target_username}."

    def get_role_description(self):
        base_description = super().get_role_description()
        return f"{base_description} They are an admin with access level '{self.access_level}'."


class PremiumUser(User):
    def __init__(self, username, email, subscription_tier):
        super().__init__(username, email)
        self.subscription_tier = subscription_tier

    def show_exclusive_content(self):
        return f"{self.username} is viewing exclusive content."

    # A full override, with no super() call shown alongside AdminUser's 
    # super()-extending version for contrast: not every override needs to
    # reuse the base implementation, only where that behaviour is still useful.
    def get_role_description(self):
        return f"{self.username} is a premium user on the '{self.subscription_tier}' tier."


# 8. Create several objects and demonstrate inherited methods,
# subclass-specific methods and overridden methods.
user_1 = User("carla_user", "carla@example.com")
admin_1 = AdminUser("alice_admin", "alice@example.com", "full")
premium_1 = PremiumUser("bob_premium", "bob@example.com", "gold")

# Inherited method `get_display_name` - identical behaviour for all three, 
# defined once on User and never overridden.
# Overridden method `get_role_description` - each class's own version runs.
for account in (user_1, admin_1, premium_1):
    print(account.get_display_name())
    print(account.get_role_description())

# Subclass-specific methods - only exist on their own class.
print(admin_1.revoke_access("bob_premium"))
print(premium_1.show_exclusive_content())

# Validation in action.
try:
    User("bad_user", "not-an-email")
except ValueError as error:
    print(f"User('bad_user', 'not-an-email') failed as expected: {error}")


# 10. In comments, explain why AdminUser and PremiumUser have an "is-a" relationship with User.
print("admin_1 is a User:", isinstance(admin_1, User))
print("premium_1 is a User:", isinstance(premium_1, User))

# AdminUser IS A User, and PremiumUser IS A User: both inherit everything a
# User has and add their own attribute and behaviour on top - access_level and
# revoke_access() for AdminUser; subscription_tier and show_exclusive_content()
# for PremiumUser. The isinstance() checks above confirm both remain Users
# while also being their own more specific type.
