a = 9
b = 6
gmean1 = (a*b)/(a+b)
print(gmean1)
c = 3
d = 1
gmean2 = (c*d)/(c+d)
print(gmean2)

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

calculateGmean(a, b)
if(a>b):
    print("first no. is greater")
else:
    print("second no. is greater or equal")

def isGreater(a, b):
    if(a>b):
        print("first no. is greater")
    else:
        print("second no. is greater or equal")
       
calculateGmean(c, d)
isGreater(c, d)

def isLesser(a, b):
    pass
