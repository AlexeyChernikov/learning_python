# Guess the number (version where the computer guesses)
#
# You select a random integer in the range of 1 to 100.
# The computer is trying to guess this number.
# The process continues until the computer guesses the number.

intro = '''Welcome to "Guess the Number (version where the computer guesses)"!
You need to select a random integer number in the range from 1 to 100.
The process continues until the computer guesses the number.
Let's go!
'''

print(intro)

# Initial values
guessed_number = 0
assumption = 0
tries = 0
left = 1
right = 100

# 
while not left <= guessed_number <= right:
    guessed_number = int(input('Make a number from 1 to 100: '))

    if not left <= guessed_number <= right:
        print('The number is not in the range! Try it again\n')

while assumption != guessed_number:
    assumption = (left + right) // 2
    tries += 1

    if assumption == guessed_number:
        print('Computer guessed!')
        print(f'It took {tries} attempts')
        break
    elif assumption > guessed_number:
        right = assumption - 1
    elif assumption < guessed_number:
        left = assumption + 1