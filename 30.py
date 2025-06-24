# factorial =5*4*3*2*1
 
# factorial (n)= n*factorial(n-1)

# def factorial(n):
#     if(n==0):
#         return 1
#     else:
#         return n*factorial (n-1)
# print(factorial(5))

# f0=0
# f1=1
# f2=f1+f0
# f(n)=f(n-1)+f(n-2)

# write a program for printing of fibonacci sequence

def fibonacci(n):
    if(n==0):
        return 0
    elif ( n==1):
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)
terms = int(input("Enter how many Fibonacci numbers to print: "))

print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")