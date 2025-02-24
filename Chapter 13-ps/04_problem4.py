def divisible5(n):
    if(n%5 == 0):
        return True
    return False
a = [676, 8, 9, 556, 87, 7, 5, 6545, 88675, 789, 876]

f = list(filter(divisible5, a))
print(f)