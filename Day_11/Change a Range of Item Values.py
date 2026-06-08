# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


"""
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
"""
thislist2 = ["apple", "banana", "cherry"]
thislist2[1:2] = ["blackcurrant", "watermelon"]
print(thislist2)

"""
If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
"""

thislist3 = ["apple", "banana", "cherry"]
thislist3[1:3] = ["watermelon"]
print(thislist3)
