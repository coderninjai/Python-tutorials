with open ('myfile.txt','r') as f:
    print(5)
    
    f.seek (10)
    print(f.tell())
    data=f.read()
    print(data)
    
# This is not working