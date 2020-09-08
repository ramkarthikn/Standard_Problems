binary= input()
li = list(binary)
li = list(map(int,li))
li.reverse()
number=0
for i in range(len(li)):
    number+= li[i]*2**i 
print(number)

