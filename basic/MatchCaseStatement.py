x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x < 10:
        print("x is < 10")
    case _:
        print(x)
        