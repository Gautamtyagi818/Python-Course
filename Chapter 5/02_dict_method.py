marks ={
    "Harry" : 100,
    "subham" : 23,
    "Rohit" : 56,
    0 : "kapil"
}    

print(marks.items())
print(marks.keys()) 
print(marks.values())
marks.update({"Harry": 99, "Ranuka": 100})
print(marks)
# print(marks.get("Harry2"))  # prints None
# print(marks["Harry2"])   # return an error

value = marks.pop("Harry")
print(value)
print(marks)

marks.clear()
print(marks)




