
din = '''
   ---_ ......._-_--.
      (|\ /      / /| \  \
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*\
       `/'\__/      \ _ _ \*\
      /^|            \ _ _ \* 
     '  `             \ _ _ \      
                       \_
'''
print(din)
print('\n\n*** Welcome to Dino Pizza Deliveries***')

name = input('\n\nPlease enter your name ?: ')
size = input(f'Hi {name}, What size pizza do you want? \nS, M or L: ')
pepporoni = input('\nDo you want pepporoni in pizza ?: Y or N: ')
cheese = input('\nDo you want extra cheese on pizza ?: Y or N: ')

bill = 0
siz = ''
ifPep = ''
ifChees = ''

if size.lower() == 's':
    bill += 50
    siz = 'Small size pizza'
elif size.lower() == 'm':
    bill += 75
    siz = 'Medium size pizza'
elif size.lower() == 'l':
    bill += 100
    siz = 'Large size pizza'
else:
    print('Invalid input')


if pepporoni.lower() == 'y':
    bill += 20
    ifPep = ' Extra pepporoni added'
elif pepporoni.lower() == 'n':
    ifPep = ' No Extra pepporoni'
else:
    print('Invalid input')

if cheese.lower() == 'y':
    bill += 20
    ifChees = ' Extra cheese added'
elif cheese.lower() == 'n':
    ifChees = ' No Extra cheese'
else:
    print('Invalid input')


print('\n\n**Billing details**\nCustomer Name: ',name)
print(siz,'|',ifPep,'|',ifChees)
print('Total amount: Rs.',bill)

