print(' This is Resetting password')


newP = input('Enter new password: ')
rep = input('Confirm new password: ')

# admin
# Admin

if newP == rep:
    print('Passwords matched.')

else:
    if newP.casefold() == rep.casefold():
        print('Please check cases and try again')

    else:
        print('Password do not match')    

