class Emplpoyee:
    name = "Harry"
    language = "python"      # This is an class attribute 
    salary = 1200000

harry = Emplpoyee() 
harry.name = "Harry"        # This is an instance attribute 
print(harry.name, harry.language, harry.salary)

Rohan = Emplpoyee()    
Rohan.name = "Rohan Roro "      
print(Rohan.name, harry.language, harry.salary)

# Here name is instance attribute and salary and language are class 
# attributes they directly belong to the class