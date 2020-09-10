from itertools import combinations 
n1,n2 = list(map(int,input().split()))
li=list()
for i in range(n1,n2+1):
    li.append(i)
count=0
prime_list=list()
for i in range(len(li)):
    if li[i]==1:
        continue
    else:
        for j in range(2,li[i]//2+1):
            if li[i]%j==0:
                count+=1
        if count==0:
            prime_list.append(li[i])
        count=0
prime_set= list(combinations(prime_list,2))
twin_prime_list= []
for i in range(len(prime_set)):
    if abs(prime_set[i][1]- prime_set[i][0]==2):
        twin_prime_list.append(prime_set[i])
print(twin_prime_list)


