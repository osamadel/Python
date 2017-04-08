# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ans = ""
    for char in secretWord:
        if char in lettersGuessed:
            ans += char
        else:
            ans += "_ "
    return ans



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    ans = ""
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            ans += char
    return ans
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    # isWordGuessed(secretWord, lettersGuessed) : bool
    # getGuessedWord(secretWord, lettersGuessed) : string
    # getAvailableLetters(lettersGuessed) : string

    mistakes = 0
    lettersGuessed = ""     # letters guessed correctly
    availableLetters = getAvailableLetters(lettersGuessed)
    letter = ""
    guessedWord = ""
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")

    while True:
        print("-------------")
        print("You have", 8-mistakes, "guesses left.")
        print("Available Letters:", availableLetters)
        letter = input("Please guess a letter: ").lower()

        # Check the entered letter.
        if letter in secretWord and (letter not in lettersGuessed):
            # The letter entered is a correct guess.
            # Add that letter to the guessed letters.
            lettersGuessed += letter
            # Print the guessed parts of the secret word (whith _ in place of unguessed letters).
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        elif letter in lettersGuessed:
            # The letter have been guessed before
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            continue
        else:
            # The letter entered is a wrong guess.
            mistakes += 1
            lettersGuessed += letter
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))

        # Update available letters
        availableLetters = getAvailableLetters(lettersGuessed)

        # Check if the letters guessed so far guessed the secret word
        if isWordGuessed(secretWord, lettersGuessed):
            print("------------\nCongratulations, you won!")
            return
        elif mistakes == 8:
            print("------------")
            print("Sorry, you ran out of guesses. The word was", secretWord + ".")
            return








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman("adel")
