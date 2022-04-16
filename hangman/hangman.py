import random

word_list = ["pizza", "apple", "phone", "speakers", "table"]
hangman_prints = {
    0: """
          ______________
          | /          |
          |/          ( )
          |            |
          |           / \\
          |
    """,
    1: """
         ______________
          | /          |
          |/          ( )
          |            |
          |           / 
          |
    """,
    2: """
         ______________
          | /          |
          |/          ( )
          |            |
          |            
          |
    """,
    3: """
         ______________
          | /          |
          |/          ( )
          |            
          |            
          |
    """,
    4: """
         ______________
          | /          |
          |/          
          |            
          |            
          |
    """,
    5: """
         ______________
          | /         
          |/          
          |           
          |           
          |
    """,
    6: """
         
          | /          
          |/          
          |           
          |           
          |
    """,
    7: ""
}

def hangman_game():
    chosen_word = random.choice(word_list)
    lives = 7
    #Shows the user the number of letters in the word
    underbar = len(chosen_word)*"_"
    print(underbar)
    #User guesses a letter
    # TODO Exit strategy:
    # 1. ask the player to guess the word. (a) if player guesses incorrectly, subtract life and display hangman. (b) if player guess correctly, exit out of the loop and say "You Won!".
    # 2. exit while loop if player fills out the entire word.
    previous_guess = underbar
    while lives > 0:
        letter = input('Guess a letter: ')
        intersect_result = intersection(chosen_word, letter)
        if intersect_result == True:
            display_guesses = ""
            for i, l in enumerate(chosen_word):
                if l == letter:
                    display_guesses = display_guesses + l
                else:
                    display_guesses = display_guesses + previous_guess[i]
            print(display_guesses)
            previous_guess = display_guesses
        else:
            lives = lives - 1
            print(hangman_prints[lives])
            print(underbar)


def intersection(c, l):
    i = set.intersection(set(c), set(l))
    if len(i) == 1:
        return True
    else:
        return False

hangman_game()