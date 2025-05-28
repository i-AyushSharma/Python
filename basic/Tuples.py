tup = (1)
print(type(tup), tup) #Identifies as Integer
Tup = (1,)
print(type(Tup), Tup) #Identifies as Tuple

t = (3, 34 ,5, 456, 675)
print(t[0])
print(t[-1])

x = input("Enter the no.:")
if x in t:
    print(x, "is present in tuple")
else:
    print(x, "is not present in tuple")

#Ttples are IMMUTABLE

t2 = t[2:]
print(t2)