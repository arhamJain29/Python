import random

operators = ['+' , '-' , '*']

def prblm_maths():

    num1 = random.randint(1,99)
    num2 = random.randint(1,99)
    ops = random.choice(operators)
    
    left = num1
    right = num2
    
    tru = True

    while tru:
        yes = input('Do you want to Generate Maths question(y/n): \n')

        if yes == 'y':
            ques = f'{str(left)}  {ops}  {str(right)}'
            s = print(ques)
            ans = int(input('Enter your answer: \n'))
            answer = eval(ques)
            if ans == answer:
                print('Very Good !!, correct answer ')
                tru = True

            else:
                print(f'Oops !! , Wrong answer')
                print(f'Correct Answer is {answer}')
                tru = True

        elif yes == 'n':
            print('Thankyou, exiting the program')
            tru = False

        else:
            print('INVALID INPUT')
            
            


prblm_maths()

