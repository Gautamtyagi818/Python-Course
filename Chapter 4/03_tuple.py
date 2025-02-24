a =  (1, 55, "Rohan", False, 55, "Shivam")
print(a)

# a[0] = 7    # it is not acceptable. tuple is immutable
no =a.count(55)
print(no)
  
i = a.index(55)
print(i)

print(len(a))  

i = a[1:3]
print(i)

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)
