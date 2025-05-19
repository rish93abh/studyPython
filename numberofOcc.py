print ("This is Number of occurence of data in a list")

#a = ['apple','banana','blueberry','orange','apple','grapes','mango','mango','apple']

a = input('Enter names seperated by space :').split()

b = []

for x in range(len(a)):
    
    if a[x] not in b:

        n = a.count(a[x])

        print(a[x],':',n)

        b.append(a[x])