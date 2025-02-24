words = ["donkey", "bad", "gande"]

with open("file.text", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))  

with open("file.text", "w") as f:
    content = f.write(content)