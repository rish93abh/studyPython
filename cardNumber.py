print ('        This is Card payment receipt')

n = input('Enter card no: ')

last4 = n[12:]

f = 'X'*4 + ' ' 

display = f*3 + last4

if len(n) != 16 or n.isdigit() == False:
    print('Invalid card number.\nPlease try again.')

else:
    print (display)

input()