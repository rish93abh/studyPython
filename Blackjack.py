import random


user = input('Please enter your name: ')
comp = 'Computer'

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def draw():
    r = random.choice(cards)
    return r

userCards = []
compCards = []

def deck(r,lst):
    lst.append(r)
    return lst

def morethan21(lst,n):
    a = sum(lst)
    if a > 21:
        print(f'Total score is {a}. {n} loses.')
        quit()


comp1 = draw()
print(f'\n{comp} deck.')
print(deck(comp1,compCards))

pick1 = input('\n\t\t\t\tPick your first card. (Press p): ')
if pick1 == 'p':
    r1 = draw()
    print(f'\t\t\t\t{user} deck.')
    print('\t\t\t\t',deck(r1,userCards))


comp2 = draw()
print(f'\n{comp} deck.')
print(deck(comp2,compCards))

pick2 = input('\n\t\t\t\tPick your second card. (Press p): ')
if pick2 == 'p':
    r2 = draw()
    print(f'\t\t\t\t{user} deck.')
    print('\t\t\t\t',deck(r2,userCards))



comp3 = draw()
print(f'\n{comp} deck.')
print(deck(comp3,compCards))

morethan21(compCards,comp)

pick3 = input('\n\t\t\t\tPick your third card. (Press p): ')
if pick3 == 'p':
    r3 = draw()
    print(f'\t\t\t\t{user} deck.')
    print('\t\t\t\t',deck(r3,userCards))

morethan21(userCards,user)


if sum(userCards) > sum(compCards):
    print(f'{userCards}\n{user} wins.')

elif sum(userCards) < sum(compCards):
    print(f'{compCards}\n{comp} wins.')

elif sum(userCards) == sum(compCards):
    print('DRAW')
