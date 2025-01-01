Menu = [
    {
        'item' : 'Pizza',
        'price': '210'
     },
    {
        'item' : 'Pasta',
        'price': '180'
     },
    {
        'item' : 'Burger',
        'price': '70'
     },
    {
        'item' : 'Noodle',
        'price': '190'
     },
    {
        'item' : 'Cold Coffee',
        'price': '90'
     }
]

print(" Welcome to Zenith!! ")
print("This is our Menu")

def order(Menu):
    for idx, i in enumerate(Menu , start=1):
        print(f'{idx}.{i["item"]} - {i["price"]} ')

    want_to_order = input('Do you want to place your order (y/n): ').lower()
    order_value = 0
    ordered_items = []
    if want_to_order == 'y':
        bill_name = input("Enter Customer Name: \n") 
        add_items = 'y'
        while add_items == 'y':
            order = input("Enter the Item No. from the menu Above to place the order \n")
            quantity = int(input('Enter the Quantity of the item \n'))
            Value = quantity * int(Menu[int(order)-1]['price']) #order - 1, gives index of the item in the list menu which helps us to get the price of it 
            order_value += Value
            ordered_items.append((Menu[int(order)-1]['item'], quantity))
            add_items = input('Do you want to add more item(y/n): \n').lower()
        if add_items =='n':
            print("Ordered Items are:")
            for item, qty in ordered_items:
                print(f'{item}, Quantity - {qty}')
            print(f'Thank you {bill_name} for ordering with us, Your order Value is : {order_value}')
            
order(Menu)
