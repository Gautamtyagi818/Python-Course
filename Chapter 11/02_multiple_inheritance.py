class Employee:
    company = "ITC"
    name = "Ashu"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")

class coder:
    language = "python"
    def printlanguage(self):
        print(f"Out of all the language here is your language : {self.language}")

class programer(Employee, coder):
    company = "ITC InfoTech"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")



a = Employee()
b = programer()

b.show()
b.printlanguage()
b.showlanguage()
