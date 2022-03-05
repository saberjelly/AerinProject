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
    #Shows the user the number of letters in the word
    underbar = len(chosen_word)*"_"
    print(underbar)
    #User guesses a letter
    letter = input('Guess a letter: ')
    intersect_result = intersection(chosen_word, letter)
    if intersect_result == True:
        display_guesses = ""
        for l in chosen_word:
            if l == letter:
                display_guesses = display_guesses + l
            else:
                display_guesses = display_guesses + "_"
        print(display_guesses)


def intersection(c, l):
    i = set.intersection(set(c), set(l))
    if len(i) == 1:
        return True
    else:
        return False

hangman_game()