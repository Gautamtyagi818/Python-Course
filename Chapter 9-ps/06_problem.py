with open("log.text") as f:
    content = f.read()

if("python" in content):
    print("yes, python is present in the list")    

else:
    print("No, python is not present in the list")    