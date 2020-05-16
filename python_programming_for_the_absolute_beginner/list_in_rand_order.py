# The list is in random order
# 
# The program displays the list in random order

import random

def my_rand(cur_list):
    new_list = []

    while cur_list:
        rand = random.randint(0, len(cur_list) - 1)
        new_list.append(cur_list[rand])
        del cur_list[rand]

    return new_list

cur_list = ['rabbit', 'mouse', 'spider', 'bear', 'lion', 'cow']

print('Original list:')
print(cur_list)
print('\nMixed using the "sample" method":')
print(random.sample(cur_list, len(cur_list)))

# Another variant
print('\nMixed using the "my_rand" method":')
print(my_rand(cur_list))