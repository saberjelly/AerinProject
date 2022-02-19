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
    intersection(chosen_word, letter)


def intersection(c, l):
    x = 7
    print(hangman_prints[x])
    while len(set.intersection(set(c), set(l))) != 1:
        print(hangman_prints[x - 1])
        letter = input('Guess a letter: ')

hangman_game()