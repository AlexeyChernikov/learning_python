# Guess the word

import random

intro = '''I made a word.
Name 5 letters, and I will tell you if they are in the word.
Then name the intended word.
Let's go!
'''

print(intro)

words = ('bird', 'pen', 'computer', 'guitar', 'cup')
guessed_letters = list()
letter_counter = 5
word = random.choice(words)

print(f'There are {len(word)} letters in a word\n')

while letter_counter:
    while True:
        letter = input('Enter a letter: ')

        if letter.isalpha():
            break

        print('This is not a letter!\n')

    if letter.lower() in word:
        if letter.lower() not in guessed_letters:
            guessed_letters.append(letter.lower())
        print('Yes\n')
    else:
        print('No\n')

    letter_counter -= 1

print('Guessed letters:')
print(guessed_letters)

answer = input('\nEnter the answer: ')

print('\nYou won' if answer == word else '\nYou lose')