print ("This is Prime numbers 1-100")


for n in range(1,101):
    count = 0

    for i in range(1,n+1 ):
        if n % i == 0:
        
            count += 1

    if count == 2:
        print(n)
    