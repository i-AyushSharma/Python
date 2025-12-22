class person:
    name = "Rohan"
    age = 20
    occupation = "Software Developer"
    def info(self):
        print(f"{self.name} is {self.age} years old and currently is an {self.occupation}")

a = person()
print(a.name)
a.occupation = "Advocate"
a.name = "Ayush"
a.age = 24
print(a.occupation)

b = person()
b.name = "Nikita"
b.age = 28
b.occupation = "Accountant"

c = person()

a.info()
b.info()
c.info()