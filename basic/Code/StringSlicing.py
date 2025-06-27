fruit = "Mango"
lengthofstring = len(fruit)
print(lengthofstring)
print(fruit[0:3])
print(fruit[:4]) #Here python will automatically put 0 before colon(:) 
print(fruit[0:]) #Here python will automatically put the length of the string after colon(:)
print(fruit[:]) #Here python will automatically put both 0 and length of string
print(fruit[:-3]) #here python automatically subtracts the given number(only negative int) from the length of string
print(fruit[-3:-1]) #len(fruit) - 3 to len(fruit) - 1

#Quick Quiz
nm = "Haary"
print(nm[-4:-2])