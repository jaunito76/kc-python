import os
# The purpose of this file is to find a word of a certain length given a list of letters and 
# to return all the possible word of that length

WORDLIST_FILENAME = "kc-python23/01 Homework/hangman/words.txt"

def main():
    word_list = loadWords()
    letters = getLetters()
    results = findWords(word_list, letters)
    for word in results:
        print(word)
    return

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def getLetters():
    return list(input('What letters do you have? '))

def findWords(word_list, letters):
    results = []
    for word in word_list:
        if len(word) > 2:
            found = True
            temp_ltrs = letters
            for letter in word:
                if letter in temp_ltrs:
                    temp_ltrs.remove(letter)
                else:
                    found = False
                    break
            if found:
                results.append(word)
    return results 

if __name__=="__main__":
    main()
            