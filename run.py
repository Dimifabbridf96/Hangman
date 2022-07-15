import random
from word import WORDS

print('Welcome to the modern Hangman game :\n', '''   +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')


class Game: 
    """
       Get difficult input to determine the difficult 
       choose from the user and start the game
    """
    def __init__(self, value):
        """
        Manage the difficult input and run game_mode function to start the game
        """
       
        self.value = value

        while self.value != 'E' or self.value != 'D':
            if self.value == 'E' or self.value == 'D':
                game_mode(self)
            else:
                print("Invalid input try again: e for easy, d for difficult")
                self.value = input(
                    "Do you want to play easy or difficult ? e/d : ").upper()


def game_mode(self):
    """
    Get input difficulty value to start a new match in hard or easy mode based
    on the user preference
    """
    word = random.choice(WORDS)
    if self.value == 'E':
        while len(word) >= 7:
            word = random.choice(WORDS)
    elif self.value == 'D':
        while len(word) < 7:
            word = random.choice(WORDS)
    guess = "_" * len(word)
    guess_word = set(word)
    letters_in_word = set()
    letters_used = set()
    print(f"{guess} \n")
    print(word)
    lives = 6
    coins = 0
    
    while guess_word != letters_in_word:  
    
        user_choice = input("Guess a letter of the word: ").upper()
        while len(user_choice) > 1 or len(user_choice) < 1 or user_choice.isalpha() is False:
            print('Invalid input, try again, only 1 letter at time')
            user_choice = input("Guess a letter of the word: ").upper()

        if user_choice in letters_used:
            print('Letter already used')
            continue

        letters_used.add(user_choice)
        
        if word.find(user_choice) == -1:
            print("I guess that you didn't guess 🤣\n")
            lives = lives - 1
            coins = coins - 5
            print(f"{lives} lives remained\n")
            print(f"You used already {letters_used}\n ")
            print(f"{coins} coin/s\n")
        else:
            if self.value == 'E':
                lives = lives + 1
            elif self.value == 'D':
                lives = lives
            coins = coins + 10
            print("i guess you guess ✌\n")
            print(f"{lives} lives remained\n")
            print(f"You used already {letters_used}\n")
            print(f"{coins} coin/s\n")
                
            if user_choice in word:
                letters_in_word.add(user_choice)
                print(f"{letters_in_word} are present in the word")

        current_word = ""
        for letter in range(len(word)):
            if user_choice == word[letter]:
                current_word += user_choice
            else:
                current_word += guess[letter]

        guess = current_word
        print(guess)
        if lives == 0:
            if self.value == 'E':
                if coins >= 0:
                    go_ahead = input("For 10 coins you can get 5 new lives, do you want to spend your coins and continue ? y/n ").upper()
                    while go_ahead != "Y" or go_ahead != 'N':
                        if go_ahead == 'Y':
                            coins = coins - 10
                            lives = lives + 5
                            break
                        elif go_ahead == 'N':
                            replay(self)
                        else:
                            print('Please try again, Y for yes and N for no')
                            go_ahead = input("For 10 coins you can get 5 new lives, do you want to spend your coins and continue ? y/n ").upper()
                        replay(self)
                
            if self.value == 'D':
                if coins >= 20:
                    go_ahead = input("For 20 coins you can get 3 new lives, do you want to spend your coins and continue ? y/n ").upper()
                    while go_ahead != "Y" or go_ahead != 'N':
                        if go_ahead == 'Y':
                            coins = coins - 20
                            lives = lives + 3
                            break
                        elif go_ahead == 'N':
                            replay(self)
                        else: 
                            print('Please try again, Y for yes and N for no')
                            go_ahead = input("For 20 coins you can get 3 new lives, do you want to spend your coins and continue ? y/n ").upper()            
                        replay(self) 
    print("Game Over \n")         
    replay(self)           


def replay(self):
    """
    Get the play input value to give to the user the chance to choose if want
    play another game or close the match
    """
    play = input("Do you want to do another game y/n ??: ").upper()
    while play != 'Y' or play != 'N':
        if play == "Y":
            self.value = input("Do you want to play easy or difficult ? e/d : ").upper()
            Game(self.value)
        elif play == "N":
            print("Thanks for your time")
            print('Game Over')
            exit()
        else:
            print("Invalid input, Y for yes and N for no ")
            play = input("Do you want to do another game y/n ??: ").upper()
    

def main():
    """
    run input pre-game and Game class
    """


user_name = input("Please insert your name: ")
while len(user_name) < 1 or user_name.isalpha() is False:
    print('Please insert only letters')
    print('Please insert at least one letter')
    user_name = input("Please insert your name: ")
    

class User:
    """
class that get the value of the input user_name and print the name of the
user
    """
    
    def __init__(self, name):
        self.name = user_name
        print(f"Ready to guess {self.name} ? ")


user = User(user_name)

difficulty = input("Do you want to play easy or difficult ? e/d : ").upper()

Game(difficulty)
main()