a = int(input("Enter your age :"))

# if elif else ladder

if(a>=18):
    print("you are the above of age of consent")
    print("this is good for you.")

elif(a<0):
    print("you are entering invalid negative age consent") 

elif(a==0):
    print("you are entering 0 which  is not  a valid consent") 

else:
    print("you are below the age coonsent ")

print("End of the program!")