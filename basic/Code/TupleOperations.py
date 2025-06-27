countries = ("Spain", "italy", "India", "England", "Germany")
helo = list(countries)
helo.append("Russia") #Add Item
helo.pop(1) #Remove Item
helo[3] = "Finland" #Change Item
countries = tuple(helo)
print(countries)

countries2 = ("India", "Pakistan", "China")
countries3 = ("Sri Lanka", "Bangladesh", "Afghanistan")
southeastasia = (countries2 + countries3)
print(southeastasia)

tuple = (0, 1, 2, 3, 4, 3, 2, 3, 3)
rez = tuple.count(3)
print("Count of 3 in tuple is:", rez)
# res = tuple.index(3)
res = tuple.index(3, 4, 8)
