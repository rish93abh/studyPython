import random

grin = "\N{grinning face}"
smil = "\N{slightly smiling face}"
wink = "\N{winking face}"

def machine(lst):
    a = random.choice(lst)
    return a

def win(a,b,c):
    if a == b or b == c or a == c:
        return 2

    elif a == b and b == c:
        return 3
    else:
        return 0

lst1 = [grin,smil,wink]
lst2 = [wink,grin,smil]
lst3 = [smil,wink,grin]

x = int(input('How many attempts: '))
score = 0

for i in range(x):

    slot1 = machine(lst1)
    slot2 = machine(lst2)
    slot3 = machine(lst3)

    print(f'\n{slot1}|{slot2}|{slot3}')
    
    w = win(slot1,slot2,slot3)

    print('Score: ',w)
    
    score = score + w


print('\nYour total score:',score)


