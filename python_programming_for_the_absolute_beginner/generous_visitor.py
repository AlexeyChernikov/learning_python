# Enter the bill for lunch at the restaurant. 
# The program outputs 2 values: tips based on 15% and 20% of the specified amount

price = int(input('Enter the bill for lunch: '))

print(f'15% of tips from the current account: {(price * 15) / 100}')
print(f'20% of tips from the current account: {(price * 20) / 100}')

input('\nPress Enter to exit...')