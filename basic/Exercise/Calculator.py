a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))

c = input("Choose the Operation: ")
d = "x"
e = "X"
f = "/"
g = "+"
h = "-"
i = "^"
if d in c:
    print("The produt of two numbers is", a*b)
elif e in c:
    print("The produt of two numbers is", a*b)
elif f in c:
    print("The division of two numbers is", a/b)
elif g in c:
    print("The sum of two numbers is", a+b)
elif h in c:
    print("The difference of two numbers is", a-b)
elif i in c:
    print("The value of", a, "to the power", b, "is", a**b)