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


def check_letter_in_word(): 
    global lives
    letters_in_word = set()
    
    while guess_word != letters_in_word:  
        
        user_choice = input("Guess a word: ").upper()
        letters_used = user_choice.split(',')
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

    def check_input():
        if user_choice in letters_in_word:
            print('letter already used') 
           
            


def main():
    check_letter_in_word()

main()
