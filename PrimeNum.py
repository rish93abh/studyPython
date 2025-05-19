print ("This is Prime numbers !")


n = int(input("Enter the number upto which you require prime numbers :"))
a = 11

pr = {1,2,3,5,7}

for item in pr:
    print(item)

while(a<=n):
    if(a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0):
        print(a)    
    a+=1


input()