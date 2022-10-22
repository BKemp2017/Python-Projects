import random


name = input('Enter name: ')
print('Welcome to the higher/lower game,', name +'!')

while True:
    low = int(input('Enter the lower bound: '))
    high = int(input('Enter the upper bound: '))
    if low < high:
        break 
    print('The lower bound must be less than the upper bound.')
    print()

rando = random.randint(low,high)
print()

user_num = int(input('Great, now guess a number between {} and {}: '.format(low, high)))

while rando != user_num:
    if user_num < rando:
        print('Nope too low.')
    if user_num > rando:
        print('Nope, too high.')
    print()
    user_num = int(input('Guess another number: '))

print('You got it!')

