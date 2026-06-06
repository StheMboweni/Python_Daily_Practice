# Identity Operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

"""
Difference Between is and ==
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
"""

print(x is not y)