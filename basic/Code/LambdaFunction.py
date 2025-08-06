# def double(x):
#     return x*2

double = lambda x:x*2
cube = lambda x:x*x*x
avg = lambda x, y, z: (x + y + z)/3

print(double(3))
print(avg(4, 3, 11))

multply = lambda x, y: print(f"{x} x {y} = {x*y}")
multply(3, 6)

#Eg

def apl(fx, value):
    return value + fx(value)

print(apl(cube, 4))