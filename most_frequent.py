from collections import OrderedDict
string1= list(input())
string = string1[::-1]
di = OrderedDict()
for i in range(len(string)):
  di[string[i]] = di.get(string[i],0)+1 
list1= max(list(di.values()))
max_char=""
for i in di.keys():
  if di[i]==list1:
    max_char=i 
    break 
print(max_char)
  