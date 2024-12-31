import random

def roll_dice():
    return random.randint(1,6) # creating a function for getting random number 1-6

while True:
    Yes = input("Do you want to roll the dice (y/n): \n").lower() # taking inputs yes or no

    if Yes == "y" :
        D1 = roll_dice() #Calling function and stores the value to D1
        D2 = roll_dice() #Calling function and stores the value to D2
        print([ D1 , D2 ]) 

        if D1 > D2:
            print(f'Player one wins by: { D1 - D2 } \n')
        elif D2 > D1:   
            print(f'Player two wins by {D2 - D1} \n')
        else:
            print('Tie')
    elif Yes == 'n':
        print("exiting the game !! Thank You")
        break
    else:
        print('invalid input given')