print ("This is Palindrome of numbers !")

n = int(input("Enter:"))

m = n
rev = 0

while(m>0):
    r = m % 10
    rev = rev * 10 + r
    m = m // 10


if(rev == n):
    print ('It is a palindrome: ',n,'=',rev)  
else:
    print('It is not a palindrome: ',n,'!=',rev)  



input()
