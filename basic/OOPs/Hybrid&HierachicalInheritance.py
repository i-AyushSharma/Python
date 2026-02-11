#Example of Hybrid Inheritance
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass

class Derived3(Derived1, Derived2):
    pass

#Hierachical Inheritance
class BaseClass:
    pass
class D1(BaseClass):
    pass