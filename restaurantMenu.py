print('\t\tThis is Restaurant Menu')


item1 = input('Enter 1st item: ')
p1 = input("Enter its price: ")


item2 = input('Enter 2nd item: ')
p2 = input("Enter its price: ")

item3 = input('Enter 3rd item: ')
p3 = input("Enter its price: ")

item4 = input('Enter 4th item: ')
p4 = input("Enter its price: ")

item5 = input('Enter 5th item: ')
p5 = input("Enter its price: ")

dash = ('-')

# len(item1) + len(p1) + n*dash = 50
# n*dash = 50 - len(item1) - len(p1)

print(item1,(40 - len(item1) - len(p1))*dash,p1)
print(item2,(40 - len(item2) - len(p2))*dash,p2)
print(item3,(40 - len(item3) - len(p3))*dash,p3)
print(item4,(40 - len(item4) - len(p1))*dash,p4)
print(item5,(40 - len(item5) - len(p5))*dash,p5)



input()
