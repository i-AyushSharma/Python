class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    @classmethod #To change class variable decorator is used
    def changeCompany(cls, newCompany): 
        cls.company = newCompany

e1 = Employee()
e1.name = "Ayush"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)