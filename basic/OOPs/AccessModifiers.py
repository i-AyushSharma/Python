class Employee:
    def __init__(self):
        self.__name = "Roshan"

a = Employee()
# print(a.__name) #Cannot be accessed directly
print(a._Employee__name) #Can be accessed indirectly 

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self): #Protected method
        return "CodeWithHarry"

class Subject(Student): #Inherited class
    pass

obj =Student()
obj1 = Subject()

print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())