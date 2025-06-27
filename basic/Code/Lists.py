marks = [3, 4, 6, "Ayush", True, 6, 67, 667]
print(type(marks))
print(marks[0])
print(marks[1])
print(marks)

print(marks[-3]) #Negative Indexing
print(marks[len(marks)-3]) #Positive Indexing

if "Ayush" in marks:
    print("Yes")
else:
    print("No")

print(marks[0:7:2])

l = [i for i in range(6)]
print(l)
lst = [i for i in range(10) if i%2==0]
print(lst)
