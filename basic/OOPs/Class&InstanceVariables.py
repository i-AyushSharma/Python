class Employee:
    companyName = "Google"
    noOfEmployes = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployes += 1
    def showDetails(self):
        print(f"The name of the empolyee is {self.name} and the raise amount in {self.noOfEmployes} sized company {self.companyName} is {self.raise_amount}")

emp1 = Employee("Ayush")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()

emp2 = Employee("Haryy")
emp2.showDetails()

emp1 = Employee("Ayush")
Employee.companyName = "Nestle"
emp1.showDetails()
