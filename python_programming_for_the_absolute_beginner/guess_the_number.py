# Guess the number
#
# The computer selects a random number in the range from 1 to 100.
# The player is trying to guess this number.
# The computer says the assumption is more / less than the guessed number or hit the point.
# The player has only 10 attempts to guess the number

import random

MAX_ATTEMPT = 10
intro = '''Welcome to "Guess the Number"!
I made up a natural number from 1 to 100.
You have only 10 attempts.
Let's go!
'''

print(intro)

guessed_number = random.randint(1, 100)
attempt = 0

while attempt < MAX_ATTEMPT:
    if (attempt == MAX_ATTEMPT // 2) or (attempt == MAX_ATTEMPT - 3) or (attempt == MAX_ATTEMPT - 2) or (attempt == MAX_ATTEMPT - 1):
        print(f'You have {MAX_ATTEMPT - attempt} attempts left')

    answer = int(input('Your guess: '))

    attempt += 1

    if answer == guessed_number:
        print('\nYou guessed!')
        print(f'You took {attempt} attempts')
        break
    elif answer != guessed_number and attempt == MAX_ATTEMPT:
        print('You did not guess. Lucky next time :)')
    elif answer > guessed_number:
        print('Less...\n')
    elif answer < guessed_number:
        print('More...\n')