print ("This is Factors & Prime !")

n = int(input('Enter the number: '))
count = 0



for i in range(1,n+1):
    if n % i == 0:
        count += 1
        print(i)
             

if count == 2:
    print(n,'is a Prime number.')
else:
    print(n,'is not a Prime')    

input()    