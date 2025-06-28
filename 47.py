st =input("Enter a string :")
words=st.split(" ")
coding =False

if(coding):
        nwords=[]
        for word in words:     
            if(len(st)>=3): 
                r1="dsa"
                r2="jks"
                stnew=r1 +word[1:]+word[0]+r2
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))
else:
    # pass
    nwords=[]
    for word in words:     
            if(len(st)>=3): 
               stnew=word[3:-3]
               stnew=stnew[-1]+stnew[:-1]
               nwords.append(stnew)
            else:
                nwords.append(word[::-1])
            print(" ".join(nwords))