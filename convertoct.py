octal= input()
li = list(octal)
li = list(map(int,li))
li.reverse()
number=0
for i in range(len(li)):
    number+= li[i]*8**i 
print(number)