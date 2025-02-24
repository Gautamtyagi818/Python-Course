# f = open("file.text")
# print(f.read())
# f.close()

# The same can be written using the  statement like this :

with open("file.text") as f:
    print(f.read())

# you don't have explicitly to close the file    