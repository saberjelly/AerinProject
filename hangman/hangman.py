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
    
    """
}

print(hangman_prints[0])
