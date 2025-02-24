with open("this.text") as f:
    content1 = f.read()

with open("poem.text") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes, these files are identiical")  

else:
    print("No, these files are not identical")      
