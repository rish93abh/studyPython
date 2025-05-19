print ("This is Maximum, minimum !")

n = int(input("How many numbers ?: "))
max = 0
min = float('inf')
i = 0


print("Enter the",n,"numbers here:")

while(i<n):
    i = i + 1
    a = int(input(''))
    if(a>max):
        max = a
    elif(a<min):
        min = a

print(max,"is maximum and",min,"is minimum")    
