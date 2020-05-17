# Who is your dad
# 
# Shows a son-father pair

import os
import time


def add_new_pair():
    global sons_dads_dict
    son_name = dad_name = ''

    while True:
        while True:
            print('Enter the name of the son:')
            son_name = input('>>> ')
            
            if not son_name.isalpha():
                print('Invalid name!\n')
            else:
                break

        while True:
            print('Enter father\'s name:')
            dad_name = input('>>> ')

            if not dad_name.isalpha():
                print('Invalid name!\n')
            else:
                break
        
        break

    sons_dads_dict[son_name] = dad_name
    print('The new pair was added successfully! Return to the main menu...')
    time.sleep(2)

def remove_pair():
    global sons_dads_dict
    son_name = ''

    while True:
        while True:
            print('Enter the name of the son:')
            son_name = input('>>> ')
            
            if not son_name.isalpha():
                print('Invalid name!\n')
            elif son_name not in sons_dads_dict:
                print('Name not found!\n')
            else:
                break
        
        break

    del sons_dads_dict[son_name]
    print('The pair was successfully deleted! Return to the main menu...')
    time.sleep(2)


clear = lambda: os.system('cls')

help = """0 - Exit
1 - Add a new pair
2 - Remove a pair
3 - Show a pair
4 - Show all pairs
5 - Help
"""

sons_dads_dict = {
    'Alexey': 'Vladimir',
    'Bruno': 'Jack',
    'Victor': 'Edward',
    'Anatoly': 'Kirill'
    }

# Main
print(help)

while True:
    action = input('>>> ')

    if action == '0':
        break
    elif action == '1':
        clear()
        add_new_pair()
        clear()
        print(help)
    elif action == '2':
        clear()
        remove_pair()
        clear()
        print(help)
    elif action == '3':
        print('\nEnter the name:')
        name = input('>>> ')
        print('\n' + sons_dads_dict.get(name, 'Name not found'))
    elif action == '4':
        print([key + ' - ' + value for key, value in sons_dads_dict.items()])   
    elif action == '5':
        print(help)        
    else:
        print('The action is not found!\n')

print('Goodbye :)')