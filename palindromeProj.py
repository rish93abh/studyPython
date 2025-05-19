print(" This is palindrome project")


p = input('Enter: ')
# Race Car

if ' ' in p:
    r = p.replace(' ','')
    # RaceCar (removing space)

else:
    r = p

Rlower = r.casefold()   # racecar
newS = Rlower[::-1]     # racecar

if newS == Rlower:
    print(p,'is already a palindrome.')

else:
    print(p,'is not a palindrome,')
    x = Rlower + newS
    print('However,',x,'is now a palindrome.')