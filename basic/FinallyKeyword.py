try:
    l = [1, 4, 5, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occured")

finally:
    print("I am always executed")

def func1():
    try:
        l = [1, 4, 5, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    
    finally:
        print("I am always executed")
    # print("I am always executed")

x = func1()
print(x)