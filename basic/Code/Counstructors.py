class person:
    def __init__(self, name, occ):
        print("Hey I'm a person")
        self.name = name
        self.occ = occ
        
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Ayush", "Student")
b = person("Harry", "Youtuber")
a.info()
b.info()