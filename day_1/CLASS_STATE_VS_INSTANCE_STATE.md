To understand Class State vs. Instance State, think of a Class as a blueprint (like a cookie cutter) and Instances as the actual objects made from that blueprint (the individual cookies).

"State" just means data (the variables stored inside them).

1. Instance State (Personal Data)
Where it lives: Attached to self (usually inside __init__).

Who owns it: Each individual object gets its own separate copy.

Effect of changing it: Changing it on one object does not affect any other object.

2. Class State (Shared Data)
Where it lives: Defined directly inside the class block, outside of any method.

Who owns it: The class itself. Every object shares this exact same variable.

Effect of changing it: Changing it on the class updates it for every single object at once.