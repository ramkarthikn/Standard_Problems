hexa = input()
li = list(hexa)
di= {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
li.reverse()
number=0
for i in range(len(li)):
    if li[i] in di.keys():
        number= number + di[li[i]]*16**i 
    else:
        number= number+ int(li[i])*16**i 
print(number)

