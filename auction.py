
print('Hello. Welcome to the auction.')

auction = {}
lst = []

def highest(dic):
    for i in dic:
        x = dic[i]
        lst.append(x)

    return max(lst)

def ke(m,dic):
    for i in dic:
        if dic[i] == m:
            return i


def bidding():
    name = input('Enter your name: ')
    price = int(input('\nEnter bidding price: '))

    auction.update({name:price})

    more = input('\nAre there any more bidders ?\nY or N: ')

    if more == 'y':
        print('\n' * 50)
        bidding()

    elif more == 'n':
        x =  highest(auction)
        for i in auction:
            print(i,':',auction[i])

        n = ke(x,auction)
        print(f'{n} has made the highest bidding with {x}')


bidding()
