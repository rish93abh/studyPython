# print ("Hi, this is 2 numbers calculator !")

def whpr():


    def opr(a,b):

        op = input("\nType p for plus.\nType s for subtract.\nType m for multiplication.\nType d for division.\n")
        
        if (op=="p"):
            c = a + b
            print(f'{a} + {b} = {c}')
            return c

        elif (op=="s"):
            c = a - b
            print(f'{a} - {b} = {c}')
            return c

        elif(op=="m"):
            c = a * b
            print(f'{a} x {b} = {c}')
            return c

        elif(op=="d"):
            c = a / b
            print(f'{a} / {b} = {c}')
            return c
        

    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))

    result = opr(num1,num2)

    while True:
        more = input(f'Continue with {result} ?\nY or N: ')

        if more == 'y':
                    
            num3 = int(input('Enter another number: '))
            result = opr(result,num3)

        elif more == 'n':
            print('Goodbye !')
            quit()



#whpr()