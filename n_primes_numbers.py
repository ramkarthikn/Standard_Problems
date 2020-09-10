def nextPrime(num):
    while True:
        num+=1 
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return num 
prime_list=list() 
def n_prime(N):
    count, num= 1,1
    while count<=N:
        num= nextPrime(num)
        prime_list.append(num)
        count+=1 
    return prime_list
print(n_prime(90))

