"""
                    Expression
The expression is the current item in the iteration, but it is also the outcome, 
which you can manipulate before it ends up like a list item in the new list
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
newlist = [x.upper() for x in thislist]
print(newlist)

"""
You can set the outcome to whatever you want
"""

newlist2 = ["Hello" for x in thislist]
print(newlist2)

"""
The expression can also contain conditions to manipulate the outcome
"""
thislist2 = [ "banana", "orange", "orange", "orange",]
newlist3 = [x if x != "banana" else "mango" for x in thislist2]
print(newlist3)