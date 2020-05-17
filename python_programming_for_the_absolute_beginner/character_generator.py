# Character generator
# 
# The program allows you to distribute points between characteristics

import os
import sys
import time


clear = lambda: os.system('cls')
common_info = """0 - back;\n1 - Strength;\n2 - Health;\n3 - Intelligence;\n4 - Dexterity.\n"""


def help():
    """0 - exit;\n1 - spend points;\n2 - return points;\n3 - show a table of characteristics;\n4 - help.\n"""

def spend_points():
    clear()
    print(common_info)
    character_status()

    while True:
        print('What characteristic do you want to increase?')
        cmd = input('>>> ')

        if cmd == '0':
            clear()
            return None
        elif cmd == '1':
            characteristics_change("str", 'spend')
            break
        elif cmd == '2':
            characteristics_change("hp", 'spend')
            break
        elif cmd == '3':
            characteristics_change("int", 'spend')
            break
        elif cmd == '4':
            characteristics_change("dex", 'spend')
            break
        else:
            print('Command not found!\n')

def return_points():
    clear()
    print(common_info)
    character_status()
    while True:
        print('Points of what characteristic do you want to return?')
        cmd = input('>>> ')

        if cmd == '0':
            clear()
            return None
        elif cmd == '1':
            characteristics_change("str", 'return')
            break
        elif cmd == '2':
            characteristics_change("hp", 'return')
            break
        elif cmd == '3':
            characteristics_change("int", 'return')
            break
        elif cmd == '4':
            characteristics_change("dex", 'return')
            break
        else:
            print('Command not found!\n')

def characteristics_change(cur_characteristic, mode):
    global point_counter
    global characteristics

    if mode == 'spend':
        content = 'How many points do you want to add? (Total points: ' + str(point_counter) + ')'
    elif mode == 'return':
        content = 'How many points do you want to return? (Can return: ' + str(characteristics[cur_characteristic]) + ')'
    else:
        print('Mode not found! Return to the main menu...')
        return None

    print(content)

    while True:
        points_num = input('>>> ')

        if points_num.isdigit():
            if mode == 'spend':
                if int(points_num) <= point_counter:
                    break
                else:
                    print(f'You cannot add so many points! Total: {point_counter}\nTry again...\n')
            elif mode == 'return':
                if int(points_num) <= characteristics[cur_characteristic]:
                    break
                else:
                    print(f'You cannot return so many points! Total: {characteristics[cur_characteristic]}\nTry again...\n')
        else:
            print('Enter the number!')

    points_num = int(points_num)

    if mode == 'spend':
        point_counter -= points_num
        characteristics[cur_characteristic] += points_num
        print(f'Points successfully added! Points left: {point_counter}. Return to the main menu...')
    elif mode == 'return':
        point_counter += points_num
        characteristics[cur_characteristic] -= points_num
        print(f'Points returned successfully! Points left: {point_counter}. Return to the main menu...')

    time.sleep(2)
    clear()
    
def character_status():
    print('+-------+-------+-------+-------+')
    print(f'|STR\t|HP\t|INT\t|DEX\t|')
    print('+-------+-------+-------+-------+')
    print(f'|{characteristics["str"]}\t|{characteristics["hp"]}\t|{characteristics["int"]}\t|{characteristics["dex"]}\t|')
    print('+-------+-------+-------+-------+')
    print(f'Total points: {point_counter}\n')


# Main

characteristics = {'str': 0, 'hp': 0, 'int': 0, 'dex': 0}
point_counter = 30

print(help.__doc__)
character_status()

while True:
    cmd = input('>>> ')

    # Exit
    if cmd == '0':
        break
    # Spend points
    elif cmd == '1':
        if point_counter != 0:
            spend_points()
            print(help.__doc__)
            character_status()
        else:
            print('You have run out of points!\n')
    # Return points
    elif cmd == '2':
        if point_counter != 30:
            return_points()
            print(help.__doc__)
            character_status()
        else:
            print('All points in place!\n')
    # Character status
    elif cmd == '3':
        character_status()
    # Help
    elif cmd == '4':
        print(help.__doc__)
    else:
        print('Command not found!\n')

print('Goodbye :)')