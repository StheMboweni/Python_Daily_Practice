# The Syntax

"""
newlist = [expression for item in iterable if condition == True]

The return value is a new list, leaving the old list unchanged.
"""
'//////////////////////////////////////////////////////////////'

"""
                    Condition
The condition is like a filter that only accepts the items that evaluate to True.
The condition will return True for all elements other than "apple", making the list
contain all fruits except "apple"
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

newlist = [x for x in thislist if x != "apple"]
print(newlist)
"/////////////////////////////////////////////////////////////////"

"""
                    Iterable
The iterable can be any iterable objec, like a list, tuple, set etc.
You can use the range(). function to create an iterable
"""
newlist2 = [x for x in range(10)]
print(newlist2)
"""
Same thing, but with a condition
accepting only numbers lower than 5
"""
newlist3 = [x for x in range(20) if x < 5]
print(newlist3)
'/////////////////////////////////////////////////////////////////////'