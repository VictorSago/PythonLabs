
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
