cube = lambda x : x*x*x

print(cube(3))

# MAP

l = [2, 4, 5, 6, 3]
newl = []
for item in l:
    newl.append(cube(item))
print(l)
print(newl)

newl2 = map(cube, l)
print(newl2)
print(list(newl2))

# FILTER

filter_function = lambda a : a>4
newl3 = filter(filter_function, l)
print(list(newl3))

# REDUCE

from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
mysum = lambda x, y: x + y
sum = reduce(mysum, numbers)
print(sum)