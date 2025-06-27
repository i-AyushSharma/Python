s = {1, 2, 3, 6}
s2 = {5, 7, 9, 8}
print(s.union(s2))
s.update(s2)
print(s, s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid", "Seoul", "Kabul"}
cities3 = cities.intersection_update(cities2)
print(cities)

cities4 = cities.symmetric_difference(cities2)
print(cities4)

cities5 = cities2.difference(cities)
print(cities5)

print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))

print(cities.add("Hamsburg"))
print(cities.remove("Tokyo"))
print(cities.discard("Tokyo2"))
item = cities.pop()
print(item)
del cities