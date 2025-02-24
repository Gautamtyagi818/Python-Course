word = "Donkey"

with open("file.text", "r") as f:
    content = f.read()

newcontent = content.replace(word, "######")  

with open("file.text", "w") as f:
    content = f.write(newcontent)