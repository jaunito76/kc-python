# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = 'words.txt'

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
    # for each letter in secretword 
    #   if letter is in LG 
    #     set to true
    #   else
    #     false
    x=True
    for letter in secretWord:
        if  letter not in lettersGuessed:
            x=False
        return x
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    # loop through secret word 
    # get each letter looped through sw
    #if l is in lg restore letter
    # store letter in output string
    # else store underscore and space  
    boogabooga=' '
    for letter in secretWord:
        if letter not in lettersGuessed:
            boogabooga=boogabooga+'_ '
        else: 
            boogabooga=boogabooga+letter
    boogabooga=boogabooga+' '
    return boogabooga






def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
    oogabooga = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    for letter in lettersGuessed:
        if letter in oogabooga:
            oogabooga= oogabooga.replace(letter,'_')
    return oogabooga 

def nognog(secretword, lettersGuessed):
    nog=8
    for letter in lettersGuessed:
        if letter not in secretword:
            nog=nog-1
    return nog


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
    yn='n'
    while yn=='n':
      print('Hello, would you like to play a game of hangman with me y/n')
      yn=input('y/n')
    hml=len(secretWord)
    print('there are',hml, 'letters in this word')
    nog=7
    lettersguessed=''
    while nog>0 and not isWordGuessed(secretWord, lettersguessed):
      ta=input('enter a letter')
      if ta in lettersguessed:
        print('oops, it looks like you already entered that letter, try again')
      else:
        lettersguessed=lettersguessed+ta    
      nog=(nognog(secretWord, lettersguessed))
      if isWordGuessed(secretWord, lettersguessed)==True:
        print('YOU WIN!!!. your word was', secretWord)
      elif nog==0:
        print('out of guesses, oh well better luck next time.')
      else:
         print('try again, your word so far is', getGuessedWord(secretWord, lettersguessed), 'here are the letters left to use',getAvailableLetters(lettersguessed), 'and you have',nog,'guesses left')




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
#isWordGuessed('apple', ['a', 'p', 'q'])