for i in range (12):
    if(i==10):
        break
    print(" 5 X ",i+1,"=", (5 * (i+1)))
print ("loop breaks")

for i in range (12):
    if(i==10):
        print ("loop breaks")
        continue
    print(" 5 X ",i,"=", (5 * i))