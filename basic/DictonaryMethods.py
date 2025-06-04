ep1 = {122: 45, 123: 89, 567: 60, 456: 90}
ep2 = {232: 87, 345: 43}

ep1.update(ep2)
# ep1.clear()
ep1.pop(232)
ep1.popitem()
print(ep1)
