def average(a=5, b=7):
    print("The average is", (a+b)/2)

average(4, 10)
average()
average(b=5)

def name(fname, mname = "Jhon", lname = "Watson"):
    print("hello", fname, mname, lname)

name("Amy")
name("Jhon", "Jones")
