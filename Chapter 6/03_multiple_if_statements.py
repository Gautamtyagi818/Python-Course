a = int(input("Enter your age :"))


# if statement no 1
if(a%2 == 0):
    print("a is even")

# if statement no 2
if(a>=18):
    print("you are the above of age of consent")
    print("this is good for you.")

elif(a<0):
    print("you are entering invalid negative age of consent") 

else:
    print("you are below the age of consent ")

print("End of the program!")