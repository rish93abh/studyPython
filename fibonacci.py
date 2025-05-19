print ("This is Fibonacci series !")

n = int(input('Enter which term: '))

a = 0
b = 1


for i in range(n):
    c = a + b
    a = b
    b = c

print (a)



input()