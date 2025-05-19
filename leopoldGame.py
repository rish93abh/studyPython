
import morseCode
import calc
import Hangman
import CaeserCipher as caeser


print('\n***** Leopold *****')
print('\n\nHello, Welcome to Leopold.\nTo begin, please enter your name.')
name = input(' > ')

nope = "Sorry, I'm not able to understand that."

print("\n\nHello",name,'! \nYou can choose any task from below.')

def mainMenu():
    print('\n1 : Morse Code Translate\n2 : Calculation on 2 numbers\n3 : ASCII code\n4 : Hangman (word guessing game)\n5 : Caeser Cipher')

    taskNo = int(input('\nType in the number with the task :\n > '))

    if taskNo == 1:
        print('\n*** Morse Code Translate ***')

        if __name__ == '__main__':
            morseCode.M()


    elif taskNo == 2:
        print('\n*** Calculation on 2 numbers ***')  
        
        if __name__ == '__main__':
            calc.whpr()

    elif taskNo == 3:
        def asc():
            print('\n***ASCII code generator***')
            inp_ASC = input('Enter here: ')
            print(inp_ASC,':',ord(inp_ASC))

            asc_r = input('\nAnother try ?\n> y/n: ')
            if asc_r == 'y':
                asc()
            elif asc_r == 'n':
                print('\nGoodbye!')
                quit()
        asc()

    elif taskNo == 4:

        if __name__ == '__main__':
            Hangman.hang()

    elif taskNo == 5:
        if __name__ == '__main__':
            caeser.ciph()


    else:
        print('\nInvalid input.\nPlease try again.\n')
        mainMenu()
    
mainMenu()


input()