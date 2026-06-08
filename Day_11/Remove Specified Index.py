# Remove Specified Index

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.pop(3)
print(thislist)


"""
If you do not specify the index, the pop() method removes the last item.
"""
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2.pop()
print(thislist2)

"""
The del keyword also removes the specified index:
"""

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
del thislist3[2]
print(thislist3)

"""
The del keyword can also delete the list completely.
"""

thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
del thislist4