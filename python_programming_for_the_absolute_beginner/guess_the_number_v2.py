# Guess the number
#
# The computer selects a random number in the range from 1 to 100.
# The player is trying to guess this number.
# The computer says the assumption is more / less than the guessed number or hit the point.
# The player has only 10 attempts to guess the number


import os
import random


LOW = 1
HIGH = 101
MAX_ATTEMPT = 10


clear = lambda: os.system('cls')
intro = '''Welcome to "Guess the Number"!
I made up a natural number from 1 to 100.
You have only 10 attempts.
Let's go!
'''


def ask_number():
    """ Asks you to enter a number within the range """

    number = None

    while number not in range(LOW, HIGH):
        number = int(input('Your guess: '))

    return number

def attempt_report(attempt_counter):
    """ Reports the number of attempts remaining """

    if (attempt_counter == MAX_ATTEMPT // 2) or (attempt_counter == MAX_ATTEMPT - 3) or \
        (attempt_counter == MAX_ATTEMPT - 2) or (attempt_counter == MAX_ATTEMPT - 1):
        print(f'You have {MAX_ATTEMPT - attempt_counter} attempts left')

def game_result(answer, guessed_number, attempt_counter):
    """ Reports game results """

    if answer == guessed_number:
        print('\nYou guessed!')
        print(f'You took {attempt_counter} attempts\n')
    elif answer != guessed_number and attempt_counter == MAX_ATTEMPT:
        print('You did not guess. Lucky next time :)\n')

def game():
    """ Game process """

    guessed_number = random.randint(LOW, HIGH)
    attempt_counter = 0
    answer = None
    
    while attempt_counter < MAX_ATTEMPT and answer != guessed_number:
        attempt_report(attempt_counter)
        answer = ask_number()
        attempt_counter += 1

        if answer > guessed_number:
            print('Less...\n')
        elif answer < guessed_number:
            print('More...\n')
    else:
        game_result(answer, guessed_number, attempt_counter)

def ask_yes_no(question):
    """ Asks a question with an answer Yes / No """

    response = None

    while response not in ('y', 'n'):
        response = input(question).lower()

        if response not in ('y', 'n'):
            print('Invalid command! Try again...\n')

    return response

def main():
    replay = None

    while replay != 'n':
        clear()
        print(intro)
        game()
        replay = ask_yes_no('Again? (Y/N): ')

    print('Thanks for the game, goodbye')

main()