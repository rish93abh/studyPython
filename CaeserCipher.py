
def ciph():

    print('This is Caeser Cipher')

    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    def caeser(m,sh,opr):
        for i in m:

            idx = alphabets.index(i)

            if opr == 'encode':
                sm = idx + sh    # adding shift number (encode)
                sm %= len(alphabets)
                return alphabets[sm]
                
            elif opr == 'decode':
                sb = idx - sh    # subtracting shift number  (decode)    
                sb %= len(alphabets)
                return alphabets[sb]


    try_again = True

    while try_again:
        menu = input("Type 'encode' to Encrypt, type 'decode' to Decrypt: ")
        shift = int(input("Type the number of shift: "))
        txt = input('Enter your message: ').lower()
        msg = ''
        for i in txt:
            if i.isalpha() == True:
                msg += i

        encod = ''
        decod = ''

        if menu == 'encode':
            for i in msg:
                encod += caeser(i,shift,menu)           
            print('Here is your encrypted message: ',encod)

        elif menu == 'decode':
            for j in msg:
                decod += caeser(j,shift,menu)
            print('Here is your Decrypted message: ',decod)

        restart = input('Do you want to try again ?\nY or N: ')     

        if restart == 'N' or restart == 'n':

            try_again = False
            print('Goodbye')

        elif restart == 'Y' or restart == 'y':
            try_again = True


    

