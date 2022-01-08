import random

def guess_game(x):
    random_number = random.randint(0, x)
    print(random_number)
    answer = 'no'
    while answer != 'yes':
        print('Is this your number?')
        answer = input(f'Type too low, too high or yes: ')
        if answer == 'too low':
            print (random_number + 1)
        elif answer == 'too high':
            print (random_number - 1)
        else:
            print ('Yay!')