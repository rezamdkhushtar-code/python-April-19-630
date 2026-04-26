print(True and True)
print(2==2 and 1>=1)
print("Test"=="hello" and True)

logged_in =False
print(not(logged_in))

if(2==2):
    print("This is True")

else:
    print("This is False")


gpa = 0

if (gpa>=3.7 and gpa<=4):
    print("This is A+")


elif (gpa>=3.3 and gpa<=3.69):
    print("This is A")

elif (gpa>=3 and gpa<=3.29):
    print("Thos is B+")

if gpa==3.45:
    print("lucky")
elif gpa==4:
    print("topper")



elif (gpa>=2.5 and gpa<=2.99):
    print("This is B")

elif (gpa>=2 and gpa<=2.49):
    print("This is C+")

elif (gpa>=0 and gpa<=1.9):
    print("This is C")

else:
    
    print("This is invalid")




gender ="F"
if gender =="M":
    print("Male")
else:
    print("Female")


data ="Male" if gender == "M" else "Female"
print(data)


