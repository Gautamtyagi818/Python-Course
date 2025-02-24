# n = int(input("Enter the number :"))
# sum = int(n*(n+1)/2)
# print(sum)

# using while loop

n = int(input("Enter the number :"))

sum  = 0
i = 1

while(i<=n):
    sum += i
    i += 1

print(sum)