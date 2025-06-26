a=input("Enter the number :")
print(f"multiplication table of {a } is :")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {i*int (a)}")
    
except Exception as e:
    print("Invalid input")
    print(e)
    
print("Some imp lines of code ")
print("end of the program ")