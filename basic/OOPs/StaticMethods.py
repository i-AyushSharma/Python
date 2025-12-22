class Math:
    def __init__(self, num):
        self.num = num

    def addtoNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b
    
a = Math(6)
a.addtoNum(6)
print(a.num)
print(Math.add(5, 7))