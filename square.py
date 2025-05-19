print ("This is another")
import math

a = int(input("Enter value of a :"))

b = int(input("Enter value of b :"))

c = int(input("Enter value of c :"))

D = b*b - 4*a*c

#x = (-b + (b*b - 4*a*c)sq.root) / 2*a

x1 = (-b + math.sqrt(D)) // (2*a)

x2 = (-b - math.sqrt(D)) // (2*a)

print("Roots are (",x1,x2,")")




input()