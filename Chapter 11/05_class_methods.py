class Employee:
    a = 1
    @classmethod     # directly access class attribute
    def show(cls):
        print(f"The attribute of class is {cls.a}")

o = Employee()        
o.a = 45
o.show()