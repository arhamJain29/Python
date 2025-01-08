import random
from game_data import data
from art import logo
from art import vs

def assign():
    return random.choice(data)

def compare():
    p1 = assign()
    p2 = assign()

    while p1 == p2:
        p2 = assign()

    v1 = p1['follower_count']
    v2 = p2['follower_count']

    max = ''

    if v1 > v2:
        max = p1['name']
    elif v2 > v1:
        max = p2['name']
    
    return p1, p2, max

def play():

    score = 0

    while True:
        p1, p2, max = compare()

        print(logo) 
        print(f"Name: {p1['name']}, description: {p1['description']}, country: {p1['country']}")
        print(vs)
        print(f"Name: {p2['name']}, description: {p2['description']}, country: {p2['country']}")

        user_input = input('Guess which one has more followers: ')

        if user_input == max:
            print('Perfect Guess !! Woohoo')
            score += 1
            break
        else:
            print('Wrong guess!!')
            break

    print(f'Your final score is {score}')

def main():
    while True:
        want_to_play = input("Do you want to play (y/n): \n").lower()
        
        if want_to_play == 'y':
            play()
        elif want_to_play == 'n':
            print('Thank you, Exiting the game.')
            break
        else:
            print('Invalid input, enter a valid input')

if __name__ == "__main__":
    main()