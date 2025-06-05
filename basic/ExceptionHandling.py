a = input("Enter the no.: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Invalid Input!")

print("Some Imp. lines of Code")
print("End of Code")

try:
    num = int(input("enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("entered character is not an integer")
except IndexError:
    print("IndexError!")