a = [12, 56, 32, 98, 12, 45, 1, 6]

# for mark in a:
#     print(mark)
#     if(index == 3):
#         print("Harry")
#     index += 1

for index, mark in enumerate(a, start = 1):
    print(mark)
    if(index == 3):
        print("Harry")