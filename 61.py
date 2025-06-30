class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is c++ ")

e1=Employee("Tony Stark",42)
e1.showDetails()
e2=Programmer("Tony",34)
e2.showLanguage()
e2.showDetails()