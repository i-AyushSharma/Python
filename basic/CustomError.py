a = int(input("Enter any no. between 5 and 9: "))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

b = input("Write 'quit': ")
if(b != "quit"):
    raise ValueError("Entered value is not word 'quit'")