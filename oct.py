n= int(input())
li=list()
while n>0:
    r = n%8
    li.append(r)
    n=n//8 
li.reverse()
print("".join(list(map(str,li))))