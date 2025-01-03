def add(x,y):
    print(f'The sum of the two numbers is: {x + y}')
def subs(x,y):
    print(f'The difference of the two numbers is: {x - y}')
def multiply(x,y):
    print(f'The multiplication of the two numbers is: {x * y}')
def division(x,y):
    print(f'The division of the two numbers is: {x / y}')

def calc():
    x = float(input("enter the first Number: \n"))
    y = float(input("enter the Secound Number: \n"))
    to_do = input("what you want to do ('add', 'subs' , 'multiply', 'division' , 'exit' ): \n").lower()


    while True:
        if to_do == 'add':
            add(x,y)
            break
        elif to_do == 'subs':
            subs(x,y)
            break
        elif to_do == 'multiply':
            multiply(x,y)
            break
        elif to_do == 'division':
            division(x,y)
            break
        elif to_do == 'exit':
            print('We are exiting! thank you')
            break
        else:
            print('invalid to_do')
            
calc()