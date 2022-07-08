import random

WORDS = ['ENERGY','SPEECH','CLIENT','INSTANCE','AIRPORT','DESK','SUCCESS','VILLAGE','DRAMA','FAMILY','REVOLUTION','LOVE','ROLE','CLIMATE','EXAM','BLOOD','EMPLOYER','EFFORT','WEAKNESS','INSTRUCTION','NEWSPAPER','SOCIETY','DIAMOND','WEALTH','DINNER','COMPLAINT','OVEN','LITERATURE','SATISFACTION','VIDEO','GUEST','NATION','PLATFORM','JUDGMENT','PASSENGER','SELECTION','STRANGER','EDITOR','MODE','DATABASE','GUIDANCE','OBLIGATION','ASSISTANT','DEPARTURE','PIANO','WRITER','LAW','PRESENTATION']

print('Welcome to the game :\n' , '''   +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

user_name = input("Please insert your name: ")





class User:
    def __init__(self, name):
        self.name = user_name
      
        print( f"Ready to guess {self.name} ? ")     
user = User(user_name)

def difficult():
    difficulty = input("Do you want to play easy or difficult ? e/d : ").upper()
    while difficulty != 'E' or 'D':
        print("Invalid input try again: e for easy, d for difficult")
        difficulty = input("Do you want to play easy or difficult ? e/d : ").upper()
        if difficulty == 'E':
            easy_mode() 
        elif difficulty == "D":
            hard_mode()
        
    

def easy_mode():
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
        x = letters_used.add(user_choice)
        
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
            replay()
    replay()           

    


def hard_mode(): 
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
        x = letters_used.add(user_choice)
        
        if word.find(user_choice) == -1:
            print("I guess that you didn't guess 🤣")
            lives = lives - 1
            print(f"{lives} lives remained")
            print(f"You used already {letters_used} ")
            print(f"{coins} coin/s")
        else:
            lives = lives + 1
            coins = coins + 30
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
    play = input("Do you want to do another game y/n ??").upper()
    if play == "Y":
       difficult()
    elif play == "N":
        print("Thanks for your time")
    else:
        print("Invalid input")
        play = input("Do you want to do another game y/n ??").upper()
        

                      

def main():
    difficult()
    hard_mode()
    easy_mode()
    replay()
main()
