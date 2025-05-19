print('This is Love Score calculate')

def calculate_love_score(name1,name2):
    
    w1 = 'TRUE'
    w2 = 'LOVE'
    n1 = name1.casefold()
    n2 = name2.casefold()
    both_names = n1 + n2
    
    total1 = 0
    for i in w1:    #TRUE
        i1 = i.casefold()
        a = both_names.count(i1)
        print(f'{i} occurs {a} times')
        total1 += a

    total2 = 0
    for j in w2:    #LOVE    
        j1 = j.casefold()
        b = both_names.count(j1)
        print(f'{j} occurs {b} times')
        total2 += b
        
    print(f'Love Score = {total1}{total2}')        
        
n1 = input('Enter name 1: ')
n2 = input('Enter name 2: ')

calculate_love_score(n1,n2)