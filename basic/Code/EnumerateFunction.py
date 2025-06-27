a = [12, 56, 32, 98, 12, 45, 1, 6]

# index = 0
# for mark in a:
#     print(mark)
#     if(index == 3):
#         print("Harry")
#     index += 1

for index, mark in enumerate(a):
    print(mark)
    if(index == 3):
        print("Harry")  
print("\n")

# string

string = ["apple", "banana", "grapes", "kiwi"]

for index, fruit in enumerate(string):
    print(index, fruit)