a = True
print(a:=False)

num = [1, 2 ,3, 4, 5]
while (n:= len(num)) > 0:
    print(num.pop())

foods = list()
while (food := input("What food do you like?: ")) != "Quit":
    foods.append(food)
print(foods)