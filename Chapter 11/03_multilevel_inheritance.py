class Employee:
    a = 1
class programer(Employee):
    b = 2
class Manager(programer):
    c = 3

o = Employee()    
print(o.a)

o = programer()    
print(o.a, o.b)

o = Manager()    
print(o.a, o.b, o.c)