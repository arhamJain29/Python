to_do = [ 'Add an expense' , 'Show budget details' , 'Exit' ]


def Budget_Tracker():
    expenditure = 0
    expenses = []
    Name = input('Please Enter Your Name:  ').upper()
    print(f'Welcome to your Personalised Budget Tracker ,{Name}')

    Budget = int(input("Please Enter your Monthly Budget"))

    print("What would you like to do? :")
    for idx, i in enumerate(to_do, start=1):
        print(f'{idx}.{i}')
    add = True
    while add == True :    
        choice = int(input('Enter your choice [ 1/2/3 ]: '))
        #print(f' {to_do[choice - 1]} ')
        if choice  == 1:
            description = input('enter expense description') 
            expense = int(input('enter expense amount'))
            expenditure += expense
            expenses.append({description : expense } )

        elif choice == 2:
            print(f'Total Budget - {Budget} \n')
            print(f'Your expenses {expenses} \n')
            print(f'Remaining Budget - {Budget - expenditure} \n')

        elif choice == 3:
            print('Thankyou !!')
            add = False
            

Budget_Tracker()
