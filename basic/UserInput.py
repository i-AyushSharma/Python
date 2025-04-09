a = input("Enter your name:")
print("my name is", a)

x = input("Enter first number:")
y = input("Enter second number:")
print(x + y) #Here input is recognised as a string and is concatinated in the output
print(int(x) + int(y)) #Here ipunt is coverted into integer

b = input("Enter first number:")
c = input("Enter second number:")
print("The sum of", b, ("and"), c, ("is"), int(b)+int(c))
print("The product of", b, ("and"), c, ("is"), int(b)*int(c))
print("The difference of", b, ("and"), c, ("is"), int(b)-int(c))
print("The division of", b, ("and"), c, ("is"), int(b)/int(c))
print("The concatination of both the number is", (b + c))


