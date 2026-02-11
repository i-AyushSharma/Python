import time

def usingWhile():
    i = 0
    while i<5000:
        i = i + 1
        print(i)
def usingFor():
    for i in range(5000):
        print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
print(t1)
print(time.time() - init)

print(4)
time.sleep(3)
print("This will print after 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%M-%D %H:%M:%S", t)
print(formatted_time)