import random
from word import WORDS

print('Welcome to the game :\n', '''   +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

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


def difficult():
    """
    Get input difficulty value to start a new match in hard or easy mode based
    on the user preference
    """
    global difficulty
    while difficulty != 'E' or 'D':
        if difficulty == 'E':
            easy_mode()
        elif difficulty == "D":
            hard_mode()
        elif difficulty == '7JM)x{':
            break
        else:
            print("Invalid input try again: e for easy, d for difficult")
            difficulty = input(
                "Do you want to play easy or difficult ? e/d : ").upper()
        
    
def easy_mode():
    """
    game mode where the word choose can be only under 7 letters, add 1 life 
    and 5 coins everytime the user guess a letter of the word choose,
    the user if lose all the lives can restart spending the coins
    obtained at the end of the match the function run replay function  
    """
    word = random.choice(WORDS)
    while len(word) >= 7:
        word = random.choice(WORDS)
    guess = "_" * len(word)
    guess_word = set(word)
    letters_in_word = set()
    letters_used = set()
    print(f"{guess} \n")
    lives = 6
    coins = 0
    
    while guess_word != letters_in_word:  
       
        user_choice = input("Guess a word:").upper()
        if len(user_choice) > 1:
            print("Invalid input try again")
            user_choice = input("Guess a word: ").upper()
        else:
            pass
        if user_choice in letters_used:
            print('letter already used')
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
            lives = lives + 1
            coins = coins + 5
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
            print("Game Over \n")
            if coins >= 10:
                go_ahead = input("For 10 coins you can get 5 new lives, do you want to spend your coins and continue ? y/n").upper()
                if go_ahead == 'Y':
                    coins = coins - 10
                    lives = lives + 5
            replay()
    replay()           

    
def hard_mode(): 
    """
    game mode where the word choose can be only over 7 letters, add 5 coins everytime the user guess a letter of the word choose,
    the user if lose all the lives can restart spending the coins
    obtained, at the end of the match the function run replay function
    """
    word = random.choice(WORDS)
    while len(word) < 7:
        word = random.choice(WORDS)
    else: 
        pass
    guess_word = set(word)
    letters_in_word = set()
    letters_used = set()
    guess_word = set(word)
    guess = "_" * len(word)
    print(f"{guess} \n")
  
    lives = 6
    coins = 0
    
    while guess_word != letters_in_word:  
       
        user_choice = input("Guess a word:").upper()
        if len(user_choice) > 1:
            print("Invalid input try again")
            user_choice = input("Guess a word: ").upper()
        else:
            pass
        if user_choice in letters_used:
            print('letter already used')
            continue
            letters_used.add(user_choice)
        
        if word.find(user_choice) == -1:
            print("I guess that you didn't guess 🤣")
            lives = lives - 1
            print(f"{lives} lives remained")
            print(f"You used already {letters_used} ")
            print(f"{coins} coin/s")
        else:
            coins = coins + 5
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
            print("Game Over\n")
            if coins >= 20:
                go_ahead = input("For 20 coins you can get 3 new lives, do you want to spend your coins and continue ? y/n").upper()
                if go_ahead == 'Y':
                    coins = coins - 20
                    lives = lives + 3
                    
            else:
                replay()
    replay()
    

def replay():
    """
    Get the play input value to give to the user the chance to choose if want
    play another game or close the match
    """
    global difficulty
    play = input("Do you want to do another game y/n ??").upper()
    while play != 'Y' or 'N':
        if play == "Y":
            difficulty = input("Do you want to play easy or difficult ? e/d : ").upper()
            difficult()
        elif play == "N":
            difficulty = "7JM)x{"
            break
        else:
            print("Invalid input")
            play = input("Do you want to do another game y/n ??\n").upper()
    print("Thanks for your time\n")
    print('Game Over')


def main():
    """
    run difficult function
    """

    difficult()    


main()
