
import random

print('\n** This is number guessing game. **')

num = random.randint(1,100)

def is_prime(num):      # PRIME NUMBER
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def hint(n):        # HINTS
    if n % 2 == 0:
        print("\n* Hint: It is an Even number *")
    elif n % 2 != 0:
        print('\n* Hint: It is an Odd number *')

    if is_prime(n) == True:
        print('*Hint: It is also a Prime number *')


print("\nI'm thinking of a number between 1 to 100.\nYou have to guess the correct number.")
mode = input("\nChoose the difficulty mode.\nType 'e' for Easy mode (10 attempts), 'h' for Hard mode (5 attemps): ")

hint(num)

def attempts(x):        # ATTEMPTS
    count = 0
    for i in range(x):
        n = int(input('Guess the number: '))

        if n == num:
            print(f'\nYay. You have guessed it correctly, in {count+1} attempts !\nThe number is :',num)
            break

        elif n < num:
            print('\nToo low. Go higher.')    

        elif n > num and n < 100:
            print('\nToo high. Go lower.')

        if n > 100:
            print(f'\nThe range is only within 1 to 100. {n} not allowed.')
        
        count += 1
        print(f'(You have {x - count} attempts left)')

        if count == x:
            print('\nGame Over.\nThe number was :',num)
            quit()
        


if mode == 'e':
    attempts(10)

elif mode == 'h':
    attempts(5)