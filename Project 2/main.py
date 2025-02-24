# Guess the number

import random9

n = random.randint(1, 100)
guess = 1
a = -1
while(a != n):
    a = int(input("Enter the number :"))
    if(a<n):
        print("higher number please")
        guess += 1
    elif(a>n):
        print("lower number please")
        guess += 1

print(f"you have guess the number {n} in {guess} attempt")