
menu = {
    'burger':80,
    'pizza':120,
    'sandwich':70,
    'momos':50,
    'samosa':20,
    'kachori':15,
    'noodles':120,
    'vada pav':30,
    'pav bhaji':80
    }

total = {}

def bill(item,price):
    
    total.update({item:price})
    return total


def dots(a,b):
    c = 20 - len(a) - len(str(b))
    return c

def sumofValues(d):
    lst = []
    for i in d:
        lst.append(d[i])
    return sum(lst)

print('\n  ------ MENU ------')
print('\nITEM','.'*dots('ITEM','PRICE'),'PRICE')

for i in menu:
    print(i.title(),'.'*dots(i,menu[i]),menu[i])

def add_item():
    item = input('\nEnter the item name: ')

    if item not in menu:
        print('Invalid input')
        add_item()
    elif item in menu:
        dish = item.lower()
        print('You have chosen:',item.title(),'-',menu[dish])
        bill(item,menu[dish])

    more = input('\nDo you want to add more ?\nY or N: ')

    if more == 'y':
        add_item()

    elif more == 'n':
        print('Your total bill is:')
        for x in total:
            print(x.title(),'.'*dots(x,total[x]),total[x])
        print('_'* 22)
        print('TOTAL','.'*dots('total',sumofValues(total)),sumofValues(total))

    else:
        print('Invalid input')

add_item()

