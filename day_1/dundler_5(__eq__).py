class User:
    def __init__(self, username):
        self.username = username

    def __eq__(self, other):
        return self.username == other.username

user1 = User("Alice")
user2 = User("Alice")
print(user1 == user2)  # Output: True