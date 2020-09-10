def gcd(a,b):
    while b:
        a,b= b, a%b 
    return a 
li=[3,21,111,123,24,12]
li.sort()
num1=li[0]
num2=li[1]
hcf= gcd(num1,num2)
for i in range(2,len(li)):
    hcf = gcd(hcf,li[i])
product = 1 
for i in range(len(li)):
    product*=li[i]
print("HCF: ",hcf)
print("LCM: ",product//hcf)