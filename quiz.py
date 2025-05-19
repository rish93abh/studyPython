print('\n------- QUIZ -------\n(1 points for each correct answer)')

questions = ('How many planets in solar system ?',
             'What is Sodium Chloride also known as ?',
             'What is the capital of India ?',
             'Which of these is an electronic device ?',
             'How many continents are there ?'
             )

options = (('A : 8','B : 3','C : 9','D : 5'),
           ('A : Salt','B : Sugar','C : Water','D : Soda'),
           ('A : Bhopal','B : Mumbai','C : Indore','D : Delhi'),
           ('A : Printer','B : Table','C : Chair','D : Sofa'),
           ('A : 2','B : 3','C : 6','D : 7')
           )

answers = ('C','A','D','A','D')

score = 0

for i in range(len(questions)):
    print(questions[i])
    for x in options[i]:
        print(x)

    userAns = input('Enter option: ')
    
    if userAns.upper() == answers[i]:
        print('Correct. +1 point.')
        score += 1
    else:
        print('Incorrect. 0 point.')
    
    print('-----------------------')

perc = score/len(answers) * 100
print(f'You scored {score} : {perc}%')