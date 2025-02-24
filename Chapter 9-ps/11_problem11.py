
with open("old.text") as f:
    content = f.read()

with open("Renamed_by_python", "w") as f:
    f.write(content)
 
