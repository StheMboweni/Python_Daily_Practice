# The global Keyword
x = "good"

def func():
    global x
    x = "bad"
func()

print("Python is", x)