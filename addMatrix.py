print ("This is Addition of Matrix (nested list)")

a = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]

b = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]

c = []

for x in range(len(a)):
    
    s = []
    
    for y in range(len(b)+1):

        n = a[x][y] + b[x][y]

        s.append(n)

    c.append(s)

print(c)        