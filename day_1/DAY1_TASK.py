"""
A simple user repository that stores user data in memory.:

1. Create a class called UserRepository that will act as a repository for user data. The class SHOULD DO THE FOLLOWING:
- Store user data in memory using a dictionary.
- Implement the following methods:
    - __setitem__(self, key, value): Store a user with the given key and value.
    - __getitem__(self, key): Retrieve the user data associated with the given key.     
    - __delitem__(self, key): Delete the user data associated with the given key.
    - __contains__(self, key): Check if a user with the given key exists in the repository.
    - __len__(self): Return the number of users in the repository.
    - __iter__(self): Return an iterator over the keys in the repository.
    -__init__(self): Initialize the repository with an empty dictionary.
"""


class UserRepository:
    def __init__(self):
        self._storage = {}

    def __setitem__(self, key, value):
        self._storage[key] = value

    def __getitem__(self, key):
        return self._storage[key]

    def __delitem__(self, key):
        del self._storage[key]

    def __contains__(self, key):
        return key in self._storage

    def __len__(self):
        return len(self._storage)

    def __iter__(self):
        return iter(self._storage)

repo= UserRepository()
repo["user1"] = "Alice"
repo["user2"] = "Bob"

print(repo["user1"]== "Alice")  # Output: True

print(len(repo))  # Output: 2

print("user1" in repo)  # Output: True
print("user3" in repo)  # Output: False

for key in repo:
    print(key, repo[key])

del repo["user1"]
    
print("user1" not in repo)  # Output: True

print(len(repo))  # Output: 1