import random

WORDS = ['ENERGY','SPEECH','CLIENT','INSTANCE','AIRPORT','DESK','SUCCESS','VILLAGE','DRAMA','FAMILY','REVOLUTION','LOVE','ROLE','CLIMATE','EXAM','BLOOD','EMPLOYER','EFFORT','WEAKNESS','INSTRUCTION','NEWSPAPER','SOCIETY','DIAMOND','WEALTH','DINNER','COMPLAINT','OVEN','LITERATURE','SATISFACTION','VIDEO','GUEST','NATION','PLATFORM','JUDGMENT','PASSENGER','SELECTION','STRANGER','EDITOR','MODE','DATABASE','GUIDANCE','OBLIGATION','ASSISTANT','DEPARTURE','PIANO','WRITER','LAW','PRESENTATION']

print('Welcome to the game :\n' , 
'''                   +---+
                    |   |
                        |
                        |
                        |
                        |
                    =========''')

user_name = input("Please insert your name: ")

lives = 6

letters_used = set()

class User:
    def __init__(self, name):
        self.name = user_name
      
        print( f"Ready to guess {self.name} ? ")     
user = User(user_name)

word = random.choice(WORDS)
guess = "_" * len(word)
guess_word = set(word)
print(guess)
print(word)
print(len(word))


def check_letter_in_word(): 
    global lives
    letters_in_word = set()
    
    while guess_word != letters_in_word:  
       
        user_choice = input("Guess a word: ").upper()
        if user_choice in letters_used:
            print('letter already used')
            continue
        x = letters_used.add(user_choice)
        print(letters_used)
        if word.find(user_choice) == -1:
            print("I guess that you didn't guess 🤣")
            lives = lives - 1
            print(lives)
            print(letters_used)
        
        else:
            lives = lives + 1
            print("i guess you guess ✌")
            print(lives)
            print(letters_used)
                
            if user_choice in word:
                letters_in_word.add(user_choice)
                print(f"{letters_in_word} is present in the word")
        current_word = ""
        for letter in range(len(word)):
            global guess
            if user_choice == word[letter]:
                current_word += user_choice
            else:
                current_word += guess[letter]

        guess = current_word
        print(guess)

def loop(): 
    global lives
    word = random.choice(WORDS)
    guess_word = set(word)
    letters_in_word = set()
    letters_used = set()
    guess_word = set(word)
    guess = "_" * len(word)
    print(guess)
    print(word)
  
    while guess_word != letters_in_word:  
       
        user_choice = input("Guess a word: ").upper()
        if user_choice in letters_used:
            print('letter already used')
            continue
        x = letters_used.add(user_choice)
        print(letters_used)
        if word.find(user_choice) == -1:
            print("I guess that you didn't guess 🤣")
            lives = lives - 1
            print(lives)
            print(letters_used)
        
        else:
            lives = lives + 1
            print("i guess you guess ✌")
            print(lives)
            print(letters_used)
                
            if user_choice in word:
                letters_in_word.add(user_choice)
                print(f"{letters_in_word} is present in the word")

        current_word = ""
        
        for letter in range(len(word)):
           
            if user_choice == word[letter] :
                current_word += user_choice
            else:
                current_word += guess[letter]

        guess = current_word
        print(guess)
    replay()

def replay():
    global WORDS
    play = input("Do you want to do another game y/n ??").upper()
    if play == "Y":
        loop()
    elif play == "N":
        print("Thanks for your time")
    else:
        print("Invalid input")
        play = input("Do you want to do another game y/n ??").upper()
        

                      

def main():
    check_letter_in_word()
    replay()

main()
