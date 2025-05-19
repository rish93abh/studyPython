import re

print('This is Extracting random numbers from demo.txt file\n\n')

filename = open('demo.txt')

lst = list()
lst2 = list()


for lines in filename:
    a = lines.rstrip()
    
    n = re.findall('[0-9]+',a)
    
    if n != []:

        lst = lst + n


for i in lst:
    lst2.append(int(i))

print(sum(lst2))

