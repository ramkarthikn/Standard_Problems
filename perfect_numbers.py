n1, n2 = list(map(int,input().split()))
li= list(range(n1,n2+1))
sum1=0
perfect_number=[]
for i in range(0,len(li)):
    for j in range(1,li[i]):
        if li[i]%j==0:
            sum1+=j
    if sum1==li[i]:
        perfect_number.append(li[i])
    sum1=0
print(perfect_number)


