n1= int(input("enter the degree for 1st Polynomial: "))
n2= int(input("enter the degree for 2nd Polynomial: "))
li1=list()
li2=list()
print("First Polynomial")
for i in range(n1):
    print("Enter degree of "+str(n1-i)+" term")
    li1.append(int(input()))
li1.reverse()
print("")
print("Second Polynomial")
for i in range(n2):
    print("Enter degree of "+str(n2-i)+" term")
    li2.append(int(input()))
li1.reverse()
li2.reverse()
print(li1)
print(li2)
minimum=None
maximum=None
if len(li1)>len(li2):
    minimum= li2
    maximum= li1
elif len(li1)<len(li2):
    minimum= li1
    maximum= li2
quotient_sum=[]
quotient_product=[]
for i in range(len(maximum)):
    if i<=len(minimum)-1:
        quotient_sum.append(maximum[i]+minimum[i])
    else:
        quotient_sum.append(maximum[i])
print(quotient_sum)