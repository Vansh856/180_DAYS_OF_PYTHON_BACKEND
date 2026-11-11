class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

my_dog = Dog("Buddy", 3)
print(my_dog)  # Output: Buddy is 3 years old.