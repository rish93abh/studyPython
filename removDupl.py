print ("This is Removing duplicates in list")


a = [3,4,8,3,2,45,98,2,7,8,87,98,115]
NewA = []


for x in a:
    if x not in NewA:
        NewA.append(x)

print(NewA)        