
# This is the lecture about the conditional statements
a=int (input("Enter your age :: "))
print("Your age is ::",a)
print(a>18)
print(a<18)
print(a<=18)
print(a>=18)

# If else py
if(a>18):
    print("you can drive")
else:
    print("You cannot drive")
    
    
# This is elif loop
if(a>18):
    print("You can drive")
elif(a==0):
    print("Are you born or not ")
    
else:
    print("You can drive") 

#Nested python loop 
if(a>0):
    if(a>18):
        print("You can drive ")
else:
    print("you can't ")