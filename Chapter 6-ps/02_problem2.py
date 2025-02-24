marks1 = int(input("enter maths marks :"))
marks2 = int(input("enter phy marks :"))
marks3 = int(input("enter chem marks :"))

#  check for total  percentage
total_percentage = 100*(marks1 + marks2 + marks3)/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass")
else:
    print("you are fail. try again in next year :", total_percentage)    

