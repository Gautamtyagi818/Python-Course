from functools import reduce

l = [676, 8, 9, 556, 87, 7, 5, 6545, 88675, 789, 876]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))

