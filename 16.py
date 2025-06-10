s=int(input("Enter your value ::"))
match s:
    case 0:
        print("case 0")
    case 1 :
        print("Case 1")
    case _ if(s!=33):
        print(s,"is not equal to 33")
    case _ if(s==3):
        print(s)
    case _:
        print(s)