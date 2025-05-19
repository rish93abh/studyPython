# print ("This is Morse Code Translator")

A = '.-'
B = '-...'
C = '-.-.'
D = '-..'
E = '.'
F = '..-.'
G = '--.'
H = '....'
I = '..'
J = '.---'
K = '-.-'
L = '.-..'
M = '--'
N = '-.'
O = '---'
P = '.--.'
Q = '--.-'
R = '.-.'
S = '...'
T = '-'
U = '..-'
V = '...-'
W = '.--'
X = '-..-'
Y = '-.--'
Z = '--..'

def M():
    i = input('Enter :')

    def morse(i):

        if i == 'A' or i == 'a':
            print('A =',A)

        elif i == 'B' or i == 'b':
            print('B =',B)

        elif i == 'C' or i == 'c':
            print('C =',C)

        elif i == 'D' or i == 'd':
            print('D =',D)

        elif i == 'E' or i == 'e':
            print('E =',E)

        elif i == 'F' or i == 'f':
            print('F =',F)

        elif i == 'G' or i == 'g':
            print('G =',G)

        elif i == 'H' or i == 'h':
            print('H =',H)

        elif i == 'I' or i == 'i':
            print('I =',I)

        elif i == 'J' or i == 'j':
            print('J =',J)

        elif i == 'K' or i == 'k':
            print('K =',K)

        elif i == 'L' or i == 'l':
            print('L =',L)

        elif i == 'M' or i == 'm':
            print('M =',M)

        elif i == 'N' or i == 'n':
            print('N =',N)

        elif i == 'O' or i == 'o':
            print('O =',O)

        elif i == 'P' or i == 'p':
            print('P =',P)

        elif i == 'Q' or i == 'q':
            print('Q =',Q)

        elif i == 'R' or i == 'r':
            print('R =',R)

        elif i == 'S' or i == 's':
            print('S =',S)

        elif i == 'T' or i == 't':
            print('T =',T)

        elif i == 'U' or i == 'u':
            print('U =',U)         

        elif i == 'V' or i == 'v':
            print('V =',V)

        elif i == 'W' or i == 'w':
            print('W =',W)

        elif i == 'X' or i == 'x':
            print('X =',X)

        elif i == 'Y' or i == 'y':
            print('Y =',Y)

        elif i == 'Z' or i == 'z':
            print('Z =',Z)

        elif i == '1':
            print('1 = .----')         

        elif i == '2':
            print('2 = ..---')         

        elif i == '3':
            print('3 = ...--')         
                
        elif i == '4':
            print('4 = ....-')         

        elif i == '5':
            print('5 = .....')         

        elif i == '6':
            print('6 = -....')         

        elif i == '7':
            print('7 = --...')        

        elif i == '8':
            print('8 = ---..')         

        elif i == '9':
            print('9 = ----.')         

        elif i == '0':
            print('0 = -----')

        
    for x in range(0,len(i)):
        morse(i[x])

#M()