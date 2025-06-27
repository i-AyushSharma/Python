#Break Statement

for i in range(12):
    if(i == 10):
        break
    print("5 x", i, "=", i * 5)

#Continue Statement

for i in range(12):
    if(i == 10):
        print("skip the iteration") 
        continue
    print("5 x", i, "=", i * 5)
