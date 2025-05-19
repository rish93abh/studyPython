import random

def hang():
    print('\n*** WELCOME TO HANGMAN ! ***')

  
    print('\nYou have to guess the correct word.\n(3 Wrong choices and Game Over)')
    lst = ['superman','batman','spiderman','thor','ironman','flash','aquaman','daredevil']

    word = random.choice(lst)
    l = len(word)


    if word == 'superman':
        print('*Hint: Luthor*')
    elif word == 'batman':
        print('*Hint: Joker*')
    elif word == 'spiderman':
        print('*Hint: Venom*')
    elif word == 'thor':
        print('*Hint: Gorr*')
    elif word == 'ironman':
        print('*Hint: Mandarin*')
    elif word == 'flash':
        print('*Hint: Zoom*')
    elif word == 'aquaman':
        print('*Hint: Manta*')
    elif word == 'daredevil':
        print('*Hint: Fisk*')                     

    lives = 3

    hidden = '_' * l
    print('\n\nYour word :',hidden)

    def pos(i,text):
        j = word.index(i)
        h = text[:j] + i + text[j+1:]
        return h

    result = ''
    count = 0
    for i in range(1,l*2):
        userInp = input('\nEnter the letter: ')
        if userInp.casefold() in word:

            print(f'\nYES, {userInp} is present in the word.')
            count += 1
            if count == 1:
                result = pos(userInp,hidden)
            elif count >1:
                result = pos(userInp,result)

            print(result)

            if result == word:
                print("CORRECT ! You have guessed the word.")
                break

        else:
            print(f'\nNO, {userInp} is not in the word.')
            lives = lives - 1
            print(f'\n*** You have {lives} wrong choice left.*** ')

            if lives == 0:
                print('\nGAME OVER\nThe word was:',word)
                break


