# The program flips a coin 100 times and counts how many times the eagle 
# fell, and how many times the tails fell

import random

variants = ('eagle', 'tail')
flip_counter = 0
eagle_counter = 0
tail_counter = 0

while flip_counter != 100:
    result = random.choice(variants)

    if result == variants[0]:
        eagle_counter += 1
    elif result == variants[1]:
        tail_counter += 1

    flip_counter += 1

print(f'The eagle fell {eagle_counter} times')
print(f'The tails fell {tail_counter} times')