# def average (a=9,b=8):
#     print("The  average is ", (a+b)/2)
    
# average(3,4)


def average (*numbers):
    sum = 0
    for i in numbers:
        sum =sum+i
    print ("Average is :",sum /len(numbers))
    
average(5,6,7,2)