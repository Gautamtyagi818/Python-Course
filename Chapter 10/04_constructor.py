class Employee:
    languagen = "python"
    salary = 13000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def getinfo(self):
        print(f"the language is{self.language}. The salary is{self.salary}")   
    
    @staticmethod
    def greet(self):
        print("good morning")
        
harry  =  Employee("harry",130000, "javascript ")     
# harry.name = "harry"
print(harry.name, harry.language, harry.salary)

# Rohan = Employee()

    