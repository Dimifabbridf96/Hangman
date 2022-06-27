import random
from word import WORDS

print('Welcome to the game :\n' , 
'''                   +---+
                    |   |
                        |
                        |
                        |
                        |
                    =========''')
letters_in_word = "\n"
user_name = input("Please insert your name: ")


class User:
    def __init__(self, name):
        self.name = user_name
        print( f"Ready to guess {self.name} ? ")     
user = User(user_name)
 
word = random.choice(WORDS)
guess = "_" * len(word)

print(guess)

user_choice = input("Guess a word: ")

guess_word = set(word)

if word.find(user_choice) == -1:
    print("I guess that you didn't guess 🤣")
else:
    letters_in_word.join(user_choice)

