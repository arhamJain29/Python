import random
import string


def password():
    letter = string.ascii_lowercase
    digit = string.digits
    uppercase = string.ascii_uppercase
    special_character = string.punctuation

    character = [] #empty list to append everytime to store the new string of the password
    tru = True 
    while tru: #
        yes = input("Do you want to generate a passward(y/n): \n").lower()
        if yes == 'y':
            length = int(input('enter the lenght of the password: \n'))
            i_char = input('include special character (y/n): ')
            i_digits = input('include Digits (y/n): ')
            i_uppercase = input('include uppercase (y/n): ')
            
            
            i =0
            while i<length:
                    character.append(random.choice(letter))
                    i += 1
                    if i_char == 'y' and i<length: #special_character
                        character.append(random.choice(special_character))
                        i += 1
                    if i_digits == 'y' and i<length:
                        character.append(random.choice(digit))
                        i += 1
                    if i_uppercase == 'y' and i<length:
                        character.append(random.choice(uppercase))
                        i += 1
            random.shuffle(character)
            print(''.join(character)) #use to remove '' from the list and convert it to a string
        elif yes == 'n':
            print('Thank you, exiting the password generator')
            tru = False
        else:
            print('wrong input')
            break

         

password()

