# Simple counter
# 
# The program counts numbers in a given interval with a given step

start = int(input('Enter the beginning of the interval: '))
stop = int(input('Enter the end of the interval: '))
step = int(input('Enter step: '))

print([num for num in range(start, stop + 1, step)])