a = int(input("Enter your age: "))

# Conditional Operators
# >, <, >=, <=, ==, !=
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

if(a>18):
    print("You can drive")
else:
    print("You cannot drive")

appleprice = 210
budget = int(input("Enter your budget: "))
b = budget//appleprice
c = budget - b*appleprice
if(appleprice < budget):
     print("You can buy", b, "kg of apples with remaining", c, "rupees in your hand")
elif(appleprice == budget):
    print("You can buy 1 kg of apples but, you will become pennyless")
else:
    print("Sorry, You are out of  budget")
print("Apple is my favourite fruit")

# Exercise
import time
Timestamp = int(time.strftime("%H"))
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if(4<=Timestamp<12):
    print("Good Morning Sir, its", timestamp)
elif(12>=Timestamp<17):
    print("Good Afternoon Sir, its", timestamp)
else:
    print("Good Evening Sir, its", timestamp)
