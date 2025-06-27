l = [1, 2, 45, 5, 89, 43]
print(l)
l.append(67)
l.sort()
l.sort(reverse=True)
l.reverse()
print(l.index(45))
print(l.count(5))
m = l.copy()
m[0] = 0
print(m)
l.insert(3, 8665)
# x = [46, 456, 3245, 678]
# l.extend(x)
k = m + l