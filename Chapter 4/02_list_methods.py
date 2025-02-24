friends = ["Apple", "Orange", 5, 3.076, False, "Akash", "Rohan"]
print(friends)

friends.append("Herry")
print(friends)

l1 = [3, 1, 8, 67, 56, 34]
l1.sort()
print(l1)

l1 = [3, 1, 8, 67, 56, 34]
l1.reverse()
print(l1)

l1 = [3, 1, 8, 67, 56, 34]
l1.insert(3, 6666)             # insert 6666 such that its index ain the list is is 3
print(l1)

l1 = [3, 1, 8, 67, 56, 34]
value = l1.pop(3)
print(value)
print(l1)

l1 = [3, 1, 8, 67, 56, 34]

l1.remove(67)            
print(l1)