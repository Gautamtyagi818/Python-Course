try:
    a = int(input("Enter a number :"))
    print(a)

except ValueError as v:
    print("heyyyyy")
    print(v)
except Exception as e:
    print(e)

print("thank you!")    