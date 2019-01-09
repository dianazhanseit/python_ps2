# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:
# Start time: 15:25 6th December

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    k = len(secret_word)
    count = 0

    for char in secret_word:
    	if char in letters_guessed:
    		count = count + 1
    if count == k:
    	return True
    else:
    	return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    s = ''
    for char in secret_word:
    	if char in letters_guessed:
    		s += char
    	else:
    		s += "_ "
    return s

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    s = ''
    for char in string.ascii_lowercase:
    	if char in letters_guessed:
    		pass
    	else:
    		s += char
    return s

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    '''
    # Starts up an interactive game of Hangman.
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word), "letters long")
    # * The user should start with 6 guesses
    trial = 6
    letters_guessed = []
    warning = 3
    letters = []
    for char in secret_word:
    	if char not in letters:
    		letters += char
    vowels = 'aeiou'
    while True:
    	if is_word_guessed(secret_word, letters_guessed) == True:
    		print("Congratulations, you won!")
    		print("Your total score for this game is:", trial*len(letters))
    		break 
    	if trial == 0:
    		print("You ran out of guesses! You lose.") 
    		print("The word is: ", secret_word) 
    		break  	
    	print("-------------------------------")
    	print("You have", warning, "warnings left")
    	print("You have", trial, "guesses left")
    	print("Available letters:", get_available_letters(letters_guessed))
    	# * Ask the user to supply one guess per round. 
    	x = input("Please guess a letter:")
    	# Remember to make sure that the user puts in a letter!
    	if x not in get_available_letters(letters_guessed):
    		warning = warning - 1
    		print("The letter was already chosen!")
    		x = input("Please guess a letter:")
    	if len(x) != 1:
    		print("1 letter only Please!")
    		warning = warning - 1
    		x = input("Please guess a letter:")
    	if x.isalpha() == False:
    		print("Oops! That is not a valid letter.")
    		warning = warning - 1
    	if warning == 0:
    		print("You ran out of warnings! You lose 1 guess")
    		trial -= 1
    	letters_guessed += x
    	# * The user should receive feedback immediately after each guess 
	    #   about whether their guess appears in the computer's word.
    	if x not in secret_word:
    		if x in vowels:
    			trial -= 2
    			print("Oops! That is not in my word:", get_guessed_word(secret_word, letters_guessed))
    		else:
    			trial = trial - 1
    			print("Oops! That is not in my word:", get_guessed_word(secret_word, letters_guessed))
    	else:
    		print("Yes!! You guessed:", get_guessed_word(secret_word, letters_guessed))



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    i = 0
    new_str = my_word.strip()
    for char in other_word:
    	if char == new_str[i]:
    		count = count + 1
    	elif char == '_ ':
    		count = count + 1
    	i = i + 1
    if count == len(other_word):
    	return True
    else:
    	return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    new_word = my_word.strip()
    for word in wordlist:
    	if len(new_word) == len(word):
    		i = 0
    		count = 0
    		for char in new_word:
    			if char == word[i]:
    				count = count + 1
    			else:
    				pass
    			i = i + 1
    		if count == 2:
    			print(word)
    		elif count > 2:
    			print(word)




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Starts up an interactive game of Hangman.
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word), "letters long")
    trial = 6
    letters_guessed = []
    warning = 3
    letters = []
    for char in secret_word:
    	if char not in letters:
    		letters += char
    vowels = 'aeiou'
    while True:
    	if is_word_guessed(secret_word, letters_guessed) == True:
    		print("Congratulations, you won!")
    		print("Your total score for this game is:", trial*len(letters))
    		break 
    	if trial == 0:
    		print("You ran out of guesses! You lose.") 
    		print("The word is: ", secret_word) 
    		break  	
    	print("-------------------------------")
    	print("You have", warning, "warnings left")
    	print("You have", trial, "guesses left")
    	print("Available letters:", get_available_letters(letters_guessed))
    	# * Ask the user to supply one guess per round. 
    	x = input("Please guess a letter:")
    	# Remember to make sure that the user puts in a letter!
    	if x not in get_available_letters(letters_guessed):
    		warning = warning - 1
    		print("The letter was already chosen!")
    		x = input("Please guess a letter:")
    	if len(x) != 1:
    		print("1 letter only Please!")
    		warning = warning - 1
    		x = input("Please guess a letter:")
    	if x.isalpha() == False:
    		print("Oops! That is not a valid letter.")
    		warning = warning - 1
    	if warning == 0:
    		print("You ran out of warnings! You lose 1 guess")
    		trial -= 1
    	letters_guessed += x
    	# * The user should receive feedback immediately after each guess 
	    #   about whether their guess appears in the computer's word.
	    if x == "*" :
	      	show_possible_matches(letters_guessed)
    	if x not in secret_word:
    		if x in vowels:
    			trial -= 2
    			print("Oops! That is not in my word:", get_guessed_word(secret_word, letters_guessed))
    		else:
    			trial = trial - 1
    			print("Oops! That is not in my word:", get_guessed_word(secret_word, letters_guessed))
    	else:
    		print("Yes!! You guessed:", get_guessed_word(secret_word, letters_guessed))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
