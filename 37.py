def func1():
    try:
        l=[1,3,4,5]
        i=int (input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("some exceeption is occurred")
    finally:
        print("I am always executed because of finally")
    print("sonon")
    
x=func1()
print(x)