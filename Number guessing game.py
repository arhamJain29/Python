import random

def random_number():
    i = 0
    lower = int(input('enter the lower limit of the range: \n'))
    upper = int(input("enter the upper limit of the range: \n"))

    Range  = {'low' : lower, 'high' :upper }
    print(f'Range is:  {Range.values()}')

    Guessing_number = random.randint(lower,upper)
    Guessed_Correctly = True
    while Guessed_Correctly == True:
        Guessed_number = int(input('Enter the Number you Guessed: \n'))
        if Guessed_number > Guessing_number:
            print('Try Again !! You have Guessed Very High')
            i += 1
        elif Guessed_number < Guessing_number:
            print('Try Again !! You have Guessed Very Low')
            i += 1
        elif Guessed_number == Guessing_number:
            Guessed_Correctly = False
            i += 1

    print('Woohoh !! You have Guessed correctly')
    print(f'Number of Guesses : {i}')


random_number()