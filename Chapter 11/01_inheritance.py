class Employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

# class programer:
#     company = "ITC  InfoTech"
#     def show(self):
#         print(f"the name of programer is {self.name} and the salary is {self.salary}")

#     def show(self):
#         print(f"the name of programmer is {self.name} and he is good with {self.language} language")

class programer(Employee):
    company = "ITC  InfoTech"
    def show(self):
        print(f"the name of programmer is {self.name} and he is good with {self.language} language")



a = Employee()
b = programer()

print(a.company, b.company)
