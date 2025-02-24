class Demo:
    a = 4

O = Demo()   
print(O.a)   # instance attribute is not present
O.a = 0
print(O.a)   # instance attribute is present so priority first 
# for instance attribute