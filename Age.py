dob= list(map(int,input().split(":")))
todays=list(map(int,input().split(":")))
dob.reverse()
todays.reverse()
if dob[0]<todays[0]:
    if dob[1]< todays[1]:
        print(str(todays[0]-dob[0])+" Years",end=" ")
        print(str(todays[1]-dob[1])+" Months",end=" ")
        print(str((30-dob[2])+todays[2])+" Days",end=" ")      
    elif dob[1]>todays[1]:
        print(str(todays[0]-dob[0]-1)+" Years",end=" ")
        print(str(12-todays[1])+" Months",end=" ")
        print(str(365-((30-todays[2])+dob[2])) + " Days", end=" ")
    else:
        print(str(todays[0]-dob[0])+" Years",end=" ")
        print("0 Months",end=" ")
        print(str(abs(todays[2]-dob[2]))+"Days")
elif dob[0]==todays[0]:
    print("same year born")


