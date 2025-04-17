# FOR LOOP
name = "Abhishek"
for x in name:
    print(x)
    if(x =="i"):
        print("Hello")
print("\n")
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for y in color:
        print(y)
print("\n")
for k in range(5):
    print(k) #0 to 4. i.e. 0 to n - 1 
print("\n")
for k in range(5):
    print(k + 1) #1 to 5. i.e. 1 to n
print("\n")
for k in range(1, 11):
    print(k) #1 to 10. i.e. x to n - 1
print("\n")
for k in range(1, 6, 2):
    print(k)

# WHILE LOOP
i = 0
while(i<=3):
    print(i)
    i = i + 1
print("\n")
x = int(input("Enter the number: "))
print(x)
while(x<=50):
    x = int(input("Enter the number: "))
    print(x)

print("Done with the loop")

count = 5
while(count>0):
    print(count)
    count = count - 1
else:
    print("I am inside else")
