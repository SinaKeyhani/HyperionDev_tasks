# shopping with function:
# this programm shows how to use function with differnt functions rather than use big chunk of a code




def add_item(shopping_list):
    '''this function will add item to the list'''

    add_item = input('Please enter the the name of the item you would like to add : ')
    shopping_list.append(add_item)
    print(f'Item {add_item} added.')



def view_items(shopping_list):
    '''This function will dispaly the items inside the shopping list'''

    if shopping_list:
        print('Shopping List')
        for num, item in enumerate(shopping_list, 1):
            print(f'{num} : {item}')
    else:
        print('Your shopping list is empty.')


def remove_item(shopping_list):
    '''This function will remove selected item from the shopping list'''
    if shopping_list:   
        view_items(shopping_list)

        try:
            remove_items = int(input('Please enter the index of the item you would like to remove from shopping list : '))
            if 0 < remove_items < len(shopping_list):
                index = remove_items - 1
                removed_items = shopping_list.pop(index)
                print(f'{removed_items} removed ')
            else:
                print('Invalid Index, please try again: ')

        except ValueError:
            print('Please enter a valid number')

    else:
        print("Your shopping list is empty.")

    

def main():
    shopping_list = []
    while True:
        try:
            menu = int(input('''
                    Please select an option below:
                     1. Add item
                     2. View items 
                     3. Sort items
                     0. Exit
Your selection: '''))
            
            if menu == 1:
                add_item(shopping_list)
            elif menu == 2:
                view_items(shopping_list)
            elif menu == 3:
                remove_item(shopping_list)
            elif menu == 0:
                print('Goodbye')
                break
            else:
                print('Invalid selection. Please try again.')
        except ValueError:
            print('Please enter a valid number.')

if __name__ == "__main__":
    main()




