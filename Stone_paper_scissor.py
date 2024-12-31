import random

choices = [ 'stone', 'paper' , 'scissor' ]

User_input = input('Enter your Choices [Stone, Paper, Scissor]: \n \n').lower()
Comp_choice = random.choice(choices)
 
print(F'User Choice is {User_input} & Computer Choice is {Comp_choice} \n')
score_player = 0
score_computer = 0

if User_input == Comp_choice:
    print('Tie')
    score_player = score_player
    score_computer = score_computer
    
elif User_input == 'stone':
    if Comp_choice == 'paper':
        print('Paper Covers the Stone. Computer Won !!')
        score_player = score_player
        score_computer += 1
    else  : #Comp_choice == scissor
        print('Stone breaks Scissor. Player Won !!')
        score_player  += 1
        score_computer = score_computer
        
elif User_input == 'paper':
    if Comp_choice == 'scissor':
        print('scissor cuts paper. Computer Won !!')
        score_player = score_player
        score_computer += 1
    else:# Comp_choice == stone:
        print('Paper Covers the Stone. Player Won !!')
        score_player  += 1
        score_computer = score_computer        
        
elif User_input == 'scissor':
    if Comp_choice == 'stone':
        print('Stone breaks Scissor. Computer Won !!')
        score_player = score_player
        score_computer += 1
    else:# Comp_choice == paper:
        print('scissor cuts paper. Player Won !!')
        score_player  += 1
        score_computer = score_computer  
else:
    print(' ')       
        
print(f"Player's Score is {score_player} & Computer's Score is {score_computer} \n" )

if  score_player > score_computer:
    print('Player Wins \n')
elif  score_player < score_computer:
    print('Computer Wins \n ')
else:
    print('Tie \n')