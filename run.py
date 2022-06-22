import random
from word import WORDS

print('Welcome to the game','''+---+
                    |   |
                        |
                        |
                        |
                        |
                    =========''')


word = random.choice(WORDS)
guess = "_" * len(word)
print(guess)

