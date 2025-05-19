print ("This is Transpose of Matrix")


a = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]

b = []

for x in range(len(a)+1):

    s = []

    for y in range(len(a)):      

        n = a[y][x]
        s.append(n)

    b.append(s)


print(b)        
