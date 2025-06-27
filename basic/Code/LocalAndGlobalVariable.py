x = 10 #Global variable

def my_function():
    global x #This will change the value of the global variable x
    x = 3
    y = 5 #Local variable
    print(y)

my_function()
print(x)
# print(y) This will cause an error as y is a Local variable