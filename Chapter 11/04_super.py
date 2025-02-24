class Employee:
    def __init__(self):
        print("construster of Employee:")
    a = 1
class programer(Employee):
    def __init__(self):
        print("construster of programer:")
    b = 2
class Manager(programer):
    def __init__(self):
        super().__init__()
        print("construster of Manager:")
    c = 3

# o = Employee()    
# print(o.a)

o = programer()    
print(o.a, o.b)

# o = Manager()    
# print(o.a, o.b, o.c)