with open("log.text") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes, python is present in the line no: {lineno}")    
        break
    lineno += 1

else:
    print("No, python is not present in the list")  