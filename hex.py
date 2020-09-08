n= int(input())
li=list()
di= {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
while n>0:
    r = n%16
    if r in di.keys():
        li.append(di[r])
    else:
        li.append(r)
    n=n//16
li.reverse()
print("".join(list(map(str,li))))
