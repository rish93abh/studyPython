print ("This is Salary calculation")

a = [int(x) for x in input('\n\nEnter working hours (seperated by space):').split()]

print('\n\nYou entered :',a)
total = sum(a)

wage = int(input('Enter hourly wage :'))
print('Total hours :',total)
print('Total salary :',total*wage)

