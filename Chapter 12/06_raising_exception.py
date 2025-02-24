a = int(input("Enter first number"))
b = int(input("Enter second number"))

if(b==0):
    raise ZeroDivisionError("heyyy our program is non ment to divide number by zero")
else:
    print(f"the division a/b is {a/b}")    