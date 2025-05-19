print ("This is Fibonacci series using while loop !")

n = int(input('Enter: '))

a = 0
b = 1

print ("[",a,"]:",a)
print ("[",b,"]:",b)

i = 0

while(i<=n):
    c = a+b
    print ("[",i+2,"]:",c)
    a = b
    b = c


    i += 1