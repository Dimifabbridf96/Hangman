# Hangman 
Hangman is a Python version of the homonymous traditional game with the opportunity of 2 different levels, coins inside the game that are used in exchange for new lives when the standard ones are finished.
In this game, the user can challenge himself to guess a random word chosen from the program.

If you want to try the game here is the link - https://hangman-eng.herokuapp.com/

## How to play:

The user is welcomed with a message then:

* To start the user need to enter his name
* The second choice that the user needs to do is the difficulty which can be easy(e) or difficult(d)
* At this point the program chooses a word that can be <7 if the user chooses easy mode or >7 if the hard mode
* From here the user chooses a letter every round to see if is part of the hidden word.
* If the letter is inside the word on the terminal is shown the current word with the letter guessed in the respective position
* Every round the lives increase (onòy easy mode) or decrease based on the presence or not of the letter in the word
* Same thing for the coins
* If the number of lives reaches 0 there are 2 possible consequences:
    1. If the user has enough coins (10 for easy mode and 20 for hard mode) can spend them to receive 5 (e) or 3 (d)
    2. Else if the user doesn't have enough coins the game finish and the user can restart the game
* Finally if the user wants to close the program can answer 'N' on the input at the end of the match.

# Features
## Existing features
* Personalized challenge message
    1. After the user insert the name printed on the terminal a message containing the user name
* Opportunity to choose the difficulty with which play
    1. The user can challenge himself if the standard easy mode is too simple.
    2. With the hard mode the user can find a more complex game without sacrifice the fun.
* Random choice of a word to guess
    1. The program choose a word beetween 50 different word creating the word to be guess with an underscore for every letter.
* Visual demostration of letter guessed
    1. Every letter guessed is replace the underscore in the word shown

 




