try:
    a = int(input("Enter a number :"))
    print(a)

except Exception as e:
    print(e)
    
finally:
    print("i'm inside a finally")  # finally block chalega hi chalega  