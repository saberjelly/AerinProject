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
    print('debug statement')
hangman_game()