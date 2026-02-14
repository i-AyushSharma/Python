import functools
import time

@functools.lru_cache(maxsize = None)
def fx(n):
    time.sleep(3)
    return n*n

print(fx(2))
print("done for 2")
print(fx(4))
print("done for 4")
print(fx(3))
print("done for 3")

print(fx(2))
print("done for 2")
print(fx(4))
print("done for 4")
print(fx(3))
print("done for 3")