What is a "Dunder" Method?
"Dunder" is just short for Double Underscore (__).

Whenever you see a method in Python with two underscores at the start and two at the end—like __init__—that is a dunder method.

Why do they exist? (The Secret Behind Python)
In Python, everything is an object. When you use simple symbols or functions like +, len(), or print(), Python doesn't magically know what to do. Behind the scenes, Python quietly translates those symbols into dunder methods.

When you write a + b, Python actually runs a.__add__(b)

When you write len(my_list), Python actually runs my_list.__len__()

When you write print(x), Python actually runs x.__str__()

In simple words: Dunder methods are secret switches inside your custom classes that teach your objects how to work with normal Python features like print(), +, len(), and ==.

Let's look at the 5 most basic and useful dunder methods using simple examples.

1. __init__ (The Setup Switch)
You might have seen this one already. Whenever you create a new object from a class, Python automatically runs __init__ to set up its starting data.


2. __str__ (The print() Switch)
Normally, if you try to print() a custom object, Python prints ugly computer memory text like <__main__.Dog object at 0x00123>.

If you add __str__ to your class, you control what print() shows.


3. __len__ (The len() Switch)
Python knows how to find the len() of a list or a string, but it doesn't know the length of your custom class—unless you teach it using __len__.


4. __add__ (The + Switch)
If you try to do dog1 + dog2, Python will crash because it doesn't know how to "add" two dogs. Using __add__, you decide what the + sign does.


5. __eq__ (The == Equal Switch)
By default, if you create two identical objects and check obj1 == obj2, Python says False because they are stored in two different spots in your computer's memory. __eq__ lets you define what makes two objects "equal."


The Golden Rule to Remember
You never call dunder methods directly like my_dog.__str__(). You just write normal Python code like print(my_dog), and Python triggers the dunder method for you automatically.