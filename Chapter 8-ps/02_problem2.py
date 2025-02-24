def F_to_C(f):
    return 5*(f-32)/9

f = int(input("Ente temperature in F :"))
c = F_to_C(f)
print(f"{round(c, 2)} degree C")
