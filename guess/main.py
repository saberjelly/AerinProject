import random

# guess game what number the computer generates
def guess_game(x):
    random_number = random.randint(0, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry guess is too low... Try again!')
        elif guess > random_number:
            print('Sorry guess is too high... Try again!')
        else:
            print('You have guess correctly!')


guess_game(10)
